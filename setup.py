import setuptools

with open("README.md", "r") as fd:
    long_description = fd.read()

setuptools.setup(
    name="amncore",
    version="0.1",
    author="The Munshi Group",
    author_email="support@munshigroup.com",
    description="AmmuNation Framework core modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/munshigroup/amncore",
    packages=setuptools.find_packages(),
    install_requires = ['bombfuse', 'kthread'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)