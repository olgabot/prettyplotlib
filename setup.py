import sys

from setuptools import setup
from setuptools import find_packages


if sys.version_info[0] == 3:
    LONG_DESCRIPTION = open('README.rst', encoding='utf-8').read()
else:
    LONG_DESCRIPTION = open('README.rst').read()

if sys.version_info[0] == 3:
    REQUIREMENTS = open('requirements.txt', encoding='utf-8').readlines()
else:
    REQUIREMENTS = open('requirements.txt').readlines()

REQUIREMENTS = [req.rstrip() for req in REQUIREMENTS]

setup(
    name='prettyplotlib',
    version='0.1.5',
    author='Olga B. Botvinnik',
    author_email='olga.botvinnik@gmail.com',
    packages=find_packages(),
    license='MIT License',
    url='http://olgabot.github.io/prettyplotlib',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Scientific/Engineering'
    ],
    description='Painlessly create beautiful default `matplotlib` plots.',
    long_description=LONG_DESCRIPTION,
    install_requires=REQUIREMENTS
)
