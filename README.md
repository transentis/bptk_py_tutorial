# Overview Of The BPTK-Py Tutorial

This tutorial contain sample agent-based and System Dynamics models along with Jupyter notebooks that illustrate the features of the BPTK-Py framework. This tutorial is designed as a companion to the [BPTK-Py online documentation](http://bptk.transentis.com).

## Installation

### Using Docker

If you have Docker installed (e.g. Docker Desktop on MacOS or on Windows), follow these steps:

1. On the command line, move into a directory where you would like to store the BPTK-Py tutorial. 
2. Clone this repository: ```git clone https://github.com/transentis/bptk_py_tutorial.git```
3. Run ```docker-compose up```
4. Point your browser at [http://localhost:8888](http://localhost:8888) – this will open JupyterLab showing the contents of your directory. 
5. Open the notebook ```readme.ipynb``` from within JupyterLab.
6. When you are finished, close your browser and call ```docker-compose down``` from within your directory. This will stop and remove the container.

### Using a virtual environment

First, make sure you have Python 3 installed on your machine.

Then follow these steps:

1. On the command line, move into a directory where you would like to store the BPTK-Py tutorial. 
2. Clone this repository: ```git clone https://github.com/transentis/bptk_py_tutorial.git```
3. Install a virtual environment in that directory: ```python3 -m venv venv```
4. Activate the virtual environment: ```source venv/bin/activate``` (MacOS/Linux) or ```venv\scripts\activate.bat``` (Windows)
5. Install the necessary python modules: ```pip install -r requirements.txt```
6. Start JupyerLab: ```jupyter lab```
7. Your browser will open showing JupyterLab and your chosen directory
8. Open the notebook ```readme.ipynb``` from within JupyterLab

## Getting Started

This tutorial contains a number of Jupyter notebooks that illustrate usage of the BPTK-Py framework. Which one to get started with depends on whether you are interested in Agent-based modeling, in System Dynamics using XMILE (e.g. using Stella Architect or iThink) or in our domain-specific language for System Dynamics (SD DSL):

* _Agent-based Modeling_ – start with [Agent-based Modeling with BPTK-Py](abm/in-depth/in_depth_agent_based_modeling/in_depth_agent_based_modeling.ipynb)
* _SD with XMILE_ – start with [Working With XMILE System Dynamics Models](xmile/how-to/how_to_working_with_xmile/how_to_working_with_XMILE.ipynb)
* _SD DSL_ – start with [A Simple Python Library for System Dynamics](sd-dsl/in-depth/in_depth_simple_python_library_sd_dsl/in_depth_simple_python_library_sd_dsl.ipynb)

## Contents

* __Step by Step Guides__
    * [Introduction to System Dynamics with Python](step-by-step-guides/introduction_sd_dsl/introduction_sd_dsl.ipynb). Introduction to System Dynamics using the SD DSL, for those new to dynamic modeling.
* __General Information on The Framework__
    * In Depth Discussions
        * [The Architecture of the BPTK-Py Framework](general/in-depth/in_depth_bptk_py_architecture/in_depth_bptk_py_architecture.ipynb) Explains the overall architecture of the BPTK-Py framework.
        * [Scenarios In Depth](general/in-depth/in_depth_scenarios/in_depth_scenarios.ipynb) Explains the scenario definition format and how to add and manipulate scenarios at run-time.
    * HOW TOs
        * [How To: Accessing Raw Simulation Results](general/how-to/how_to_accessing_raw_simulation_results/how_to_accessing_raw_simulation_results.ipynb) Explains how to access raw simulation results with scenarios.
        * [How To: Advanced Plotting Features](general/how-to/how_to_advanced_plotting_features/how_to_advanced_plotting_features.ipynb) Discusses some advanced features of the `bptk.plot_scenarios` method.
        * [How To:  Develop Dashboards Using the SimpleDashboard Utility Class](general/how-to/how_to_develop_dashboards_using_simpledashboard/how_to_developing_dashboards_using_simpledashboard.ipynb). Shows how do build simple interactive dashboards using the `bptk.dashboard` method.
        * [How To: Develop Dashboards Using Jupyter Widgets](general/how-to/how_to_develop_dashboards_using_jupyter_widgets/how_to_developing_dashboards_using_juypter_widgets.ipynb) Explains how to develop more advanced user interfaces using Jupyter Widgets, Pandas dataframes and Matplotlib.
        * [How To: Persist BPTK-Server State](general/how-to/how_to_external_state/how_to_external_state.ipynb) Show how to persist the state of BptkServer using an ExternalStateAdapter.
* __Agent-based Modeling__
    * In Depth Discussions
        * [Agent-based Modeling with BPTK-Py](abm/in-depth/in_depth_agent_based_modeling/in_depth_agent_based_modeling.ipynb) Illustrates how to create an agent-based implementation of a simple project management model.
* __System Dynamics using XMILE__
    * In Depth Discussions
        * [Writing Computational Essays Using Simulation Models](xmile/in-depth/writing_computational_essays/writing_computational_essays.ipynb). Introduction to writing Computational Essays around System Dynamics models created using the XMILE Standard (e.g. using  ®Stella or ®iThink).
    * HOW TOs
        * [How To: Working With XMILE System Dynamics Models](xmile/how-to/how_to_working_with_xmile/how_to_working_with_XMILE.ipynb) Illustrates the quickest route to importing a System Dynamics model stored in the XMILE format, such as those created with ®Stella (*.stmx) or ®iThink (*.itmx).
        * [How To: Exporting Simulation Results](xmile/how-to/how_to_exporting_simulation_results/how_to_exporting_simulation_results.ipynb) Explains how to export simulation results into a spreadsheet.
        * [How To: Working with Arrayed Variables in XMILE Models](xmile/how-to/how_to_xmile_arrays/how_to_XMILE_arrays.ipynb) Explains how to use arrayed operators aund functions in BPTK_Py
        
* __System Dynamics using SD DSL__
    * In Depth Discussions
        * [A Simple Python Library for System Dynamics](sd-dsl/in-depth/in_depth_simple_python_library_sd_dsl/in_depth_simple_python_library_sd_dsl.ipynb). Introduction to building System Dynamics models directly in Juptyer Notebooks, using SD DSL, a specially created domain specific language for System Dynamics, that is part of BPTK-Py.
        * [SD DSL Functions](sd-dsl/in-depth/in_depth_sd_dsl_functions/in_depth_sd_dsl_functions.ipynb) An overview of how to use the SD DSL operators such as MIN, MAX and DELAY.
    * HOW TOs
        * [How To: Creating User Defined Functions in SD Models](sd-dsl/how-to/how_to_sd_user_defined_functions/how_to_sd_user_defined_functions.ipynb) Explains how to create user defined functions in SD models.  
    
## Learning More About System Dynamics and Agent-based Modeling

The main objective of this tutorial is to show you how to use the BPTK-Py framework and not to explain System Dynamics or Agent-based modeling. 

For those new to dynamic modeling, we have included a small step-by-step [Introduction to System Dynamics with Python](step-by-step-guides/introduction_sd_dsl/introduction_sd_dsl.ipynb).

You can also find further introductions on our blog:

* [Step-by-step introduction to System Dynamics](https://www.transentis.com/step-by-step-tutorials/introduction-to-system-dynamics/) using the simple project management model.
* Introduction to the [Bass Diffusion Model](https://www.transentis.com/causal-loop-diagramming/).
* The [Customer Acquisition Model](https://www.transentis.com/an-example-to-illustrate-the-business-prototyping-methodology) is discussed in our series of post introducing the Business Prototyping Methodology.
* Our [Business Prototyping Toolkit Meetup Group](https://www.transentis.com/business-prototyping-toolkit-meetup/en/) gathers online regularly. This is a good place to see BPTK in action, ask questions and suggest new features. We record every session and you can _view past recordings_ on the [meetup homepage](https://www.transentis.com/resources/business-prototyping-toolkit-meetup).

## Advanced Examples on GitHub

You can find more advanced examples of models and dashboards build using BPTK on GitHub:

* [COVID Simulation](https://github.com/transentis/sim-covid-19). Jupyter notebooks and dashboards illustrating the SIR model.
* [COVID Simulation Dashboard](https://github.com/transentis/sim-covid-dashboard). A web-based simulation dashboard for the COVID simulation built using our BPTK Widgets library for Javascript. View a [live version](http://www.covid-sim.com) of the dashboard online.
* [Beer Distribution Game](https://github.com/transentis/beergame). In-depth analysis of the beergame using both System Dynamics and Agent-based simulation. Includes an illustration of how to use BPTK in conjunction with reinforcement learning to train agents to play the beergame autonomously. 
* [Model Library Repository](https://github.com/transentis/bptk-model-library). A growing repository which contains a number of models that illustrate how to model socio-economic systems using Agent-based modeling, System Dynamics and BPTK.

## Get in Touch

Please let us know if you need help getting started, if you find a bug or are missing important functionality.

We are keen to hear how you use BPTK-Py – your feedback is invaluable in helping us improve BPTK-Py.

You can best reach us per e-mail at [support@transentis.com](mailto:support@transentis.com)


```python

```