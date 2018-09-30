from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jmms.calculadora',
    version='v0.0.3',
    description='Example to test package with a Calculator',
    long_description=long_description,
    url='https://nexus/jmms/pysaurio',
    author='Jose Miguel Mirana',
    author_email='jmmirand@gmail.com',
    license='GNU GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
    keywords='jmms test calculator',
    packages=['jmms'],
    package_dir = {'jmmms':'jmms'},
)
