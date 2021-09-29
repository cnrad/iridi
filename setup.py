import pathlib
import setuptools

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# This call to setup() does all the work
setuptools.setup(
    name="iridi",
    version="1.1.0",
    description="Beautify your command line interfaces",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cnrad/iridi",
    author="Conrad Crawford",
    author_email="hello@cnrad.dev",
    license="GNU GPL 3.0",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
)