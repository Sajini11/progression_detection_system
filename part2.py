progress_num, trailer_num, excluded_num, retriever_num = 0, 0, 0, 0  #create variables

list_of_progress=[]                #create lists
list_of_trailer=[]
list_of_excluded=[]
list_of_retriever=[]

print('_____Welcome to  Progression Measuring System______')

def main(progress_num, trailer_num, excluded_num, retriever_num):  #create a function called 'main'
    try:
        login = int(input("\nPlease enter number '1' For Student Login, enter number '2' For Staff Login: ")) #ask user option to select the staff login or student login
        while True:
            if login == 1:
                print("\n______Student Login_____")
                while True:
                    try:
                        credit_pass = int(input("\nPlease enter your credits at pass: "))         #get user input for credit at pass
                        if 0 <= credit_pass <= 120 and credit_pass % 20 == 0:                    #check user input for credit at pass is out of range or not
                            credit_differ = int(input("Please enter your credits at differ: "))  #get user input for credit at differ
                            if 0 <= credit_differ <= 120 and credit_differ % 20 == 0:            #check user input for credit at differ is out of range or not
                                credit_fail = int(input("Please enter your credits at fail: "))  #get user input for credit at fail
                                if 0 <= credit_fail <= 120 and credit_fail % 20 == 0:            #check user input for credit at fail is out of range or not
                                    total = credit_pass + credit_differ + credit_fail            #get total value
                                    if total != 120:
                                        print("Total incorrect")  #Check the total is correct or not
                                        continue                  #if total is incorrect again ask for inputs

                                    elif credit_pass == 120:
                                        print("Progress")       #check user inputs whether progress,module trailer,module retriever or exclude
                                    elif credit_pass == 100:
                                        print("Progress (module trailer)")
                                    elif 0 <= credit_pass <= 80 and 0 <= credit_differ <= 120 and 0 <= credit_fail <= 60:
                                        print("Module retriever")
                                    elif 0 <= credit_pass <= 40 and 0 <= credit_differ <= 40 and 80 <= credit_fail <= 120:
                                        print("Exclude")
                                    exit()   #exit from the loop and programme

                                else:
                                    print("out of range")
                            else:
                                print("out of range")
                        else:
                            print("Out of range")
                    except ValueError:
                        print("Integer required")
            elif login == 2:
                print("\n_____Staff Login_____")
                while True:
                    try:
                        credit_pass = int(input("\nEnter your total PASS credits: "))
                        if 0 <= credit_pass <= 120 and credit_pass % 20 == 0:
                            credit_differ = int(input("Enter your total DEFER credits: "))
                            if 0 <= credit_differ <= 120 and credit_differ % 20 == 0:
                                credit_fail = int(input("Enter your total FAIL credits: "))
                                if 0 <= credit_fail <= 120 and credit_fail % 20 == 0:
                                    total = credit_pass + credit_differ + credit_fail
                                    if total != 120:
                                        print("Total incorrect")
                                        continue

                                    elif credit_pass == 120:
                                        print("Progress")
                                        progress_num = progress_num + 1
                                        list_of_progress.append([credit_pass, credit_differ, credit_fail])  #add user inputs for the created lists
                                    elif credit_pass == 100:
                                        print("Progress (module trailer)")
                                        trailer_num = trailer_num + 1
                                        list_of_trailer.append([credit_pass, credit_differ, credit_fail])
                                    elif 0 <= credit_pass <= 80 and 0 <= credit_differ <= 120 and 0 <= credit_fail <= 60:
                                        print("Module retriever")
                                        retriever_num = retriever_num + 1
                                        list_of_retriever.append([credit_pass, credit_differ, credit_fail])
                                    elif 0 <= credit_pass <= 40 and 0 <= credit_differ <= 40 and 80 <= credit_fail <= 120:
                                        print("Exclude")
                                        excluded_num = excluded_num + 1
                                        list_of_excluded.append([credit_pass, credit_differ, credit_fail])

                                    histogram(progress_num, trailer_num, excluded_num, retriever_num)  #call histogram function

                                else:
                                    print("out of range")
                            else:
                                print("out of range")
                        else:
                            print("Out of range")
                    except ValueError:
                        print("Integer required")
            else:
                print("Please enter '1' or '2' for version select")
                main(progress_num, trailer_num, excluded_num, retriever_num)           #call main function
    except ValueError:
        print("Integer required")
        main(progress_num, trailer_num, excluded_num, retriever_num)                #call main function

def histogram(progress_num, trailer_num, excluded_num, retriever_num):     #create a function called 'histo' for histogram
    while True:
        print("\nWould you like to enter another set of data?")
        choose = input("Enter 'y' for yes or 'q' to quit and view results: ")                #get user input y or n
        choose = choose.lower()                                                              #convert user choice input into simple letters
        if choose == "y":
            break           #if user input 'y' it break from the loop and start executing from the first iteration after loop
        elif choose == "q":
            print("-"*64)
            print("Histogram",) #if user input 'q' then programme will end and print histogram and total out come
            print(f"progress  {progress_num} :", progress_num * ' *')
            print(f"trailer   {trailer_num} :", trailer_num * ' *')
            print(f"retriever {retriever_num} :", retriever_num * ' *')
            print(f"excluded  {excluded_num} :", excluded_num * ' *')

            total_num = progress_num + trailer_num + retriever_num + excluded_num
            print('\n',total_num, "outcomes in total")
            print("-" * 64)
            print("Part 2:")

            for progress in (list_of_progress):   #lists
                print("Progress  - ", end='')
                print(str(progress).strip('[]'))  #https://stackoverflow.com/questions/29459008/how-to-remove-brackets-from-python-string
            for trailer in (list_of_trailer):
                print("Progress (module trailer) - ", end='')
                print(str(trailer).strip('[]'))
            for retriever in (list_of_retriever):
                print("Module retriever - ", end='')
                print(str(retriever).strip('[]'))
            for exclude in (list_of_excluded):
                print("Exclude - ", end='')
                print(str(exclude).strip('[]'))
            print('-' * 64)
            exit()
        else:
            print("Enter a valid value")


main(progress_num, trailer_num, excluded_num, retriever_num)                   #call main function
