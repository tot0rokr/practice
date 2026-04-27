#include <stdio.h>

struct A {
	struct {
		union {
			int a;
			int b;
		};
	};
	union {
		struct {
			int c;
			int d;
		};
		int e;
	};
};

int main()
{
	struct A a;
	struct A b;
	a.c = 10;
	a.d = 20;
	b = a;
	printf("%d %d %d\n", b.c, b.d, b.e);
	return 0;
}
