
'''
المطلوب عمل نظام للضريبة 😎


طبعًا باستخدام الكلاس

النظام راح يطلب الاسم و الراتب 
وراح يحدد هل الشخص يدفع ضريبة مضافة ام لا وكم قيمتها 

استنادًا ع البيانات التالية 
اقل من 
10000
لا ضريبة مضافة 


20000
الضريبة المضافة
10 % 

40000
الضريبة المضافة 
20% 

اكثر من ذلك 
الضريبة المضافة 
30%
'''

#------------------ @start:zaid------------------------------

class TaxCalc:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
    
  def tax(self):
    if self.salary <10000:
      return 0
    elif self.salary<20000:
      return self.salary*0.10
    elif self.salary<40000:
      return self.salary*0.20
    else:
      return self.salary*0.30
    
  def details(self):
    return f"{self.name} is getting ${self.salary} as his salary, so he has to pay ${self.tax()} as a salary tax.\n\nThank you for using the Tax Calculator🌹"
  
eName=str(input("please insert the employee name here:\n"))
print("\n")
eSalary=int(input(f"please insert {eName}'s salary here:\n"))
  
  
emp=TaxCalc(eName,eSalary)
print("\n")
print("Tax=$",emp.tax())
print("\n")
print(emp.details())

#-------------------- @end:zaid------------------------------





#------------------ @start:khalid------------------------------












#-------------------- @end:khalid------------------------------



#------------------ @start:عبدالرحمن------------------------------











#-------------------- @end:عبدالرحمن------------------------------


#------------------ @start:ممدوح------------------------------










#-------------------- @end:ممدوح------------------------------
