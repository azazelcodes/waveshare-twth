from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wavesharetwth',
    version='0.0.2',
    description='Use the Waveshare 2.13" V3 easily.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/azazelcodes/wavesharetwth',
    author='Raphael Yancey',
    author_email='azazel.codes@gmail.com',
    keywords='waveshare epaper display 2.13"',
    #py_modules=["wavesharetwth"],
    packages=find_packages(),
    install_requires=['RPi.GPIO', 'spidev'],
)
