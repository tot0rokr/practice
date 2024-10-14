# include stack 유효범위

test.c --- main.c  --- external.c
       |
       |
       --- libcommon.c


이런 형태에서 `libcommon.c` 에서 `external.c`의 메소드를 호출할 수 있다.
즉, `main.c`와 `libcommon.c`에서 `external()`을 모두 호출할 수 있다.


### test.c

```c
#include "main.c"
#include "libcommon.c"

int main()
{
	printf("start test\n");
	process();
	common();
	printf("end test\n");
	return 0;
}
```


### main.c

```c
#include <stdio.h>
#include "external.c"

int process()
{
	printf("process\n");
	external();
	return 0;
}
```


### external.c

```c
#include <stdio.h>

static void external()
{
	printf("external\n");
}
```


### libcommon.c

```c
static void common()
{
	external();
}
```
