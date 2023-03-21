---
title: Scheduler
description: BPTK API Documentation for the Scheduler class
keywords: agent-based modeling, bptk, bptk-py, python, business prototyping
---

# Scheduler

Scheduler for agent based modelling. 

## Scheduler Constructor

**Scheduler()**

Scheduler for agent based modelling

## Scheduler.handle_delayed_event

**handle_delayed_event(event, dt)**

This method checks to see whether the event is a DelayedEvent.

If not, it simply returns the event.

If yes, it counts down the delay by one timestep (dt), caches the event in delayed_events and returns None.

* **Parameters**

    
    * **event** – Event.
    The event to check


    * **dt** – Integer
    the timestep to count down.


Returns

    The event if this is not a DelayedEvent or the delay<=0 , otherwise None
 
## Scheduler.run

**run(model, progress_widget=None, collect_data=True)**

Run the simulation.
Override this in a subclass.


* **Parameters**

    
    * **model** – Model instance.


    * **progress_widget** – Widget (Default=None).
    If set, the widget is used to show progress during execution

## Scheduler.run

**run_step(model, sim_round, dt, progress_widget=None, collect_data=True)**

Run a simulation step.

Override this in a subclass.


* **Parameters**

    
    * **model** – Model
    Model instance


    * **sim_round** – Integer
    round of simulator


    * **dt** – Integer.
    Current step of round


    * **progress_widget** – Widget (default=None)
    Live instance of FloatProgressBar


    * **collect_data** – Boolean.
    Flag that indicates whether to collect data.
