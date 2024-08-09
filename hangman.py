import random

def hangman():
    wrong=0
    num=random.randint(0,8)
    word_list=["apple","cat","dog","fish","write","kind","egg","important","whenever"]
    word=word_list[num]
    stages=["",
            "________       ",
            "|              ",
            "|       |      ",
            "|       O      ",
            "|      /|\     ",
            "|      / \     ",
            "|              "
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("ハングマンへようこそ！")
    while wrong<len(stages)-1:
        print("\n")
        msg="一文字を予想してね"
        char=input(msg)
        if len(char)>1:
            continue
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]="$"
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}".format(word))


hangman()