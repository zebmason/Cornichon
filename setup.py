import setuptools
import os
import os.path


def SubDirecs(direc, pre):
    list = []
    for sub in os.listdir(direc):
        if sub == "__pycache__":
            continue
        path = os.path.join(direc, sub)
        if not os.path.isdir(path):
            continue
        list.append(pre + sub)
    return list


with open("README.md", "r") as fh:
    long_description = fh.read()

packages = ["cornichon"]
root = os.path.dirname(__file__)
packages.extend(SubDirecs(os.path.join(root, "cornichon"), "cornichon/"))

setuptools.setup(
    name="cornichon",
    version="0.9.5",
    author="Zeb Mason",
    author_email="consulting@cyclerouter.co.uk",
    maintainer="Zeb Mason",
    maintainer_email="consulting@cyclerouter.co.uk",
    license="LGPL v2",
    description="A small Gherkin DSL parser that generates stub code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zebmason/Cornichon",
    packages=packages,
    classifiers=[
        "Framework :: Pytest",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Testing :: BDD",
        "Topic :: Text Processing",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Programming Language :: C#",
        "Programming Language :: C++",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Visual Basic",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires='>=3.0.0',
)
