import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sable-cloud",
    version="0.0.1",
    author="Brett",
    author_email="brett.powell@sable.cloud",
    description="Testing github actions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "app"},
    python_requires=">=3.6",
    install_requires=[
      "setuptools",
      "fastapi",
      "uvicorn"
    ]
)

