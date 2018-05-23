
guessed = []
# Take a string
Word = "CHARU"
present_word = []
for i in range(0,len(Word)):
  present_word.append("_")

count = len(Word)
flag = 0

hangman_board = ["""
    <//////////>

    --------|
      !     | 
      o     |
     /|\\    |
      |     |
     / \\    |
    ""","""
    <//////////>

    --------|
      !     | 
      o     |
     /|\\    |
      |     |
       \\    |
    ""","""
    <//////////>

    --------|
      !     | 
      o     |
     /|\\    |
      |     |
            |
    ""","""
    <//////////>

    --------|
      !     | 
      o     |
     /|\\    |
            |
            |
    ""","""
    <//////////>

    --------|
      !     | 
      o     |
      |\\    |
            |
            |
    ""","""
    <//////////>

    --------|
      !     | 
      o     |
      |     |
            |
            |
    ""","""
    <//////////>

    --------|
      !     | 
      o     |
            |
            |
            |
    """]

#Get the letter from the user
def get_letter():       
    Letter = input("Make a Rough guess: ").upper()
    if len(Letter)>1:
        print("Select only 1 letter.")        
    else:
        return Letter


#Store it and check for duplicacy
def checking_and_upgrade():
    letter = get_letter()
    if letter in guessed:
        print("You have already guessed this word")
        
    else:        
        print("You have guessed ",letter,"\n")
        guessed.append(letter)
        return letter
    

def Hangman_Check():
    global count
    global flag
    count2 = count
    
    letter = checking_and_upgrade()
    
    for i in range(0,len(Word)):    
        if letter == Word[i].upper():
            count = count - 1            
            present_word[i] = Word[i].upper()

    if count2 == count:
        flag += 1
        
   
print("\n******************")    
print("GUESS THE WORD WHICH IS of ",len(Word),"letters")
print('  '," ".join(present_word))
print(hangman_board[flag])            

while True:
   
    
    Hangman_Check()
    
    if flag == 7:
        print ('OOPS!!! YOU LOOSE')
        break
    else:    
        print(hangman_board[flag])
        
    print('  '," ".join(present_word))  
    print("Your repository till now -->",guessed)
    if count == 0:
        print('HURRAAAYYYY!!!! YOU WIN....')
        break

    
    
            




