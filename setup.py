from setuptools import setup, find_packages
import ljpypi_test

VERSION = ljpypi_test.__version__

setup(
    name = 'ljpypi_test',
    version = VERSION,
    packages = find_packages(),
    description = "uploading python package",
    long_description = open('README.md').read(), 
    long_description_content_type = 'text/markdown',
    url = "https://github.com/Leejung8763/ljpypi_test",
    download_url = f"https://github.com/Leejung8763/ljpypi_test/archive/refs/tags/{VERSION}.tar.gz",
    author = "LJ",
    author_email = "lj.lee@nexr.com",
    keywords = ["pypi"],
    python_requires = ">=3",
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
