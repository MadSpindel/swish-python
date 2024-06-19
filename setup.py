from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'LONG_DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='swish',
    version='1.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Swish Python Client Library',
    long_description=long_description,
    url='https://github.com/MadSpindel/swish-python',
    author='Fredrik Sundqvist',
    author_email='fsundqvist@gmail.com',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        "Topic :: Software Development :: Libraries :: Python Modules",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    install_requires=['requests>=2.9.1', 'schematics>=2.0.0.dev2'],
    zip_safe=False
)
