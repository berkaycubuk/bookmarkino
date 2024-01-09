from setuptools import setup, find_packages

setup(
    name = 'bookmarkino',
    description = 'Simple program to save your bookmarks separate from the browser.',
    version = '1.0.0',
    author = 'Berkay Çubuk',
    author_email = 'berkay@berkaycubuk.com',
    packages = find_packages(),
    install_requires = [],
    license = 'MIT',
    entry_points = {
        'console_scripts': 'bookmarkino=bookmarkino.main:main',
    }
)
