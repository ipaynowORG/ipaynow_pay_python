import os
import sys
import warnings


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))


if sys.version_info < (2, 6):
    warnings.warn(
        'Python 2.5 is no longer officially supported by ipaynow. '
        'If you have any questions, please contact us at www.ipaynow.cn.',
        DeprecationWarning)
  

  
# Don't import ipaynow module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ipaynow'))
from version import VERSION


setup(
    name='ipaynow',
    cmdclass={'build_py': build_py},
    version=VERSION,
    description='ipaynow python bindings',
    author='ipaynow',
    author_email='www.ipaynow.com',
    url='https://payment.ipaynow.cn/',
    packages=['ipaynow'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
