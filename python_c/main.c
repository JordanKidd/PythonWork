#include <python3.4/Python.h>

// Three forms functions can take:
// static PyObject *MyFunction( PyObject *self, PyObject *args );
// static PyObject *MyFunctionWithKeywords(PyObject *self, PyObject *args, PyObject *kw);
// static PyObject *MyFunctionWithNoArgs( PyObject *self );

static PyObject* helloworldfn(PyObject* self) {
    return Py_BuildValue("s", "Hello, CPython from C a extension!!");
}

static PyMethodDef module_methods[] = {
    {
        "helloworld",
        (PyCFunction) helloworldfn,
        METH_VARARGS,
        "says hello"
    }, {NULL, NULL, 0, NULL} // Sentinel
};

static struct PyModuleDef helloworld = {
    PyModuleDef_HEAD_INIT,
    "helloworld", /* name of module */
    "",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    module_methods
};

PyMODINIT_FUNC PyInit_helloworld(void) {
    return PyModule_Create(&helloworld);
}
