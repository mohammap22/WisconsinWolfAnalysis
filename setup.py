"""
importing setuptools due to 
inherant requirement of package
"""
from setuptools import setup, find_packages

with open("README.md","r") as fh:
    long_desc = fh.read()

setup(
    name='wolf_package',
    version='0.1',
    description='Modules and packages required to use our tools for working with DNR data',
    long_description=long_desc,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python 3",
        "License :: OSI Approved :: MIT License"
        ],
    install_requires=[
        'camelot-py==0.10.1',
        'debugpy==1.5.1',
        'opencv-python-headless==4.7.0.72',
        'pandas==1.5.2',
        'pylint==2.16.2',
        'scipy==1.10.0',
        'seaborn==0.12.2',
        'PyYAML>=0.2.5',
        'ghostscript==0.7',
    ],
    python_requires='>=3.9',
)


