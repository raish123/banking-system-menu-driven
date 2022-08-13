
import DatabaseBank as db

while (True):
    
    print ('''Welcome to ITVEDANT BANK
              Select the option you want to perform operation:
              0. Exit
              1. Open a bank account
              2. Deposit Money in his account
              3. Withdraw money from his account
              4. change owner name
              5. display transaction details
              6. close account
              ''')

    choice=int(input('Enter your choice to perform operation: '))
    if choice ==0:
        break
    elif choice == 1:
        db.bank_detail()
    elif choice==2:
        db.deposit()
    elif choice==3:
        db.withdraw()
    elif choice==4:
        db.changename()
    elif choice==5:
        db.transdetail()
    elif choice==6:
        db.removeaccount()
        
    else:
        print("INVALID ENTERIES")

 




       