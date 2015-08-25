"""
Flask-SES
-------------

Flask extension for interfacing with AWS' SES service.
"""
from setuptools import setup


setup(
    name='Flask-SES',
    version='1.0',
    license='MIT',
    author='Stuart Robertson',
    author_email='stooie.robertson@gmail.com',
    description='Flask extension for interfacing with AWS\' SES service',
    long_description=__doc__,
    py_modules=['flask_ses'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'boto'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
