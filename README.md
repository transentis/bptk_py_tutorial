# Overview Of The BPTK-Py Tutorial

This tutorial contain sample agent-based and System Dynamics models along with Jupyter notebooks that illustrate the features of the BPTK-Py framework. This tutorial is designed as a companion to the [BPTK-Py online documentation](https://bptk.transentis.com) – the online documentation is generated from these notebooks using [quarto](https://www.quarto.org)

## Installation

First, make sure you have Python 3 installed on your machine.

Then follow these steps:

1. On the command line, move into a directory where you would like to store the BPTK-Py tutorial. 
2. Clone this repository: ```git clone https://github.com/transentis/bptk_py_tutorial.git```
3. Install a virtual environment in that directory: ```python3 -m venv venv```
4. Activate the virtual environment: ```source venv/bin/activate``` (MacOS/Linux) or `venv\scripts\activate.bat` (Windows)
5. Install the necessary python modules: ```pip install -r requirements.txt```
6. Start JupyerLab: ```jupyter lab```
7. Your browser will open showing JupyterLab and your chosen directory
8. Open the notebook ```readme.md``` from within JupyterLab

## Getting Started

This tutorial contains a number of Jupyter notebooks that illustrate usage of the BPTK-Py framework. Which one to get started with depends on whether you are interested in Agent-based modeling, in System Dynamics using XMILE (e.g. using Stella Architect or iThink) or in our domain-specific language for System Dynamics (SD DSL).

The best place to get started is the [Quickstart](./quickstart/quickstart.ipynb), which illustrates System Dynamics and Agent-based Modeling using a simple customer acquisition model.

You might also like the [System Dynamics Tutorial](./tutorials/system_dynamics/sd_tutorial.ipynb).

Our model library contains some interesting models that you can use as a starting point for understanding System Dynamics, Agent-based Modeling and the BPTK-Framework:


* [Bass Diffusion Model](./model_library/bass_diffusion/bptk_py_bass_diffusion.ipynb). The classic [Bass Diffusion Model](https://en.wikipedia.org/wiki/Bass_diffusion_model) that is used to explain the dynamics of introductiong a new product or service into a market.
* [Beer Distribution Game](./model_library/beergame/beergame.ipynb). In-depth analysis of the beergame using both System Dynamics and Agent-based simulation. Includes an illustration of how to use BPTK in conjunction with reinforcement learning to train agents to play the beergame autonomously.
* [Competitive Pricing](./model_libary/competitive_pricing/competitive_pricing_dynamics_sd_dsl.ipynb) A neat little model that can be used to understand pricing dynamics.
* [Customer Acquisition](.model_library/customer_acquisition/customer_acquisition.ipynb). A model that analyses the effects of referral marketing on customer acquisition.
* [Make Your Professional Service Firm Grow](./model_library/make_your_psf_grow/sddsl/make_your_psf_grow_part_1.ipynb). A model that analyses growth strategies in professional service firms.

## The BPTK-Py Meetup Group

Our [Business Prototyping Toolkit Meetup Group](https://www.transentis.com/business-prototyping-toolkit-meetup/en/) gathers online regularly. This is a good place to see BPTK in action, ask questions and suggest new features. We record every session and you can _view past recordings_ on the [meetup homepage](https://www.transentis.com/resources/business-prototyping-toolkit-meetup).

## Get in Touch

Please let us know if you need help getting started, if you find a bug or are missing important functionality.

We are keen to hear how you use BPTK-Py – your feedback is invaluable in helping us improve BPTK-Py.

You can best reach us per e-mail at [support@transentis.com](mailto:support@transentis.com)
## Contents

[Installation](./usage/installation.md)

[Quickstart](./quickstart/quickstart.ipynb)

[Tutorials](./tutorials/tutorials.md)

[Concepts](./concepts/concepts.ipynb)

- [Architecture of the BPTK Framework](./concepts/bptk_architecture/bptk_architecture.ipynb)
- [Scenarios in Depth](./concepts/scenarios/scenarios.ipynb)
- [Accessing Raw Simulation Results](./concepts/accessing_raw_simulation_results/accessing_raw_simulation_results.ipynb)
- [Advanced Plotting Features](./concepts/advanced_plotting_features/advanced_plotting_features.ipynb)
- [Developing Dashboards using Jupyter Widgets](./concepts/develop_dashboards_using_jupyter_widgets/developing_dashboards_using_juypter_widgets.ipynb)
- [Developing Dashboards using the SimpleDashboard Utility Class](./concepts/develop_dashboards_using_simpledashboard/develop_dashboards_using_simpledashboard.ipynb)
- [Introduction to BPTK Server](./concepts/bptk_server/bptk_server_intro.ipynb)
- [Persisting the BPTK-Server State](./concepts/external_state/external_state.html)

[Agent Based Modeling](abm/abm.ipynb)

- [Agent-based Modeling With BPTK-Py](./abm/agent_based_modeling/agent_based_modeling.ipynb)
- [Custom Data Collectors](./abm/custom_datacollectors/custom_datacollectors.ipynb)

[System Dynamics](sd-dsl/sddsl.ipynb)

- [A Simple Python Library For System Dynamics](./sd-dsl/simple_python_library_sd_dsl/simple_python_library_sd_dsl.ipynb)
- [SD DSL Functions](./sd-dsl/sd_dsl_functions/sd_dsl_functions.ipynb)
- [Creating User-defined Functions in SD Models](./sd-dsl/sd_user_defined_functions/sd_user_defined_functions.ipynb)
- [SD DSL: Under The Hood](./sd-dsl/sd_dsl_unter_the_hood/sd_dsl_under_the_hood.ipynb)
- [The Mathematics Underlying the SD DSL](./sd-dsl/sd_dsl_mathematics/sd_dsl_mathematics.ipynb)
- [Working With XMILE](./xmile/xmile.ipynb)

[Model Library](./model_library/model_library.ipynb)

- [Bass Diffusion Model](./model_library/bass_diffusion/bass_diffusion.ipynb). The classic [Bass Diffusion Model](https://en.wikipedia.org/wiki/Bass_diffusion_model) that is used to explain the dynamics of introductiong a new product or service into a market.
- [Beer Distribution Game](./model_library/beergame/beergame.ipynb). Computational notebooks, simulation models and AI training algorithms that explore the [beer distribution game](https://beergame.transentis.com) in depth.
- [Competitive Pricing Dynamics](./model_library/competitive_pricing/competitive_pricing_dynamics.ipynb) A neat little model that can be used to understand pricing dynamics.
- [Customer Acquisition](./model_library/customer_acquisition/customer_acquisition.ipynb). A model that analyses the effects of referral marketing on customer acquisition.
- [Enterprise Digital Twin](./model_library/enterprise_digital_twin/enterprise_digital_twin.ipynb). A simulation of a professional service firm that forms part of the transentis Enterprise Digital Twin. This is work in progress that accompanies our current [meetup series](https://www.transentis.com/resources/business-prototyping-toolkit-meetup)
- [Make Your Professional Service Firm Grow](./model_library/make_your_psf_grow/make_your_psf_grow.md). A model that analyses growth strategies in professional service firms.
- [System Archetypes](./model_library/system_archetypes/system_archetypes.ipynb). System Archtetypes are basic patterns of behaviour of a system. The model library provides System Dynamics models and dashboards to gain a deeper understanding of the archetypes and of how to model them.


[BPTK API](api/api.md)

* [Agent](./api/api_agent.md)
* [bptk](./api/api_bptk.md)
* [BptkServer](./api/api_bptk_server.md)
* [Biflow](./api/api_biflow.md)
* [Constant](./api/api_constant.md)
* [Converter](./api/api_converter.md)
* [DataCollector](./api/api_datacollector.md)
* [Element](./api/api_element.md)
* [Event](./api/api_event.md)
* [Flow](./api/api_flow.md)
* [Model](./api/api_model.ipynb)
* [Module](./api/api_module.ipynb)
* [Scheduler](./api/api_scheduler.md)
* [SimpleDashboard](./api/api_simpledashboard.md)
* [SimulationScenario](./api/api_simulation_scenario.md)
* [Simultaneous Scheduler](./api/api_simultaneousScheduler.md)
* [Stock](./api/api_stock.md)

[Limitations](./usage/limitations.md)

[Changelog](changelog.md)

## Further Examples on GitHub

You can find further examples of models and dashboards build using BPTK in the following GitHub repositories:

* [COVID Simulation](https://github.com/transentis/sim-covid-19). Jupyter notebooks and dashboards illustrating the SIR model.
* [COVID Simulation Dashboard](https://github.com/transentis/sim-covid-dashboard). A web-based simulation dashboard for the COVID simulation built using our BPTK Widgets library for Javascript. View a [live version](http://www.covid-sim.com) of the dashboard online.


