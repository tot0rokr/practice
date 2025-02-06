#include <stdio.h>
#include <stdint.h>

//======================================================================
// 1) 고정소수점 정의
//======================================================================
#define SHIFT       8
#define ONE         (1 << SHIFT)  // 1.0 고정소수점 표현 (SHIFT=8 → 1.0=256)

// 정수 -> 고정소수점
#define TO_FIXED(x)     ((x) << SHIFT)
// 고정소수점 -> 정수(내림)
#define FROM_FIXED(x)   ((x) >> SHIFT)

// 고정소수점 곱셈: (a * b) >> SHIFT
static inline int fixedMul(int a, int b) {
    long long temp = (long long)a * (long long)b;
    return (int)(temp >> SHIFT);
}

// 고정소수점 나눗셈: (a << SHIFT) / b
static inline int fixedDiv(int a, int b) {
    long long temp = ((long long)a << SHIFT);
    return (int)(temp / b);
}

//======================================================================
// 2) 1차원 칼만 필터 구조체
//======================================================================
typedef struct {
    int x;  // 추정 상태 (고정소수점)
    int P;  // 추정 공분산 (고정소수점)
    int Q;  // 프로세스 노이즈 공분산 (고정소수점)
    int R;  // 측정 노이즈 공분산 (고정소수점)
} KalmanFilter;

//======================================================================
// 3) 칼만 필터 초기화
//======================================================================
void KalmanFilter_Init(KalmanFilter* kf, int init_x, int init_P, int Q, int R) {
    kf->x = init_x;   // 초기 상태값(고정소수점)
    kf->P = init_P;   // 초기 추정 공분산
    kf->Q = Q;        // 프로세스 노이즈
    kf->R = R;        // 측정 노이즈
}

//======================================================================
// 4) 칼만 필터 업데이트 (Predict + Update)
//======================================================================
int KalmanFilter_Update(KalmanFilter* kf, int z) {
    // z: 측정값(고정소수점)

    //---------- 1) 예측(Predict) ----------
    // x_pred = x(k-1|k-1)
    int x_pred = kf->x;
    // P_pred = P(k-1|k-1) + Q
    int P_pred = kf->P + kf->Q;

    //---------- 2) 갱신(Update) ----------
    // K = P_pred / (P_pred + R) (고정소수점 나눗셈)
    int denom = P_pred + kf->R;
    if (denom == 0) denom = 1; // 0으로 나누지 않도록 안전장치
    int K = fixedDiv(P_pred, denom); // 고정소수점으로 계산됨

    // x(k|k) = x_pred + K * (z - x_pred)
    int diff = z - x_pred;            // (z - x_pred)도 고정소수점
    int incr = fixedMul(K, diff);     // K * (z - x_pred) => 고정소수점
    kf->x = x_pred + incr;            // 최종 x(k|k)

    // P(k|k) = (1 - K) * P_pred
    //        = P_pred - K * P_pred
    int KPP = fixedMul(K, P_pred);
    kf->P = P_pred - KPP;

    // kf->x는 고정소수점 표현값
    return kf->x;
}

int main(void)
{
    //==================================================================
    // 예시) 센서(조도) 원본 데이터 (정수라 가정)
    // 실제 환경에 맞게 값이 100~300 정도 나올 수 있다고 가정.
    //==================================================================
    int raw_sensor_data[] = {
        200, 202, 210, 90, 185,
        400, 215, 510, 205, 200,
        195, 98, 203, 210, 220
    };
    int data_count = sizeof(raw_sensor_data) / sizeof(raw_sensor_data[0]);

    //==================================================================
    // 1) 고정소수점으로 변환
    //==================================================================
    int sensor_data_fx[50];
    for(int i = 0; i < data_count; i++) {
        //  예) 200 → 51200 (200 << 8)
        sensor_data_fx[i] = TO_FIXED(raw_sensor_data[i]);
    }

    //==================================================================
    // 2) 칼만 필터 초기화
    //    - Q, R은 엑셀로부터 추정된 분산 또는 스케일 조정값
    //      (아래는 예시로 Q=2.0, R=10.0 정도를 SHIFT=8 기준으로 세팅)
    //==================================================================
    KalmanFilter kf;
    // init_x = 첫 측정값, init_P = 다소 큰 값(초기 불확실성)
    int init_x = sensor_data_fx[0];        // 첫 측정값을 초기 상태로
    int init_P = TO_FIXED(50);            // 50 정도를 (SHIFT=8) 스케일링 → 12800
    int Q_fx   = TO_FIXED(2);             // 프로세스 노이즈 2.0 → 512
    int R_fx   = TO_FIXED(10);            // 측정 노이즈 10.0 → 2560

    KalmanFilter_Init(&kf, init_x, init_P, Q_fx, R_fx);

    //==================================================================
    // 3) 필터 적용 및 결과 출력
    //==================================================================
    printf("Idx\tRaw\tKalman(Scaled)\tKalman(Int)\n");
    for(int i = 0; i < data_count; i++) {
        // 센서 측정값(고정소수점)으로 업데이트
        int filtered_fx = KalmanFilter_Update(&kf, sensor_data_fx[i]);

        // FROM_FIXED()로 정수부 변환
        int filtered_int = FROM_FIXED(filtered_fx);

        printf("%3d\t%3d\t%12d\t%11d\n",
               i, raw_sensor_data[i], filtered_fx, filtered_int);
    }

    return 0;
}
