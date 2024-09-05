#include <stdio.h>
#include <stdint.h>

int main(void)
{
	uint32_t flag = 0xDEADBEAF;
	uint32_t flag2 = 0xF00;

	printf("#04x|4.4x|4x\n");
	printf("%#04x|%#4.4x|%#4x|\n", flag, flag, flag);
	printf("%#04x|%#4.4x|%#4x|\n", flag2, flag2, flag2);
	return 0;
}
