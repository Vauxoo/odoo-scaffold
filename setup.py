from distutils.core import setup

setup(
    name='OERP MODULE',
    version='0.0.1',
    author='Katherine Zaoral',
    author_email='kathy@vauxoo.com',
    packages=['oerp_module'],
    scripts=['bin/oerpmodule'],
    #~ url='http://pypi.python.org/pypi/.../',
    #~ license='LICENSE.txt',
    description='Creating updating openerp module tool.',
    long_description=open('README.rst').read(),
    #~ install_requires=[],
)