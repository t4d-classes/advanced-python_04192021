from ctypes import windll, WinDLL, c_char_p, CDLL, cdll
import ctypes, ctypes.util

label = c_char_p(b'A Message Box')
message = c_char_p(b'...with a message!')

windll.user32.MessageBoxA(0, message, label, 0x00000000)
