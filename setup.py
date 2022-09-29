[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

Project_name = "OneNeuron_pypi"
user_name = "PavanJahagirdar"
name = f"{project_name}-{user_name}"
version = "0.0.1"
authors = [
  { name=user_name, email="pavanjahagirdar7@gmail.com" },
]
description = "This is the implementation of Perceptron"
readme = "README.md"

requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "https://github.com/PavanJahagirdar/OneNeuron_pypi.git"
"Bug Tracker" = f"https://github.com/PavanJahagirdar/OneNeuron_pypi/issues"

package_dir = {"", "src"},
packages = setuptools.find_packages(where = "src")
install_requires = [
    "numpy",
    "tqdm"
]