import os
import re
import sys

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
NAME = 'aioxmlrpc'
with open(os.path.join(here, 'README.rst')) as readme:
    README = readme.read()
with open(os.path.join(here, 'CHANGES.rst')) as changes:
    CHANGES = changes.read()

with open(os.path.join(here, NAME, '__init__.py')) as version:
    VERSION = re.compile(r".*__version__ = '(.*?)'",
                         re.S).match(version.read()).group(1)


requires = ['httpx']

setup(name=NAME,
      version=VERSION,
      description='XML-RPC client for asyncio',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License'
          ],
      author='Guillaume Gauvrit',
      author_email='guillaume@gauvr.it',
      url='https://github.com/mardiros/aioxmlrpc',
      keywords='asyncio xml-rpc rpc',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='{}.tests'.format(NAME),
      install_requires=requires
      )
