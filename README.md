# BPTK_Py tutorial

This tutorial repository contains example notebooks, simulation models and scenarios to get started.

It uses an interactive approach to explain you how to work with the Business Prototyping Toolkit for Python.


## Installing the BPTK_PY framework
Like every piece of software, BPTK_Py has to be installed correctly, including its dependencies. 

Assuming you are starting from scratch, you need to perform the following steps

1. Install Python
2. Install Node
3. Install BPTK_Py
4. Install JupyterLab (optional)
5. Setup a virtual environment (optional)
6. Download our BPTK_Py tutorial (optional)

### Install Python
First of all, you need [Python](https://www.python.org/). Download the latest version for your operating system. 
BPTK-Py was tested with Python 3.7, 3.6 and 3.4. 


### Install Node
Both for our sdcc compiler and also for displaying interactive widgets in Jupyter you need to install [Node.js](https://nodejs.org/en/) for your operating system.
Make sure you install npm (the node.js package manager) along with node.js. This should be done automatically when downloading and installing from the official site. 

Please follow the guide for your operating system

#### Python and Node on your favorite Linux Distribution
If you are using a Linux Distribution, you may want to use your preferred package manager for downloading Python and node:

For Ubuntu using apt:
```commandline
sudo apt update
sudo apt install nodejs python3 python3-pip
```

Other Linux distributions should have similar packages. 
You may always refer to the official websites of [Python](https://www.python.org/) and [Node.js](https://nodejs.org/en/) for help on installing on your operating system.

### Install BPTK_Py using Pip
After the prerequisites, we have to install ``BPTK_Py`` into our python environment.
This requires you to use the command shell. In windows, press ``windows + R`` and type "powershell". In Mac OS X run the Terminal app. 
Linux users may use their preferred terminal emulator.

To install the package, just type ``pip install BPTK-Py`` or ``pip3 install BPTK-Py``. Pip is a package manager that keeps Python packages up-to-date.

Pip installs the package and makes it available system-wide. It downloads all dependencies for the package automatically.

After Pip finished successfully, you are ready for working with the framework. 

If for some reason Pip is not available on your system, first download it. Regardless the operating system, this should do:
1. Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py). The file may open in your browser tab. Make sure to save it on your hard drive.
2. Install pip: in a terminal, go to the directory of the downloaded script and issue ``python3 ./get-pip.py`` and wait a minute or two.

Linux/UNIX shorthand: [1]
```commandline
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

### Install JupyterLab
Additionally, you may want to use Jupyter Lab to work interactively on the simulations - just as we do.

```
pip install jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```
Now you have a functioning version of jupyter lab and can start working 
interactively using jupyter notebooks. Just type ``jupyter lab`` in the terminal to get started.

In order to keep your system clean, you may want to use a [virtual environment](https://docs.python-guide.org/dev/virtualenvs/) instead of installing Python system-wide.

### Setup a virtual environment

A virtual environment is a local copy of your Python distribution that stores all packages required and does not interfere with your system's packages. 

Following steps are required to set up the venv and and install BPTK_Py into it:

```
pip install virtualenv
virtualenv bptk_test 

# Enter the virtual environment. In the beginning of your prompt you should see "(bptk_test)"
source bptk_test/bin/activate  #  For UNIX/Linux/Mac OS X
bptk_test\Scripts\activate.bat # For Windows

pip install BPTK-Py
pip install jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

