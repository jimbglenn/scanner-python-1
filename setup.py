from setuptools import setup

setup(
    name='scanner-python-1',
    version='1.0',
    packages=[''],
    url='',
    license='',
    author='Jim Glenn',
    author_email='jimbglenn@gmail.com',
    description='Custom Scanner in Python for Brian',
    install_requires=["paramiko"],
    package_dir={"": "src"},  # Optional
    entry_points={  # Optional
        "console_scripts": [
            "scanner=main:main",
        ],
    },
)

