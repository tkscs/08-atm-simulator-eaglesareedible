"""
Options:
- check the balance: prints current balance
- withdraw money:
    ask you how much to withdraw
    reduce the balance by that amount
    if you try to withdraw more than you have...
        print error don't update the balance
    don't withdraw a negative amount
- deposit money:
    ask you how to deposit
    increase the balance by that amount
    don't deposit a negative amount
- loop (with a while loop) until the user says "exit"
"""

# start with 1 million dollars
balance = 0
action = 'home'

while action == 'home':
    print(f'Your current balance is ${balance}')
    action = input("Please select an action\nDeposit\nWithdraw\nExit\n")
    while action == 'Deposit':
        DepositAmount=float(input("Select deposit amount:\n"))
        balance=balance+DepositAmount
        while DepositAmount<0:
            balance=balance-DepositAmount
            DepositAmount=float(input("Cannot make negative deposit. Please try again.\n"))
            balance=balance+DepositAmount
        action = 'home'
    while action == 'Withdraw':
        WithdrawAmount=float(input("Enter amount of Withdraw\n"))
        balance=balance-WithdrawAmount
        while balance < 0:
            balance=balance+WithdrawAmount
            WithdrawAmount=float(input(f"Balance too low, current balance ={balance} enter allowed withdraw amount:\n"))
            action = 'home'
    while action == 'Exit':
        break