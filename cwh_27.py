que = [
    "What is largest planet in our Solar System? ",
    "Who is known as father of computer? ",
    "What is square root of 144? ",
    "Which country has the most population? ",
    "How many continents are on earth? ",
    "What is chemical symbol of Gold? ",
    "Which is fastest land animal? ",
    "What is capital of Japan? ",
    "How many sides does a hexagon has? ",
    "Who wrote Harry potter? "
]
ans = [
    "Jupiter",
    "Charles Babbage",
    "12",
    "India",
    "7",
    "Au",
    "Cheetah",
    "Tokyo",
    "6",
    "J. K. Rowling"
]
score=0
for i in range(len(que)):
    user_ans = input(que[i])
    if(user_ans.upper() == ans[i].upper()):
        print("Your answer is correct!")
        score += 1
    else:
        print("Sorry, Wrong answer")
print("Your complete score is:",score)
price = score*1000
print("And you won",price,"!!!!!!!!!")    