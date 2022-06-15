deposit=float(input("How much money that you put in your saving account? "))
month=int(input("How many month that want to put your money? " ))
interest=float(input("What is the interest rate as decimal? "))
interest_each_month=interest/1200
total_value_to_date = 0   
print("Month\t deposit\t ToTal deposit\t This Month interest\t\t Total-Interest-Earned\t\tTotal-value-to-date")
def this_month(deposit, month, interest):
    F = deposit*(1+interest/1200)**month
    this_month_interest = F - deposit
    return this_month_interest
    
for time in range(1,month+1):
  if deposit<0:
    print("Invalid input")
    break  
  if month<0:
    print("Invalid Input")
    break
  if interest<0:
    print("Invalid input")
    break
  if month>32:
    print("The month can't be greater than 32months or 3 years")
    break
  if interest>12:
    print("The interest can't be greater than 12%")
    break
  #Total Deposit
  total_deposit=deposit*time
  #Total_value_to_date
  total_value_to_date +=deposit*(1+interest_each_month)**time
  #Total interest earned
  total_interest_earned = total_value_to_date - total_deposit
  #This month interest
  this_month_interest = this_month(deposit,time,interest)
  print(f'{time}\t\t {format((deposit),".2f")}\t\t {format((total_deposit),".2f")}\t\t\t\t\t   {"{:.2f}".format(this_month_interest)}\t\t\t\t\t\t  {"{:.2f}".format(total_interest_earned)}\t\t\t\t\t\t{format((total_value_to_date),".2f")}\t\t\t ')
