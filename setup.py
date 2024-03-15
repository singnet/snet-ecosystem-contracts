from setuptools import setup, find_packages

PACKAGE_NAME = "snet.contracts"

version_dict = {}
with open("./version.py") as fp:
    exec(fp.read(), version_dict)

setup(
    nname=PACKAGE_NAME,
    version=version_dict['__version__'],
    packages=find_packages(include=['snet.*']),
    url='https://github.com/singnet/snet-ecosystem-contracts',
    author='SingularityNET Foundation',
    author_email='info@singularitynet.io',
    description='SingularityNET Ecosystem Contracts',
    license='MIT',
    python_requires='>=3.11',
    install_requires=[
        'web3==6.11.1',
    ],
)
