groceries = ['Eggs', 'Butter', 'Milk', 'Flour'] 
#Defines the the list of variables in groceries
howmuch = ['= 2', '= 2 TBSP', '= 1 and a third cups', '= 1 cup']
#Defines the list of variables in howmuch
for g in groceries:
    for h in howmuch:
        while groceries:
            while howmuch:
                print(groceries.pop() + ' ' + howmuch.pop())
#This is a change for a commit
