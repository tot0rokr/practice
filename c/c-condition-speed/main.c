#include <time.h>
#include <stdio.h>

#define MEASURE(__t, __n, __func) printf("%s: %lf\n", (#__func), measure(__t, __n, (__func)))

#define NUM 1

int add(int n) {
	int i;
	int tmp = 0;

	for (i = 0; i < n; i++) {
		tmp += NUM;
		tmp += NUM;
		tmp += NUM;
	}
}

int condition1(int n) {
	int i;
	int tmp = 0;

	for (i = 0; i < n; i++) {
		if (i % 2 == 0) {
			tmp += NUM;
		}
	}
}

int condition2(int n) {
	int i;
	int tmp = 0;

	for (i = 0; i < n; i++) {
		if (i % 3 == 0) {
			tmp += NUM;
		}
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
	MEASURE(t, n, condition1);
	MEASURE(t, n, condition2);


	return 0;
}
