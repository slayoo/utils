"""
the magick behind ``pip install ...``
"""
from setuptools import setup, find_packages


def get_long_description():
    """returns contents of README.md file"""
    with open("README.md", "r", encoding="utf8") as file:
        long_description = file.read()
    return long_description


setup(
    name='atmos-cloud-sim-uj-utils',
    description='utility routines used in PySDM and PyMPDATA examples and tests',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=['ipywidgets', 'IPython', 'matplotlib'],
    author='https://github.com/atmos-cloud-sim-uj/utils/graphs/contributors',
    author_email='sylwester.arabas@uj.edu.pl',
    license="GPL-3.0",
    packages=find_packages(include=['atmos_cloud_sim_uj_utils', 'atmos_clous_sim_uj_utils.*']),
    long_description=get_long_description(),
    long_description_content_type="text/markdown"
)
