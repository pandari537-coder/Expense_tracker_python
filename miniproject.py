# Expense Tracker Project:
expensesList=[]
print("Welcome To Expense Tracker:")

while True:
    print("======MENU=======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Khrcha ")
    print("4. Exit")
    
    choice= int(input("Enter your choice:"))
    
    if(choice == 1):
        date= input("Kis Date Par Khrcha Kiya?:")
        category= input("Kis Type Ka Khrcha Kiya ?:(food,Travel,Gaming,Books,Movies.......)")
        description= input("Aur Details Dedo:")
        amount= float(input("Enter the amount:"))
        
        expense= {
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expensesList.append(expense)
        print("\n DONE Bro .Expense Is Added Successfully:")
        
    elif(choice==2):
        if(len(expensesList)==0):
            print("No Expenses Added. Jao Pehle Khrcha Karo:")
        else:
            print("=====ye y apka sara expense:")
            count=1
            for eachkhrcha in expensesList:
                print(f"khrcha Number {count} -> {eachkhrcha["date"]}, {eachkhrcha["category"]},{eachkhrcha["description"]},{eachkhrcha["amount"]}")
                count= count+1
                
    elif(choice == 3):
        total= 0
        for eachkhrcha in expensesList:
            total = total + eachkhrcha["amount"]
            
            print("\n TOTAL KHRCHA =",total)
            
    elif(choice == 4):
        print("Dhanyawad aapne humara system use kiya:")
        break
    
    else:
        print("INVALID CHOICE. TRY AGAIN")