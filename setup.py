from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sixty",
    version="0.1",
    author="Angel Ruiz",
    author_email="angel.ruizca@gmail.com",
    description="Python wrapper for SIXTE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ruizca/sixty",
    packages=["sixty"],
    package_dir={"sixty": "sixty"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
