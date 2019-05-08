import sys
from setuptools import setup, Extension, find_packages
import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

extra_compile_args = ['-Wno-cpp', '-Wno-unused-function', '-std=c99']
is_windows = sys.platform == 'win32' or sys.platform == 'cygwin'
if is_windows:
    extra_compile_args = []
ext_modules = [
    Extension(
        'hpycocotools._mask',
        sources=['common/maskApi.c', 'hpycocotools/_mask.pyx'],
        include_dirs = [np.get_include(), 'common'],
        extra_compile_args=extra_compile_args,
    )
]

setup(
    name='pycocotools-hrvvi-ext',
    packages=find_packages(),
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0'
    ],
    version='2.0',
    ext_modules=ext_modules
)
