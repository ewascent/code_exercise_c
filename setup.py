"""add package setup"""
from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name='code_exercize_c',
    version='0.1.0.0',
    author="ewascent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ewascent/code_exercise_c",
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'mains':[
            'repeater = __main__:main'
        ]
    },
)
