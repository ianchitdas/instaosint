from setuptools import setup, find_packages

setup(
    name='instaosint',
    version='1.0.0',
    description='Instagram OSINT tool for extracting public metadata',
    author='Anchit D',
    packages=['instaosint'],
    install_requires=[
        'requests',
        'beautifulsoup4',
        'instaloader',
    ],
    entry_points={
        'console_scripts': [
            'instaosint=instaosint.main:main',
        ],
    },
) 