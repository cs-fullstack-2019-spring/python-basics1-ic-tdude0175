def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()
'''
Create a function that asks for a student's name.
Then ask for another student's name.
Print [first student] and [second student] went to class.
'''
# input is used to ask for userInput.
# if you want to set userInput to an integer user [int()]
#  # is how you make single line comments you CAN make multi line comments
# if you want to do quote MULTILINE COMMENTS end quote use [''']
#  that won't make a real comment so don't use that INSIDE functions
def problem1():
    student1 = input("who is the first student here?")
    student2 = input("Who is the second student here?")
    print(student1 + " got here before " + student2 + " by 700 hours.")

'''
Create a function to ask the user for a grade. 
Then ask the user how much extra credit they earned. 
Print the grade plus extra credit.
'''

def problem2():
    StudentGrade = int(input("What's your grade?"))
    StudentExtraCredit = int(input("How much extra credit did you get?"))
    print(str(StudentGrade + StudentExtraCredit) + " is your final score.")

'''
Create a function to ask the user for three numbers. Print the sum as it would be written in stadard formula
'''
def problem3():
    number1= int(input("give me a number"))
    number2= int(input("give me another number"))
    number3= int(input("give me a final number"))
    print(number1,"+",number2,"+",number3,"=",number1+number2+number3)

'''
Create a function to ask the user for a number. 
If the number is negative print "Negative!". 
If the number is positive, print "Positive!. 
Otherwise print the only other number it can be.
'''
# read the instructions thoroughly
def problem4():
    number = int(input("gimme a number!"))
    if(number > 0):
        print("thats positive")
    elif(number <0):
        print("that's negative")
    else:
        print("it's zero")


if __name__=='__main__':
        main()
