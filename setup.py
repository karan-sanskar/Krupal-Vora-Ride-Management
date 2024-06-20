from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ride_managment/__init__.py
from ride_managment import __version__ as version

setup(
	name="ride_managment",
	version=version,
	description="ride app",
	author="krupal vora",
	author_email="krupalvora789@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
