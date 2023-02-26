# DataCollector


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
## _class_ DataCollector()
=======
### _class_ DataCollector()
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
## _class_ DataCollector()
>>>>>>> master
=======
## _class_ DataCollector()
>>>>>>> master
A datacollector for the agent based simulation.
Collects the output data of each agent/event and makes it available to external resources such as BPTK-Py to plot the data


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### collect_agent_statistics(time, agents)
=======
#### collect_agent_statistics(time, agents)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### collect_agent_statistics(time, agents)
>>>>>>> master
=======
### collect_agent_statistics(time, agents)
>>>>>>> master
Collect agent statistics from agent(s).


* **Parameters**

    
    * **time** – Timestep.
    The timestep at which to collect agents.


    * **agents** – List of agent.
    The list of agents to collect.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### record_event(time, event)
=======
#### record_event(time, event)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### record_event(time, event)
>>>>>>> master
=======
### record_event(time, event)
>>>>>>> master
Record an event


* **Parameters**

    
    * **time** – Timestep.
    The time at which to record the event.


    * **event** – event instance
    The event to record.



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
Get the statistics collected.


* **Returns**

    A dictionary with the data that was collected.
