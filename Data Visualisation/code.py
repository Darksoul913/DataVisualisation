import pandas as pd
import csv 
import plotly.graph_objects as go

df = pd.read_csv('/Volumes/U/Data Visualisation/data.csv')
print(df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x = df.groupby("level")["attempt"].mean(),
    y = ['Level1', 'Level2', 'Level3', 'Level4'],
    orientation = 'h'
))

fig.show()