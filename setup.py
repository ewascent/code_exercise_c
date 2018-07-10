"""add package setup"""
from setuptools import setup, find_packages
setup(
    name='code_exercize_c',
    version='0.1.0.0',
    packages='find_packages',
    entry_points={
        'mains':[
            'repeater = __main__:main'
        ]
    },
)
