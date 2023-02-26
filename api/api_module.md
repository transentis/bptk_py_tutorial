# Module


<<<<<<< HEAD
## _class_ Module(model, name, parent=None)

=======
### _class_ Module(model, name, parent=None)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
The Module class is used to structure SD DSL models into individual modules.
Modules can be nested. If you create model elements such as stocks, flows and
converters via the module, the elments are added to the model, but the element
names are turned into fully qualified names of the form
parent_module_name.module_name.name. The fully qualfied name is used as the equation
name in the Model class and is needed when making calls to bptk.run_scenario or
bptk.plot_scenario.

<<<<<<< HEAD
Check our [Enterprise Digital Twin](../model_library/enterprise_digital_twin/enterprise_digital_twin.ipynb) to see an example that uses the module class


### biflow(name)
=======
Check our [Beer Distribution Game](https://github.com/transentis/beergame/blob/master/beergame_sd_dsl.ipynb) model to see how to use the Module class


#### biflow(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Add a biflow to the model. The name of the biflow will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name


<<<<<<< HEAD
### constant(name)
=======
#### constant(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Add a constanst to the model. The name of the constant will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name


<<<<<<< HEAD
### converter(name)
=======
#### converter(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Add a converter to the model. The name of the converter will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name


<<<<<<< HEAD
### flow(name)
=======
#### flow(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Add a flow to the model. The name of the flow will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name


<<<<<<< HEAD
### fqn(name)
=======
#### fqn(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Given a name this returns the fully qualified name, i.e. name prefixed
by the module namespace.


* **Parameters**

    **name** – String
    The name that is to be converted into a fully qualified name.


Returns the fully qualified name, i.e. namespace.name. The namespace is defined
by the names of all the parent modules, e.g. parent_module_name.module_name


<<<<<<< HEAD
### initialize()
=======
#### initialize()
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Override this method in concrete Module subclasses. All elements that
are internal to the module should be declared here and the equations
for both the exported elements as well as the internal elements should
be defined here.


<<<<<<< HEAD
### stock(name)
=======
#### stock(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
Add a stock to the model. The name of the stock will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name
