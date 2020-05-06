import os
import sys

from setuptools import find_packages, setup

setup_dir = os.path.abspath(os.path.dirname(__file__))


def read_file(filename):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(this_dir, filename)
    with open(filepath) as file:
        return file.read()


def parse_git(root, **kwargs):
    """
    Parse function for setuptools_scm
    """
    from setuptools_scm.git import parse

    kwargs["describe_command"] = "git describe --dirty --tags --long"
    return parse(root, **kwargs)



setup(
    name="{{ cookiecutter.module_name }}",
    packages=find_packages() + ["{{ cookiecutter.module_name }}.tests"],
    zip_safe=False,
    include_package_data=True,
    # package_data={"{{ cookiecutter.module_name }}": ["includes/*"]},
    # data_files=data_files,
    # cmdclass={"install": InstallCmd},
    # entry_points = {},
    use_scm_version={
        "root": setup_dir,
        "parse": parse_git,
        "write_to": os.path.join("{{ cookiecutter.module_name }}/_generated_version.py"),
    },
    test_suite="{{ cookiecutter.module_name }}/tests",
    setup_requires=["setuptools_scm"],
    install_requires=read_file("requirements.package.txt").splitlines(),
    tests_require=["pytest",],
    python_requires=">=3.6",
    description="",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    license="Apache License, Version 2.0",
    maintainer="{{ cookiecutter.maintainer }}",
    maintainer_email="{{ cookiecutter.author_email }}",
    url="{{ cookiecutter.home_page }}",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=[],
)
