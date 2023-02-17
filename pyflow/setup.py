# Author: Deepak Pathak (c) 2016

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
# from __future__ import unicode_literals
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

import numpy

sourcefiles = ["/content/iSeeBetter/pyflow/pyflow.pyx", "/content/src/Coarse2FineFlowWrapper.cpp","/content/src/OpticalFlow.cpp"]
extensions = [Extension("pyflow", sourcefiles, include_dirs=[numpy.get_include()])]
setup(
    name="pyflow",
    version="1.0",
    description="Python wrapper for the Coarse2Fine Optical Flow code.",
    author="Deepak Pathak",
    ext_modules=cythonize(extensions),
    include_dirs=[numpy.get_include()]
)
