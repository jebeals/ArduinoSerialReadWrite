from setuptools import setup, find_packages

setup(
    name='SArduinoSerialReadWrite',  # Your package name
    version='0.1.0',  # Initial version
    author='Jason Beals',
    author_email='jebeals@calpoly.edu',
    description='A package for reading serial data (from Arduino) and writing to one''s computer.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # Make sure you use markdown in README
    url='https://github.com/jebeals/ArduinoSerialReadWrite',  # Link to your GitHub repo
    packages=find_packages(where="src"),  # Find all packages in the 'src' folder
    package_dir={"": "src"},  # Location of your packages (in src/)
    install_requires=[  # List your dependencies here
        'pyserial',  # Example dependency, add more as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
)

## This might bemore on track (JB  10/24 - 13:41)
# from setuptools import setup, find_packages

# setup(
#     name="SerialReadWrite",
#     version="0.1",
#     packages=find_packages(where="src"),
#     package_dir={"": "src"},
#     install_requires=[
#         # Add any dependencies here
#     ],
#     entry_points={
#         'console_scripts': [
#             'serial-reader=SerialReadWrite.SerialReader:main',
#         ],
#     }
# )
