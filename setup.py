from setuptools import find_packages, setup



setup(
    name='smutils',
    version='0.1.1e',
    packages=find_packages(include=['smutils']),
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
