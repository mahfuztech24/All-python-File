#sorted
students=[("Mina",82),("Rafi",95),("Tara",76)]
by_score=sorted(students,key=lambda item:item[1])
print(by_score)

#map(use for iteration as given format)
numbers=[1,2,3,4]
result=map(lambda x:x*2,numbers)
print(list(result))


def double(number):
    return number*2
numbers=[2,4,6]
result=map(double,numbers)
print(list(result))

#short comprehension
numbers = [1, 2, 3, 4, 5]

squares = []

for x in numbers:
    squares.append(x**2)

print(squares)

#filter (specific item iteration)
numbers = [1, 2, 3, 4, 5, 6]

def even(x):
    return x % 2 == 0

result = list(filter(even, numbers))

print(result)

#re (finding specific word or character)
import re
text="Python is fun. learn Python Today"
result=re.findall(r"o",text)
print(result)

#search & test a match
text="Contact sfupport at the help@example.com"
match=re.search(r"\w+@\w+\.\w+",text)
if match:
    print(match.group())

#capture usefull pieces with regex
text="Date: 2026-10-13"
match=re.search(r"(\d{4})-(\d{2})-(\d{2})",text)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

#text replace
text="one two\tthree"
print(re.sub(r"\s+"," ",text))

parts=re.split(r"[,;]\s*","red,green;blue")
print(parts)

#Phone digit validation
m_number=input("Please Give Me a valid Mobile Number: ")
pattern=r"01\d{9}$"
if re.fullmatch(pattern,m_number):
    print("Mobile Number Looks valid")
else:
    print("Mobile Number Looks not Valid")    
