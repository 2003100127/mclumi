# Installation

## System Requirement

There is no requirement for mclUMI, a cross-platform package.

## PyPI

[mclumi homepage](https://pypi.org/project/mclumi/)

```shell
# create a conda environment
conda create --name mclumi python=3.11

# activate the conda environment
conda activate mclumi

# the latest version
pip install mclumi --upgrade
```

## Conda

[mclumi homepage on Anaconda](https://anaconda.org/Jianfeng_Sun/mclumi)

```shell
# create a conda environment
conda create --name mclumi python=3.11

# activate the conda environment
conda activate mclumi

# the latest version
conda install jianfeng_sun::mclumi
```


## Docker

[mclumi homepage on Docker](https://hub.docker.com/r/2003100127/mclumi)

```shell
docker pull 2003100127/mclumi
```


## Github

[mclumi homepage on Github](https://github.com/2003100127/mclumi)

```shell
# create a conda environment
conda create --name mclumi python=3.11

# activate the conda environment
conda activate mclumi

# create a folder
mkdir project

# go to the folder
cd project

# fetch mclUMI repository with the latest version
git clone https://github.com/2003100127/mclumi.git

# enter this repository
cd mclumi

# do the following command
pip install .
# or
python setup.py install
```
