from setuptools import setup, find_packages

setup(
    name="jsonapi",
    version="0.0.1",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    author='Kun Wang',
    author_email='wang.kun6@northeastern.edu',
    description='A Python package for JSON encoding and decoding complex and range object.',
    install_requires=[],
)
