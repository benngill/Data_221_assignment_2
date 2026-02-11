import pandas as pd

data = pd.read_csv("student.csv")

data["grade_band"] = pd.cut(
    data["grade"],
    bins=[-float("inf"), 9, 14, float("inf")], # sets bins to <= 9, <=14, >14
    labels=["Low", "Medium", "High"] # bin labels
    )

groupedSummary = data.groupby("grade_band").agg(number_of_student = ("grade","count"), # adds number of students
                                                          average_absences = ("absences", "mean"), # adds average number of absences
                                                          percent_with_internet = ("internet", "mean")) # adds percent of students with internet access

print(groupedSummary)
groupedSummary.to_csv("student_bands.csv") # save grouped summary to .csv

