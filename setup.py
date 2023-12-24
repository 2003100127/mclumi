from setuptools import setup, find_packages

setup(
    name="mclumi",
    version="0.0.1",
    keywords=("pip", "mclUMI"),
    description="mclUMI",
    long_description="UMI de-duplication using mclUMI",
    license="MIT",

    url="https://github.com/cribbslab; https://github.com/2003100127",
    author="Jianfeng Sun",
    author_email="jianfeng.sun@ndorms.ox.ac.uk",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires='>3.6',
    install_requires=[
        'pandas', # 1.3.3
        'numpy', # 1.22.0
        'pysam', # 0.17.0
        'pyfastx',
        'markov_clustering==0.0.6.dev0',
        'networkx==2.6.3',
        'pyfiglet==0.8.post1',
    ],
    entry_points={
        'console_scripts': [
            'mclumi=mclumi.main:main',
        ],
    }
)