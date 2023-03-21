---
title: Simple Dashboard
description: BPTK API Documentation for the SimpleDashboard class
keywords: agent-based modeling, system dynamics, bptk, bptk-py, python, business prototyping
---

# Simple Dashboard

Helper class that can be used to set up a dashboard. Check the [Develop Dashboards Using SimpleDashboard](/tutorials/develop_dashboards_using_simpledashboard/develop_dashboards_using_simpledashboard.ipynb) document for an in-depth explanation.

## SimpleDashboard Constructor

**SimpleDashboard(bptk, scenario_manager, scenario, style={}, layout={})**

## SimpleDashboard.add_custom_plot

**add_custom_plot(plot: Callable)**

Adds custom plot. Plotting must be handeled in the function.
:param equations: Callable

> Reference to function that plots.


* **Returns**

    The output the plot gets drawn on.


* **Return type**

    widgets.Output

## SimpleDashboard.add_plot

**add_plot(equations: List[str], title: str, names: List[str], x_label='', y_label='', start_date='', kind: Optional[str] = None, visualize_from_period=0, visualize_to_period=0, freq='D', agents: List[str] = [], agent_states: List[str] = [], agent_properties: List[str] = [], agent_property_types: List[str] = [])**

Wrapper function for bptk.plot_scenarios.
:param equations: List.

> Names of equations to plot (System Dynamics, SD).


* **Parameters**

    
    * **title** – String.
    Title of plot


    * **names** – List
    Names of equations. Used to map equation names to human readable names.


    * **x_label** – String.
    Label for x axis.


    * **y_label** – String.
    Label for y axis.


    * **start_date** – String.
    Start date for time series.


    * **kind** – String.
    Type of graph to plot (“line” or “area”).


    * **visualize_from_period** – Integer
    Visualize from specific period onwards.


    * **visualize_to_period** – Integer
    Visualize until a specific period.


    * **freq** – String.
    Frequency of time series. Uses the pandas offset aliases.


    * **agents** – List.
    List of agents to plot (Agent based modeling).


    * **agent_states** – List:
    List of agent states to plot, REQUIRES “AGENTS” param


    * **agent_properties** – List.
    List of agent properties to plot, REQUIRES “AGENTS” param


    * **agent_property_types** – List.
    List of agent property types to plot, REQUIRES “AGENTS” param



* **Returns**

    Plot id (used for identification when plot data is updated).

## SimpleDashboard.add_widget

**add_widget(widget, model_connection: Optional[Union[str, ModelConnection, Callable]] = None)**

Add any custom widget to the dashboard

* **Parameters**

    
    * **widget** – Widget


    * **model_connection** – Union[str, ModelConnection, Callable, None] - Optional
    The connection this widget has to the model. Can either be a direct connection to a constant using a string, a ModelConnection or a Callable, that gets called when the widget updates.


## SimpleDashboard.start

**start()**

Starts the dashboard. Call this at the end of the script.


## SimpleDashboard.update_plot_data

**update_plot_data(attribute: str, value: str, plot: int)**

* **Parameters**
    
    * **attribute** – string
    The attribute of the plot that will be updated.

    * **value** – string
    The value the attribute will be set to.

    * **plot** – int
    The plot id to update. Plot ids are returned when plots are added to the dashboard using the add_plot function.
    If plot < 0, all plots that contain the attribute will be updated.
