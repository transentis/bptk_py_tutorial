# Simultaneous Scheduler


<<<<<<< HEAD
## _class_ SimultaneousScheduler()
Implementation of a scheduler. Runs steps synchronously


### run(model, progress_widget=None, collect_data=True)
=======
### _class_ SimultaneousScheduler()
Implementation of a scheduler. Runs steps synchronously


#### run(model, progress_widget=None, collect_data=True)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Run method


* **Parameters**

    
    * **model** – Model instance.
    Instance of the model this is a scheduler for.


    * **progress_widget** – FloatBarProgress instance.
    Used to display progress of the scheduler.

<<<<<<< HEAD
### run_step(model, sim_round, step, progress_widget=None, collect_data=True)
=======


#### run_step(model, sim_round, step, progress_widget=None, collect_data=True)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Run one step.


* **Parameters**

    
    * **sim_round** – simulator round.


    * **dt** – step of round.


    * **model** – Model instance.


    * **progress_widget** – FloatBarProgress instance.
    Ipywidgets element used to track progress.
