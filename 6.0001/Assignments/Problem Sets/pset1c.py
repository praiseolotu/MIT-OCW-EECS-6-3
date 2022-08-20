import math, sys, os, time
t0 = time.process_time()
init_annual_salary = float(input("Enter the starting salary: "))
annual_salary = init_annual_salary
semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000.0
required_months = 36
current_savings = 0
portion_down_payment = total_cost * 0.25
low = 0
high = max(1.0, 10000.0)
avg = (low + high)/2
epsilon = 100  #$100
months = 0
start = 1
num_steps = 0

while start:
	while (portion_down_payment - current_savings) > epsilon:
		monthly_salary = annual_salary/12
		investment_returns = current_savings * (r/12)
		current_savings += investment_returns + monthly_salary*(avg/10000)
		months += 1
		
		if months % 6 == 0:
			annual_salary += annual_salary * semi_annual_raise
		
	if months > required_months:
		low = avg
		current_savings = 0
		months = 0
		annual_salary = init_annual_salary
		
	elif months < required_months:
		high = avg
		current_savings = 0
		months = 0
		annual_salary = init_annual_salary
		
	else: # months == required_months
		best_rate = avg/10000
		possible = 1
		start = 0
		#since we have gotten best rate
	num_steps += 1
	avg = (high + low)/2
		
#since avg represent %, an higher avg means more % of saving
	if avg == 9999: #if saving 99.99% of salary
		possible = 0
		start = 0
if possible:
	print("Best savings rate: ", best_rate)
	print("Steps in bisection search: ", num_steps)
else:
	print("It is not possible to pay the down payment in three years.")
t1 = time.process_time() - t0
print("t =", t0, ":", t1, "s")
