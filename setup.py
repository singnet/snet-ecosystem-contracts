from setuptools import setup, find_namespace_packages
from os import path

PACKAGE_NAME = "snet.contracts"

version_dict = {}
with open("./version.py") as fp:
    exec(fp.read(), version_dict)

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=PACKAGE_NAME,
    version=version_dict['__version__'],
    packages=find_namespace_packages(include=['snet.*']),
    namespace_packages=['snet'],
    url='https://github.com/singnet/snet-ecosystem-contracts',
    author='SingularityNET Foundation',
    author_email='info@singularitynet.io',
    description='SingularityNET Ecosystem Contracts',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    python_requires='>=3.10',
    install_requires=[
        'web3==6.11.1',
    ],
    include_package_data=True
)
