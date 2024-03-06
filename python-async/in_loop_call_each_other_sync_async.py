# 결론부터 이야기하면 안됨.


import asyncio
import threading

# 비동기 함수 B 정의
async def async_func_B():
    print("B: Running async function B")
    await asyncio.sleep(1)  # 비동기 작업 흉내
    return "Result from B"

# 동기 함수 C 정의
def sync_func_C(result):
    print(f"C: Using result '{result}' from B to run sync function C")

# 동기 함수 A 정의
def sync_func_A(loop):
    print("A: Running sync function A and calling async function B")
    # 비동기 함수 B 호출 및 결과 기다림
    future = asyncio.run_coroutine_threadsafe(async_func_B(), loop)
    result = future.result()  # 결과 기다림
    # 결과를 사용하여 동기 함수 C 호출
    sync_func_C(result)

# 자식 스레드에서 실행할 이벤트 루프
def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

# 메인
def main():
    loop = asyncio.new_event_loop()  # 새 이벤트 루프 생성
    t = threading.Thread(target=start_loop, args=(loop,))  # 자식 스레드에 이벤트 루프 실행
    t.start()

    # 메인 스레드에서 A 실행 요청
    loop.call_soon_threadsafe(sync_func_A, loop)

    t.join()  # 자식 스레드가 완료될 때까지 대기

if __name__ == "__main__":
    main()

