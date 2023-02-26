---
title: "Installation"
description: "Explains how to install the BPTK-Py business simulation framework."
keywords: "agent-based modeling, abm, bptk, bptk-py, python, business simulation"
---

# Installation

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
Installing BPTK within your Python enviroment is simple, all you need to call is

```bash
pip install BPTK-Py
```
If you are new to BPTK-Py and maybe even Python, you should install the entire BPTK-Py tutorial – the tutorial contains a number of Juypter notebooks and both System Dynamics and Agent-based Models built with BPTK.

It is the best place to see BPTK in action.

If you are reading this documentation online at [bptk.transentis.com](https://bptk.transentis.com/usage/installation.html): This documentation was generated from the BPTK-Py Tutorial using [quarto](https://www.quarto.org).

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======

Like every piece of software, BPTK-Py and its dependencies have to be
installed correctly.

## For Advanced Users

Once you know what you are doing and yo already have a running Python
environment, you only need to call `pip install BPTK-Py` or
`pip3 install BPTK-Py`.

If you are not an advanced user, it is best to start with our BPTK-Py
tutorial, which you can clone or download from our [git
repository](https://github.com/transentis/bptk_py_tutorial/) on Github.

## Keeping BPTK-Py up-to-date

Software evolves. We regularly release new versions to add
functionality, improve the code and fix bugs. Since version 1.1.2, we
offer a seamless way for checking for updates and installing new ones.

In your favorite Python environment (we suggest Jupyter Notebook),
simply run the following code:
```python
    from BPTK_Py import bptk
    bptk = bptk()
    bptk.update()
```
The update mechanism automatically checks for a newer version and (if
necessary) downloads and installs it.

To check for the currently installed version, simple run these commands:
```python
    from BPTK_Py import bptk
    bptk = bptk()
    print(bptk.version)
```
## Installing the BPTK-Py Tutorial Using Docker

If you have Docker installed (e.g. Docker Desktop on MacOS or on
Windows), follow these steps:

1.  On the command line, move into a directory where you would like to
    store the BPTK-Py tutorial.
2.  Clone the BPTK-Py tutorial repository using git clone:
    `git clone https://github.com/transentis/bptk_py_tutorial.git`
3.  Run `docker-compose up`
4.  Point your browser at <http://localhost:8888> -- this will open
    JupyterLab showing the contents of your directory.
5.  Open the notebook `readme.ipynb` from within JupyterLab.
6.  When you are finished, close your browser and call
    `docker-compose down` from within your directory. This will stop and
    remove the container.
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master

## Installing The BPTK-Py Tutorial Starting From Scratch

Assuming you are starting from scratch, you need to perform the
following steps:

1.  Install Python
2.  Clone the BPTK-Py tutorial
3.  Set up a virtual environment
4.  Install BPTK-Py and JupyterLab
5.  Start JupyterLab

### Install Python

First of all, you need [Python](https://www.python.org/). Download the
latest version for your operating system.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
BPTK-Py was tested with Python 3.10, but should also run fine with Python 3.9
=======
BPTK-Py was tested with Python 3.9.
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
BPTK-Py was tested with Python 3.10, but should also run fine with Python 3.9
>>>>>>> master
=======
BPTK-Py was tested with Python 3.10, but should also run fine with Python 3.9
>>>>>>> master
=======
BPTK-Py was tested with Python 3.10, but should also run fine with Python 3.9
>>>>>>> master
=======
BPTK-Py was tested with Python 3.10, but should also run fine with Python 3.9
>>>>>>> master

### Clone the BPTK-Py tutorial

On the command line, move into a directory where you would like to store
the BPTK-Py tutorial.

Clone the BPTK-Py tutorial repository using `git clone`:
```python
git clone https://github.com/transentis/bptk_py_tutorial.git
```
### Set up a virtual environment

A virtual environment is a local copy of your Python distribution that
stores all packages required and does not interfere with your system\'s
packages.

Following steps are required to set up a virtual environment in a folder
called `venv`:
```python
python3 -m venv venv
```
Enter the virtual environment using one of the following commands
appropriate:

| OS                 | Command                      |
|--------------------|------------------------------|
| `UNIX/Linux/MacOS` | source venv/bin/activate     |
| `Windows`          | venv\Scripts\activate.bat    |

Now you should see \"(venv)\" at the beginning of your command prompt.

### Install BPTK-Py and JupyterLab

Now we have a virtual environment, we can install BPTK-Py and
JupyterLab:
```python
pip install -r requirements.txt
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
jupyter labextension install @jupyter-widgets/jupyterlab-manager
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
```
### Start JupyterLab

Now you have a functioning version of JupyterLab and can start working
interactively using jupyter notebooks.

Just type `jupyter lab` in the terminal to get started. This will
automatically open your browser with JupyterLab running in it, pointing
at the directory of the tutorial

Open the notebook `readme.ipynb` from within JupyterLab.

Once you are finished, close your browser and kill the JupyterLab
process in your terminal.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
## Keeping BPTK-Py up-to-date

Software evolves. We regularly release new versions to add
functionality, improve the code and fix bugs.

If you are on the command line using pip, you can update BPTK-Py as follows:

```bash
pip install --upgrade BPTK-Py
```

We also offer a seamless way for checking for updates and installing new ones from within a notebook environment such as Jupyter Lab, simply run the following code:
```python
    from BPTK_Py import bptk
    bptk = bptk()
    bptk.update()
```
The update mechanism automatically checks for a newer version and (if
necessary) downloads and installs it.

To check for the currently installed version, simple run these commands:
```python
    from BPTK_Py import bptk
    bptk = bptk()
    print(bptk.version)
```

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
## Package dependencies

If for any reason, you want to install the requirements manually or need
to know why we need the packages, here comes the list.

If you observe malfunctions in the framework and believe the reason may
be incompatibilities with newer versions of the packages, please inform
us.

We have tested the framework with Python 3.9 and above. BPTK Server
requires a version of Python \>= 3.9, other parts of the framework
should work fine with older versions of Python.

  Package name   What we use it for
  -------------- ---------------------------------------------------
  pandas         DataFrames and internal results storage
  matplotlib     Plotting environment
  ipywidgets     Widget environment for notebooks
  jinja2         Generating python classes for XMILE SD models
  parsimonious   Parsing XMILE models
  pyyaml         Using YAML to specify scenarios (instead of JSON)
  scipy          Linear interpolation for graphical functions
  numpy          Linear interpolation and required by pandas
  xlsxwriter     Exporting simulation results to CSV files
  xmltodict      Reading XMILE files
  distlib        Update checks
  flask          REST API