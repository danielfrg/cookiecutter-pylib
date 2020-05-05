import os
import sys
from setuptools import setup
from setuptools import find_packages
import versioneer


def read_file(filename):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(this_dir, filename)
    with open(filepath) as file:
        return file.read()

setup(
    name="{{ cookiecutter.module_name }}",
    version=versioneer.get_version(),
    description="",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    url="{{ cookiecutter.homepage }}",
    license="Apache 2.0",
    python_requires=">=3.0,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    install_requires=read_file("requirements.package.txt").splitlines(),
    keywords=["jupyter", "ipython", "widgets", "voila", "nbconvert", "dashboards"],
    packages=find_packages(),
    include_package_data=True,
    data_files=data_files,
    zip_safe=False,
    cmdclass=versioneer.get_cmdclass(),
    entry_points = {},
)
