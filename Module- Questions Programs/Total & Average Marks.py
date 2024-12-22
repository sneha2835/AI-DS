id=int(input("Enter student ID: "))
c1=int(input("Enter marks in subect - C (out of 100) : " ))
c2=int(input("Enter marks in subect - C++(out of 100) : " ))
c3=int(input("Enter marks in subect - Java(out of 100) : " ))
total =c1+c2+c3
avg=(c1+c2+c3)/3
print("Sum of marks of 3 subject is: ", total)
print("Average of marks of 3 subjects is : ",avg )
if (total >=100 ):
  print("Passed")
else:
  print("Failed")
if total >=1000 and total <=150:
  print("P grade")
elif total >=150 and total <=200:
  print("C grade")
elif total >=200 and total <=250:
  print("B grade")
elif total >= 250 and total<=280:
  print("A grade")
else:
  print("S grade")