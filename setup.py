from distutils.core import setup

setup(
    name='address_correct',
    version='1.0.0',
    packages=[''],
    url='https://github.com/chrstof/address_correct.git',
    license='BSD',
    author='Christof Petrick',
    author_email='',
    description='Program to correct erroneous addresses using google maps api',
    install_requires=[
        'python>=3.5',
        'PyQt>=5.0',
    ]
)



"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
"""