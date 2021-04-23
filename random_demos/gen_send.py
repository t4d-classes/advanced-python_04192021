
from collections.abc import Generator

def do_it() -> Generator[int, str, None]:

    result = yield 1
    print(result)

    result = yield 2
    print(result)

    yield 3


gen = do_it()
print(next(gen))
print(gen.send('a'))
print(gen.send('b'))

