import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-aws-manager',
    version='0.1',
    packages=['aws_manager'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A  Django app to manage Amazon AWS servers.',
    long_description=README,
    url='https://github.com/jromich/django-aws-manager',
    author='Joe Rothermich',
    author_email='author@email.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django',
        'boto',
    ]
)

