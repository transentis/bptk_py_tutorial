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
Distribution Game_. Our [model library](/model_library/model_library.md) contains simulation models of the Beergame in both System Dynamics and Agent-based versions. It also contains an illustration of how to [train reinforcement-learning algorithms to play the Beer Distribution Game](/model_library/beergame/training_ai_beergame.ipynb).

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

[Installation](usage/installation.md)

[Quickstart](quickstart/quickstart.ipynb)

[Tutorials](tutorials/tutorials.md)

[Concepts](concepts/concepts.md)

{{< include concepts/_concepts_content.md >}}

[Agent Based Modeling](abm/abm.md)

{{< include abm/_abm_content.md >}}

[Introduction to XMILE](xmile/xmile.md)

{{< include xmile/_xmile_content.md >}}

[Introduction to SD DSL](sd-dsl/sddsl.md)

{{< include sd-dsl/_sddsl_content.md >}}

[Model Library](model_library/model_library.md)

{{< include model_library/_model_library_content.md >}}

[BPTK API](api/api.md)

{{< include api/_api_content.md >}}

[Limitations](usage/limitations.md)

[Changelog](changelog.md)