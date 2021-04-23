#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <Python.h>

static PyObject *method_fputs(PyObject *self, PyObject *args)
{
    char *str, *filename = NULL;
    int bytes_copied = -1;

    if (!PyArg_ParseTuple(args, "ss", &str, &filename))
    {
        return NULL;
    }

    FILE *fp = fopen(filename, "w");
    bytes_copied = fputs(str, fp);
    fclose(fp);

    return PyLong_FromLong(bytes_copied);
}

static PyMethodDef MyFputsMethods[] = {
    {"fputs", method_fputs, METH_VARARGS, "Python interface for fputs C library function"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef myfputsmodule = {
    PyModuleDef_HEAD_INIT,
    "myfputs",
    "Python interface for the fputs C library function",
    -1,
    MyFputsMethods
};

PyMODINIT_FUNC PyInit_myfputs(void)
{
    return PyModule_Create(&myfputsmodule);
}
