def converter():
    print("----WELCOME TO CONVERTER----")
    decision = input('What do you want to convert? \n[a]Binary\n[b]Number\n: ')
    decision = decision.lower()
    if decision == 'a':
        binary = input("Enter binary with space as separator\n: ")
        binary = binary.split()
        arr = []
        for i in binary:
            arr.append(int(i))
        print(binaryToNum(arr))
    elif decision == 'b':
        num = int(input("Enter a number: "))
        print(numToBinary(num))
    else:
        print("Invalid input. Please try again.\n")
        converter()

def binaryToNum(arr):
    total = 0
    for i in arr:
        total = total * 2 + i
    return total

def numToBinary(num):
    return bin(num).replace('0b','')

#Executes the main program
converter()



