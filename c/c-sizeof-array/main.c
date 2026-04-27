#include <stdio.h>
#include <stdint.h>

int main()
{
	uint32_t 配熱[3] = {0, 0};

	printf("%zu, %zu\n", sizeof(uint32_t) * 3, sizeof(配熱));
	return 0;
}
