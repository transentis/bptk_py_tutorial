# Module


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
## _class_ Module(model, name, parent=None)

=======
### _class_ Module(model, name, parent=None)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
## _class_ Module(model, name, parent=None)

>>>>>>> master
=======
## _class_ Module(model, name, parent=None)

>>>>>>> master
=======
## _class_ Module(model, name, parent=None)

>>>>>>> master
=======
## _class_ Module(model, name, parent=None)

>>>>>>> master
The Module class is used to structure SD DSL models into individual modules.
Modules can be nested. If you create model elements such as stocks, flows and
converters via the module, the elments are added to the model, but the element
names are turned into fully qualified names of the form
parent_module_name.module_name.name. The fully qualfied name is used as the equation
name in the Model class and is needed when making calls to bptk.run_scenario or
bptk.plot_scenario.

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
Check our [Enterprise Digital Twin](../model_library/enterprise_digital_twin/enterprise_digital_twin.ipynb) to see an example that uses the module class


### biflow(name)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
Check our [Beer Distribution Game](https://github.com/transentis/beergame/blob/master/beergame_sd_dsl.ipynb) model to see how to use the Module class


#### biflow(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
Add a biflow to the model. The name of the biflow will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### constant(name)
=======
#### constant(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### constant(name)
>>>>>>> master
=======
### constant(name)
>>>>>>> master
=======
### constant(name)
>>>>>>> master
=======
### constant(name)
>>>>>>> master
Add a constanst to the model. The name of the constant will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### converter(name)
=======
#### converter(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### converter(name)
>>>>>>> master
=======
### converter(name)
>>>>>>> master
=======
### converter(name)
>>>>>>> master
=======
### converter(name)
>>>>>>> master
Add a converter to the model. The name of the converter will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### flow(name)
=======
#### flow(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### flow(name)
>>>>>>> master
=======
### flow(name)
>>>>>>> master
=======
### flow(name)
>>>>>>> master
=======
### flow(name)
>>>>>>> master
Add a flow to the model. The name of the flow will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### fqn(name)
=======
#### fqn(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### fqn(name)
>>>>>>> master
=======
### fqn(name)
>>>>>>> master
=======
### fqn(name)
>>>>>>> master
=======
### fqn(name)
>>>>>>> master
Given a name this returns the fully qualified name, i.e. name prefixed
by the module namespace.


* **Parameters**

    **name** – String
    The name that is to be converted into a fully qualified name.


Returns the fully qualified name, i.e. namespace.name. The namespace is defined
by the names of all the parent modules, e.g. parent_module_name.module_name


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### initialize()
=======
#### initialize()
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### initialize()
>>>>>>> master
=======
### initialize()
>>>>>>> master
=======
### initialize()
>>>>>>> master
=======
### initialize()
>>>>>>> master
Override this method in concrete Module subclasses. All elements that
are internal to the module should be declared here and the equations
for both the exported elements as well as the internal elements should
be defined here.


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### stock(name)
=======
#### stock(name)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### stock(name)
>>>>>>> master
=======
### stock(name)
>>>>>>> master
=======
### stock(name)
>>>>>>> master
=======
### stock(name)
>>>>>>> master
Add a stock to the model. The name of the stock will be a fully qualified name
consisting of all nested module names plus the actual element name using dot
notation, i.e. namespace.name
