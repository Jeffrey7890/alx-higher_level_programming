#include <stdio.h>
#include <Python.h>

/**
  * print_python_list_info - prints info about python list
  * @p: list object
  */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t length, i;

	PyObject *type;

	length = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < length; i++)
	{
		type = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(type)->tp_name);
	}
}
