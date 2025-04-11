# Proyek Ujian Tengah Semester
# IBDA1011 - Pengantar Algoritma & Pemrograman

# Kelompok:
# Devlin Manuel (232202935)
# Howell Deevan Gunawan (232102206)
# Keanrich Cordana (232301226)
# Naftali Aditya Agung Dwi Nugraha (232300333)


#intro
print("Welcome to Python Hangman!!")
print("find the mystery word by guessing one letter at a time!")
print("if you guessed wrong 7 times, you lost the round and will start a new game with new letter\n\n")

print("first, input the words")
#Persiapan game
word_list = [] #list yang akan diisi kata kata yang akan ditebak
while True:
    number = int(input("pick amount of words(1-5): "))
    if number <= 5 and number > 0:
        break
    print("input only 1-5")

for words in range(number):
    while True: #untuk memastikan kata yang diinput adalah kata baru, tidak terulang
        user_input=input("input word: ").lower()
        if user_input not in word_list: #if condition yang memastikan kata itu belom ada di list
            word_list.append(user_input)
            break
        print("Word already inputed")


#functions
def hangman():#function untuk print keutuhan hangman sesuai dengan jumlah tebakan salah
    if wrong_guess == 1 :
        print(""""
                --------
                |      |
                |      
                |     
                |     
                |     
                -
                
            """)
    elif wrong_guess == 2 :
        print("""
                --------
                |      |
                |      O
                |     
                |     
                |     
                -

            """)
    elif wrong_guess == 3 :
        print("""
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -

            """)
    elif wrong_guess == 4 :
        print("""
                --------
                |      |
                |      O
                |     /|
                |      |
                |     
                -

            """)
    elif wrong_guess == 5 :
        print("""
                --------
                |      |
                |      O
                |     /|\ 
                |      |
                |     
                -

        """)
    elif wrong_guess == 6 :
        print("""
                --------
                |      |
                |      O
                |     /|\ 
                |      |
                |     / 
                -

            """)
    elif wrong_guess == 7 :
        print("""
                --------
                |      |
                |      O
                |     /|\ 
                |      |
                |     / \ 
                -
                
        """)
def print_list(list):#function untuk print blank slot huruf huruf tebakan
    print("Guess the Word:")
    print("(", end = "")
    for letter in list:
        print(letter, end = " ")
    print(")\n")


#game on
print("\nGame is on! guess the word and don't mistakenly guess more than 7 times")
print("Good luck!\n")
for game in range(len(word_list)):
    print("Generating new game...")
    print("You have ", len(word_list), "more words")
    #memilih kata baru tiap ronde
    word = word_list[random.randint(0, len(word_list) - 1)]#memilih kata random dari word list    
    word_list.remove(word) #remove kata itu agar tidak terpilih ulang
    
    #Variabel variabel ini perlu direset tiap ronde maka dimasukan dalam loop

    #letters =jawaban menjadi LIST cth: [H, O, W, E, L , L] 
    letters = []
    for letter in word:
        letters.append(letter)

    #guess_list = slot untuk tebakan, awal adalah = [_, _, _, _, _]
    guess_list = []
    for index in range(len(word)):
        guess_list.append("_ ")

    #list untuk diisi oleh HANYA TEBAKAN YANG SALAH
    wrong_guessed = []

    #list untuk menjadi kunci jawaban, karena list(letters) akan diubah oleh sistem game
    answer = letters.copy()

    #nyawa / berapa banyak kali tebakan salah
    wrong_guess = 0


    print_list(guess_list)

    while True:#looping yang akan di break saat menang atau kalah

        while True:#input, dan memastikan bahwa user input tidak lebih dari satu huruf
            guess = input("tebak HURUF: ").lower()
            if len(guess) == 1:#break hanya jika panjang input = 1
                break 
            print("Guess ony ONE letter!")

        ###kalo input sudah pernah ditebak dan benar kedua kalinya
        if guess in guess_list:
            print("already guessed")

        ###kalau input sudah pernah ditebak tapi salah
        elif guess in wrong_guessed: 
            print("letter already guessed and wrong!")  
            
        ###kalo input belum pernah ditebak
        else:
            #kalau input benar
            if guess in word:
                while guess in letters: #looping untuk memastikan sudah mendetek SEMUA huruf yang sama
                    index = letters.index(guess) #mencari index keberapa kah huruf guess
                    letters[index] = 0 #mengganti list letters ke index menjadi 0 agar tidak kedetect lagi saat pengecekan ulang
                    guess_list[index] = guess #mengganti list tebakan kita ke index menjadi tebakan benar
                print("The letter ", guess, ",is correct!")
                print_list(guess_list)
                if answer == guess_list: #jika list tebakan kita sudah sama dengan jawaban, selesaikan game
                    print("Congratulation!")
                    print("YOU WIN!!!\n")
                    break

            #kalau input salah
            else: #masuk sini hanya jika huruf tebakan tidak terkandung di kata jawaban
                wrong_guess = wrong_guess + 1 #menambah jumlah tebakan salah
                if wrong_guess <= 6: #jika salahnya masih dibawah 7, mark tebakan salah lalu lanjut gamenya
                    print("Your letter", guess ," doesn't exsist")
                    wrong_guessed.append(guess) #tambahkan tebakan salah ke list agar tidak terulang
                    print("wrong guesses: ",wrong_guess)
                    hangman()
                    print_list(guess_list)
                else: #jika tebakan salah sudah mencapai 7, patahkan looping ronde dan mulai ronde baru
                    hangman()
                    print("\nGAME OVER!!!")
                    print("you lost, the word is: ", word, "\n")                    
                    break
        print()

print("Game over, all words are used, press run again to play again")