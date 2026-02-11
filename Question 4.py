import pandas as pd

data = pd.read_csv("student.csv")

high_engagement = data.query('studytime >= 3 and absences <= 5 and internet == 1')
high_engagement.to_csv("high_engagement.csv")

numberOfStudent = len(high_engagement)
averageGrade = sum(high_engagement['grade'])/numberOfStudent
print(f"# of students: {numberOfStudent}")
print(f"average grade: {averageGrade}")