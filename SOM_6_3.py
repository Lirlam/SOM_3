
###Uebungsblatt 6 SOM
## Imports
import pm4py
import pandas as pd

# process mining libraries
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization
from pm4py.objects.petri_net.obj import PetriNet, Marking
from pm4py.objects.petri_net.utils import petri_utils

## reading data
fn = 'interval_event_log_with_artificial_resources.csv'
events = pd.read_csv(fn)

events.columns = ['orderID', 'activity', 'endtime', 'starttime', 'resource']
events.head()

events['endtime'] = pd.to_datetime (events [ 'endtime'])
events['starttime'] = pd.to_datetime(events['starttime'])

## Aufgabe 3 DFG
# read in pandas dataframe into pm4py log
eventlog = events.copy()

# Specify which columns correspond to case (case:concept:name), # event (concept: name) and timestamp (time:timestamp) eventlog.rename(columns={'endtime': 'time:timestamp',

eventlog.rename(columns={"endtime": "time:timestamp", "starttime": "start_timestamp",
                         "orderID": "case:concept:name", "activity": "concept:name",
                         "resource": "org:resource"}, inplace=True)

log = log_converter.apply(eventlog)

## Aufgabe 3
#Create graph from log (annotated with frequency)
dfg = dfg_discovery.apply(log)

# viz
gviz = dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.FREQUENCY)
dfg_visualization.view(gviz)

# creatig the graph from log (annotated with time)
dfg = dfg_discovery.apply(eventlog, variant=dfg_discovery.Variants.PERFORMANCE)

# viz
gviz = dfg_visualization.apply(dfg, log=eventlog, variant=dfg_visualization.Variants.PERFORMANCE)
dfg_visualization.view(gviz)