# SimulationScenario


<<<<<<< HEAD
## _class_ SimulationScenario(dictionary, name, model, scenario_manager_name)
=======
### _class_ SimulationScenario(dictionary, name, model, scenario_manager_name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
This class stores the settings for each scenario for pure SD models (SD DSL and XMILE)


* **Parameters**

    
    * **dictionary** – Scenario dictionary from the source JSON file


    * **name** – Name of the scenario


    * **model** – Simulation_model object


    * **scenario_manager_name** – Name of scenario manager

<<<<<<< HEAD
### get_property_value(name)
=======


#### get_property_value(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Retrieve the current value of a property.

    
    * **param name**

        The name of the property whose value you want to retrieve.



    * **type name**

        String



    * **return**

        Returns the value of the property



    * **rtype**

        A numerical value

<<<<<<< HEAD
### set_property_value(name, value)
=======


#### set_property_value(name, value)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Set the property with given name to given value

    
    * **param name**

        The name of the property to set



    * **type name**

        String



    * **param value**

        The value to set the property to



    * **type value**

        A numerical value


<<<<<<< HEAD
### setup_constants()
=======

#### setup_constants()
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Sets up the constants of the simulation model upon scenario manager initialization
:return: None


<<<<<<< HEAD
### setup_points()
=======
#### setup_points()
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Sets up the points of the simulation model upon scenario manager initialization
:return: None
