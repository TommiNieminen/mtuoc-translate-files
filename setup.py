from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name="mtuoc-translate-files",
    version="0.1",
    description="Translate files with MTUOC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tommi Nieminen (based on work by S. Thuret)",
    author_email="nieminentommi@hotmail.com",
    packages=find_packages(),
    install_requires=required_packages,
)
