from setuptools import setup, find_packages
import versioneer


setup(
    name='Kalman filter',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Simple implementation of Kalman Filter algorithm',
    author='Alejandro Pérez',
    install_requires=[
        "numpy",
        "jupyter",
        "matplotlib"
    ],
)