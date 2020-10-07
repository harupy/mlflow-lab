import os

from setuptools import find_packages, setup

import mlflow_lab

ROOT = os.path.abspath(os.path.dirname(__file__))
GITHUB_REPO_URL = "https://github.com/harupy/mlflow-lab"


def get_readme():
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as f:
        return f.read()


def get_install_requires():
    return ["mlflow"]


def get_extra_require():
    return {"dev": ["flake8", "black", "isort", "pytest"]}


setup(
    name="mlflow-lab",
    version=mlflow_lab.__version__,
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