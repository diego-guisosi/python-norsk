from distutils.core import setup

setup(
    name='words',
    version='1.0',
    py_modules=['words'],

    # metadata
    author='Diego',
    author_email='diego.guisosi@gmail.com',
    description='A module for counting words from urls',
    license='Public domain',
    keywords='example'
)

# setup.py can be used to distribute modules

# python setup.py install -> installs py_modules into python environment (it can be a virtual environment)
# python setup.py sdist --format zip -> can be used to pack py_modules. These packed modules can be unzipped
# on other systems and than installed with setup.py install
# it's also possible to install packed modules using pip install PACKED_MODULE_NAME

# the advantage on using pip is that it makes it easier to uninstall the PACKED_MODULE,
# since pip provides the uninstall command. e.g: pip uninstall PACKED_MODULE
