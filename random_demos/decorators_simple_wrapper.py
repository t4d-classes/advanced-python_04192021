from typing import Any, Callable

def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
    def inner(*args: tuple[Any], **kwargs: dict[str, Any]) -> Any:
        print("start")
        return fn(*args, **kwargs) # do_it invoked
    return inner

# def do_it(a: int, b: int) -> int:
#     return a + b

# func_a = wrapper(do_it)
# print(func_a(1,2))

@wrapper
def do_it2(a: int, b: int) -> int:
    return a + b

print(do_it2(1,2))