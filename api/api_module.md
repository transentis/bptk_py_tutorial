# Module

## Module Constructor

**Module(model, name, parent=None)**

The Module class is used to structure SD DSL models into individual modules.
Modules can be nested. If you create model elements such as stocks, flows and
converters via the module, the elments are added to the model, but the element
names are turned into fully qualified names of the form
parent_module_name.module_name.name. The fully qualfied name is used as the equation
name in the Model class and is needed when making calls to bptk.run_scenario or
bptk.plot_scenario.

Check the [Beergame](/model_library/beergame/beergame_sd_dsl.ipynb) or [Enterprise Digital Twin](/model_library/enterprise_digital_twin/enterprise_digital_twin.ipynb) models to see the module class in action. 

## Module.biflow

**biflow(name)**

Add a biflow to the model. The name of the biflow will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name


## Module.constant

**constant(name)**

Add a constanst to the model. The name of the constant will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name


## Module.converter

**converter(name)**

Add a converter to the model. The name of the converter will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name

## Module.flow

**flow(name)**

Add a flow to the model. The name of the flow will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name

## Module.fqn

**fqn(name)**

Given a name this returns the fully qualified name, i.e. name prefixed
by the module namespace.


* **Parameters**

    **name** – String
    The name that is to be converted into a fully qualified name.


Returns the fully qualified name, i.e. namespace.name. The namespace is defined
by the names of all the parent modules, e.g. parent_module_name.module_name

## Module.initialize

**initialize()**

Override this method in concrete Module subclasses. All elements that
are internal to the module should be declared here and the equations
for both the exported elements as well as the internal elements should
be defined here.


## Module.stock

**stock(name)**

Add a stock to the model. The name of the stock will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name
