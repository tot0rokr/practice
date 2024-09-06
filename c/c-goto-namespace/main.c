#include <stdio.h>

void func1(void)
{
	printf("func1\n");
	goto out;
	printf("skip func1\n");
out:
	printf("out func1\n");
	return;
}

void func2(void)
{
	printf("func2\n");
	goto out;
	printf("skip func2\n");
out:
jump:
	printf("out func2\n");
	return;
}

int main(void)
{
	printf("main\n");
	func1();
	goto out;
	printf("skip main\n");
out:
	/* goto jump; 불가 */
	func2();
	printf("out main\n");
	return 0;
}
