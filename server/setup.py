#!/usr/bin/env python3

'''Ejemplo de API REST para ADI'''

from setuptools import setup

setup(
    name='restdir',
    version='0.1',
    author= 'Rosa Álvarez, Jose Miguel Moreno',
    description=__doc__,
    packages=['restdir', 'restdir_script'],
    entry_points={
        'console_scripts': [
            'restdir_server=restdir_script.server:main',
        ]
    }
)