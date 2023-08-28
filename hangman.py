import random
list_l = ["apple", "banana", "cherry"]

def choose_word():  #returns a random word from the predefined list.
    return random.choice(list_l)

#random_word = choose_word()
#print(random_word)

def display_word(my_list,max_attempt):     #takes the chosen word and a list of guessed letters as input and returns the word with underscores for unguessed letters.
    print(my_list)
    print(f"Number of attempts remaining is: {max_attempt}")

def hangman():
    random_word = choose_word()
    l = list(random_word)
    org = list(random_word)
    #print(l)
    max_attempt = len(random_word)+2
    print("===========================")
    print(" !Welcome to play HANGMAN!")
    print("===========================")
    print()

    my_list = []
    for i in range(len(l)):
       my_list.append('_')
    blanks = " ".join(my_list)
    print(f"Your word is: {blanks}", end="")
     
    print(f" (You get, {max_attempt} attempts.)")
    flag = False
    while max_attempt != 0:
        name = input("Enter your guess: ")
        if name in l:
            print("your guess is correct.👌")
            indx = l.index(name)
            my_list[indx] = name
            l[indx] = "*"
        else:
            print("your guess is wrong.😒")
        max_attempt = max_attempt - 1
        display_word(my_list,max_attempt)
        if my_list == org:
            print("you won.✌️")
            flag = True
            break

    if flag == False:
        print("You ran out of attempts,you lost.🥲")
        

hangman()


