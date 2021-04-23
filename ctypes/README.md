# Windows CTypes Python

## Setup

If you do not have GCC installed for Windows, I recommend installing [Win-builds](http://win-builds.org/doku.php). Be sure to add the Win-builds `bin` folder to your user/system path on Windows.

## Demo 1 - Printf

The following demo uses the Windows `printf` function to print a message to the console.

```bash
python .\printf_demo.py
```

## Demo 2 - Message Box

The following demo uses the Windows `MessageBoxA` function to display a message in a GUI window.

```bash
python .\message_box_demo.py
```

## Demo 3 - Custom DLL

Change into the `simple` folder, and run the following commands to compile the DLL.

```bash
gcc -std=c11 -Wall -Wextra -pedantic -c -fPIC simple.c -o simple.o
gcc -shared simple.o -o simple.dll
```

Change in the project root folder, and run the following command to use the ctypes functions imported from the DLL.

```bash
python .\custom_dll_demo.py
```