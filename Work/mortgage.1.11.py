# mortgage.py
#
# Exercise 1.10
# mortgage.py
# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

# Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.

# When you run the new program, it should report a total payment of 929,965.62 over 342 months.
# Modify the program so that extra payment information can be more generally handled. Make it so that the user can set these variables:

# extra_payment_start_month = 60
# extra_payment_end_month = 108
# extra_payment = 1000

# 1.10: make a payment table

extra_payment_start_month = int(input("extra payment start month: "))
extra_payment_end_month = int(input("end month: "))
extra_payment_amount = int(input('amount: '))

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
payment_count = 0 
current_payment = 0

while principal > 0:
    extra = 0
    payment_count += 1

    if payment_count >= extra_payment_start_month and payment_count <= extra_payment_end_month:
        extra = extra_payment_amount

    principal *=  (1+rate/12) 
    current_payment = payment + extra
    #last payment
    if principal < current_payment:
        current_payment = principal
    
    principal -= current_payment
    total_paid = total_paid + current_payment
    print(f'payment#: {payment_count:03} total paid: {total_paid:8.2f} remaining principle: {principal:7.2f}')

print(f'Total paid {total_paid} over {payment_count} months')