#list comprehension program
numbers=[1,2,3,4,5]
squares=[]

for n in numbers:
    squares.append(n*n)

print(squares)

#second program-----------

numbers=[1,2,3,4,5,6]
evens=[n for n in numbers if n %2==0]
print(evens)

#3rd program
numbers=[1,2,3,4,5]
result=[]
for n in numbers:
    result.append(n*2)
#or
num=[1,2,3,4]
output=[n*2 for n in num]
print(output)


#list lenght
words=["apple","banana","mango"]
length=[len(word) for word in words]
print(length)

#sum of digit
n = int(input("একটি সংখ্যা লিখুন: "))
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("অঙ্কগুলোর যোগফল =", sum)


