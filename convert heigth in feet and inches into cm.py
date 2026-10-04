''' convert heigth in feet and inches to cm.
[1 feet=12 inch and 1 inch=2.54cm]
(sample input :2 feet 7 inch
sample output:78.74cm)
prompt the user to input their height.'''
print("input your heigth:")
feet=int(input("feet"))
inches=int(input("inches:"))
#convert the heigth from feet to inches and added to inches.
inches+=feet*12
#calculate the heigth in centimeter by multiplying
#   with the conversion factor (2.54)
h_cm=inches*2,54
#print the calculated heigth in centimeters.
print("height in cm is:",h_cm)
