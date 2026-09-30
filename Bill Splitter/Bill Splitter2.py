import sys 

running_total = 0

num_of_friends = int(input("Number Of Friends In The Group : "))

i = 0
while i <= 2 :
    simple_or_complex = input("\nType 'yes' If You Want To Add The Bill By Dividing Into Sections (or) Type 'no' If You Want To Directly Add The Whole Value Given In The Bill\n")

    if simple_or_complex == 'yes' :
     appetizers = int(input("\nMoney Spent On Appetizers (value only) : ")) 
     main_courses = int(input("Money Spent On Main Course (value only) : "))
     desserts = int(input("Money Spent On Desserts (value only) : "))
     drinks = int(input("Money Spent On Drinks (value only) : "))
     

     running_total += appetizers + main_courses + desserts + drinks
     print('\nTotal Bill So Far :', running_total)
     break

    elif (simple_or_complex == 'no') :
     running_total = int(input("\nMoney Spent In Total (value only) : "))
     break

    else :
        if i < 2 :
            print("\nPlease Make Sure That The Word Matches The Options Given (words are case sensitive)")
            i += 1
        else :
            print("\nToo Many Invalid Attempts. Please Refresh And Make Sure That The Word Matches The Options Given (words are case sensitive)")
            sys.exit()

tip = int(input("\nTip (value only in %) : "))
calculate_tip = (running_total) * (tip/100)
print('Tip Amount: ', calculate_tip)

running_total += tip
round_off = round(running_total)
print('\nTotal With Tip (round off) : ', round_off)

final_bill = running_total / num_of_friends
print('Bill Per Person : ', final_bill)

each_pays = round(final_bill)
print("Each person pays : ", each_pays)
