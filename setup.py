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
    packages=["hooley1971_commands"],
    entry_points={
        "lexibank.dataset": ["hooley1971=lexibank_hooley1971:Dataset"],
        "cldfbench.commands": ["hooley1971=hooley1971_commands"],
    },
    install_requires=["pylexibank>=4.0", "nexusmaker"],
    extras_require={"test": ["pytest-cldf"]},
)
