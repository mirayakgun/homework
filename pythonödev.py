name ="Miray"
surname="Akgün"


counter = 0


def check():
    global counter
    inputname = input("name:  ")
    inputsurname = input("surname:  ")
    if (name != inputname or surname != inputsurname):
        counter = counter +1
        print("failed")
    else:
        print("Welcome")
        counter = 99
        
    if (counter == 3):
        print("try again")

while (counter < 3):
    check()

counterr = 0
courses = ["art","music","maths", "computer science", "physics"]

for course in courses:
    print(course)

selectedCourses = []

while (len(selectedCourses) < 3):
    selected = input("selected course: ")
    if selected in courses and selected not in selectedCourses:
        selectedCourses.append(selected)
        print("added")
    else:
        print("failed")

counterrrr = len(selectedCourses)

while (counterrrr < 5):
    extracourses = input("course: ")
    if extracourses in courses and  extracourses not in selectedCourses:
        selectedCourses.append(extracourses)
        counterrrr+=1
        print("added")

    elif extracourses == "":
        print("blank")
        counterrrr+=1
    else:
        print("failed")

print(selectedCourses)
 
while (True):
    examC=input("Choose your exam course: ")
    if examC in selectedCourses:
        print("OK")
        break
    else:
        print("please try again")
grades={
"midterm": 50,
"final": 45,
"project": 65,
}
averagegrade =  ((60* grades["midterm"]/100) + (50*grades["final"]/100) + (70*grades["project"]/100))/3


if averagegrade>90:
    print("Your score is AA")
elif 70<averagegrade<90 :
    print("Your score is BB")
elif 50<averagegrade<70 :
    print("Your score is CC")
elif 30<averagegrade<50 :
    print("Your score is DD")
elif 0<averagegrade<30:
    print("Your score is FF. You failed the class.")






