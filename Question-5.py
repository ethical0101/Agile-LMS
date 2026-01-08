basic = float(input("Enter basic salary: "))

hra = 0.20 * basic
da = 0.10 * basic
gross_salary = basic + hra + da
tax = 0.05 * gross_salary
net_salary = gross_salary - tax

print("Net Salary:", net_salary)
