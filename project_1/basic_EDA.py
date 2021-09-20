"""
This module allows to do a basic exploratory data analysis.
It allows to answer questions.
"""

import json
import pandas as pd



filename = "neos.csv"
df = pd.read_csv(filename)

filename2 = "cad.json"
with open("cad.json") as f:
    content = json.load(f)
df2 = pd.DataFrame(content['data'], columns= content["fields"])
masks = df2.cd.str.contains('2000-Jan-01')
print(content)
subset = df2[masks]

info = subset[["des", "jd", "dist", "v_rel"]]