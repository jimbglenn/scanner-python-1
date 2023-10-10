import setuptools
from setuptools import setup

setup(
    name='scanner-python-1',
    version='1.0',
    url='',
    license='',
    author='Jim Glenn',
    author_email='jimbglenn@gmail.com',
    description='Custom Scanner in Python for Brian',
    install_requires=["paramiko"],
    packages=setuptools.find_packages(),
    scripts=['./src/scanner/scanner.py'],
    entry_points={  # Optional
        "console_scripts": [
            "scanner=scanner:scanner",
        ],
    },
)

