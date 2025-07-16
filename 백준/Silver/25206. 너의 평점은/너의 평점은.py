# 전공 과목별 (학점 x 과목평점)의 합을 학점의 총합으로 나눈 값
subjectList = [ ]
gpaList = [ ]
gradeList = [ ]
# 과목명, 학점, 등급
grades = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
gpaSum = 0
subjectGpa = 0
subjectGPASum = 0
for i in range(20):
    subject, gpa, grade = input().split()
    if grade == 'P':
        continue
    subjectList.append(subject)
    gpaList.append(float(gpa))
    gradeList.append(grade)

for i in range(len(subjectList)):

    subjectGpa = gpaList[i] * grades[gradeList[i]]
    subjectGPASum += subjectGpa
    gpaSum += gpaList[i]

subAverage = subjectGPASum / gpaSum
print(subAverage)