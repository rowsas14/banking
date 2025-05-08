admin_username="Admin"
admin_password=123456

customer={}

#admin login
def admin_login():
    admin_name=input("enter admin username")
    admin_pwd=int(input("enter password"))


    if admin_name == admin_username and admin_password == admin_pwd :
        print("admin logoin")
        if admin_login:
            admin_menu()
            

    else:
        print("Login failed")    

 #admin create account

def create_account():
   name=input("enter name")
   age=int(input("enter name"))
   acc_number=int(input("enter account Number"))
   initial_balance=float(input("Enter amount"))

   customer[acc_number]={
      "Name":name,
      "Age":age,
      "Initial balance":initial_balance
    }
   print(f"\nsucessfull customer {name} added\n")

  

       

def admin_menu():

    while True:
        print("\n-------Welcom Admin Menu-------\n")
        print("1. customer create account")
        print("2. view all customer") 
        print("3. view one customer") 
        print("4. Exit")

        choice=input("enter choice")
        if choice == "1":
          create_account()
        elif choice =="2":
            pass
        elif choice =="3":
            pass
        elif choice =="4":
            break
        else:
            (" invalid choice ")


def menu():

     while True:

        print("\n --------MINI BANKING SYSTEM --------\n")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")

        choice =input("input choice: ")
        if choice == "1":
            admin_login()
        
        elif choice == "2":
            pass
        elif choice == "3":
            break
        else:
            print("Invalid choice..")
menu()