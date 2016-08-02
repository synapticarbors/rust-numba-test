# rust-numba-test
Proof-of-concept of calling a [Numba](http://numba.pydata.org/) jit'd function from [Rust](https://www.rust-lang.org) from Python using [CFFI](https://cffi.readthedocs.io)

This example defines a function in Rust that doubles the result of the function passed to it. The Numba `@cfunc` decorator with CFFI support
requires Numba 0.27. This allows Numba to [create a C callback](http://numba.pydata.org/numba-doc/0.27.0/user/cfunc.html) that can be passed
to Rust. 

Basic instructions for running the example:

If you need to install numba, then I recommend first getting [Miniconda](http://conda.pydata.org/miniconda.html) and then:

```
conda create -n rust-numba-example cffi numba numpy
source activate rust-numba-example  # or just `activate rust-numba-example` on Windows
```

Then to compile the Rust code and run the python example:

```
cargo build --release
python test.py
```
