class Budget():
    def_init_(self,amount) :

    #the amount of money we have to spend
    self.funds = amount

    #A dictionary of our items we are spending our budget on
    # the key is the name of the item; the value is the budget amount for that item
    budgets= {}

   # A dictionary of the expenese of each budgeted item
    # The key is the name of the item, the value is the amount spent on the item
    expenses= {}
    
#Adds an item to the budgets dictionary

    def AddBudget(self,name, amount):
            global funds
            if name in budgets: # If the key is already in our budgets dictionary
                raise ValueError("Budget for item already exists")
            if amount > funds:
                raise ValueError("No can do, you are too broke")
            Budgets[name] = amount # Adds the budgeted item to the budgets dictionary
            funds -= amount #Substracts the amount from the funds
            expenses[name] = 0 #Add the budgeted item to the expenses dictionary
            return funds

    def Spend(name,amount):
            if name not in expenses: # if the eitem is not in our budget
                raise ValueError("Item not in budget")
            expenses[name] += amount # Add the expense to the budgeted item
            budgeted= budgets[name]
            Spent= expenses [name]
            return budgeted - Spent

    def PrintBudget():
            print("Budget     Budgeted   Spent   Remaining" )
            print("-----------------------------------")
            
            
            for name in budgets:
                budgeted= budgets[name] # store the amount associated with that key
                spent= expenses[name] # store the amount spent on that given item
                remaningBudget= budgeted- spent # Calculate the remaining budget for 
                print (f'{name:15s}, {budgeted:10.2f}, {spent: 10.2f}'
                    f' {remaningBudget:10.2f}')
                totalBudgeted += budgeted
                totalSpent += spent


print("Total Funds ", funds)
# Add some items to the budget
AddBudget("books", 100)
AddBudget("Jersey", 80)
AddBudget("Jordan shoes", 200)
AddBudget("Clothes", 70)


#Spend some money on items in our budget
Spend("books",50)


#Display the entire budget
PrintBudget(50)