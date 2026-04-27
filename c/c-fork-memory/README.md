# fork 이후 메모리 영역 확인

`fork()` 전후에 전역 변수, 스택, 힙, 공유 메모리가 부모/자식 프로세스에서 어떻게 보이는지 확인하는 예제.

- `g`, `local`, `*heap`은 자식이 바꿔도 부모에서는 원래 값이 유지된다.
- `*shared`는 `mmap(MAP_SHARED | MAP_ANONYMOUS)`로 만든 공유 메모리라 부모도 변경값을 확인할 수 있다.

```sh
gcc -O2 -Wall main.c -o fork_memory_test
./fork_memory_test
```
