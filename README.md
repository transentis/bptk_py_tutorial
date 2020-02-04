# BPTK-Py Tutorial

This tutorial contain sample agent-based and System Dynamics models along with Jupyter notebooks that illustrate the features of the BPTK-Py framework. This tutorial is designed as a companion to the [BPTK-Py online documentation](http://bptk.transentis-labs.com).

## Installation

### Using Docker

If you have Docker installed (e.g. Docker Desktop on MacOS or on Windows), follow these steps:

1. On the command line, move into a directory where you would like to store the BPTK-Py tutorial. 
2. Clone this repository: ```git clone https://github.com/transentis/bptk_py_tutorial.git```
3. Run ```docker-compose up```
4. Point your browser at [http://localhost:8888](http://localhost:8888) – this will open JupyterLab showing a "work" directory in the file browser. This directory is mapped to your working directory. 
5. Open the notebook ```readme.ipynb``` from within JupyterLab to get started.
6. When you are finished, close your browser and call ```docker-compose down``` from within your directory. This will stop and remove your containers.

### Using a virtual environment

First, make sure you have Python 3 installed on your machine.

Then follow these steps:

1. On the command line, move into a directory where you would like to store the BPTK-Py tutorial. 
2. Clone this repository: ```git clone https://github.com/transentis/bptk_py_tutorial.git```
3. Install a virtual environment in that directory: ```python3 -m venv venv```
4. Activate the virtual environment: ```source venv/bin/activate``` (MacOS/Linux) or ``venv\scripts\activate.bat``` (Windows)
5. Install the necessary python modules: ```pip install -r requirements.txt```
6. Start JupyerLab: ```jupyter lab```
7. Your browser will open showing JupyterLab and your chosen directory
8. Open the notebook ```readme.ipynb``` from within JupyterLab

## Getting Started

The tutorial contains a number of noteboos and models. Which one to get started with depends on whether you are interested in Agent-based modeling, in System Dynamics using XMILE (e.g. Stella Architect or iThink) or in the System Dynamics DSL:

* _Agent-based Modeling_ – start with [Agent-based Modeling with BPTK-Py](notebooks/abm/in-depth/in_depth_agent_based_modeling.ipynb)
* _SD with XMILE_ – start with [Working With XMILE System Dynamics Models](notebooks/xmile/how-to/how_to_working_with_XMILE.ipynb)
* _SD DSL_ – start with [A Simple Python Library for System Dynamics](notebooks/sd-dsl/in-depth/in_depth_simple_python_library_sd_dsl/in_depth_simple_python_library_sd_dsl.ipynb)


## Contents

We illustrate the BPTK-Py framework using three simple models:

* __Simple Project Management Model__. This model is an illustration of [Parkinson's law](https://en.wikipedia.org/wiki/Parkinson%27s_law), which states that work expands so as to fill the time available for its completion. 
* __Bass Diffusion Model__. This model is an implementation of the [Bass diffusion model](https://en.wikipedia.org/wiki/Bass_diffusion_model) originally created by [Frank Bass](https://en.wikipedia.org/wiki/Frank_Bass) that describes the process of how new products get adopted in a population. The Bass model has been widely used in forecasting, especially new products' sales forecasting and technology forecasting.
* __Customer Acquisition Model__. A small model about referral marketing that builds upon the Bass Diffusion Model.

Here is an overview of the documents contained in this tutorial, they all use at least one of the models listed above.

* __General Information on The Framework__
    * In Depth Discussions
        * [The Architecture of the BPTK-Py Framework](notebooks/general/in-depth/in_depth_bptk_py_architecture/in_depth_bptk_py_architecture.ipynb) Explains the overall architecture of the BPTK-Py framework.
        * [Scenarios In Depth](notebooks/general/in-depth/in_depth_scenarios.ipynb) Explains the scenario definition format and how to add and manipulate scenarios at run-time.
    * HOW TOs
        * [How To: Accessing Raw Simulation Results](notebooks/general/how-to/how_to_accessing_raw_simulation_results.ipynb) Explains how to access raw simulation results with scenarios.
        * [How To: Advanced Plotting Features](notebooks/general/how-to/how_to_advanced_plotting_features.ipynb) Discusses some advanced features of the `bptk.plot_scenarios` method.
        * [How To: Building Interactive Dashboards](notebooks/general/how-to/how_to_interactive_dashboards.ipynb). Shows how do build simple interactive dashboards using the `bptk.dashboard` method.
        * [How To: Developing Advanced User-Interfaces](notebooks/general/how-to/how_to_developing_advanced_user_interfaces.ipynb) Explains how to develop more advanced user interfaces using Jupyter Widgets, Pandas dataframes and Matplotlib.
        * [How To: Writing Tests For Models](notebooks/general/how-to/how_to_writing_tests_for_models.ipynb) Explains how to write model tests using the `bptk.model_check` method.
* __Agent-based Modeling__
    * In Depth Discussions
        * [Agent-based Modeling with BPTK-Py](notebooks/abm/in-depth/in_depth_agent_based_modeling.ipynb) Illustrates how to create an agent-based implementation of a simple project management model.
* __System Dynamics using XMILE__
    * In Depth Discussions
        * [Writing Computational Essays Using Simulation Models](notebooks/xmile/in-depth/writing_computational_essays/writing_computational_essays.ipynb). Introduction to writing Computational Essays around System Dynamics models created using the XMILE Standard (e.g. using  ®Stella or ®iThink).
    * HOW TOs
        * [How To: Working With XMILE System Dynamics Models](notebooks/xmile/how-to/how_to_working_with_XMILE.ipynb) Illustrates the quickest route to importing a System Dynamics model stored in the XMILE format, such as those created with ®Stella (*.stmx) or ®iThink (*.itmx).
        * [How To: Exporting Simulation Results](notebooks/xmile/how-to/how_to_exporting_simulation_results.ipynb) Explains how to export simulation results into a spreadsheet.
        * [How To: Modifying Models At Runtime](notebooks/xmile/how-to/how_to_modifying_models_at_runtime.ipynb) Explain how to modify models that have been transpiled from XMILE models at runtime.
* __System Dynamics using SD DSL__
    * In Depth Discussions
        * [A Simple Python Library for System Dynamics](notebooks/sd-dsl/in-depth/in_depth_simple_python_library_sd_dsl/in_depth_simple_python_library_sd_dsl.ipynb). Introduction to building System Dynamics models directly in Juptyer Notebooks, using SD DSL, a specially created domain specific language for System Dynamics, that is part of BPTK-Py.
        * [SD DSL Functions](notebooks/sd-dsl/in-depth/in_depth_sd_dsl_functions/in_depth_sd_dsl_functions.ipynb) An overview of how to use the SD DSL operators such as MIN, MAX and DELAY.
    * HOW TOs
        * [How To: Creating User Defined Functions in SD Models](notebooks/sd-dsl/how-to/how_to_sd_user_defined_functions.ipynb) Explains how to create user defined functions in SD models.
    
  
## Learning More About System Dynamics and Agent-based Modeling

The objective of this tutorial is to show you how to use the BPTK-Py framework and not to explain System Dynamics or Agent-based modeling. If you want to learn more about the techniques themselves, please refer to our blog:

* [Step-by-step introduction to System Dynamics](https://www.transentis.com/step-by-step-tutorials/introduction-to-system-dynamics/) using the simple project management model.
* Introduction to the [Bass Diffusion Model](https://www.transentis.com/causal-loop-diagramming/).
* The [Customer Acquisition Model](https://www.transentis.com/an-example-to-illustrate-the-business-prototyping-methodology) is discussed in our series of post introducing the Business Prototyping Methodology.

## Get in Touch

Please let us know if you need help getting started, if you find a bug or are missing important functionality.

We are keen to hear how you use BPTK-Py – your feedback is invaluable in helping us improve BPTK-Py.

You can best reach us per e-mail at [support@transentis.com](mailto:support@transentis.com)

