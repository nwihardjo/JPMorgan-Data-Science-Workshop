# Introduction to Data Science

## Useful links for the day

* link to content that will be used for the day: https://s3-eu-west-1.amazonaws.com/com.cambridgespark.content/pub/introDS_content.zip 
* link to (encrypted) competition data: https://s3-eu-west-1.amazonaws.com/com.cambridgespark.datasets/kick.zip the password will be revealed at the start of the competition

## Preparing for the weekend

For the workshop, you will need to bring your own laptop (see setup instructions further down).

Download this repository and put it somewhere appropriate on your computer. 
Bookmark the address of the repository as we will use it to share additional files on the day. 
In it, you will find the following files to help you prepare for the day:

* `introDS_warmup.ipynb` a Jupyter notebook that runs through the python commands we will use during the weekend. We will not use classes but we will use lists manipulations, as well as `numpy` and `matplotlib`. 
If you haven't used those before we strongly recommend you go through this notebook and read up on those topics (otherwise you *will* struggle).

**Note**: we will use Jupyter notebook throughout the day. If you've never used a Jupyter notebook before, read [this tutorial](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html).

## Setup Instructions

### Advanced python users

If you use Python on a regular basis and are familiar with the way Python environments work, you can skip these instructions. 
Just bear in mind that we will use Python 3 syntax so that if you prefer using Python 2.7, you'll have to remember to write

```python
from __future__ import print_function, division
```

at the beginning of your notebooks to make sure everything is compatible. 
Also please upgrade the following libraries to their latest versions:

* pandas
* numpy
* matplotlib
* sklearn
* scipy
* seaborn

use

```bash
(sudo) pip --upgrade numpy
```

or if you don't have the library

```bash
(sudo) pip install numpy
```

where `sudo` may be required for Linux and Mac users (if you get an error about access rights).

### New/Intermediate python users

If you haven't already, please install the latest version of [Anaconda](https://www.continuum.io/downloads) with Python 3.6. Note that:

* if you already have some pre-existing, older, installation of Anaconda, we recommend uninstalling that one first and installing the latest one. If you have another existing Python setup like WinPython or Enthought Canopy, we still strongly recommend you install Anaconda so that everyone works in the same environment.
* we will use Python 3 conventions. If you have learned a bit of Python 2, don't worry, most of it will look very similar.
* if you encounter an issue, have a look [here](https://docs.continuum.io/anaconda/faq) to see if it hasn't been answered already.

Once you have installed Anaconda,

* (Windows) launch the `conda prompt` and navigate (using `cd`) to the course folder. Write `jupyter notebook`
* (Mac, Linux) in your terminal, navigate to the course folder and write `jupyter notebook`

this will launch a web browser and you will be able to launch the `introDS_warmup.ipynb` notebook.

## Contacts

* Logistics: lucy@cambridgespark.com
