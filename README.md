# Carpet Optimization Algorithm

## Before using:
- Make sure to have installed the `MIP` Python package
    - See https://docs.python-mip.com/en/latest/install.html for instructions
    - One may also require Gurobi installation, covered in https://www.gurobi.com/documentation/quickstart.html
    - For more complex and industry deployment, a valid Gurobi license is required
- Other dependencies should be covered with a normal Python installation

## Files
- `lp.py`: Contains the linear program formulation
- `objects.py`: Representation of abstraction terminology we use
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
    1. [Contact Info](#contact)

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
    These are parameters that either harm or help the overall numerical benefit. For example, recyclability of a carpet given a particular design decision may increase the overall benefit, but manufacturing cost would decrease it.
2. **Carpet design template.** 
    In this step the layers that a carpet is to be constituted by are specified along with the candidate materials possible for each layer. Furthermore, the decision factor quantitative information should also be available for each layer. That is, following the previous example, recyclability of a layer should be known.
3. **Quantifying all considerations.** 
    In this step, weights are assigned to the decision factors previously determined, as well as the formulation of any constraints under which either party may be subject.

### Mathematical Formulation <a name="subparagraph1"></a>
The model's sets are as follows:

$$
\begin{aligned}
    L & & \text{set of layers in carpet design} \\
    M_l & & \text{set of materials that a layer $l \in L$ can be made from} \\
    M = \bigcap\limits_{l \in L} M_l & & \text{set of all materials to be considered across entire carpet} \\
\end{aligned}
\\
$$

The parameters (which would in practice be determined through conversations and possibly other supporting computational methods) are as follows:

$$
\begin{aligned}
    r_{l_m} & l \in L, m \in M_l & \text{recyclability of material $m$ in layer $l$} \\
    c_{l_m} & l \in L, m \in M_l & \text{processing cost of material $m$ in layer $l$} \\
    v_{l_m} & l \in L, m \in M_l & \text{market value} \\
    f_l     & l \in L & \text{fraction of carpet a layer $l$ will be} \\
    p_m     & m \in M & \text{maximum proportion} \\
    \alpha \in \Re & & \text{weight attributed to recyclability factor} \\
    \beta \in \Re & & \text{weight attributed to processing cost} \\
    \gamma \in \Re & & \text{weight attributed to market value} \\
\end{aligned}
$$

Our decision variables represent the material choices made for each layer of the proposed carpet design:

$$
\begin{aligned}
   x_{l_m} & & l \in L, m \in M_l & & \text{ 1 if $m$ is used in $l$, else 0} \\
\end{aligned}
\\
$$

The optimization problem we have formulated thusly:

$$
\begin{equation}
\begin{aligned}
    \max_{x_{l_m}} & \sum_{l \in L}\sum_{m \in M_l} (\alpha{r_{l_m}} + \beta{c_{l_m}} + \gamma{v_{l_m}}) x_{l_m} \\
    \textrm{s.t.} & \sum_{m \in M_l} x_{l_m} = 1, \; \forall \; l \in L & \textrm{enforce one material decision per layer} \\
    & \sum_{l \in L} f_lx_{l_m} \leq p_m ,        \; \forall \; m \in M & \textrm{do not exceed max proportion of any one material} \\
\end{aligned}
\end{equation}
$$

## Another paragraph <a name="paragraph2"></a>
The second paragraph text

## Extensions <a name="paragraph3"></a>
Because our code is merely a prototype, we realize that full adoption in an industry 
setting would require at least the following extensions:
1. Write code to generate `.json` files for carpet designs, with corresponding GUI
    - Include functionality to modify current `.json` files so that 
2. Make the optimization and parser more generalizable for additional or different
kinds of decision factors that manufacturers and recyclers may be considering

For now, we keep this as a proof-of-concept as a feasible way to facilitate more
productive and frequent conversations between recyclers and manufacturers.

### Contact
If you wish for extensions to be implemented, or have additional questions,
feel free to contact: (include names and emails if you'd like)