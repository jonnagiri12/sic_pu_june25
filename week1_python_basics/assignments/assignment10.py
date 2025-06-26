name = input("Enter your name : ")
emp_id = int(input("Enter your id : "))

basic_monthly_sal = int(input("Enter basic monthly salary : "))
if basic_monthly_sal < 0 or basic_monthly_sal >10000000:
    print("Invalid basic salary")
    l = True
    while l :
        basic_monthly_sal = int(input("Enter basic monthly salary : "))
        if basic_monthly_sal > 0 and basic_monthly_sal <= 10000000:
            l = False

special_allowances = int(input("Enter special allowances : "))
if special_allowances < 0 or special_allowances >10000000:
    print("Invalid special allowances")
    l = True
    while l :
        special_allowances = int(input("Enter basic monthly salary : "))
        if special_allowances > 0 and special_allowances <= 10000000:
            l = False

bonus_percentage = float(input("Enter bonus percentage annual : "))
if  bonus_percentage < 0 or bonus_percentage > 100:
    print("Invalid Bonus percentage")
    l = True
    while l :
        bonus_percentage = int(input("Enter basic monthly salary : "))
        if bonus_percentage > 0 and bonus_percentage <= 100:
            l = False


gross_mon_sal = basic_monthly_sal + special_allowances
gross_annual_sal = gross_mon_sal * 12
bonus_percentage_annual = (bonus_percentage / 100) * gross_annual_sal
gross_annual_sal = gross_annual_sal + bonus_percentage_annual

print("*" * 50)
print("Employee Name :", name)
print("Employee Id :", emp_id)
print("Gross monthly salary :", gross_mon_sal)
print("Gross annual salary :", gross_annual_sal)
print("*" * 50)

print()

print("--------Taxable Income Calculation----------")
standard_deducton = 50000
print("Gross annual salary :", gross_annual_sal)
print("Standard deduction is decided : ", standard_deducton)
taxable_income = gross_annual_sal-standard_deducton
print("Gross annual salary(After Standard deduction) :", taxable_income)


print("Tax Payable using the new Tax Regime under 2023 act :")
print('''o ₹0 - ₹3,00,000: 0%
         o ₹3,00,001 - ₹6,00,000: 5%
         o ₹6,00,001 - ₹9,00,000: 10%
         o ₹9,00,001 - ₹12,00,000: 15%
         o ₹12,00,001 - ₹15,00,000: 20%
         o Above ₹15,00,000: 30%
''')
tax_payable = 0
# if taxable_income <= 700000:
#     tax_payable = 0
if gross_annual_sal > 0 and gross_annual_sal <= 300000:
    tax_payable = 0
elif gross_annual_sal <= 600000:
    tax_payable = (0.05 * gross_annual_sal)
elif gross_annual_sal <= 900000 :
    tax_payable = (0.1 * gross_annual_sal)
elif gross_annual_sal <= 1200000 :
    tax_payable = (0.15 * gross_annual_sal)
elif gross_annual_sal <= 1500000 :
    tax_payable = (0.2 * gross_annual_sal)
elif gross_annual_sal > 1500000 :
    tax_payable = (0.3 * gross_annual_sal)

print("Tax payable because of Gross amount", gross_annual_sal, ":", tax_payable)
print("Health and Education cess :", (0.04 * gross_annual_sal))
tax_payable = tax_payable + (0.04 * gross_annual_sal)
print("Tax payable after health and education cess :", tax_payable)
print()

print("Final Outcome : ")
net_salary = gross_annual_sal - tax_payable
print("Annual Gross Salary :", gross_annual_sal)
print("Total Tax Payable :", tax_payable)
print("Annual Net Salary :", gross_annual_sal)

