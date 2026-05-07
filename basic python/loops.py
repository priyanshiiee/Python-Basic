subject = ["english", "cs", "mathematics"]
marks = [100, 95, 98]
print(marks[1], subject[1])
for i in range(len(subject)):
    print(f"{subject[i]} { marks[i]}")
    print(f"sum of marks:{sum(marks)}")
    average = (sum(marks)/3)
    print(f"average marks: {average}")