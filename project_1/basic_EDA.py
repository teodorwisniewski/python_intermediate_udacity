import requests
import json
import pandas as pd



filename = "neos.csv"
df = pd.read_csv(filename)
print(df)


filename2 = "cad.json"
with open("cad.json") as f:
    content = json.load(f)
df2 = pd.DataFrame(content['data'], columns= content["fields"])
print(content)
