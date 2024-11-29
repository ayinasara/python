'''
description:Program to check whether the given number is a valid mobile number or not using functions.
return:true if  number is valid else false
'''
def numbers(number):
    if len(number)==10 and number[0] in ["9","8","7"]:
       return True
    return False
mobile_number=input("enter phone number")
if numbers==mobile_number:
    print(f"the mobile number  {mobile_number} is valid")
else:
    print(f"the mobile number {mobile_number} is not valid")
numbers(mobile_number)



