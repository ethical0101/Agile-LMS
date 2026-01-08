balance = 10000
amount = int(input("Enter withdrawal amount: "))

if amount % 100 != 0:
    print("Amount must be a multiple of 100")
elif amount > balance:
    print("Insufficient balance")
else:
    balance -= amount
    print("Withdrawal successful")
    print("Updated Balance:", balance)
