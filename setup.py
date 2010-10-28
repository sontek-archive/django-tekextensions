try: 
    from setuptools import setup
except ImportError: 
    from distutils.core import setup 

setup(
    name='django-tekextensions',
    version=__import__('tekextensions').__version__,
    description='A set of re-usable widgets and commands for django',
    long_description=open('README.markdown').read(),
    author='John Anderson',
    author_email='sontek@gmail.com',
    url='http://github.com/sontek/django-tekextensions',
    download_url='http://github.com/sontek/django-tekextensions',
    license='BSD',
    packages=['tekextensions'],
    classifiers = [
            'Framework :: Django',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
    ],
)
