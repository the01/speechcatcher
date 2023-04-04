from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='speechcatcher',
    version='0.1',
    author="Benjamin Milde",
    author_email="bmilde@users.noreply.github.com",
    description="A short description of your project",
    url="https://github.com/speechcatcher-asr/speechcatcher",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'speechcatcher=speechcatcher.speechcatcher:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
