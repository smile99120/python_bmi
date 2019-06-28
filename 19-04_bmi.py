  # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

kg = int(input("kg="));
m = int(input("cm="))/100;

BMI = kg/(m*m);              
print("BMI = ",BMI);

if BMI < 18.5:        
    print("體重過輕");
elif 18.5 <= BMI < 24:
    print("體重正常");   
elif 24 <= BMI < 27:
    print("體重過重"); 
else:
    print("體重肥胖");  