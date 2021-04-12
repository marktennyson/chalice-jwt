import io
import re

from setuptools import setup

with io.open("chalice_jwt/__init__.py", encoding="utf-8") as f:
    version = re.search(r"__version__ = \"(.+)\"", f.read()).group(1)


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="chalice-jwt",
    version=version,
    url="https://github.com/marktennyson/chalice-jwt",
    license="MIT",
    author="Aniket Sarkar",
    author_email="aniketsarkar@yahoo.com",
    description="JWT integration with Chalice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["chalice", "jwt", "json web token", 'aws'],
    packages=["chalice_jwt"],
    zip_safe=False,
    platforms="any",
    install_requires=[ 
        "PyJWT>=2.0,<3.0", 
        "chalice>=1.0,<3.0",
    ],
    extras_require={},
    python_requires=">=3.6,<4",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Chalice",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)