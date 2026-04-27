// main.c
// gcc -O2 -Wall main.c -o fork_memory_test
// ./fork_memory_test

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/wait.h>

int g = 100; // 전역(데이터 영역)

int main(void) {
	setbuf(stdout, NULL); // 출력 버퍼링 끄기(부모/자식 출력 섞일 때 보기 편함)

	int local = 200;                 // 스택
	int *heap = malloc(sizeof(int)); // 힙
	if (!heap) { perror("malloc"); return 1; }
	*heap = 300;

	// 공유 메모리(부모/자식이 같이 보게 만들기)
	int *shared = mmap(NULL, sizeof(int),
	                   PROT_READ | PROT_WRITE,
	                   MAP_SHARED | MAP_ANONYMOUS, -1, 0);
	if (shared == MAP_FAILED) { perror("mmap"); return 1; }
	*shared = 400;

	printf("=== BEFORE fork ===\n");
	printf("pid=%d  &g=%p g=%d  &local=%p local=%d  heap=%p *heap=%d  shared=%p *shared=%d\n",
	       getpid(), (void*)&g, g, (void*)&local, local, (void*)heap, *heap, (void*)shared, *shared);

	pid_t pid = fork();
	if (pid < 0) { perror("fork"); return 1; }

	if (pid == 0) {
		// child
		printf("\n[child] pid=%d ppid=%d\n", getpid(), getppid());
		printf("[child] addrs: &g=%p &local=%p heap=%p shared=%p\n",
		       (void*)&g, (void*)&local, (void*)heap, (void*)shared);

		// 값 변경
		g = 111;
		local = 222;
		*heap = 333;
		*shared = 444;

		printf("[child] AFTER write: g=%d local=%d *heap=%d *shared=%d\n",
		       g, local, *heap, *shared);

		// 부모가 읽을 시간 주기
		sleep(1);
		return 0;
	} else {
		// parent
		printf("\n[parent] pid=%d child=%d\n", getpid(), pid);
		printf("[parent] addrs: &g=%p &local=%p heap=%p shared=%p\n",
		       (void*)&g, (void*)&local, (void*)heap, (void*)shared);

		// child가 바꾼 뒤 확인(일반 메모리는 그대로여야 함, shared만 바뀌어야 함)
		sleep(2);
		printf("[parent] AFTER child write: g=%d local=%d *heap=%d *shared=%d\n",
		       g, local, *heap, *shared);

		int status = 0;
		waitpid(pid, &status, 0);

		munmap(shared, sizeof(int));
		free(heap);
		return 0;
	}
}
