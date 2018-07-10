"""add package setup"""
from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

def _parse_packages(self, value):
        """Parses `packages` option value.

        :param value:
        :rtype: list
        """
        find_directive = 'find:'

        if not value.startswith(find_directive):
            return self._parse_list(value)

        # Read function arguments from a dedicated section.
        find_kwargs = self.parse_section_packages__find(
            self.sections.get('packages.find', {}))

        from setuptools import find_packages

        return find_packages(**find_kwargs)

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
