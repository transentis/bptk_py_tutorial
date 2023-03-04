---
title: Simultaneous Scheduler
description: API Documentation for the Simultaneous Scheduler class
keywords: agent-based modeling, bptk, bptk-py, python, business prototyping
---

# Simultaneous Scheduler

## SimultaneousScheduler Constructor

**SimultaneousScheduler()**

Implementation of a scheduler. Runs steps synchronously


## SimultaneousScheduler.run

**run(model, progress_widget=None, collect_data=True)**

Run method

* **Parameters**
    
    * **model** – Model instance.
    Instance of the model this is a scheduler for.

    * **progress_widget** – FloatBarProgress instance.
    Used to display progress of the scheduler.

## SimultaneousScheduler.run_step

**run_step(model, sim_round, step, progress_widget=None, collect_data=True)**

Run one step.

* **Parameters**
    
    * **sim_round** – simulator round.

    * **dt** – step of round.

    * **model** – Model instance.

    * **progress_widget** – FloatBarProgress instance.
    Ipywidgets element used to track progress.
