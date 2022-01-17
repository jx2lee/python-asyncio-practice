import asyncio
import inspect


async def f():
    return 123


print(f'type(f): {type(f)}')
print(f'inspect.iscoroutinefunction(f): {inspect.iscoroutinefunction(f)}')
print("\n")

coro = f()
print(f'type(f): {type(coro)}')
print(f'inspect.iscoroutine(coro): {inspect.iscoroutine(coro)}')
print("\n")

# coroutine: 일시 정지(suspend)했던 함수를 재개할 수 있는 기능을 가진 객체
# python generator 와 흡사
# async def & await: native coroutine

try:
    coro.send(
        None)  # coroutine 에 None 을 전달 하여 초기화. 생성한 coroutine 은 모두 loop.create_task() 혹 await coro 를 이용 하면 자동으로 None 을 전달 한다.
except StopIteration as e:  # coroutine 반환 시 StopIteration 예외가 발생한다.
    print(f'The answer was: ', e.value)
    print("\n")


async def await_f():
    await asyncio.sleep(0)
    return 123


async def main():
    result = await await_f()
    print(f'result: {result}')
    return result


asyncio.run(main())


# coroutine 예외 주입
# throw method 를 이용해 task 를 취소한다. (task cancellation)

# coro_exp = await_f()
# coro_exp.send(None)
# coro_exp.throw(Exception, 'exception')


# CancelledError 를 이용한 coroutine cancellation
async def cancel_f():
    try:
        while True: await asyncio.sleep(0)
    except asyncio.CancelledError:
        print("I was cancelled")
    else:
        return 111


cancel_coro = cancel_f()
cancel_coro.send(None)
cancel_coro.send(None)
# cancel_coro.throw(asyncio.CancelledError)

# coroutine 은 취소 신호를 받으면 정리 및 종료만 해야한다. 절대 취소 신호를 무시하거나 건너뛰지 않는다.
# coroutine with event loop
async def event_loop_f():
    await asyncio.sleep(0)
    return 111

loop = asyncio.get_event_loop()
event_coro = event_loop_f()
loop.run_until_complete(event_coro)
