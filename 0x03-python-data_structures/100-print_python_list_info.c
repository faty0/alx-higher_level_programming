#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: python object
 *
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *element = PyList_GetItem(p, i);
        const char *type = Py_TYPE(element)->tp_name;

        printf("Element %ld: %s\n", i, type);
    }
}