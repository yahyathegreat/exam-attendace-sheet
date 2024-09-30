medicalcause=input("did you have a medical cause yes or no")
atten=int(input("enter the attendance of student:"))
if medicalcause =='yes':
    print("you are allowed")
else:
   if atten>=75:
    print("allowed")
   else:
    print("you are allowed") 