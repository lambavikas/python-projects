from setuptools import setup, find_packages

setup(
    name='my-python-tutorials',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List the dependencies for your tutorials here
        # Example: 'numpy', 'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            # You can include any command-line scripts here
            # Example: 'tutorial1=my_tutorials.project1.script:main'
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A collection of Python tutorials',
    long_description='Detailed description of your tutorials',
    url='https://github.com/yourusername/my-python-tutorials',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
