import json
from .common import *
import os

loc = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(loc, 'angles_regular_graphs.json'), 'r') as json_file:
    fixed_angles_data = json.load(json_file)