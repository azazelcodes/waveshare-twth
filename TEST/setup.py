from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Waveshare 2.13" Wrapper'
LONG_DESCRIPTION = 'Communicate with the Waveeshare 2.13" with ease!'

# Setting up
setup(
        name="wsh213", 
        version=VERSION,
        author="Azazel",
        author_email="azazel.codes@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['RPi.GPIO', 'spidev'],
        
        keywords=['rpi', 'waveshare', 'display', '2.13"', 'epaper'],
)