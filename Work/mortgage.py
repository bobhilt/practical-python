# mortgage.py
#
# Exercise 1.7
# mortgage.py
# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

# Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.

# When you run the new program, it should report a total payment of 929,965.62 over 342 months.



principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
payment_count = 0 
current_payment = 0

while principal > 0:
    extra = 0
    payment_count += 1

    if payment_count <= 12:
        extra = 1000
        print('payment#', payment_count)

    principal *=  (1+rate/12) 
    current_payment = payment + extra
    #last payment
    # if principal < (payment + extra):
    #     payment, extra = principal, 0
    
    principal -= current_payment
    total_paid = total_paid + current_payment

print(f'Total paid {total_paid} over {payment_count} months')