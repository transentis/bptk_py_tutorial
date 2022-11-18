# Model


### _class_ Model(starttime=0, stoptime=0, dt=1, name='', scheduler=None, data_collector=None)
This is the main agent base / System dynamics / Hybrid model class

It can run manually generated SD models, AB Models or define hybrid models.


* **Parameters**

    
    * **name** – String.
    Name of the model.


    * **scheduler** – Scheduler.
    Scheduler object (e.g. simultaneousScheduler). This is configurable, so that you can add your own scheduling algorithms.


    * **data_collector** – DataCollector
    Instance of DataCollector. This is configurable, so that you can add your own data collection algorithms.



#### agent(agent_id)
Get an agent by ID.

Retrieve one agent by its ID


* **Parameters**

    **agent_id** – Integer.
    ID of agent that is to be retrieved.



* **Returns**

    Agent object



#### agent_count(agent_type)
Get count of agents of a given type.


* **Parameters**

    **agent_type** – String.
    Agent type to get count for



* **Returns**

    Integer. Number of agents (Integer)



#### agent_count_per_state(agent_type, state)
Get number of agents in a specific state


* **Parameters**

    
    * **agent_type** – String.
    Agent type to get count for


    * **state** – String.
    The state of agents to get count for



* **Returns**

    Integer.



#### agent_ids(agent_type)
Get agent IDs.

Retrieve agent IDs for all agents of type agent_type.


* **Parameters**

    **agent_type** – String.
    Agent type to get IDs for



* **Returns**

    List of IDs



#### begin_episode(episode_no)
Called at beginning of an episode.

When running a simulation repeatedly in episodes (e.g. because you are training the model using reinforcement learning), this method is called by the framework to allow tidy up at the beginning of an episode, e.g. a “soft” reset of the simulation.

The default implementation calls begin_episode on each agent.


* **Parameters**

    **episode_no** – Integer.
    The number of the episode



#### begin_round(time, sim_round, step)
Called at the beginning of a simulation round.

Should be called by the Scheduler at the beginning of each round, before the agents act methods are called. Add any logic here that is needed to update dynamic properties.


* **Parameters**

    
    * **time** – Integer.
    The current timestep of the simulation, i.e.(round+step\*dt)


    * **sim_round** – Integer
    The current round of the simulation.


    * **step** – Integer.
    The step number of round



#### biflow(name)
Create a System Dynamics biflow


* **Parameters**

    **name** – String.
    Name of the biflow



* **Returns**

    A Biflow object



#### broadcast_event(agent_type, event_factory)
Broadcast an event to all agents of a particular agent_type


* **Parameters**

    
    * **agent_type** – String.
    Agent type that is to receive the event


    * **num_agents** – Integer.
    Number of random agents that should receive the event


    * **event_factory** – Function.
    The factory (typicalla a lambda function) that generates the desired event for a given target agent type. The function receives the agent_id as its parameter.



#### configure(config)
Called to configure the model using a dictionary. This method is called by the framework if you instantiate models from scenario files. But you can also call the method directly.


* **Parameters**

    **config** – Dict.
    Dictionary containing the config: {“runspecs”:<dictionary of runspecs>,”properties”:<dictionary of properties>,”agents”:<list of agent-specs>}.



#### constant(name)
Create a System Dynamics constant


* **Parameters**

    **name** – String.
    Name of the constant


Returns: Constant.

    A Constant object


#### converter(name)
Create a System Dynamics converter


* **Parameters**

    **name** – String.
    Name of the converter



* **Returns**

    A Converter object



#### create_agent(agent_type, agent_properties)
Create one agent of the given type and with the given properties.

Internally this method then uses the registered agent factories to actually create an agent.


* **Parameters**

    
    * **agent_type** – String.
    Type of agent


    * **agent_properties** – Dict.
    The properties to initialize the agent with.



#### create_agents(agent_spec)
Create agents according to the agent specificaction.

The agent specification is a dictionary containing the agent name and properties. Internally, this method then uses the registered agent factories to actually create the agents.


* **Parameters**

    **agent_spec** – Dict.
    Specification of an agent using a dictionary with format {“name”:<agent name>, “count”: <initial count>}



#### end_episode(episode_no)
Called at the end of an episode.

When running a simulation repeatedly in episodes, this method is called by the framework to allow tidy up at the end of an episode.

The default implementation calls end_episode on each agent.


* **Parameters**

    **episode_no** – Integer.
    The number of the episode



#### end_round(time, sim_round, step)
Called at end of a simulation round.

Should be called by the Scheduler at the end of each round, before the agents act methods are called. Add any logic here that is needed to update dynamic properties.


* **Parameters**

    
    * **time** – Integer.
    The current timestep of the simulation, i.e.(round+step\*dt)


    * **sim_round** – Integer
    The current round of the simulation.


    * **step** – Integer.
    The step number of round



#### enqueue_event(event)
Called by the framework to enqueue events.

In general you don’t need to override this method or call it directly.


* **Parameters**

    **event** – Event.
    Instance of the event.



#### _property_ equation_prefix()
An id that is unique within this model that can be used to generate unique equation names


* **Returns**

    Integer. An id that is unique within the model.



#### evaluate_equation(name, t)
Evaluate an System Dynamics element’s equation at timestep t.


* **Parameters**

    
    * **name** – String.
    Name of the equation.


    * **t** – Float.
    Timestep to evaluate for


Return: Float

    The value of the equation at time t.


#### flow(name)
Create a System Dynamics flow


* **Parameters**

    **name** – String.
    Name of the flow



* **Returns**

    A Flow object



#### function(name, fn)
Create a user defined function for System Dynamics.


* **Parameters**

    
    * **name** – String.
    Name of the function.


    * **fn** – returns


Returns:
A function which wraps the user defined function for use within System Dynamics.


#### get_property(name)
Get a property of the model by name.

The value of the model properties can also be accessed directly as a model attribute, i.e. as self.<name of property>


* **Parameters**

    **name** – String.
    Name of property



* **Returns**

    Dictionary for property



#### get_property_value(name)
Get a property of the model by name.

The value of the model properties can also be accessed directly as a model attribute, i.e. as self.<name of property>


* **Parameters**

    **name** – String.
    Name of property



* **Returns**

    Value of the property.



#### _static_ get_random_integer(min_value, max_value)
A random integer within bounds

This method is useful for simulating random behaviour.


* **Parameters**

    
    * **min_value** – Integer.
    Min value for random integer


    * **max_value** – Integer.
    max value for random integer



* **Returns**

    Random integer.



#### instantiate_model()
Set properties during model initialization.

This method does nothing in the parent class and can be overriden in child classes. It is called by the frame directly after the model is instantiated.

Implement this method in your model to perform any kind of initialization you may need. Typically you would register your agent factories hier and set up model properties.


#### next_agent(agent_type, state)
Get the next agent by type and state.

Runs through the internal agent store and retrieves the first agent that matches in type and state.


* **Parameters**

    
    * **agent_type** – String.
    Agent type


    * **state** – String.
    State the agent is in



* **Returns**

    The first agent object that matches the criterian None otherwise.



#### plot_lookup(lookup_names, config=None)
Plots lookup functions for the given list of lookup names


* **Parameters**

    **lookup_names** – String or List.
    A name or list of names of lookup functions. The list can be passed as a Python list or a comma separated string.



#### random_agents(agent_type, num_agents)
Retreive a number of random agents


* **Parameters**

    
    * **agent_type** – String.
    Type of agent to retrieve.


    * **num_agents** – Number of agents of this type to retreive.



* **Returns**

    List of agent IDs. The number of IDs might be less then num_agents if fewer agents are available.



#### random_events(agent_type, num_agents, event_factory)
Distribute events to a number of random agents


* **Parameters**

    
    * **agent_type** – String.
    Agent type that is to receive the event


    * **num_agents** – Integer.
    Number of random agents that should receive the event


    * **event_factory** – Function.
    The factory (typicalla a lambda function) that generates the desired event for a given target agent type. The function receives the agent_id as its parameter.



#### register_agent_factory(agent_type, agent_factory)
Register an agent factory.

Agent factories are used at run-time to populate the model with agents. This method is used to register an agent factory, which is typically just a lambda function which returns an agent.


* **Parameters**

    
    * **agent_type** – String.
    Type of agent to register


    * **agent_factory** – Function.
    Function that returns an agent given an id and the model. Typically a lambda, but not limited to that. Input: agent_id, model -> Output: Agent of agent_type



#### reset()
Reset the model.
Cleara out all agents, agent and event statistics and resets the cache of SD equations. Keeps the agent factories though, so you could directly reconfigure the model using the configure method.


#### reset_cache()
Reset cache of all System Dynamics equations.


#### run(show_progress_widget=False, collect_data=True)
Run the simulation.

This esssentially just calls the run method of the models scheduler.


* **Parameters**

    
    * **show_progress_widget** – Boolean (Default=False).
    If True, shows a progress widget (only in Jupyter environment!)


    * **collect_data** – Boolean (Default=True).
    If True, data is automatically collected in the models DataCollector, e.g. for plotting the model behaviour. If you are training the model e.g. using reinforcement learning, it might be useful to turn data collection of.



#### run_specs(starttime, stoptime, dt)
Configure the runspecs of the model.


* **Parameters**

    
    * **starttime** – Integer.
    The starttime of the model.


    * **stoptime** – Integer.
    The stoptime of the model.


    * **dt** – The dt of the model.



#### run_step(step, show_progress_widget=False, collect_data=True)
Run a simulation step.

This esssentially just calls the run method of the models scheduler.


* **Parameters**

    
    * **step** – Int.
    The step to run


    * **show_progress_widget** – Boolean (Default=False).
    If True, shows a progress widget (only in Jupyter environment!)


    * **collect_data** – Boolean (Default=True).
    If True, data is automatically collected in the models DataCollector, e.g. for plotting the model behaviour. If you are training the model e.g. using reinforcement learning, it might be useful to turn data collection of.



#### set_property(name, property_spec)
Configure a property of the model itself, as opposed to the properties of individual agents.

Properties set via this mechanism are stored internally in a dictionary of properties, the value of the property directly can be access directly as an object attribute, i.e. as self.<name of property>.

The key point about keeping properties in this way is that they can then easily be collected in a data collector.


* **Parameters**

    
    * **name** – String.
    Name of the property to set.


    * **property_spec** – Dict.
    Specification of property: {“type”:<type of property, free form string>,”value”:<value of property>}. In principle the property can store any kind of value, the type is currently not evaluated by the framework.



#### set_property_value(name, value)
Set the value of a model property by name.

Model properties can also be set directly via the model attributes, i.e. as self.<nname of property>=<value of property>


* **Parameters**

    
    * **name** – String.
    Name of property.


    * **value** – Any.
    Value of the property to set.



#### set_scenario_manager(scenario_manager)
Set the name of the scenario manager that is handling this model. Used by bptk during scenario registration.


* **Parameters**

    **scenario_manager** – String.
    Name of the scenario manager.



#### statistics()
Get statistics from DataCollector


* **Returns**

    The DataCollector used to collect the simulation statistics.



#### stock(name)
Create a System Dynamics stock


* **Parameters**

    **name** – String.
    Name of the stock.



* **Returns**

    The stock object.
