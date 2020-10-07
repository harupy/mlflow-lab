import os
import re

from setuptools import find_packages, setup

ROOT = os.path.abspath(os.path.dirname(__file__))
GITHUB_REPO_URL = "https://github.com/harupy/mlflow-lab"


def extract_version(line):
    return re.search(r'__version__ = "(.+)"', line).group(1)


def get_version():
    version_filepath = os.path.join(ROOT, "mlflow_lab", "version.py")
    with open(version_filepath) as f:
        for line in f:
            if line.startswith("__version__"):
                return extract_version(line)
    assert False


def get_readme():
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as f:
        return f.read()


def get_install_requires():
    return ["mlflow"]


def get_extra_require():
    return {"dev": ["flake8", "black", "isort", "pytest"]}


setup(
    name="mlflow-lab",
    version=get_version(),
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=get_install_requires(),
    extras_require=get_extra_require(),
    maintainer="harupy",
    maintainer_email="hkawamura0130@gmail.com",
    description="Provide experimental features for MLflow",
    url=GITHUB_REPO_URL,
    long_description=get_readme(),
    long_description_content_type="text/markdown",
)
