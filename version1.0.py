
#get user's pass credits
def getPassCredits():
    credit_range = [0,20,40,60,80,100,120]
    while True:
        try:
            pass_credit = int(input("Enter your total PASS credits: "))
            
            if pass_credit in credit_range:
                return pass_credit
            else:
                print("Out of range \n")
        except:
            print("Integer required \n")
            
#get user's defer credits            
def getDeferCredits():
    credit_range = [0,20,40,60,80,100,120]
    while True:
        try:
            defer_credits = int(input("enter your total DEFER credits: "))
            
            if defer_credits in credit_range:
                return defer_credits
            else:
                print("Out of range \n")
        except:
            print("Integer required \n")
   
#get user's fail credits
def getFailCredits():
    credit_range = [0,20,40,60,80,100,120]
    while True:
        try:
            fail_credits = int(input("Enter your total FAIL credits: "))
            
            if fail_credits in credit_range:
                return fail_credits
            else:
                print("Out of range \n")
                
        except:
            print("Integer required \n")
        
#calculate total credits and check lower than 120
def getTotalCredits():
    global pass_credits
    global defer_credits
    global fail_credits
    
    while True:
            total_credits = pass_credits + defer_credits + fail_credits
            
            if total_credits <= 120:
                return total_credits
            else:
                print("Total incorrect \n")
                return total_credits
                
#get user answer to loop or quit                
def getAnswer():
    while True:
        answer = input("Enter 'y' for yes or 'q' to quit and view results: ")
        print("\n")
        answer = answer.lower()
        if answer == "y":
            return answer
        elif answer == "q":
            return answer
        else:
            print("----Enter 'y' for yes or 'q' to quit and view results----")
            
#check user status among credits            
def checkStatus():
         
    global pass_credits
    global defer_credits
    global fail_credits
    global total_credits

    if pass_credits == 120:
        print("Progress \n")
        
    elif (defer_credits == 20 and fail_credits == 0) or (defer_credits == 0 and fail_credits == 20):
        print("Progress (module trailer) \n")
        
    elif pass_credits <= 40 and fail_credits >=80:
        print ("Exclude \n")
        
    else:
        print("Do not progress - module retriever \n")


#Main programe
                
pass_credits = getPassCredits()
defer_credits = getDeferCredits()
fail_credits = getFailCredits()
total_credits = getTotalCredits()
status = checkStatus()

while total_credits > 120:
    pass_credits = getPassCredits()
    defer_credits = getDeferCredits()
    fail_credits = getFailCredits()
    total_credits = getTotalCredits()
    status = checkStatus()

print("Would you like to enter another set of data?")
user_answer = getAnswer()
while True:
    if user_answer == "y":
        pass_credits = getPassCredits()
        defer_credits = getDeferCredits()
        fail_credits = getFailCredits()
        total_credits = getTotalCredits()
        status = checkStatus()


        while total_credits > 120:
            pass_credits = getPassCredits()
            defer_credits = getDeferCredits()
            fail_credits = getFailCredits()
            total_credits = getTotalCredits()
            status = checkStatus()
            
    elif user_answer == "q":
        break
    print("Would you like to enter another set of data?")
    user_answer = getAnswer()
    
        
    
