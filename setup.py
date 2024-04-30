from setuptools import find_packages, setup

setup(
    name='smurtls',
    version='0.1a7',
    packages=find_packages(include=['smurtls']),
    install_requires=['pandas', 'numpy', 'scikit-learn', 'lifelines'],
    description='Collection of useful classes and functions',
    author='Jan P. Hummel',
    author_email='jan.hummel@med.uni-muenchen.de',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ]
)
