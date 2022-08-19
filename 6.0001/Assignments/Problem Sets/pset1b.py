import math, sys, os, threading

annual_salary = float(input("Enter your starting annual salary:"))
portion_save = float(input("Enter the percent of your salary to save,  as a  decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semiannual raise, as  a  decimal:"))

current_savings = 0
r = 0.04
portion_down_payment = total_cost * 0.25

months = 0

while current_savings <= portion_down_payment:
	monthly_salary = annual_salary/12
	real_portion_saved = portion_save * monthly_salary
	investment_returns = current_savings * (r/12)
	current_savings += investment_returns + real_portion_saved
	months += 1
	
	if months % 6 == 0:
		annual_salary += annual_salary * semi_annual_raise
		
print("Number of months", months)
