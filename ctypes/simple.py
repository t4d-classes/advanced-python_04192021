from typing import Any
from ctypes import c_char_p, cdll, c_float, c_int, POINTER

_simple = cdll.LoadLibrary(f"simple\simple")

print_me = _simple.print_me

_print_msg = _simple.print_msg
_print_msg.argtypes = [c_char_p]
_print_msg.restype = None

def print_msg(msg: Any) -> None:
    _print_msg(c_char_p(str(msg).encode("UTF-8")))

_add_two_nums = _simple.add_two_nums
_add_two_nums.argtypes = [c_float, c_float]
_add_two_nums.restype = c_float

def add_two_nums(num_a: float, num_b: float) -> float:
    return _add_two_nums(num_a, num_b)

_sum_nums = _simple.sum_nums
_sum_nums.argtypes = [POINTER(c_int), c_int]
_sum_nums.restype = c_int

def sum_nums(nums: list[int]) -> int:
    nums_len = len(nums)
    nums_data = (c_int * nums_len)(*nums)
    return _sum_nums(nums_data, nums_len)