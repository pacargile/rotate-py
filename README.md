# rotate-py
Python hooks and glue code for Bob Kurucz rotate.for program

CURRENTLY A WORK IN PROGRESS

Files:

rotate.f90 -> Fortran code that is directly taken from Bob's rotate.for code
rotate.py  -> Python code using ctypes to access the hooks placed in the fortan

Steps to install:

1) Compile the fortran code into a shared object library with something like:

gfortran -shared -fPIC -o librotate.so rotate.f90

2) Edit the path to this shared library within the rotate.py python code
