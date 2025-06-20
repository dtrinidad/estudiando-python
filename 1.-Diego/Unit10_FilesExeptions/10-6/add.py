success = False
while(not success):
    
    try:
        Anumber = int(input("Enter A number: "))
        Bnumber = int(input("Enter B number: "))
    except ValueError:
        print("You must enter a valid number!")
    else:
        addition = Anumber + Bnumber
        print(f"Result = {addition}")
        success = True 