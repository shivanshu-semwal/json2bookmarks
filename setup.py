import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='json2bookmarks',
    version='0.1',
    scripts=['json2bookmarks'],
    author="Shivanshu Semwal",
    description="A package to make a bookmark site from json data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shivanshu-semwal/json2bookmarks",
    packages=setuptools.find_packages(),
    install_requires=["favicon", "json", "sys"],
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
