from setuptools import setup. find_packages

setup(
    name="milib-example",
    version="0.0.1",
    author="Veronica",
    author_email="tuemail@ejemplo.com",
    description="Una libreria de prueba para subir a nexus",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)