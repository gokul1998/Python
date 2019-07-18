print("think between 0 to 100")
#higher = "higher", lower = "lower", correct = "correct"
low = 0
high = 100
while True:
    print("is your secret number is {}",int((low+high)/2))
    inp = input()
    mid = int((low+high)/2)
    if inp == "correct":
        break
    elif inp == "higher":
        high = mid
    elif inp == "lower":
        low = mid
print("done...")