def toConvert(grade):
    """ Returns grade weight """
    if grade >= 90 & grade <= 100:
        return 4.00
    elif grade >= 80 & grade <= 89:
        return 3.00
    elif grade >= 70 & grade <= 79:
        return 2.00
    elif grade >= 60 & grade <= 69:
        return 1.00
    else:
        return 0.00

def getGPA(course, grade, credits):
    """ Processing output """
    totalGradePoints = 0
    # Printing header
    print("\n%-15s %-10s %-15s %-10s %-10s \n" % ("Course", "Grade", "Grade Weight", "Credits", "Grade Points"))
    for i in range(4):
        wt = toConvert(grade[i])
        print("%-15s %-10s %-15.2f %-10.2f %-10.2f \n" % (course[i], grade[i], wt, credits[i], wt * credits[i]))
        totalGradePoints += (wt * credits[i])
    print("%-15s %-10s %-15.2s %-10.2f %-10.2f \n" % ("Total", " ", " ", sum(credits), totalGradePoints))

    print("\n\n\t\t Semester GPA = %.1f/%.1f = %.2f\n\n" % (
    totalGradePoints, sum(credits), (totalGradePoints / sum(credits))))


def main():
    course = []
    grade = []
    credits = []

        # Reading four values
    for i in range(4):
        course.append(input("Enter Course Name: "))
        grade.append(int(input("Enter Grade: ")))
        credits.append(float(input("Enter Credits: ")))
        print("\n")
    #return course, grade, credits
    getGPA(course, grade, credits)

# Calling main
main()