from setuptools import setup

setup(
    name='my_python_app',
    version='0.1.15',  # bump this whenever you make changes
    py_modules=['main'],  # points to your main.py
    install_requires=['flask'],
    entry_points={
        'console_scripts': [
            'myapp = main:main',
        ],
    },
)
