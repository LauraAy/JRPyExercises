gross_inc = input("Enter your gross income from your W-2 for 2020")
#print(gross_inc)

num_dep = input("How many dependents are you claiming?")
#print(num_dep)

#convert the input values to numbers
gross_inc_float = float(gross_inc)
num_dep_int = int(num_dep)

tax_income = gross_inc_float - 12200 - (2000 * num_dep_int)
print(tax_income)

# calculate tax due
tax_due = tax_income * 0.1

#print the result
print(tax_due)

