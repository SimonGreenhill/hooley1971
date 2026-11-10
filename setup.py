from setuptools import setup
import json

with open("metadata.json") as fp:
    metadata = json.load(fp)

setup(
    name="lexibank_hooley1971",
    description=metadata["title"],
    license=metadata.get("license", ""),
    url=metadata.get("url", ""),
    py_modules=["lexibank_hooley1971"],
    include_package_data=True,
    zip_safe=False,
    entry_points={"lexibank.dataset": ["hooley1971=lexibank_hooley1971:Dataset"]},
    install_requires=["pylexibank>=4.0"],
    extras_require={"test": ["pytest-cldf"]},
)
