"""
Setup configuration for django-castle-adventure.
Portable Django app module for text adventure game.
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django-castle-adventure",
    version="1.0.0",
    author="nwheelo",
    description="Dark-humorous 80s-style text adventure game as a Django module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nestorwheelock/django-castle-adventure",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Games/Entertainment",
    ],
    python_requires=">=3.10",
    install_requires=[
        "Django>=4.2,<5.0",
    ],
    include_package_data=True,
    zip_safe=False,
)
