---
title: Simulation Scenario
description: BPTK API Documentation for the SimulationScenario class
keywords: system dynamics, bptk, bptk-py, python, business prototyping
---

# Simulation Scenario

## SimulationScenario Constructor

**SimulationScenario(dictionary, name, model, scenario_manager_name)**
This class stores the settings for each scenario for pure SD models (SD DSL and XMILE)

* **Parameters**

    
    * **dictionary** – Scenario dictionary from the source JSON file


    * **name** – Name of the scenario


    * **model** – Simulation_model object


    * **scenario_manager_name** – Name of scenario manager

## SimulationScenario.get_property_value

**get_property_value(name)**

Retrieve the current value of a property.

* **Parameters**
    
    * **param name**

        The name of the property whose value you want to retrieve.

    * **type name**

        String

    * **return**

        Returns the value of the property

    * **rtype**

        A numerical value

## SimulationScenario.set_property_value

**set_property_value(name, value)**

Set the property with given name to given value

* **Parameters**
    
    * **param name**

        The name of the property to set

    * **type name**

        String

    * **param value**

        The value to set the property to

    * **type value**

        A numerical value

## SimulationScenario.setup_constants

**setup_constants()**

Sets up the constants of the simulation model upon scenario manager initialization

## SimulationScenario.setup_constants

**setup_points()**

Sets up the points of the simulation model upon scenario manager initialization
