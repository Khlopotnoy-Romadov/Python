print("Is it raining?")
answer1 = input()
if answer1 == "Yes":
    print("It is windy outside?")
    answer2 = input()
    if answer2 == "Yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy you day")