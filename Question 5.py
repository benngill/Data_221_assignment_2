import pandas as pd

data = pd.read_csv("student.csv")

data["grade_band"] = pd.cut(
    data["grade"],
    bins=[-float("inf"), 9, 14, float("inf")],
    labels=["Low", "Medium", "High"]
    )

groupedSummary = data.groupby("grade_band").agg(number_of_student = ("grade","count"),
                                                          average_absences = ("absences", "mean"),
                                                          percent_with_internet = ("internet", "mean"))

print(groupedSummary)
groupedSummary.to_csv("student_bands.csv")

