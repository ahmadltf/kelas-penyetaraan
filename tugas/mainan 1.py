#ahmad luthfi hanif, maninan 1

kata="Fuad"
OUT_OF_GUESS=False
ANSWER_CORRECT=False
max_guess=3
guess=0

while not (OUT_OF_GUESS) or not (ANSWER_CORRECT):
    jawaban_orang=input("Apa Tebakannya?")
    if jawaban_orang == kata:
        ANSWER_CORRECT=True
        break
    guess +=1
    print("kamu punya sisa"+ str(max_guess-guess)+"/"+str(max_guess)+"nyawa")
    if guess == max_guess:
        OUT_OF_GUESS=True

if(OUT_OF_GUESS);
    print("Kamu Kalah")
else:
    print("kamu Menang")