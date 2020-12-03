from setuptools import setup, find_packages
import os

cwd = os.path.abspath(os.path.dirname(__file__))

setup(
    name='objtree',
    version='0.5.0',
    description="tree but for Objective-C messages",
    author='hot3eed',
    author_email='hot3eed@gmail.com',
    install_requires=[
        'frida-tools >= 9.0.0, < 10.0.0',
    ],
    license='Apache License 2.0',
    keywords='dynamic-instrumentation ios macos frida debugger',
    packages=find_packages(),
    package_data={
        'objtree': [os.path.join(cwd, './_agent.js')]
    },
    entry_points={
        'console_scripts': [
            'objtree=objtree.cli:main'
        ]
    }
)
