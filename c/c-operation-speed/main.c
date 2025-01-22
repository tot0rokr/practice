#include <time.h>
#include <stdio.h>

#define MEASURE(__t, __n, __func) printf("%s: %lf\n", (#__func), measure(__t, __n, (__func)))

#define NUM 5

int add(int n) {
	int i, j;
	int tmp = 0;

	for (i = 0; i < n; i++) {
		tmp += NUM;
	}
}

int sub(int n) {
	int i, j;
	int tmp = 0;

	for (i = 0; i < n; i++) {
		tmp -= NUM;
	}
}

int mul(int n) {
	int i, j;
	int tmp = 0;

	for (i = 0; i < n; i++) {
		tmp *= NUM;
	}
}

int div(int n) {
	int i, j;
	int tmp = 0;

	for (i = 0; i < n; i++) {
		tmp /= NUM;
	}
}

double measure(int t, int n, int (*cb)(int)) {
	int i;
	double sum;
	clock_t start, end;

	for (i = 0; i < t; i++) {
		start = clock();
		cb(n);
		end = clock();
		sum += (double)(end - start);
	}
	return sum / t;
}

int main() {
	int t = 100;
	int n = 100000000;

	MEASURE(t, n, add);
	MEASURE(t, n, div);
	MEASURE(t, n, mul);
	MEASURE(t, n, sub);


	return 0;
}
