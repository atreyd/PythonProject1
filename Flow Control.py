# if elif else

marks = 75
if marks > 80:
    print("Grade A")
elif(marks > 60) and (marks <= 80):
    print("Grade B")
elif(marks > 40) and (marks <= 60):
    print("Grade C")
else:
    print("Grade D")


# while
num = int(input("Enter the value of n="))
if(num <= 0):
    print("Enter a valid value")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
print(sum)

# break
count = 0
while True:
    print(count)
    count += 1
    if count > 1000:
        break

# continue

for x in range(20):
    if(x % 2) == 0:
        continue
    print(x)
