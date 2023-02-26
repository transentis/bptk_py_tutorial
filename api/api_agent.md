# Agent


<<<<<<< HEAD
## _class_ Agent(agent_id, model, properties, agent_type='agent')
=======
### _class_ Agent(agent_id, model, properties, agent_type='agent')
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Agent for agent based simulation.
Your agents must inherit from this class if they are to be part of an agent-based simulation.


* **Parameters**

    
    * **agent_id** – Integer.
    Id of agent. Model should manage this. Do use agent factories!


    * **model** – Model instance
    The agent-based model this agent will be part of.


    * **properties** – Dictionary of agent properties. These properties will be available as object attributes (i.e. via self.<name of property>)



<<<<<<< HEAD
### act(time, round_no, step_no)
=======
#### act(time, round_no, step_no)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Called by the scheduler every timestep.

Does nothing in the base class, typically agents will implement most of their action logic in this method (and in the event handlers).


* **Parameters**

    
    * **time** – Float.
    This is the current simulation time (equivalent to round_no+step_no\*dt)


    * **round_no** – Integer.
    The current round.


    * **step_no** – Integer.
    The current step (within the round)



<<<<<<< HEAD
### begin_episode(episode_no)
=======
#### begin_episode(episode_no)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Called by the framework at the beginning of each episode.

Useful to allow a soft reset of the agent, e.g. when training a model for reinforcement learning.

The default implementation does nothing.


* **Parameters**

    **episode_no** – Integer.
    The number of the episode.



<<<<<<< HEAD
### end_episode(episode_no)
=======
#### end_episode(episode_no)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Called by the framework at the end of each epsiode, to allow tidy up if necessary. The default implementation does nothing.


* **Parameters**

    **episode_no** – Integer.
    The number of the episode



<<<<<<< HEAD
### get_property(name)
=======
#### get_property(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Get the settings of a property.


* **Parameters**

    **name** – String.
    Name of property



* **Returns**

    Dictionary with keys type and value.



<<<<<<< HEAD
### get_property_value(name)
=======
#### get_property_value(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Retrieves the value of a property.


* **Parameters**

    **name** – String.
    The name of the property whose value is to be retrieved.



* **Returns**

    The value of the property.



<<<<<<< HEAD
### handle_events(time, sim_round, step)
=======
#### handle_events(time, sim_round, step)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Called by the framework to handle events.

This method then calls the registered event handlers.


* **Parameters**

    
    * **time** – Float.
    The current simulation time (sim_round+dt\*step)


    * **sim_round** – Integer.
    The current simulation round.


    * **step** – Integer.
    The current simulation step (within the round).



<<<<<<< HEAD
### initialize()
=======
#### initialize()
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Initialize the agent.

Called by the framework directly after the agent is instantiated, useful for any kind of initialization code such as setting the agent type, current state and registering event handlers.


<<<<<<< HEAD
### _static_ is_event_relevant(threshold)
=======
#### _static_ is_event_relevant(threshold)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Helper function used to differentiate relevant and irrelevant events.

The function generates a random number in the range [0.0, 1.0) using Pythons random.random(). If this is smaller than the threshold, the event is deemed relevant.


* **Parameters**

    **threshold** – Float.
    Threshold for relevance, should be in the range [0.0,1.0]



* **Returns**

    Boolean



<<<<<<< HEAD
### receive_event(event)
=======
#### receive_event(event)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Receive an event.


* **Parameters**

    **event** – Event instance.
    The event that the agent receives.



<<<<<<< HEAD
### receive_instantaneous_event(event)
=======
#### receive_instantaneous_event(event)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Handle an event immediately, do not wait for the next round.


* **Parameters**

    **event** – event instance.
    Event that the agent receives.



<<<<<<< HEAD
### register_event_handler(states, event, handler)
=======
#### register_event_handler(states, event, handler)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Register an event handler.

The event handler is called by the framework if a relevant event occurs. The event handler is registered for all relevant state.


* **Parameters**

    
    * **states** – List.
    List of states (String) for which the event handler is valid


    * **event** – String
    The type of event the handler reacts to.


    * **handler** – Function.
    The actual event handler. This must be a function that accept the event as its parameter. Typically this will be a method of the agent class.



<<<<<<< HEAD
### serialize()
=======
#### serialize()
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Serialize the agent.


* **Returns**

    id, state, type and all properties.



* **Return type**

    Returns a dictionary containing all relevant agent data



<<<<<<< HEAD
### set_property(name, data)
=======
#### set_property(name, data)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Configure an agent property by passing a dictionary specifying the property.


* **Parameters**

    
    * **name** – String.
    The name of the property whose data is being set.


    * **data** – Dictionary.
    Specification of property in dictionary with keys type and values. Currently the types Double, String, Integer, Lookup, Dictionary, Boolean and Agent are supported.



<<<<<<< HEAD
### set_property_value(name, value)
=======
#### set_property_value(name, value)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Sets the value of a property.


* **Parameters**

    
    * **name** – String.
    The name of the property to set.


    * **value** – (Agent|Dictionary|Double|Integer|String|Array of Points).
    The value of the property to set.
