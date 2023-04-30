import json
from objects import *
from lp import *

# input the file that we want to parse via the GUI or some other means


# parse the json file

filename = "sample_carpet_design1.json"
with open(filename) as myFile:
    fileData = json.load(myFile)
    #print(fileData)

# go through each layer pull out layer name - create layer object
# while parsing through materials list, create corresponding material objects and fill in params
# 
layers = []
index = 0
for layer_type in fileData:
    layer_data = fileData[layer_type][0]
    layers.append(Layer(layer_type, [], float(layer_data["Proportion"][0])))
    
    for material in layer_data["Material"]:
        m = Material(material, 0, 0, 0)
        layers[index].materials.append(m)
    
    for i in range(len(layers[index].materials)):
        layers[index].materials[i].rec = float(layer_data["Recyclability"][i])
        layers[index].materials[i].proc_cost = float(layer_data["ProcessCost"][i])
        layers[index].materials[i].mkt_value = float(layer_data["MarketValue"][i])

    index += 1

alpha = 90
beta = -40
gamma = -25

lp_solve(alpha, beta, gamma, layers)
