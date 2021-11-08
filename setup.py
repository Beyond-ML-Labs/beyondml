from distutils.core import setup
from mann import __version__

setup(
    name = 'mann',
    version = __version__,
    packages = ['mann', 'mann.layers', 'mann.utils'],
    author = 'Jacob Renn',
    author_email = 'jacob.renn@squared.ai',
    description = 'Package containing utilities for implementing RSN2/MANN',
    long_description = open('README.md').read()
)
