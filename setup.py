from setuptools import setup, find_packages


setup(
    version='1.0.0',
    name='envattrs',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'attrs>=17.1.0',
    ],
    license='APLv2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6'
    ]
)
