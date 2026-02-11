import pandas as pd

data = pd.read_csv("student.csv")

high_engagement = data.query('studytime >= 3 and absences <= 5 and internet == 1') # queries rows that have high studytime, low absences and internet
high_engagement.to_csv("high_engagement.csv") # saves desired rows to new .csv file

numberOfStudent = len(high_engagement) # gets number of students
averageGrade = sum(high_engagement['grade'])/numberOfStudent # gets average grade of students
print(f"# of students: {numberOfStudent}") # prints the number of students in high engagement
print(f"average grade: {averageGrade}") # prints the grade average of students in high engagement