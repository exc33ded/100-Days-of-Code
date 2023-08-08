print("Welcome to tip calculator!!")
bill = float(input('How much was the total bill? '))
tip = int(input('How much would you like to tip? 10, 12, 15 or ....'))
people = int(input('How many ways was the bill split? '))

tip_percent = tip/100
total_tip_amount = bill*tip_percent
total_bill = bill + total_tip_amount
print(total_bill)
