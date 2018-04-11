'''def fibo(n):
    a=0
    b=1
    for x in range(n):
        a=b
        b=a+b
        print(a, '\n')
    return b
num=int(input("enter the value of n: "))
print(fibo(num))
'''

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("you have %d cheeses!!!" %cheese_count)
    print("you have %d boxes of crackers!!!" %boxes_of_crackers)
    print("Man that's enough for a party")
    print("Get a blanket\n")

print("We can just give the function numbers directly: ")
cheese_and_crackers(20,30)

print("OR, we can use variables from our scripts")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print("we can even do math inside too: ")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variab20les and math: ")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

print("Finally, we can take the values of variables from user input")
amount_of_crackers = int(input())
amount_of_cheese = int(input())
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
