from setuptools import setup, find_packages #type: ignore[import-untyped]

VERSION = '0.0.0' 
DESCRIPTION = ''

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="verysimplemodule", 
        version=VERSION,
        author="Aberdeen Powell",
        author_email="<aberdeen.powell@gmail.com>",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)