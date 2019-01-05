"""
Copyright (c) 2019 Patrick Dill

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys

from setuptools import setup

long_desc = ""

if sys.argv[1] == "sdist":
    print("sdist")

    with open("readme.rst") as file:
        long_desc = file.read()

setup(
    name="colorguard",
    version="0.3.1",
    packages=["colorguard"],
    url="http://github.com/reshanie/colorguard",
    license="MIT",
    author="Patrick Dill",
    author_email="jamespatrickdill@gmail.com",
    description="Better bit manipulation that allows indexing, and automatic bit flags.",
    long_description=long_desc,
    requires=[],
)
