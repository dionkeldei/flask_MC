from setuptools import setup

setup(
    name='flask_mc',
    version='0.1',
    packages=['flask_mc'],
    entry_points={
        'console_scripts': [
            'flask-mc = flask_mc.main:main',
        ],
    },
)