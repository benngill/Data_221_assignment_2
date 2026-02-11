import pandas as pd

data = pd.read_csv("crime.csv")


data["risk"] = pd.cut(data["ViolentCrimesPerPop"], # creates new column called risk
                      bins=[float("-inf"),0.5,float("inf")], # bins are <= 0.5, and > 0.5
                      labels = ["LowCrime", "HighCrime"] # bin labels
                      )
print(f"Low Crime Average Unemployment: " # prints lowCrime average unemployment %
      f"{data.groupby("risk")["PctUnemployed"].mean().loc["LowCrime"]}"
      )
print(f"High Crime Average Unemployment: " # prints highCrime average unemployment %
      f"{data.groupby("risk")["PctUnemployed"].mean().loc["HighCrime"]}"
      )

