from distutils.core import setup

setup(
    name='prettyplotlib',
    version='0.1.0',
    author='Olga B. Botvinnik',
    author_email='olga.botvinnik@gmail.com',
    packages=['prettyplotlib'],
#    scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
#    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Prettify matplotlib plots by removing "chartjunk".',
    long_description=open('README.txt').read()
)
