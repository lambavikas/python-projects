print("Test 200")
print(10)
print(3.545)
print("20 days are " + str(20*24*60) + " seconds")
##after Pytho 3.0
print(f"20 days are {20*24*60} seconds")

def calc():
   print(f"20 days are {20*24*60} seconds") 
   print("Inside the Function")

calc()


def days_to_units(days, calc_to_units, units):
   print(f"{days} days are {days * calc_to_units} {units}")

days = 10
calc_to_units = 24
units = "hours"
days_to_units(days, calc_to_units, units)

