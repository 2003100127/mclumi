<h1 align="center">
    <img src="https://github.com/2003100127/mclumi/blob/main/img/mclumi-logo-trans.png?raw=true" width="200" height="124">
    <br>
</h1>



[![Anaconda-Server Badge](https://anaconda.org/jianfeng_sun/mclumi/badges/latest_release_date.svg)](https://anaconda.org/jianfeng_sun/mclumi)
![PyPI](https://img.shields.io/pypi/v/mclumi?logo=PyPI)
![Docker Image Version (latest)](https://img.shields.io/docker/v/2003100127/mclumi)
![Docker Pulls](https://img.shields.io/docker/pulls/2003100127/mclumi)
[![Anaconda-Server Badge](https://anaconda.org/jianfeng_sun/mclumi/badges/version.svg)](https://anaconda.org/jianfeng_sun/mclumi)
![](https://img.shields.io/docker/automated/2003100127/mclumi.svg)
![](https://img.shields.io/github/stars/2003100127/mclumi?logo=GitHub&color=blue)
[![Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=for-the-badge&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
[![Downloads](https://pepy.tech/badge/mclumi)](https://pepy.tech/project/mclumi)

<hr>

#### Platform

![Python](https://img.shields.io/badge/-Python-000?&logo=Python)
![Docker](https://img.shields.io/badge/-Docker-000?&logo=Docker)
![Anaconda](https://img.shields.io/badge/-Anaconda-000?&logo=Anaconda)
![PyPI](https://img.shields.io/badge/-PyPI-000?&logo=PyPI)

###### tags: `UMI deduplication` `PCR artefacts` `scRNA-seq` `bulk RNA-seq`

```yaml
                   ____  ____  _______
   ____ ___  _____/ / / / /  |/  /  _/
  / __ `__ \/ ___/ / / / / /|_/ // /  
 / / / / / / /__/ / /_/ / /  / // /   
/_/ /_/ /_/\___/_/\____/_/  /_/___/
```
## Overview
mclUMI is developed by the Markov clustering (MCL) network-based algorithm for deduplicating redundant UMIs and thus removing PCR duplicates. mclUMI enables construction of sub-graphs where UMI nodes are relatively strongly connected.

## 📔 Documentation
Please check https://2003100127.github.io/mclumi for how to use mclUMI.

## 🛠️ Installation Steps

mclUMI can be installed in the following ways.

* ![PyPI](https://img.shields.io/badge/-PyPI-000?&logo=PyPI) (https://pypi.org/project/mclumi)

  ``` shell
  conda create --name mclumi python=3.11
      
  conda activate mclumi
  
  pip install mclumi --upgrade
  ```
  
* ![Anaconda](https://img.shields.io/badge/-Anaconda-000?&logo=Anaconda) (https://anaconda.org/Jianfeng_Sun/mclumi)

  ``` shell
  conda create --name mclumi python=3.11
      
  conda activate mclumi
  
  conda install -c jianfeng_sun mclumi
  ```
  
* ![Docker](https://img.shields.io/badge/-Docker-000?&logo=Docker) (https://hub.docker.com/repository/docker/2003100127/mclumi/general)

  ``` shell
  docker pull 2003100127/mclumi:latest
  ```

* ![Github](https://img.shields.io/badge/-Github-000?&logo=Github)

  ``` shell
  conda create --name mclumi python=3.11
    
  conda activate mclumi
  
  git clone https://github.com/2003100127/mclumi.git
  
  cd mclumi
  
  pip install .
  ```

## 🚀 Get started



* shell

    ``` shell
    # convert example.bam to example_bundle.bam in bundle forms as in UMI-tools.
    mclumi bundle -m umi-tools -bfpn ./mclumi/data/example.bam -wd ./mclumi/data/ -vb True

    # deduplicate UMIs
    mclumi loci -m mcl -ed 1 -pfpn ./mclumi/data/params.yml -bfpn ./mclumi/data/example_bundle.bam -wd ./mclumi/data/ -vb True
    ```

* python

    ``` python
    import mclumi as mumi

    mumi.multipos.run(
        method='mcl',
        bam_fpn='example_bundle.bam',
        ed_thres=1,
        pos_tag='PO',
        work_dir='./',
        verbose=True,
    )
    ```

## 📄 Citation
``` angular2html
@article{mclumi,
    title = {mclUMI: Markov clustering of unique molecular identifiers allows removing PCR duplicates dynamically},
    author = {Jianfeng Sun and Adam P. Cribbs},
    doi = {xxx},
    url = {https://github.com/2003100127/mclumi},
    year = {2024},
}
```

## 🏠 Homepage
[📍Cribbslab](https://www.ndorms.ox.ac.uk/team/adam-cribbs) 

## 📧 Reach us
[![Linkedin Badge](https://img.shields.io/badge/-Jianfeng_Sun-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/jianfeng-sun-2ba9b1132)](https://www.linkedin.com/in/jianfeng-sun-2ba9b1132) 
[![Gmail Badge](https://img.shields.io/badge/-jianfeng.sunmt@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:jianfeng.sunmt@gmail.com)](mailto:jianfeng.sunmt@gmail.com)
[![Outlook Badge](https://img.shields.io/badge/jianfeng.sun@ndorms.ox.ac.uk--000?style=social&logo=microsoft-outlook&logoColor=0078d4&link=mailto:jianfeng.sun@ndorms.ox.ac.uk)](mailto:jianfeng.sun@ndorms.ox.ac.uk)
<a href="https://twitter.com/Jianfeng_Sunny" ><img src="https://img.shields.io/twitter/follow/Jianfeng_Sunny.svg?style=social" /> </a>