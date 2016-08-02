from cffi import FFI

import numba as nb
import numpy as np

ffi = FFI()
lib = ffi.dlopen('./target/release/libnumba_test.dylib')

ffi.cdef('double rust_double_callback(void*, int);')


def func(n):
    x = np.zeros(n, dtype=np.float64)

    for i in xrange(n):
        x[i] = 1.0 * (i + 2)

    return np.mean(np.sin(x))

f_cfunc = nb.cfunc('float64(int64)', nopython=True)(func)
f_nb = nb.jit(nopython=True)(func)

print 'Result from Rust via CFFI: ', lib.rust_double_callback(f_cfunc.cffi, 4)
print 'Result from Python:        ', 2.0 * f_nb(4)


