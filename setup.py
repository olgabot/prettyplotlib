from distutils.core import setup

setup(
    name='prettyplotlib',
    version='0.1.1',
    author='Olga B. Botvinnik',
    author_email='olga.botvinnik@gmail.com',
    packages=['prettyplotlib'],
    license='LICENSE.txt',
    url='http://github.com/olgabot/prettyplotlib',
    description='Painlessly create beautiful default `matplotlib` plots.',
    long_description=open('README.md').read(),
    install_requires=['matplotlib >= 1.2.1',
              'brewer2mpl >= 1.3.1']
)
