from itertools import count
import sys
import os
import time
print( '''
 _______  _______  ______    __   __  _______  __    _  ___   ___   _  __   __  _______ 
|       ||       ||    _ |  |  |_|  ||   _   ||  |  | ||   | |   | | ||  | |  ||       |
|    ___||    ___||   | ||  |       ||  |_|  ||   |_| ||   | |   |_| ||  | |  ||  _____|
|   | __ |   |___ |   |_||_ |       ||       ||       ||   | |      _||  |_|  || |_____ 
|   ||  ||    ___||    __  ||       ||       ||  _    ||   | |     |_ |       ||_____  |
|   |_| ||   |___ |   |  | || ||_|| ||   _   || | |   ||   | |    _  ||       | _____| |
|_______||_______||___|  |_||_|   |_||__| |__||_|  |__||___| |___| |_||_______||_______|
''')
print("Welocome to 'Germanikus, it is a letter for numbers encoder that I learned in scouts as a kid. I decided to write it down in a symple code.")
time.sleep(2)
print("All it does is take a input from you, the user, and checks if it conains letters that are in the word 'germanikus' and than substitutes them with a corresponding number.")
time.sleep(2)
choice_1 = input("Do you want to see the scheme? y/n")
if choice_1 == "y":
    print('''
      _   _   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( G ( E ( R ( M ( A ( N ( I ( K ( U ( S )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( 0 ( 1 ( 2 ( 3 ( 4 ( 5 ( 6 ( 7 ( 8 ( 9 )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
    ''')
germanikus = ["g", "e", "r", "m", "a", "n", "i", "k", "u", "s"]
germanikus_numbers = ["0","1", "2","3","4","5","6","7","8","9"]
def encrypt(input_text):
    user_list = list(input_text)
    final_text = ""
    count = 0
    for i in range(len(user_list)): 
        if user_list[count] not in germanikus:
            final_text += user_list.pop(count)
            count -= 1
        elif user_list[count] in germanikus:
            letter = user_list[0]
            index = germanikus.index(letter) 
            new_letter = germanikus_numbers[index]
            user_list.pop(count)
            final_text += new_letter
            count -=1
        count += 1
    print(f"The encoded text is {final_text}.")
    restart = input ("Do you want to restart? (y/n): ")
    while True:
        if restart == "y":
            os.execl(sys.executable, sys.executable, *sys.argv)
            break
        elif restart == "n":
            print("Thanks for using this software!")
            sys.exit(0)
            break
        else:
            restart = input("Do you want to restart? (y/n): ")
def decode(enc_txt):
    enc_txt_list = list(enc_txt)
    final_decoded_text =""
    count = 0
    for i in range (len(enc_txt)):
        if enc_txt_list[count] not in germanikus_numbers:
            final_decoded_text += enc_txt_list.pop(count)
            count -= 1
        elif enc_txt_list[count] in germanikus_numbers:
            number_decoded = enc_txt_list[0]
            index_decoded = germanikus_numbers.index(number_decoded)
            new_letter = germanikus[index_decoded]
            enc_txt_list.pop(count)
            final_decoded_text += new_letter
            count -= 1
        count += 1
    print(final_decoded_text)
    restart = input ("Do you want to restart? (y/n): ")
    while True:
        if restart == "y":
            os.execl(sys.executable, sys.executable, *sys.argv)
            break
        elif restart == "n":
            print("Thanks for using this software!")
            sys.exit(0)
            break
        else:
            restart = input("Do you want to restart? (y/n): ")
choice = input("Would you like to decode or encrypt a text: ").lower()
while True:
    if choice == 'decode':
        user = input("Type text here: ").lower()
        decode(user)
        break
    elif choice == 'encrypt':
        user = input("Type text here: ").lower()
        encrypt(user)
        break
    else:
        choice = input("Type again, 'encrypt' or 'decode' ").lower()
