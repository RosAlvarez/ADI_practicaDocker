#!/usr/bin/env python3

'''Ejemplo de API REST para ADI'''

from setuptools import setup

setup(
    name='src',
    version='0.1',
    author= 'Rosa Álvarez, Jose Miguel Moreno',
    description=__doc__,
    packages=['src'],
    entry_points={
        'console_scripts': [
            'restdir_client=client_script.server:main',
        ]
    }
)