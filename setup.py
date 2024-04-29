from setuptools import find_packages, setup

setup(
    name='best-friend',
    packages=find_packages(include=['best-friend']),
    version='0.0.1',
    description='Collection of useful classes and functions',
    author='Jan P. Hummel',
    install_requires=['pandas', 'numpy', 'scikit-learn', 'lifelines'],
    license='MIT',
)