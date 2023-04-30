# Carpet Optimization Algorithm

## Before using:
- Make sure to have installed the `MIP` Python package
    - See https://docs.python-mip.com/en/latest/install.html for instructions
- Other dependencies should be covered with a normal Python installation
- Note: while the code should be relatively agnostic to the system provided Python
    is installed, we successfully ran this code only on Windows 10/11, MacOS, Ubuntu 22.04

## Files
- `lp.py`: Contains the linear program formulation
- `objects.py`: Representation of abstraction terminology we use
- `process_run.py`: Runs the linear program solver on a given filename
- `gui.py`: Implements a simple GUI to run the program

## To Run:
Run `python3 gui.py` to interact with the programs

# Table of Contents
1. [Introduction to Problem](#introduction)
2. [Approach to Solution](#paragraph1)
    1. [Mathematical Formulation](#subparagraph1)
3. [Another paragraph](#paragraph2)

## Introduction <a name="introduction"></a>
As part of our deliverable regarding breaking down the current state of carpet recycling
and manufacturing from a materials/carpet design perspective, we noted the disconnect
that exists between carpet recyclers and manufacturers. Instead of merely suggesting that
manufacturers just make the carpet more recyclable, we propose that both parties
_systematically and consistently_ communicate their needs and achieve reasonable compromises.

We prototyped a simple algorithmic approach to aid in the decisions made in a carpet design.
While we will describe it as a solution to a specific question, the approach is flexible
and expandable enough for the complicated and large problem space we are studying.

Our question is as follows:

Given a carpet design defined by its constituent layer types, 
what materials should be chosen for each layer so that all specified 
goals are met as much as possible?

## Approach to Solution <a name="paragraph1"></a>
Linear programs, ubiquitous in logistical planning, are a suitable starting
point as a backbone to our problem formulation.
It is not a new idea in industry in general to employ these techniques,
but a large part of our point is to stress the need for systematic and
serious efforts to make conversations between recyclers and manufacturers
common and productive. It can serve as a tool for both parties to express
their goals.

### Mathematical Formulation <a name="subparagraph1"></a>
To be included

## Another paragraph <a name="paragraph2"></a>
The second paragraph text