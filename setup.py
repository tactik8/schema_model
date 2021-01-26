import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="kraken-record",
    version="0.0.1",
    description="Kraken schema helper",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tactik8/schema_model",
    author="Tactik8",
    author_email="info@tactik8.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["kraken_record"],
    include_package_data=True,
    install_requires=[],
    
)
