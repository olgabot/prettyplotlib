from setuptools import setup
from setuptools import find_packages

setup(
    name='prettyplotlib',
    version='0.1.3',
    author='Olga B. Botvinnik',
    author_email='olga.botvinnik@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    url='http://olgabot.github.io/prettyplotlib',
    description='Painlessly create beautiful default `matplotlib` plots.',
    long_description=open('README.txt').read(),
    install_requires=['matplotlib >= 1.2.1',
              'brewer2mpl >= 1.3.1']
)
