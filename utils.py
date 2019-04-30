from typing import Callable


def make_matrix(size: int, obj: Callable = None) -> list:
    return [[obj() if callable(obj) else None for j in range(size)] for i in
            range(size)]
