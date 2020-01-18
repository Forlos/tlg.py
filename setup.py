from setuptools import setup, find_namespace_packages

setup(
    name="tlg.py",
    version="0.1",
    description="Convert tlg files to png",
    author="Forlos",
    author_email="forlos@disroot.org",
    packages=find_namespace_packages(),
    install_requires=["kaitaistruct", "Pillow"],
)
