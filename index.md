# BPTK-Py: System Dynamics and Agent-based Modeling In Python

::: {.meta description="In-depth explanation of agent-based modeling" keywords="agent-based modeling, system dynamics, python, bptk, sddsl, xmile, smile, stella, ithink"}
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
and then use them *independently* in a Python environment such as
[JupyterLabs](https://jupyter.org).

## Main Features

-   The BPTK-Py framework supports System Dynamics models in XMILE
    Format, native SD models and native Agent-based models. You can also
    build hybrid SD-ABM-Models natively in Python.
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

The best way to get started with BPTK is our tutorial, which contains a
number of simulation models and Jupyter notebooks to get you started --
you can clone or download the tutorial from our [git
repository](https://github.com/transentis/bptk_py_tutorial/) on Github.

Our [Business Prototyping Toolkit
Meetup](https://www.transentis.com/business-prototyping-toolkit-meetup/en/)
meets online regularly. All meetups are recorded and the recordings are
available on the meetup page.

You might also like to clone our [model library
repository](https://github.com/transentis/bptk-model-library/) , which
contains a number of models that illustrate how to model business models
and market strategies using Agent-based modeling, System Dynamics and
BPTK.

BPTK was also used to build our implementation of the infamous [Beer
Distribution Game](https://beergame.transentis.com). Our [beergame
repository](https://github.com/transentis/beergame) contains Jupyter
notebooks that analyse the Beergame in-depth and also provides XMILE, SD
DSL and Agent-based versions of the Beergame.

## Getting Help

BPTK-Py is developed and maintained by [transentis
labs](https://www.transentis.com/business-prototyping-toolkit/en/).
Currently the main developers are [Dr. Oliver
Grasl](https://linkedin.com/in/olivergrasl), [Jeremy
Funk](https://linkedin.com/in/nathan-jeremy-funk-344617216) and [David
Granzin](https://linkedin.com/in/makisuo), former contributors include
Dominik Schröck and Ahmed Eldably.

The best place to ask questions about the framework is our [Business
Prototyping Toolkit
Meetup](https://www.transentis.com/business-prototyping-toolkit-meetup/en/),
which meets online regularly.

You can also contact us any time at <support@transentis.com>, we are
always happy to help.

## Content

[Installation](usage/installation.md)

[Quickstart](usage/quickstart.md)

[Limitations](usage/limitations.md)

[General Information](general/general.md)

{{< include general/_general_content.md >}}

[Agent Based Modeling](abm/abm.md)

{{< include abm/_abm_content.md >}}

[Introduction to XMILE](xmile/xmile.md)

{{< include xmile/_xmile_content.md >}}

[Introduction to SD DSL](sd-dsl/sddsl.md)

{{< include sd-dsl/_sddsl_content.md >}}
