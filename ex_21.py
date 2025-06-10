# ATM Cash Withdrawal Validator
# Ask user for amount to withdraw.
# Must be a multiple of 100.
# Must not exceed ₹10,000.
# Must not be more than current balance (assume ₹8,500).

money = float(input("enter the amount = "))

if money %100 == 0 and money <= 10000 and money <= 8500:
    print("please collect your amonut")
else:
    print("please enter correct denomination")

