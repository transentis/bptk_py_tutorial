# Business Prototyping Toolkit
**System Dynamics and Agent-based Modeling In Python**

::: {.meta description="In-depth explanation of agent-based modeling"
title="BPTK Py" 
keywords="agent-based modeling, system dynamics, python, bptk, sddsl, xmile, smile, stella, ithink"}
:::

The Business Prototyping Toolkit for Python (BPTK-Py) is a computational
modeling framework that enables you to build simulation models using
System Dynamics (SD) and/or agent-based modeling (ABM) natively in
Python and manage simulation scenarios with ease.

Next to providing the necessary SD and ABM language constructs to build
models directly in Python, the framework also includes a compiler for
transpiling System Dynamics models conforming to the XMILE standard into
Python code.

This means you can build models in a XMILE-compatible visual modeling
environment (such as [iseesystems Stella](http://www.iseesystems.com))
and then use them *independently* in a Python.

## Main Features

-   The BPTK-Py framework supports System Dynamics models in XMILE
    Format, native SD models using the SD DSL and native Agent-based models. You can also build hybrid SD-ABM-Models natively in Python.
-   The objective of the framework is to let the modeller concentrate on
    building simulation models by providing a seamless interface for
    managing model settings and scenarios and for plotting simulation
    results.
-   All plotting is done using [Matplotlib](http://www.matplotlib.org).
-   Simulation results are returned as [Pandas
    dataframes](http://pandas.pydata.org).
-   Model settings and scenarios are kept in JSON files. These settings
    are automatically loaded by the framework upon initialization, as
    are the model classes themselves. This makes interactive modeling,
    coding and testing very painless, especially if using the Jupyter
    notebook environment.

## Getting Started

The best way to get started with BPTK is to read our [Quickstart](quickstart/quickstart.ipynb). You might also like the [System Dynamics Tutorial](tutorials/tutorials.md)

Our [Business Prototyping Toolkit
Meetup](https://www.transentis.com/business-prototyping-toolkit-meetup/en/)
meets online regularly. Materials and recordings from past meetups are available on the meetup page.

BPTK was also used to build our implementation of the infamous _Beer
Distribution Game_. Our [model library](/model_library/model_library.ipynb) contains simulation models of the Beergame in both System Dynamics and Agent-based versions. It also contains an illustration of how to [train reinforcement-learning algorithms to play the Beer Distribution Game](/model_library/beergame/training_ai_beergame.ipynb).

You can play the game online at [beergame.transentis.com](https://beergame.transentis.com)

Currently we are working on an _Enterprise Digital Twin_ for transentis. You can find the simulation part of the digital twin in our [model library](/model_library/enterprise_digital_twin/enterprise_digital_twin.ipynb) 

## Getting Help

BPTK-Py is developed and maintained by [transentis
labs](https://www.transentis.com/business-prototyping-toolkit/en/).
Currently the main developers are [Dr. Oliver
Grasl](https://linkedin.com/in/olivergrasl), [David
Granzin](https://linkedin.com/in/makisuo) and Dionysios Basdanis, former contributors include Ahmed Eldably, Jeremy Funk and
Dominik Schröck.

The best place to ask questions about the framework is our [Business
Prototyping Toolkit
Meetup](https://www.transentis.com/business-prototyping-toolkit-meetup/en/),
which meets online regularly.

You can also contact us any time at <support@transentis.com>, we are
always happy to help.

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

[XMILE Models](xmile/xmile.ipynb)

- [Working With XMILE System Dynamics Models](./xmile/working_with_XMILE/working_with_XMILE.ipynb)
- [Exporting Simulation Results](./xmile/exporting_simulation_results/exporting_simulation_results.ipynb)
- [Working with Arrayed Variables in XMILE Models](./xmile/xmile_arrays/xmile_arrays.ipynb)
- [Using the XMILE Compiler Standalone](./xmile/use_sd_compiler_standalone/use_sd_compiler_standalone.md)
- [Writing Computational Essays](./xmile/writing_computational_essays/writing_computational_essays.ipynb)

[Model Library](./model_library/model_library.ipynb)

- [Bass Diffusion Model](./model_library/bass_diffusion/bass_diffusion.ipynb). The classic [Bass Diffusion Model](https://en.wikipedia.org/wiki/Bass_diffusion_model) that is used to explain the dynamics of introductiong a new product or service into a market.
- [Beer Distribution Game](./model_library/beergame/beergame.ipynb). Computational notebooks, simulation models and AI training algorithms that explore the [beer distribution game](https://beergame.transentis.com) in depth.
- [Competitive Pricing Dynamics](./model_library/competitive_pricing/competitive_pricing_dynamics.ipynb) A neat little model that can be used to understand pricing dynamics.
- [Customer Acquisition](./model_library/customer_acquisition/customer_acquisition.ipynb). A model that analyses the effects of referral marketing on customer acquisition.
- [Enterprise Digital Twin](./model_library/enterprise_digital_twin/enterprise_digital_twin.ipynb). A simulation of a professional service firm that forms part of the transentis Enterprise Digital Twin. This is work in progress that accompanies our current [meetup series](https://www.transentis.com/resources/business-prototyping-toolkit-meetup)
- [Make Your Professional Service Firm Grow](./model_library/make_your_psf_grow/make_your_psf_grow.md). A model that analyses growth strategies in professional service firms.


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
* [Model](./api/api_model.md)
* [Module](./api/api_module.md)
* [Scheduler](./api/api_scheduler.md)
* [SimpleDashboard](./api/api_simpledashboard.md)
* [SimulationScenario](./api/api_simulation_scenario.md)
* [Simultaneous Scheduler](./api/api_simultaneousScheduler.md)
* [Stock](./api/api_stock.md)

[Limitations](./usage/limitations.md)

[Changelog](changelog.md)