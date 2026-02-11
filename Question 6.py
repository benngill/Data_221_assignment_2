import pandas as pd

data = pd.read_csv("crime.csv")


data["risk"] = pd.cut(data["ViolentCrimesPerPop"],
                      bins=[float("-inf"),0.5,float("inf")],
                      labels = ["LowCrime", "HighCrime"]
                      )
print(f"Low Crime Average Unemployment: "
      f"{data.groupby("risk")["PctUnemployed"].mean().loc["LowCrime"]}"
      )
print(f"High Crime Average Unemployment: "
      f"{data.groupby("risk")["PctUnemployed"].mean().loc["HighCrime"]}"
      )

