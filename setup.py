import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name                            = "PyGoogleNb",
    version                         = "1.1.0",
    author                          = "niba291",
    author_email                    = "nibaldochavezp@gmail.com",
    description                     = "API google",
    url                             = "https://github.com/niba291/PyDrive",
    license                         = "MIT",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    package_dir                     = {"": "src"},
    packages                        = setuptools.find_packages(where="src"),
    classifiers                     = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # install_requires                = ["google-api-python-client >= 2.116.0", "google >= 3.0.0"]
)