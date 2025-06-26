from setuptools import setup, find_packages

setup(
    name='my_python_app',
    version='0.1.16',
    packages=find_packages(),  # ✅ picks up my_app
    entry_points={
        'console_scripts': [
            'myapp = my_app.main:main',  # ✅ points to my_app/main.py
        ],
    },
    install_requires=[
        'flask',
    ]
)
