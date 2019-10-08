import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cornichon",
    version="0.9.0",
    author="Zeb Mason",
    author_email="consulting@cyclerouter.co.uk",
    maintainer="Zeb Mason",
    maintainer_email="consulting@cyclerouter.co.uk",
    license="LGPL v2",
    description="A small Gherkin DSL parser that generates stub code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zebmason/Cornichon",
    packages=["cornichon", "cornichon/cpp", "cornichon/cs", "cornichon/py", "cornichon/vb"],
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
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Visual Basic",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires='>=3.7.0',
)
