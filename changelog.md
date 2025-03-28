# Changelog

## BPTK Change Log

### 2.0.0

* Support for multidimensional sddsl

### 1.9.6

* Enabled modulo operation for sddsl-elements
* removed unnecessary code
* added unittests/pytests 

### 1.9.5

* Fix publication issues

### 1.9.4

* Fix publication issues

### 1.9.3

* Fix agent.py serialize method
* Removed to_string method of agent.py
* Fix csv_datacollector.py 
* Removed kinesis_datacollector.py, yaml_model_parser.py and serializer.py
* Fix model.py reset method
* Adjusted model.py configure_properties method (only dict-values allowed)
* added unittests

### 1.9.2

* Fix to build script

### 1.9.1

* Bump versions of key dependencies
* Update XMILE parser grammar to remove depreciation warning
* Remove obsolete documentation files
* Update setup to use pyproject.toml
* Bump Python Version to 3.11

### 1.9.0
* BPTKServer: `run` endpoint now also works for agent-based models
* Model: Add `configure_agent`, `configure_properties` and `delete_agent(s)` methods
* Bump versions of key dependencies

### 1.8.0
* BPTKServer: Add new endpoint `start-instances` that starts multiple instances in one goo

### 1.7.6
* BPTK: Improve handling of floating point numbers when using small DTs
* ScenarioManagerSD: Fixed an issue that caused models with biflows to be cloned incorrectly

### 1.7.5
* BPTK: Fix that caused a crash when using multiple scenario files for hybrid models

### 1.7.4
* BPTK: Fix bug in reset_scenarios for Hybrid Scenario Managers

### 1.7.3
* BPTK: Update dependencies of Pandas / Matplotlib / Sympy / Parsimonious / Pyyaml / Xlsxwriter / Jinja2 / Requests / Jsonpickle / Flask
* Successfully tested with Python 3.11

### 1.7.2
* BPTK: Fix imports of SimpleDashboard class
* BPTK: Update dependency of Scipy, Numpy and Pyyaml

### 1.7.1
* BPTK: reset_cache now also resets the data collector in agent based models
* BPTK: reset_cache calls the reset_cache method on all agents
* BPTK: agents now have a reset_cache method that can be used to reset agent state
* BPTK: Updated dependency on ipywidgets to 8.0.4

### 1.7.0
* BPTK Server: Remote authorization for root, full-metrics and metrics endpoints
* BPTK Server: Add /healthy endpoint
* BPTK Server: stop-instance and load-state are now POST resources
* Bug Fix: Remove debug print message

## BPTK Tutorial and Documentation Change Log

### 2025-03-27

* Update to BPTK 2.0.0
* Add notebook on multidimensional models

### 2023-11-03

* Update to Enterprise Digital Twin


### 2023-04-02

* Add section on System Archetypes to model library
* Update and fix some of the diagrams

### 2023-03-21

* Simplify SD model in Enterprise Digital Twin
* Update documentation of Model and Module
* Re-organize tutorials
* Merge docs on BptkServer
* Move doc on ExternalStateAdapter to API section
* Add a document on the mathematics underlying the SD DSL
* Update document on SD DSL functions
* Bump version of BPTK

### 2023-03-11

* Bump version of BPTK

### 2023-03-04

* Move XMILE into System Dynamcis section
* Add Algolia search

### 2023-03-03

* Improve readability of API docs
* Use Jupyter notebooks instead of markdown for overview pages
* Add "Introduction to BPTK Server" notebook
* Add "SD DSL Under The Hood" notebook
* Remove readme.ipynb to reduce reduncancy

### 2023-03-01

* Bump version of BPTK to 1.7.4
* Add Beer Distribution Game to Model Library
* Improve link structure

### 2023-02-26

* Change theme
* Add Quickstart
* Migrate model library from Model Library Github repo
* Add Enterprise Digital Twin to Model Libary


