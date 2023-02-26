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
8. Open the notebook ```readme.ipynb``` from within JupyterLab

## Getting Started

This tutorial contains a number of Jupyter notebooks that illustrate usage of the BPTK-Py framework. Which one to get started with depends on whether you are interested in Agent-based modeling, in System Dynamics using XMILE (e.g. using Stella Architect or iThink) or in our domain-specific language for System Dynamics (SD DSL).

The best place to get started is the [Quickstart](./quickstart/quickstart.ipynb), which illustrates System Dynamics and Agent-based Modeling using a simple customer acquisition model.

You might also like the [System Dynamics Tutorial](./tutorials/system_dynamics/sd_tutorial.ipynb).

Our model library contains some interesting models that you can use as a starting point for understanding System Dynamics, Agent-based Modeling and the BPTK-Framework:


* [Bass Diffusion Model](./model_library/bass_diffusion/bptk_py_bass_diffusion.ipynb). The classic [Bass Diffusion Model](https://en.wikipedia.org/wiki/Bass_diffusion_model) that is used to explain the dynamics of introductiong a new product or service into a market.
* [Competitive Pricing](./model_libary/competitive_pricing/competitive_pricing_dynamics_sd_dsl.ipynb) A neat little model that can be used to understand pricing dynamics.
* [Customer Acquisition](.model_library/customer_acquisition/customer_acquisition.ipynb). A model that analyses the effects of referral marketing on customer acquisition.
* [Make Your Professional Service Firm Grow](./model_library/make_your_psf_grow/sddsl/make_your_psf_grow_part_1.ipynb). A model that analyses growth strategies in professional service firms.

## The BPTK-Py Meetup Group

Our [Business Prototyping Toolkit Meetup Group](https://www.transentis.com/business-prototyping-toolkit-meetup/en/) gathers online regularly. This is a good place to see BPTK in action, ask questions and suggest new features. We record every session and you can _view past recordings_ on the [meetup homepage](https://www.transentis.com/resources/business-prototyping-toolkit-meetup).

## Further Examples on GitHub

You can find further examples of models and dashboards build using BPTK in the following GitHub repositories:

* [COVID Simulation](https://github.com/transentis/sim-covid-19). Jupyter notebooks and dashboards illustrating the SIR model.
* [COVID Simulation Dashboard](https://github.com/transentis/sim-covid-dashboard). A web-based simulation dashboard for the COVID simulation built using our BPTK Widgets library for Javascript. View a [live version](http://www.covid-sim.com) of the dashboard online.
* [Beer Distribution Game](https://github.com/transentis/beergame). In-depth analysis of the beergame using both System Dynamics and Agent-based simulation. Includes an illustration of how to use BPTK in conjunction with reinforcement learning to train agents to play the beergame autonomously.

## Get in Touch

Please let us know if you need help getting started, if you find a bug or are missing important functionality.

We are keen to hear how you use BPTK-Py – your feedback is invaluable in helping us improve BPTK-Py.

You can best reach us per e-mail at [support@transentis.com](mailto:support@transentis.com)
