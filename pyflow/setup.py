# Author: Deepak Pathak (c) 2016

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
# from __future__ import unicode_literals
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from glob import glob

import argparse
import numpy

parser = argparse.ArgumentParser(description='')
parser.add_argument('-s', '--source', default="pyflow.pyx", help="pyx")
parser.add_argument('-s2', '--source2', default="src/*.cpp", help="pyx2")

args = parser.parse_args()

sourcefiles = [args.source, ]
sourcefiles.extend(glob(args.source2 + "*.cpp"))
extensions = [Extension("pyflow", sourcefiles, include_dirs=[numpy.get_include()])]
setup(
    name="pyflow",
    version="1.0",
    description="Python wrapper for the Coarse2Fine Optical Flow code.",
    author="Deepak Pathak",
    ext_modules=cythonize(extensions),
    include_dirs=[numpy.get_include()]
)
