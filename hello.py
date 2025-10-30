pin = "1234"
attempts = 3

while attempts > 0:
    passw = input("Enter the ATM PIN: ")
    if passw == pin :
        print("Access Granted ")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN . you have(attempts) attempts left")

 if attempts == 0:
    print("Account Locked ")