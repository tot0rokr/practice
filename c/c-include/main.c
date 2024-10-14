#include <stdio.h>
#include "external.c"

int process()
{
	printf("process\n");
	external();
	return 0;
}
