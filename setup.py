from setuptools import setup

setup(name='Pybtex htmldiv',
    author='Massimo Santini <santini@di.unimi.it>',
    py_modules=['htmldiv'],
    entry_points = {
        'pybtex.backends': 'htmldiv = htmldiv:Backend',
    },
)
