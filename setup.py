"""
importing setuptools due to 
inherant requirement of package
"""
from setuptools import setup, find_packages

setup(
    name='wolf_package',
    version='0.1',
    description='Modules and packages required to use our tools for working with DNR data',
    packages=find_packages(),
    install_requires=[
        'camelot-py==0.10.1',
        'debugpy==1.5.1',
        'opencv==4.6.0',
        'pandas==1.5.2',
        'pylint==22.3.1',
        'scipy==1.10.0',
        'seaborn==0.12.2',
        'yaml==0.2.5',
        'ghostscript==0.7',
    ],
    python_requires='>=3.9',
)


