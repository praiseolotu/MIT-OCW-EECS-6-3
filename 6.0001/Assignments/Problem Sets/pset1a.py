import math, sys, os, threading

annual_salary = float(input("Enter your annual salary:"))
portion_save = float(input("Enter the percent of your salary to save,  as a  decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))

current_savings = 0
monthly_salary = annual_salary/12
real_portion_saved = portion_save * monthly_salary
r = 0.04
portion_down_payment = total_cost * 0.25

months = 0

while current_savings <= portion_down_payment:
	investment_returns = current_savings * (r/12)
	current_savings += investment_returns + real_portion_saved
	months += 1

print("Number of months", months)
