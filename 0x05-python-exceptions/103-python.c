#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_bytes_info - print information about Python bytes objects
 * @p: pointer to PyObject p
 */
void print_python_bytes_info(PyObject *p)
{
    size_t b, i;
    char *str;

    setbuf(stdout, NULL);
    printf("[.] Bytes Object Information\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    str = ((PyBytesObject *)(p))->ob_sval, b = PyBytes_Size(p);
    printf("  Size: %ld\n  Trying String: %s\n", b, str);
    b >= 10 ? b = 10 : b++;
    printf("  First %ld Bytes: ", b);
    for (i = 0; i < b - 1; i++)
        printf("%02hhx ", str[i]);
    printf("%02hhx\n", str[i]);
}

/**
 * print_python_float_info - print information about Python float objects
 * @p: pointer to PyObject p
 */
void print_python_float_info(PyObject *p)
{
    char *str;
    double f;

    setbuf(stdout, NULL);
    printf("[.] Float Object Information\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }
    f = ((PyFloatObject *)(p))->ob_fval;
    str = PyOS_double_to_string(f, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  Value: %s\n", str);
    free(str);
}

/**
 * print_python_list_info - print information about Python list objects
 * @p: pointer to PyObject p
 */
void print_python_list_info(PyObject *p)
{
    size_t a, size, i;
    const char *t;
    PyListObject *list;

    setbuf(stdout, NULL);
    printf("[*] Python List Information\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }
    list = (PyListObject *)p;
    size = PyList_GET_SIZE(p);
    a = list->allocated;
    printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", size, a);
    for (i = 0; i < size; i++)
    {
        t = (list->ob_item[i])->ob_type->tp_name;
        printf("Element %li: %s\n", i, t);
        if (!strcmp(t, "bytes"))
            print_python_bytes_info(list->ob_item[i]);
        else if (!strcmp(t, "float"))
            print_python_float_info(list->ob_item[i]);
    }
}
