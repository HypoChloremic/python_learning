
// This is so as to pull in the python api
#include <Python.h>
static PyObject *

// For error handling
static PyObject *SpamError;

// C function always has two arguments, conventionally named self and args
spam_system(PyObject *self, PyObject *args)
{
	const char *command;
	int sts;

	if (!PyArg_ParseTuple(args, "s", &command))
		// This is for error detection
		return NULL;
	sts = system(command)
	return PyLong_FromLong(sts)
}