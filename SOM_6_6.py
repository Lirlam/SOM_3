#Author: Liam Decaster
#Date: 04/04/2024
#####################################

import pandas as pd

import pm4py
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization
from pm4py.objects.petri_net.obj import PetriNet, Marking
from pm4py.objects.petri_net.utils import petri_utils


# create the net
net = PetriNet("doctor_net")

# creating places: source, p_1 and sink place
source = PetriNet.Place("source")
sink = PetriNet.Place("sink")
p_1 = PetriNet.Place("p_1")
p_2 = PetriNet.Place("p_2")
p_3 = PetriNet.Place("p_3")
p_4 = PetriNet.Place("p_4")
p_5 = PetriNet.Place("p_5")
p_6 = PetriNet.Place("p_6")

# add the places to the Petri Net
net.places.add(source)
net.places.add(sink)
net.places.add(p_1)
net.places.add(p_2)
net.places.add(p_3)
net.places.add(p_4)
net.places.add(p_5)
net.places.add(p_6)

# Create transitions
t_1 = PetriNet.Transition("Place Order", "Place Order")
t_2 = PetriNet.Transition("Invoice", "Invoice")
t_3 = PetriNet.Transition("Reminder", "Reminder")
t_4 = PetriNet.Transition("Pay", "Pay")
t_5 = PetriNet.Transition("Prepare Delivery", "Prepare Delivery")
t_6 = PetriNet.Transition("Make Delivery", "Make Delivery")
t_7 = PetriNet.Transition("Confirm Payment", "Confirm Payment")
empty_trans = PetriNet.Transition("hid_1", None)

# Add the transitions to the Petri Net
net.transitions.add(t_1)
net.transitions.add(t_2)
net.transitions.add(t_3)
net.transitions.add(t_4)
net.transitions.add(t_5)
net.transitions.add(t_6)
net.transitions.add(t_7)
net.transitions.add(empty_trans)

# Add arcs
petri_utils.add_arc_from_to(source, t_1, net)
petri_utils.add_arc_from_to(t_1, p_1, net)
petri_utils.add_arc_from_to(p_1, t_2, net)
petri_utils.add_arc_from_to(t_2, p_2, net)
petri_utils.add_arc_from_to(p_2, empty_trans, net)
petri_utils.add_arc_from_to(p_2, t_3, net)
petri_utils.add_arc_from_to(empty_trans, p_3, net)
petri_utils.add_arc_from_to(t_3, p_3, net)
petri_utils.add_arc_from_to(p_3, t_4, net)
petri_utils.add_arc_from_to(t_4, p_4, net)
petri_utils.add_arc_from_to(p_4, t_5, net)
petri_utils.add_arc_from_to(t_5, p_5, net)
petri_utils.add_arc_from_to(p_5, t_6, net)
petri_utils.add_arc_from_to(t_6, p_6, net)
petri_utils.add_arc_from_to(p_6, t_7, net)
petri_utils.add_arc_from_to(t_7, sink, net)

# Adding tokens
initial_marking = Marking()
initial_marking[source] = 1
final_marking = Marking()
final_marking[sink] = 1
pm4py.view_petri_net(net, initial_marking, final_marking)