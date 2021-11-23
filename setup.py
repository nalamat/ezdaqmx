#!/usr/bin/env python

from distutils.core import setup

setup(
    name='ezdaqmx',
    version='1.0',
    description='No-brainer object-oriented interface for NI DAQ devices',
    author='Nima Alamatsaz',
    author_email='nima.alamatsaz@gmail.com',
    url='https://github.com/nalamat/ezdaqmx',
    py_modules=['ezdaqmx'],
    install_requires=[
        'numpy',
        'scipy',
        'pydaqmx',
        'pype',
        ],
    )
