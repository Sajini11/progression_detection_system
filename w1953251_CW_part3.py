# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953251
# Date: 25/11/2022


progress_num, trailer_num, excluded_num, retriever_num = 0, 0, 0, 0     #create variables

list_of_progress=[]        #create lists
list_of_trailer=[]
list_of_excluded=[]
list_of_retriever=[]

print('_____Welcome to  Progression Measuring System______')

while True:

    try:
        credit_pass = int(input("\nEnter your total PASS credits: "))
        if 0 <= credit_pass <= 120 and credit_pass % 20 == 0:
            credit_differ = int(input("Enter your total DEFER credits: "))
            if 0 <= credit_differ <= 120 and credit_differ % 20 == 0:
                credit_fail = int(input("Enter your total FAIL credits: "))
                if 0 <= credit_fail <= 120 and credit_fail % 20 == 0:
                    total = credit_pass + credit_differ + credit_fail  #get total value
                    if total != 120:
                        print("Total incorrect")
                        continue
                    elif credit_pass == 120:
                        print("Progress")
                        progress_num = progress_num + 1
                        list_of_progress.append([credit_pass,credit_differ,credit_fail])
                    elif credit_pass == 100:
                        print("Progress (module trailer)")
                        trailer_num = trailer_num + 1
                        list_of_trailer.append([credit_pass,credit_differ,credit_fail])
                    elif 0 <= credit_pass <= 80 and 0 <= credit_differ <= 120 and 0 <= credit_fail <= 60:
                        print("Module retriever")
                        retriever_num = retriever_num + 1
                        list_of_retriever.append([credit_pass,credit_differ,credit_fail])
                    elif 0 <= credit_pass <= 40 and 0 <= credit_differ <= 40 and 80 <= credit_fail <= 120:
                        print("Exclude")
                        excluded_num = excluded_num + 1
                        list_of_excluded.append([credit_pass,credit_differ,credit_fail])
                    while True:
                        print("\nWould you like to enter another set of data?")
                        choose = input("Enter 'y' for yes or 'q' to quit and view results: ")      #get user input y or n
                        choose = choose.lower()                                                    #convert user choice input into simple letters
                        if choose == "y":
                            break            #if user input 'y' it break from the loop and start executing from the first iteration after loop
                        elif choose == "q":
                            print("-" * 64)
                            print("Histogram", '\n') #if user input 'q' then programme will end and print histogram and total out come
                            print(f"progress  {progress_num} :", progress_num * ' *')
                            print(f"trailer   {trailer_num} :",trailer_num * ' *')
                            print(f"retriever {retriever_num} :", retriever_num * ' *')
                            print(f"excluded  {excluded_num} :", excluded_num * ' *')
                            print("-" * 64)

                            total_num = progress_num + trailer_num + retriever_num + excluded_num

                            print(total_num, "outcomes in total", '\n')
                            print("-" * 64)
                            print("Part 3:")

                            file = open("outcomes.txt", "w")
                            for progress in (list_of_progress):
                                file.write("Progress - ")
                                file.write(str(progress).strip('[]')) #https://stackoverflow.com/questions/29459008/how-to-remove-brackets-from-python-string
                                file.write('\n')
                            for trailer in (list_of_trailer):
                                file.write("Progress (module trailer) - ")
                                file.write(str(trailer).strip('[]'))
                                file.write('\n')
                            for retriever in (list_of_retriever):
                                file.write("Module retriever - ")
                                file.write(str(retriever).strip('[]'))
                                file.write('\n')
                            for exclude in (list_of_excluded):
                                file.write("Exclude - ")
                                file.write(str(exclude).strip('[]'))
                                file.write('\n')
                            file = open("outcomes.txt", "r")
                            print(str(file.read()).strip('[]'))
                            file.close()
                            print('-' * 64)
                            exit()
                        else:
                            print("enter a valid value")
                else:
                    print("out of range")
            else:
                print("out of range")
        else:
            print("Out of range")
    except ValueError:
        print("Integer required")