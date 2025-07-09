#1. Create an empty dictionary
#2. Prompt the user for the student name key --> Add the value to the dictionary
#3. Prompt the user for student age key
#4. Prompt the user for the student grade key
#5. Prompt the user for the student hobbies key(A nested list)
#6. Print the dictionary to the console

student = {}

studentName= input ("Enter your student's name:")
student["Name"] = studentName

studentAge= input("Enter your student's age")
student["age"] = studentAge

studentgrade= input("Enter your student's grade")
student["grade"] = studentgrade

hobbies = []
hobby = input ("Enter your student's hobby; Type 'done:"). lower()
hobbies.append(hobby)

while hobby != "done":
      hobby= input ("Enter your student's hobby; Type 'done'when done:") . lower()
student["Hobbies"] = hobbies

print(student)
