# Writing Computational Essays Based On Simulation Models

## Using Jupyter/IPython to rapidly build interactive stories based on System Dynamics simulations

**If you want to use the insights gained from simulation models to transform your business, just having the model and the insights is often not enough – you need to develop a good story that persuades your stakeholders to make decisions and take action. Our BPTK_PY library allows you to import System Dynamics models into Jupyter/IPython and run them there.**

In my post [Telling Stories with System Dynamics Models](https://www.transentis.com/telling-stories-with-system-dynamics-models/) I introduced our approach to telling interactive stories based on simulation models built using System Dynamics. The final work products of our approach are interactive presentations that run in a browser, built using modern web-technology.

Writing such interactive stories is quite challenging, even if your simulation model is already fairly complete, because you need to craft the storyline while testing different scenarios with the simulation model.

Our experience is that while web applications are great to deploy interactive stories (because everyone has a browser), they are not suited to supporting the writing process itself, because they require quite a bit of engineering – the story really needs to be finished before you start building the web application.

We realised early on that what we needed was a tool that would help us to prototype a complex story line while still building the model:

* Build an initial simulation model using a visual modeling environment.
* Start writing a story around the model using the tool.
* Use the new questions and insights that arise during the writing process to drive experiments with the simulation model – this may lead to changes in both the model and the storyline.

In 2014 we started writing such "computational essays" using Mathematica® from [Wolfram Research](http://www.wolfram.com). Mathematica is a wonderful and very powerful tool to support this process – it is a complete environment that supports writing, computation, presentation and sophisticated interactive dashboards.

Mathematica does not contain native support for System Dynamics, but we crafted a small library that allows us to import System Dynamics models based on the XMILE standard and to run them in Mathematica (see this [blog post](https://www.transentis.com/building-interactive-stories-from-simulation-models/) for details on that).

But since 2014 a lot has happened in the world of computational modelling ... thanks to the rise of data science the Python programming language has become more and more ubiquitous, and with it the Jupyter/IPython notebook environemnt.

Both Mathematica and Jupyter/IPython are fantastic environments for creating computational essays and "story-driven simulations":

* Working with Mathematica and the Wolfram Language is incredibly productive thanks to the symbolic nature of the language and the way it integrates into the highly sophisticated Mathematica notebook environment.
* Jupyter notebooks lack the sophistication of Mathmeatica notebooks but what sets the Jupyter/IPython ecosystem appart is that it is open source (and thus free to use for everyone), highly extensible and very widely used in the data science/computational modeling community - it is thus much easier to find books, training materials and skilled resources.

Hence we decided to port our Business Prototyping Toolkit to the Jupyer/Python universe - which means we can now create simluation models using System Dynamics and let them run in Python, Wolfram Language or in Javascript.

>For a more in-depth comparison of Jupyter and Mathematica see Paul Romer's very interesting [blog post](https://paulromer.net/jupyter-mathematica-and-the-future-of-the-research-paper/) on this topic. Also be sure to read the Atlantic Article referenced by Paul Romer.

Our approach is very powerful and liberating, because it turns our models into computable objects – we can now use our simulation models in new ways, quite independently of the modeling environment in which we create the model.

Some "everyday" examples of such uses are:

* Creating and managing a comprehensive set of scenarios pertaining to a model
* Writing up a paper/report based on an SD model using Jupyter/IPython and plotting all related graphs directly in Jupyter. 
* Creating an interactive dashboard for a model
* Sharing models, dashboards and reports with people who do not have access to the original model environment.
* Comparing multiple versions of a model to each other

We provide examples for all these points later in this document.

More advanced examples for using models as computable objects are:

* creating interactive games (see our version of the [Beergame](https://www.transentis.com/understanding-the-beer-game) for a simple example using our Javascript transpiler),
* performing monte-carlo sensitivity analysis of a model on multiple machines in parallel, using state-of-the art, scalable parallel processing engines such as [Apache Spark](http://spark.apache.org)
* training machine learning algorithms using System Dynamics models.
* combining system dynamics models with other computational model techniques, such as agent based modeling.

This document demonstrates our storytelling approach using our BPTK PY framework and a very simple project management simulation. The System Dynamics model itself was built using the dynamic modeling and simulation software Stella® from [iseesystems](http://www.iseesystems.com).

We are providing the BPTK PY framework as a closed source framework under the MIT license, which means you are free to use the framework in your own modeling projects. You can download the Jupyter Notebook corresponding to this blog post  along with installation instructions and a more detailed tutorial in our [member area](https://www.transentis.com/member-area/) - please sign up to member area first if you do not have an account yet.

Stella saves models using the [XMILE format](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=xmile), which is an open XML protocol for sharing interoperable system dynamics models and simulations. The XMILE standard is governed by the OASIS standards consortium - our framework currently only supports the XMILE standard, we may create a compiler for other formats (such as Vensim® by [Ventana Systems](http://www.vensim.com)) in the future.

To illustrate how our framework works, this post uses the model from our [Step-By-Step Introduction To System Dynamics](https://www.transentis.com/step-by-step-tutorials/introduction-to-system-dynamics/).

We've included the stock and flow diagram of the entire model below – you don't need to understand how the model works to follow this post, but knowing the stock and flow structure will be useful.

![Simple Project Management Model](images/intro/simple_project_diagram.png)

The following sections illustrated various aspects of our framework and of how to use it.

* Importing the BPTK_Py Framework
* Setting Up the Scenario Manager
* Plotting Scenario Results
* Creating Interactive Simulation Dashboards
* Accessing the Underlying Model
* A Closer Look at the Underlying Equations
* Accessing Model Information
* Checking and Comparing Models

### Installation
Like every piece of software, BPTK-Py has to be installed correctly, including its dependencies. 

1. Obvisouly, you need [Python](https://www.python.org/). Download the latest version for your operating system. BPTK-Py was tested with Python 3.7, 3.6 and 3.4.
2. Install [Node.js](https://nodejs.org/en/) for your operating system. We encourage you to use Node8 due to a known bug with jupyter lab.

After the prerequisites, we have to install ``BPTK_Py`` into our python environment.
This requires you to use the command shell. In windows, press ``windows + R`` and type "powershell". In Mac OS X run the Terminal app. 
Linux users may use their preferred terminal emulator.
To install the package, just type ``pip install BPTK_Py``. Pip is a package manager that keeps Python packages up-to-date.
Pip installs the package and makes it available system-wide. It downloads all dependencies for the package automatically.
After Pip finished successfully, you are ready for working with the framework. 

Additionally, you may want to use Jupyter Lab to work interactively on the simulations - just as we do.
```
pip install jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```
Now you have a functioning version of jupyter lab and can start working 
interactively using jupyter notebooks. Just type ``jupyter lab`` in the terminal to get started.

In order to keep your system clean, you may want to use a [virtual environment](https://docs.python-guide.org/dev/virtualenvs/) instead, a local copy of your Python distribution that stores all packages required and does not interfere with your system's packages. 
Following steps are required to set up the venv and and install BPTK_Py into it:
```
pip install virtualenv
virtualenv bptk_test 

# Enter the virtual environment. In the beginning of your prompt you should see "(bptk_test)"
source bptk_test/bin/activate  #  For UNIX/Linux/Mac OS X
bptk_test\Scripts\activate.bat # For Windows

pip install BPTK_Py
pip install jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

### Importing The Framework

The Business Prototyping Toolkit for Python comes with a model transpiler, which automatically converts SD-models created with [Stella](http://www.iseesystems.com) into Python Code, a model simulator which let's you run those models in a Python environment (such as a Jupyter notebook), a simple format for defining scenarios, and some methods to plot simulation results - these methods form the BPTK API.

For most users, this will be enough initialy: you create the model using Stella and experiment with it by defining scenarios and plotting graphs in Jupyter notebooks. Whenever you change the model in Stella, the model is automatically transpiled to Python in a background process. Hence you can work on your model (in Stella) and write your computational essay (in Jupyter) in parallel.

We have found that even modelers who are new to Jupyter and Python can get productive within a few hours.

The following sections show all the code that is needed to get up and running.

More advanced users can use the full power of Jupyter and Python to access and manipulate the underlying simulation model and simulation results.

>For those of you that are new to Jupyter: Please run the code cells by pushing ``Shift + Enter``. The next code cell imports the BPTK_Py package and initializes it. This may take some time during the first run, because some necessary libraries will be downloaded from the [NPM repository](http://www.npmjs.org). 

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

To install the package, just type ``pip install BPTK_Py`` or ``pip3 install BPTK_Py``. Pip is a package manager that keeps Python packages up-to-date.

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

pip install BPTK_Py
pip install jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

 
## Package dependencies
If for any reason, you want to install the requirements manually or need to know why we need the packages, here comes the list. 

If you observe malfunctions in the framework and believe the reason may be incompatibilities with newer versions of the packages, please inform us.

So far, we tested the framework with Python 3.4, 3.6 and 3.7. It should be working fine with other Python 3.x versions.

Package name | What we use it for | Latest tested version
--- | --- | ---
pandas |DataFrames and internal results storage | 0.23.4
matplotlib |Plotting environment | 2.2.2
ipywidgets |Widget environment for notebooks | 7.4.0
scipy |Linear interpolation for graphical functions  | 1.1.0
numpy |Linear interpolation and required by pandas | 1.15.0
jupyter lab extension for jupyter-widgets |Use ipywidgets in jupyter lab | 0.36.1
