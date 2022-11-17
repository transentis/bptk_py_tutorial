# DataCollector


### _class_ DataCollector()
A datacollector for the agent based simulation.
Collects the output data of each agent/event and makes it available to external resources such as BPTK-Py to plot the data


#### collect_agent_statistics(time, agents)
Collect agent statistics from agent(s).


* **Parameters**

    
    * **time** – Timestep.
    The timestep at which to collect agents.


    * **agents** – List of agent.
    The list of agents to collect.



#### record_event(time, event)
Record an event


* **Parameters**

    
    * **time** – Timestep.
    The time at which to record the event.


    * **event** – event instance
    The event to record.



#### statistics()
Get the statistics collected.


* **Returns**

    A dictionary with the data that was collected.
