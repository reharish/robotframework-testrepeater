from setuptools import setup
from setuptools import find_namespace_packages
from setuptools import find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), "r") as fd:
    long_description = fd.read()

setup(
    name='robotframework-testrepeater',
    version='1.0.0',
    description='A listener to repeat testscases for given iterations.',
    license="Apache License 2.0",
    url="https://reharish.github.io/cv",
    author='reharish',
    author_email='rengarajharish@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_namespace_packages(),
    py_modules=['TestRepeater'],
    install_requires=["robotframework"],
)
