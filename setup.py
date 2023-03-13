
from setuptools find packages,setup

setup(
  name="mlproject",
  version="0.0.1",
  author="Umesh Tiwari"
  packages=find_packages(),
  install_requires = ["pandas","numpy","seaborn"]
)
