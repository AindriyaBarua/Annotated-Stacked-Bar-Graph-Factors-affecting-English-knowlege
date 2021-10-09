"""
Developed by Aindriya Barua in April, 2019
Thoughrough explantion of the code can be found in on my medium blog: https://medium.com/@barua.aindriya 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def draw_stacked_graph(criteria, color):
  df = pd.read_excel("FactorsData/" + criteria + ".xlsx")
  
# view dataset
  print(df)
  rows_count = len(df.index)
  
# plot a Stacked Bar Chart using matplotlib
  df.plot(
    x = criteria, 
    kind = 'barh', 
    stacked = True, 
    title = '% of responses to "Do you speak English?"', 
    figsize=(15, rows_count + 1),
    fontsize = 20,
    mark_right = True, 
    colormap = color)

  df_total = df["Yes"] + df["No"] + df["Unanswered"]
  df_rel = df[df.columns[1:]].div(df_total, 0)*100
  plt.rcParams.update({'font.size': 20})
  for n in df_rel:
      for i, (cs, ab, pc) in enumerate(zip(df.iloc[:, 1:].cumsum(1)[n], 
                                           df[n], df_rel[n])):
          plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%', 
                   va = 'center', ha = 'left',  fontsize = 20)
  plt.legend( bbox_to_anchor=(1, 1), fontsize = 20)
  plt.savefig("OutputVizualisation/" + criteria + '_english.png')



if __name__ == '__main__':
  
  draw_stacked_graph("Caste", "Accent") 
  draw_stacked_graph("Class", "Paired") 
  draw_stacked_graph("Religion", "cool")
  draw_stacked_graph("Education", "Set3") 
  draw_stacked_graph("Region", "rainbow")

