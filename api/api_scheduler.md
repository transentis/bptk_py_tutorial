# Scheduler


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
## _class_ Scheduler()
Scheduler for agent based modelling


### handle_delayed_event(event, dt)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
### _class_ Scheduler()
Scheduler for agent based modelling


#### handle_delayed_event(event, dt)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
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


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### run(model, progress_widget=None, collect_data=True)
=======
#### run(model, progress_widget=None, collect_data=True)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### run(model, progress_widget=None, collect_data=True)
>>>>>>> master
=======
### run(model, progress_widget=None, collect_data=True)
>>>>>>> master
=======
### run(model, progress_widget=None, collect_data=True)
>>>>>>> master
=======
### run(model, progress_widget=None, collect_data=True)
>>>>>>> master
Run the simulation.
Override this in a subclass.


* **Parameters**

    
    * **model** – Model instance.


    * **progress_widget** – Widget (Default=None).
    If set, the widget is used to show progress during execution



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### run_step(model, sim_round, dt, progress_widget=None, collect_data=True)
=======
#### run_step(model, sim_round, dt, progress_widget=None, collect_data=True)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### run_step(model, sim_round, dt, progress_widget=None, collect_data=True)
>>>>>>> master
=======
### run_step(model, sim_round, dt, progress_widget=None, collect_data=True)
>>>>>>> master
=======
### run_step(model, sim_round, dt, progress_widget=None, collect_data=True)
>>>>>>> master
=======
### run_step(model, sim_round, dt, progress_widget=None, collect_data=True)
>>>>>>> master
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
