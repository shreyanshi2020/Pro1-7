import pandas as pd
import plotly.graph_objects as pgo

data = pd.read_csv("data.csv")
print(data.groupby("level")["attempt"].mean())

studentdf = data.loc[data["student_id"]=="TRL_xsl"]
fig = pgo.Figure(pgo.Bar(x = studentdf.groupby("level")["attempt"].mean(), y = ["Level 1", "Level 2", "Level 3", "Level 4"], orientation = "h"))
fig.show()