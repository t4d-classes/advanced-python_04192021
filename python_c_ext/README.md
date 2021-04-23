# Python C Extension

## Setup

To build the C extension, [Visual Studio](https://visualstudio.microsoft.com/) is required. The Community Edition is all that is needed.

## Build the C Extension

Builds the C Extension package.

```bash
python setup.py build
```

## Install the C Extension

Builds and install the C Extension package.

```bash
python setup.py install
```

## Explore the Module

Start the Python REPL.

```bash
python
```

Run the following commands in the REPL.

```bash
import myfputs
myfputs.fputs("test", "test.txt")
```
