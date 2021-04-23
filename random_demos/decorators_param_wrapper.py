from typing import Any, Callable

def param_wrapper(msg: str) -> Callable[..., Any]:
    def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
        def inner(*args: tuple[Any], **kwargs: dict[str, Any]) -> Any:
            print(msg)
            return fn(*args, **kwargs)
        return inner
    return wrapper

@param_wrapper("this is cool")
def do_it2(a: int, b: int) -> int:
    return a + b

print(do_it2(1,2))