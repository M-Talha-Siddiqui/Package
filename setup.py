from setuptools import setup, find_packages

setup(
    name = "PyGeo", 
    version = "0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where= "src"),
#    install_requires=["pytest"],
    install_requires=["numpy"],
    extras_require={'dev': ['pytest']},
)
#install_requires tell the packages what other libraries or packages to install , which will be used in the package
#extra_requires is used for packages which is only requires for development , since we have no regural requirement yet
