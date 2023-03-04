# Changelog

## BPTK Change Log

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