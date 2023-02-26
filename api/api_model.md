# Model


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
## _class_ Model(starttime=0, stoptime=0, dt=1, name='', scheduler=None, data_collector=None)
=======
### _class_ Model(starttime=0, stoptime=0, dt=1, name='', scheduler=None, data_collector=None)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
## _class_ Model(starttime=0, stoptime=0, dt=1, name='', scheduler=None, data_collector=None)
>>>>>>> master
=======
## _class_ Model(starttime=0, stoptime=0, dt=1, name='', scheduler=None, data_collector=None)
>>>>>>> master
=======
## _class_ Model(starttime=0, stoptime=0, dt=1, name='', scheduler=None, data_collector=None)
>>>>>>> master
=======
## _class_ Model(starttime=0, stoptime=0, dt=1, name='', scheduler=None, data_collector=None)
>>>>>>> master
This is the main agent base / System dynamics / Hybrid model class

It can run manually generated SD models, AB Models or define hybrid models.


* **Parameters**

    
    * **name** – String.
    Name of the model.


    * **scheduler** – Scheduler.
    Scheduler object (e.g. simultaneousScheduler). This is configurable, so that you can add your own scheduling algorithms.


    * **data_collector** – DataCollector
    Instance of DataCollector. This is configurable, so that you can add your own data collection algorithms.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### agent(agent_id)
=======
#### agent(agent_id)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### agent(agent_id)
>>>>>>> master
=======
### agent(agent_id)
>>>>>>> master
=======
### agent(agent_id)
>>>>>>> master
=======
### agent(agent_id)
>>>>>>> master
Get an agent by ID.

Retrieve one agent by its ID


* **Parameters**

    **agent_id** – Integer.
    ID of agent that is to be retrieved.



* **Returns**

    Agent object



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### agent_count(agent_type)
=======
#### agent_count(agent_type)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### agent_count(agent_type)
>>>>>>> master
=======
### agent_count(agent_type)
>>>>>>> master
=======
### agent_count(agent_type)
>>>>>>> master
=======
### agent_count(agent_type)
>>>>>>> master
Get count of agents of a given type.


* **Parameters**

    **agent_type** – String.
    Agent type to get count for



* **Returns**

    Integer. Number of agents (Integer)



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### agent_count_per_state(agent_type, state)
=======
#### agent_count_per_state(agent_type, state)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### agent_count_per_state(agent_type, state)
>>>>>>> master
=======
### agent_count_per_state(agent_type, state)
>>>>>>> master
=======
### agent_count_per_state(agent_type, state)
>>>>>>> master
=======
### agent_count_per_state(agent_type, state)
>>>>>>> master
Get number of agents in a specific state


* **Parameters**

    
    * **agent_type** – String.
    Agent type to get count for


    * **state** – String.
    The state of agents to get count for



* **Returns**

    Integer.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### agent_ids(agent_type)
=======
#### agent_ids(agent_type)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### agent_ids(agent_type)
>>>>>>> master
=======
### agent_ids(agent_type)
>>>>>>> master
=======
### agent_ids(agent_type)
>>>>>>> master
=======
### agent_ids(agent_type)
>>>>>>> master
Get agent IDs.

Retrieve agent IDs for all agents of type agent_type.


* **Parameters**

    **agent_type** – String.
    Agent type to get IDs for



* **Returns**

    List of IDs

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### begin_episode(episode_no)
=======


#### begin_episode(episode_no)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### begin_episode(episode_no)
>>>>>>> master
=======
### begin_episode(episode_no)
>>>>>>> master
=======
### begin_episode(episode_no)
>>>>>>> master
=======
### begin_episode(episode_no)
>>>>>>> master
Called at beginning of an episode.

When running a simulation repeatedly in episodes (e.g. because you are training the model using reinforcement learning), this method is called by the framework to allow tidy up at the beginning of an episode, e.g. a “soft” reset of the simulation.

The default implementation calls begin_episode on each agent.


* **Parameters**

    **episode_no** – Integer.
    The number of the episode



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### begin_round(time, sim_round, step)
=======
#### begin_round(time, sim_round, step)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### begin_round(time, sim_round, step)
>>>>>>> master
=======
### begin_round(time, sim_round, step)
>>>>>>> master
=======
### begin_round(time, sim_round, step)
>>>>>>> master
=======
### begin_round(time, sim_round, step)
>>>>>>> master
Called at the beginning of a simulation round.

Should be called by the Scheduler at the beginning of each round, before the agents act methods are called. Add any logic here that is needed to update dynamic properties.


* **Parameters**

    
    * **time** – Integer.
    The current timestep of the simulation, i.e.(round+step\*dt)


    * **sim_round** – Integer
    The current round of the simulation.


    * **step** – Integer.
    The step number of round



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### biflow(name)
=======
#### biflow(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### biflow(name)
>>>>>>> master
=======
### biflow(name)
>>>>>>> master
=======
### biflow(name)
>>>>>>> master
=======
### biflow(name)
>>>>>>> master
Create a System Dynamics biflow


* **Parameters**

    **name** – String.
    Name of the biflow



* **Returns**

    A Biflow object

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### broadcast_event(agent_type, event_factory)
=======


#### broadcast_event(agent_type, event_factory)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### broadcast_event(agent_type, event_factory)
>>>>>>> master
=======
### broadcast_event(agent_type, event_factory)
>>>>>>> master
=======
### broadcast_event(agent_type, event_factory)
>>>>>>> master
=======
### broadcast_event(agent_type, event_factory)
>>>>>>> master
Broadcast an event to all agents of a particular agent_type


* **Parameters**

    
    * **agent_type** – String.
    Agent type that is to receive the event


    * **num_agents** – Integer.
    Number of random agents that should receive the event


    * **event_factory** – Function.
    The factory (typicalla a lambda function) that generates the desired event for a given target agent type. The function receives the agent_id as its parameter.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### configure(config)
=======
#### configure(config)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### configure(config)
>>>>>>> master
=======
### configure(config)
>>>>>>> master
=======
### configure(config)
>>>>>>> master
=======
### configure(config)
>>>>>>> master
Called to configure the model using a dictionary. This method is called by the framework if you instantiate models from scenario files. But you can also call the method directly.


* **Parameters**

    **config** – Dict.
    Dictionary containing the config: {“runspecs”:<dictionary of runspecs>,”properties”:<dictionary of properties>,”agents”:<list of agent-specs>}.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### constant(name)
=======
#### constant(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### constant(name)
>>>>>>> master
=======
### constant(name)
>>>>>>> master
=======
### constant(name)
>>>>>>> master
=======
### constant(name)
>>>>>>> master
Create a System Dynamics constant


* **Parameters**

    **name** – String.
    Name of the constant


Returns: Constant.

    A Constant object


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### converter(name)
=======
#### converter(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### converter(name)
>>>>>>> master
=======
### converter(name)
>>>>>>> master
=======
### converter(name)
>>>>>>> master
=======
### converter(name)
>>>>>>> master
Create a System Dynamics converter


* **Parameters**

    **name** – String.
    Name of the converter



* **Returns**

    A Converter object

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### create_agent(agent_type, agent_properties)
=======


#### create_agent(agent_type, agent_properties)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### create_agent(agent_type, agent_properties)
>>>>>>> master
=======
### create_agent(agent_type, agent_properties)
>>>>>>> master
=======
### create_agent(agent_type, agent_properties)
>>>>>>> master
=======
### create_agent(agent_type, agent_properties)
>>>>>>> master
Create one agent of the given type and with the given properties.

Internally this method then uses the registered agent factories to actually create an agent.


* **Parameters**

    
    * **agent_type** – String.
    Type of agent


    * **agent_properties** – Dict.
    The properties to initialize the agent with.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### create_agents(agent_spec)
=======


#### create_agents(agent_spec)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### create_agents(agent_spec)
>>>>>>> master
=======
### create_agents(agent_spec)
>>>>>>> master
=======
### create_agents(agent_spec)
>>>>>>> master
=======
### create_agents(agent_spec)
>>>>>>> master
Create agents according to the agent specificaction.

The agent specification is a dictionary containing the agent name and properties. Internally, this method then uses the registered agent factories to actually create the agents.


* **Parameters**

    **agent_spec** – Dict.
    Specification of an agent using a dictionary with format {“name”:<agent name>, “count”: <initial count>}


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### end_episode(episode_no)
=======

#### end_episode(episode_no)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### end_episode(episode_no)
>>>>>>> master
=======
### end_episode(episode_no)
>>>>>>> master
=======
### end_episode(episode_no)
>>>>>>> master
=======
### end_episode(episode_no)
>>>>>>> master
Called at the end of an episode.

When running a simulation repeatedly in episodes, this method is called by the framework to allow tidy up at the end of an episode.

The default implementation calls end_episode on each agent.


* **Parameters**

    **episode_no** – Integer.
    The number of the episode



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### end_round(time, sim_round, step)
=======
#### end_round(time, sim_round, step)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### end_round(time, sim_round, step)
>>>>>>> master
=======
### end_round(time, sim_round, step)
>>>>>>> master
=======
### end_round(time, sim_round, step)
>>>>>>> master
=======
### end_round(time, sim_round, step)
>>>>>>> master
Called at end of a simulation round.

Should be called by the Scheduler at the end of each round, before the agents act methods are called. Add any logic here that is needed to update dynamic properties.


* **Parameters**

    
    * **time** – Integer.
    The current timestep of the simulation, i.e.(round+step\*dt)


    * **sim_round** – Integer
    The current round of the simulation.


    * **step** – Integer.
    The step number of round



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### enqueue_event(event)
=======
#### enqueue_event(event)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### enqueue_event(event)
>>>>>>> master
=======
### enqueue_event(event)
>>>>>>> master
=======
### enqueue_event(event)
>>>>>>> master
=======
### enqueue_event(event)
>>>>>>> master
Called by the framework to enqueue events.

In general you don’t need to override this method or call it directly.


* **Parameters**

    **event** – Event.
    Instance of the event.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### _property_ equation_prefix()
=======
#### _property_ equation_prefix()
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### _property_ equation_prefix()
>>>>>>> master
=======
### _property_ equation_prefix()
>>>>>>> master
=======
### _property_ equation_prefix()
>>>>>>> master
=======
### _property_ equation_prefix()
>>>>>>> master
An id that is unique within this model that can be used to generate unique equation names


* **Returns**

    Integer. An id that is unique within the model.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### evaluate_equation(name, t)
=======
#### evaluate_equation(name, t)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### evaluate_equation(name, t)
>>>>>>> master
=======
### evaluate_equation(name, t)
>>>>>>> master
=======
### evaluate_equation(name, t)
>>>>>>> master
=======
### evaluate_equation(name, t)
>>>>>>> master
Evaluate an System Dynamics element’s equation at timestep t.


* **Parameters**

    
    * **name** – String.
    Name of the equation.


    * **t** – Float.
    Timestep to evaluate for


Return: Float

    The value of the equation at time t.


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### flow(name)
=======
#### flow(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### flow(name)
>>>>>>> master
=======
### flow(name)
>>>>>>> master
=======
### flow(name)
>>>>>>> master
=======
### flow(name)
>>>>>>> master
Create a System Dynamics flow


* **Parameters**

    **name** – String.
    Name of the flow



* **Returns**

    A Flow object



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### function(name, fn)
=======
#### function(name, fn)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### function(name, fn)
>>>>>>> master
=======
### function(name, fn)
>>>>>>> master
=======
### function(name, fn)
>>>>>>> master
=======
### function(name, fn)
>>>>>>> master
Create a user defined function for System Dynamics.


* **Parameters**

    
    * **name** – String.
    Name of the function.


    * **fn** – returns


Returns:
A function which wraps the user defined function for use within System Dynamics.


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### get_property(name)
=======
#### get_property(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### get_property(name)
>>>>>>> master
=======
### get_property(name)
>>>>>>> master
=======
### get_property(name)
>>>>>>> master
=======
### get_property(name)
>>>>>>> master
Get a property of the model by name.

The value of the model properties can also be accessed directly as a model attribute, i.e. as self.<name of property>


* **Parameters**

    **name** – String.
    Name of property



* **Returns**

    Dictionary for property



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### get_property_value(name)
=======
#### get_property_value(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### get_property_value(name)
>>>>>>> master
=======
### get_property_value(name)
>>>>>>> master
=======
### get_property_value(name)
>>>>>>> master
=======
### get_property_value(name)
>>>>>>> master
Get a property of the model by name.

The value of the model properties can also be accessed directly as a model attribute, i.e. as self.<name of property>


* **Parameters**

    **name** – String.
    Name of property



* **Returns**

    Value of the property.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### _static_ get_random_integer(min_value, max_value)
=======
#### _static_ get_random_integer(min_value, max_value)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### _static_ get_random_integer(min_value, max_value)
>>>>>>> master
=======
### _static_ get_random_integer(min_value, max_value)
>>>>>>> master
=======
### _static_ get_random_integer(min_value, max_value)
>>>>>>> master
=======
### _static_ get_random_integer(min_value, max_value)
>>>>>>> master
A random integer within bounds

This method is useful for simulating random behaviour.


* **Parameters**

    
    * **min_value** – Integer.
    Min value for random integer


    * **max_value** – Integer.
    max value for random integer



* **Returns**

    Random integer.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### instantiate_model()
=======
#### instantiate_model()
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### instantiate_model()
>>>>>>> master
=======
### instantiate_model()
>>>>>>> master
=======
### instantiate_model()
>>>>>>> master
=======
### instantiate_model()
>>>>>>> master
Set properties during model initialization.

This method does nothing in the parent class and can be overriden in child classes. It is called by the frame directly after the model is instantiated.

Implement this method in your model to perform any kind of initialization you may need. Typically you would register your agent factories hier and set up model properties.


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### next_agent(agent_type, state)
=======
#### next_agent(agent_type, state)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### next_agent(agent_type, state)
>>>>>>> master
=======
### next_agent(agent_type, state)
>>>>>>> master
=======
### next_agent(agent_type, state)
>>>>>>> master
=======
### next_agent(agent_type, state)
>>>>>>> master
Get the next agent by type and state.

Runs through the internal agent store and retrieves the first agent that matches in type and state.


* **Parameters**

    
    * **agent_type** – String.
    Agent type


    * **state** – String.
    State the agent is in



* **Returns**

    The first agent object that matches the criterian None otherwise.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### plot_lookup(lookup_names, config=None)
=======
#### plot_lookup(lookup_names, config=None)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### plot_lookup(lookup_names, config=None)
>>>>>>> master
=======
### plot_lookup(lookup_names, config=None)
>>>>>>> master
=======
### plot_lookup(lookup_names, config=None)
>>>>>>> master
=======
### plot_lookup(lookup_names, config=None)
>>>>>>> master
Plots lookup functions for the given list of lookup names


* **Parameters**

    **lookup_names** – String or List.
    A name or list of names of lookup functions. The list can be passed as a Python list or a comma separated string.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### random_agents(agent_type, num_agents)
=======
#### random_agents(agent_type, num_agents)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### random_agents(agent_type, num_agents)
>>>>>>> master
=======
### random_agents(agent_type, num_agents)
>>>>>>> master
=======
### random_agents(agent_type, num_agents)
>>>>>>> master
=======
### random_agents(agent_type, num_agents)
>>>>>>> master
Retreive a number of random agents


* **Parameters**

    
    * **agent_type** – String.
    Type of agent to retrieve.


    * **num_agents** – Number of agents of this type to retreive.



* **Returns**

    List of agent IDs. The number of IDs might be less then num_agents if fewer agents are available.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### random_events(agent_type, num_agents, event_factory)
=======
#### random_events(agent_type, num_agents, event_factory)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### random_events(agent_type, num_agents, event_factory)
>>>>>>> master
=======
### random_events(agent_type, num_agents, event_factory)
>>>>>>> master
=======
### random_events(agent_type, num_agents, event_factory)
>>>>>>> master
=======
### random_events(agent_type, num_agents, event_factory)
>>>>>>> master
Distribute events to a number of random agents


* **Parameters**

    
    * **agent_type** – String.
    Agent type that is to receive the event


    * **num_agents** – Integer.
    Number of random agents that should receive the event


    * **event_factory** – Function.
    The factory (typicalla a lambda function) that generates the desired event for a given target agent type. The function receives the agent_id as its parameter.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### register_agent_factory(agent_type, agent_factory)
=======
#### register_agent_factory(agent_type, agent_factory)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### register_agent_factory(agent_type, agent_factory)
>>>>>>> master
=======
### register_agent_factory(agent_type, agent_factory)
>>>>>>> master
=======
### register_agent_factory(agent_type, agent_factory)
>>>>>>> master
=======
### register_agent_factory(agent_type, agent_factory)
>>>>>>> master
Register an agent factory.

Agent factories are used at run-time to populate the model with agents. This method is used to register an agent factory, which is typically just a lambda function which returns an agent.


* **Parameters**

    
    * **agent_type** – String.
    Type of agent to register


    * **agent_factory** – Function.
    Function that returns an agent given an id and the model. Typically a lambda, but not limited to that. Input: agent_id, model -> Output: Agent of agent_type



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### reset()
=======
#### reset()
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### reset()
>>>>>>> master
=======
### reset()
>>>>>>> master
=======
### reset()
>>>>>>> master
=======
### reset()
>>>>>>> master
Reset the model.
Cleara out all agents, agent and event statistics and resets the cache of SD equations. Keeps the agent factories though, so you could directly reconfigure the model using the configure method.


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
### reset_cache()
Reset cache of all System Dynamics equations and call the reset_cache method on all agents. Clear the agent statistics.


### run(show_progress_widget=False, collect_data=True)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
#### reset_cache()
Reset cache of all System Dynamics equations.


#### run(show_progress_widget=False, collect_data=True)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
Run the simulation.

This esssentially just calls the run method of the models scheduler.


* **Parameters**

    
    * **show_progress_widget** – Boolean (Default=False).
    If True, shows a progress widget (only in Jupyter environment!)


    * **collect_data** – Boolean (Default=True).
    If True, data is automatically collected in the models DataCollector, e.g. for plotting the model behaviour. If you are training the model e.g. using reinforcement learning, it might be useful to turn data collection of.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### run_specs(starttime, stoptime, dt)
=======
#### run_specs(starttime, stoptime, dt)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### run_specs(starttime, stoptime, dt)
>>>>>>> master
=======
### run_specs(starttime, stoptime, dt)
>>>>>>> master
=======
### run_specs(starttime, stoptime, dt)
>>>>>>> master
=======
### run_specs(starttime, stoptime, dt)
>>>>>>> master
Configure the runspecs of the model.


* **Parameters**

    
    * **starttime** – Integer.
    The starttime of the model.


    * **stoptime** – Integer.
    The stoptime of the model.


    * **dt** – The dt of the model.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### run_step(step, show_progress_widget=False, collect_data=True)
=======
#### run_step(step, show_progress_widget=False, collect_data=True)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### run_step(step, show_progress_widget=False, collect_data=True)
>>>>>>> master
=======
### run_step(step, show_progress_widget=False, collect_data=True)
>>>>>>> master
=======
### run_step(step, show_progress_widget=False, collect_data=True)
>>>>>>> master
=======
### run_step(step, show_progress_widget=False, collect_data=True)
>>>>>>> master
Run a simulation step.

This esssentially just calls the run method of the models scheduler.


* **Parameters**

    
    * **step** – Int.
    The step to run


    * **show_progress_widget** – Boolean (Default=False).
    If True, shows a progress widget (only in Jupyter environment!)


    * **collect_data** – Boolean (Default=True).
    If True, data is automatically collected in the models DataCollector, e.g. for plotting the model behaviour. If you are training the model e.g. using reinforcement learning, it might be useful to turn data collection of.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### set_property(name, property_spec)
=======
#### set_property(name, property_spec)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### set_property(name, property_spec)
>>>>>>> master
=======
### set_property(name, property_spec)
>>>>>>> master
=======
### set_property(name, property_spec)
>>>>>>> master
=======
### set_property(name, property_spec)
>>>>>>> master
Configure a property of the model itself, as opposed to the properties of individual agents.

Properties set via this mechanism are stored internally in a dictionary of properties, the value of the property directly can be access directly as an object attribute, i.e. as self.<name of property>.

The key point about keeping properties in this way is that they can then easily be collected in a data collector.


* **Parameters**

    
    * **name** – String.
    Name of the property to set.


    * **property_spec** – Dict.
    Specification of property: {“type”:<type of property, free form string>,”value”:<value of property>}. In principle the property can store any kind of value, the type is currently not evaluated by the framework.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### set_property_value(name, value)
=======
#### set_property_value(name, value)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### set_property_value(name, value)
>>>>>>> master
=======
### set_property_value(name, value)
>>>>>>> master
=======
### set_property_value(name, value)
>>>>>>> master
=======
### set_property_value(name, value)
>>>>>>> master
Set the value of a model property by name.

Model properties can also be set directly via the model attributes, i.e. as self.<nname of property>=<value of property>


* **Parameters**

    
    * **name** – String.
    Name of property.


    * **value** – Any.
    Value of the property to set.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### set_scenario_manager(scenario_manager)
=======
#### set_scenario_manager(scenario_manager)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### set_scenario_manager(scenario_manager)
>>>>>>> master
=======
### set_scenario_manager(scenario_manager)
>>>>>>> master
=======
### set_scenario_manager(scenario_manager)
>>>>>>> master
=======
### set_scenario_manager(scenario_manager)
>>>>>>> master
Set the name of the scenario manager that is handling this model. Used by bptk during scenario registration.


* **Parameters**

    **scenario_manager** – String.
    Name of the scenario manager.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### statistics()
=======
#### statistics()
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### statistics()
>>>>>>> master
=======
### statistics()
>>>>>>> master
=======
### statistics()
>>>>>>> master
=======
### statistics()
>>>>>>> master
Get statistics from DataCollector


* **Returns**

    The DataCollector used to collect the simulation statistics.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### stock(name)
=======
#### stock(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### stock(name)
>>>>>>> master
=======
### stock(name)
>>>>>>> master
=======
### stock(name)
>>>>>>> master
=======
### stock(name)
>>>>>>> master
Create a System Dynamics stock


* **Parameters**

    **name** – String.
    Name of the stock.



* **Returns**

    The stock object.
