# -*- coding:utf-8 -*-

from setuptools import find_packages, setup

README = """{{readme}}"""


setup(
    name='{{name}}',
    version='{{version}}',
    description='{{description}}',
    long_description=README,
    author='{{author}}',
    url='{{url}}',
    packages=find_packages(exclude=['tests']),
    install_requires={{requirements}},
    entry_points={
        'console_scripts': {{console_scripts}},
    },
    zip_safe=True,
    license='{{license}}',
    classifiers={{classifiers}}
)
