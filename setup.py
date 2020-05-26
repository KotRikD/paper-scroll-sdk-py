import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="paperscrollsdk",
    version="1.0.0",
    author="KotRik",
    author_email="supadmin@kotrik.ru",
    description="A simple wrapper for VK game PaperScroll!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KotRikD/paper-scroll-sdk-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)