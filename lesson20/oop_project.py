from bank_accounts import *

Dorian = BankAccount(1000, "Dorian")
Sara = BankAccount(2000, "Sara")

Dorian.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dorian.withdraw(10000)
Dorian.withdraw(10)

Dorian.transfer(10000, Sara)
Dorian.transfer(100, Sara)

Jim = IntrestRewardsAcc(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dorian)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)
