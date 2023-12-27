from setuptools import setup, find_packages

setup(
    name="mclumi",
    version="0.0.1",
    keywords=["pip", "mclumi"],
    description="UMI de-duplication",
    long_description="UMI de-duplication mclUMI",
    license="MIT",

    url="https://github.com/cribbslab; https://github.com/2003100127",
    author="Jianfeng Sun",
    author_email="jianfeng.sun@ndorms.ox.ac.uk",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires='>3.9',
    install_requires=[
        'pandas',
        'numpy',
        'pysam',
        'pyfastx',
        'click',
        'pyyaml',
        'scikit-learn',
        'markov_clustering==0.0.6.dev0',
        'pyfiglet==0.8.post1',
    ],
    entry_points={
        'console_scripts': [
            'mclumi=mclumi.main:main',
        ],
    }
)