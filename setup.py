import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyIeJs",
    version="0.0.2",
    author="Martin",
    author_email="1403951401@qq.com",
    description="Interop.SHDocVw",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/Martin-word/PyIeJs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
    ]
)