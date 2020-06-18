import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='payu-python',
      version='0.1.6',
      description='API wrapper for PayU written in Python',
      long_description=read('README.md'),
      url='https://github.com/dnarvaez27/payu-python',
      author='David Narvaez',
      author_email='dnarvaez27@outlook.com',
      license='MIT',
      packages=['payu'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
