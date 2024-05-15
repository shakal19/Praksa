# principal = 500000.0
# rate = 0.05
# payment = 2684.11
# total_paid = 0.0

# while principal > 0:
#     principal = principal * (1+rate/12) - payment
#     total_paid = total_paid + payment

# print('Total paid', total_paid)

# druga verzija

# principal = 500000.0
# rate = 0.05
# payment = 2684.11
# total_paid = 0.0
# months=0
# while principal > 0:
#    if(months<=11):
#       principal = principal*(1+rate/12)-payment-1000
#       total_paid=total_paid+payment
#       months+=1
#    else :
#       principal = principal*(1+rate/12)-payment
#       total_paid=total_paid+payment
#       months+=1
    
# print(f'{total_paid} over {months} months')



# treca verzija

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months=1
while principal > 0:
   if(months<60 or months>108):
      principal = principal*(1+rate/12)-payment
      total_paid=total_paid+payment
      months+=1
   else:
      principal = principal*(1+rate/12)-payment-1000
      total_paid=total_paid+payment
      months+=1

    
print(f'{total_paid} over {months} months')

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

# cetvrta verzija
print("Cetvrta verzija\n: ")
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months=1
while principal > 0:
   if(months<extra_payment_start_month or months>extra_payment_end_month):
      principal = principal*(1+rate/12)-payment
      total_paid=total_paid+payment
      months+=1
      print(f'{months} {total_paid} {principal} ')
   else:
      principal = principal*(1+rate/12)-payment-extra_payment
      total_paid=total_paid+payment
      months+=1
      print(f'{months} {total_paid} {principal} ')

print(f'Total paid {total_paid}' )
print('Months ', months)

    


