# Carpet Optimization Algorithm
### _Arba Shkreli, Francisco Marquez, Nicholas Laws_

## Notes

The following documentation is an explanation of the prototype implementation of 
the algorithm presented in our report.

## Before using:
- Make sure to have installed the `MIP` Python package
    - See https://docs.python-mip.com/en/latest/install.html for instructions
    - One may also require Gurobi installation, covered in https://www.gurobi.com/documentation/quickstart.html
    - For more complex and industry deployment, a valid Gurobi license is required
- Other dependencies should be covered with a normal Python installation

## Files
- `objects.py`: Representation of abstraction terminology we use
- `lp.py`: Contains the linear program formulation
- `process_run.py`: Runs the linear program solver on a given filename
- `gui.py`: Implements a simple GUI to run the program
- `sample_carpet_design1.json`: Sample basic carpet design with parameters specified (numbers in it are not realistic or particularly meaningful)

## To Run:
Run `python3 gui.py` to interact with the programs

# Table of Contents
1. [Introduction to Problem](#introduction)
2. [Approach to Solution](#approach-to-solution)
    1. [Mathematical Formulation](#mathematical-formulation)
3. [Another paragraph](#another-paragraph)
4. [Extension Possibilities](#extensions)
    1. [Contact](#contact)

## Introduction <a name="introduction"></a>
As part of our deliverable regarding breaking down the current state of carpet recycling
and manufacturing from a materials/carpet design perspective, we noted the disconnect
that exists between carpet recyclers and manufacturers. Instead of merely suggesting that
manufacturers just make the carpet more recyclable, we propose that both parties
_systematically and consistently_ communicate their needs and achieve reasonable compromises.

We prototyped a simple algorithmic approach to aid in the decisions made in a carpet design.
While we will describe it as a solution to a specific question, the approach is flexible
and expandable enough for the complicated and large problem space we are studying.

The kind of question our algorithm answers is the following:

Given a carpet design defined by its constituent layer types, 
what materials should be chosen for each layer so that all specified 
goals are met as much as possible?

## Approach to Solution <a name="paragraph1"></a>
We are looking at an optimization problem with possible constraints. To maintain
generality and simplicity, we opted to formulate this as a binary integer program.
Linear programs, ubiquitous in logistical planning, are a suitable starting
point as a backbone to our problem formulation.

It is not a new idea in industry to employ these techniques,
but a large part of our point is to stress the need for systematic and
serious efforts to make conversations between recyclers and manufacturers
common and productive. It can serve as a tool for both parties to express
their goals.

1. **Determination of decision factors important to both manufacturers and recyclers.** 
    These are parameters that either harm or help the overall numerical benefit. For example, recyclability of a carpet given a particular design decision may increase the overall 
    benefit, but manufacturing cost would decrease it.
2. **Carpet design template.** 
    In this step the layers that a carpet is to be constituted by are specified along with the candidate materials possible for each layer. Furthermore, the decision factor quantitative information should also be available for each layer. That is, following the previous example, recyclability of a layer should be known.
3. **Quantifying all decision factors.** 
    In this step, weights are assigned to the decision factors previously determined, as well 
    as the formulation of any constraints under which either party may be subject.

More information about the underlying mathematical formulation can be found in our report.

## Breakdown of Functionality Implementation <a name="paragraph2"></a>

`objects.py`

To follow an object-oriented paradigm and remove the optimization code's direct 
interaction with the database files, we defined the objects relevant to our 
computation.

`lp.py`

Using a linear programming package called `MIP`, this file expresses the Binary
Integer Program formulation outlined in the report. Assumes that inputs will be
given in the format specified in `objects.py`. The functions specified in this
file return strings given to the GUI.

`process_run.py`

Performs parsing of the carpet design file, places the parsed information into the
format specified by `objects.py` and runs the optimization algorithm. The parameter
weights are specified and should be changed here.

`gui.py`

Implements GUI for the previously-specified code. A user can choose from a dropdown
menu from all the carpet design `.json` files in the same directory, and then run
the optimization on the 

`sample_carpet_design1.json`

This is an example of how one would format a carpet design file. `.json` files organize 
data with `key:value` pairs. Each layer is specified with a name, and within there are 
the fields of interest that are specified. Currently, our model **requires** the fields 
"Proportion" "Material", "Recyclability", "ProcessCost", and "MarketValue", with those 
names verbatim to be specified with a list of values.

Note: the "Proportion" list should contain one value, and the proportions across all layers
should add up to 1, and each respectively be strictly positive.

Furthermore, for the other fields, the same number of elements should be in each list. 
Corresponding values across fields are determined by their relative order in the list.
For example, the first value in the "Material" list corresponds to the first value in
the "Recyclability" list. 

For even more specific details, see the individual files' comments.

## Extensions <a name="paragraph3"></a>
Because our code is merely a prototype, we realize that full adoption in an industry 
setting would require at least the following extensions:
1. Write code to generate `.json` files for carpet designs, with corresponding GUI
    - Include functionality to modify current `.json` files so that no formatting
    errors are introduced by users
2. Make the optimization and parser more generalizable for additional or different
kinds of decision factors that manufacturers and recyclers may be considering
    - Some aspects are essentially hard-coded that we would like to make more
    dynamic and easier to change.

For now, we keep this as a proof-of-concept as a feasible way to facilitate more
productive and frequent conversations between recyclers and manufacturers.

## Contact

Thanks for your interest! For questions or code issues, feel free to start a thread 
in this repository.