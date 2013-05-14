from setuptools import setup

setup(name='Pybtex htmldiv',
    author='Massimo Santini <santini@di.unimi.it>',
    py_modules=['htmldiv'],
    version="0.2",
    entry_points = {
        'pybtex.backends': 'htmldiv = htmldiv:Backend',
    },
)
