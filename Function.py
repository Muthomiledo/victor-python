def hello():
    print("This is my first function")
hello()
hello()

def calculate():
    x=10
    y=60
    print(x*y)
calculate()
def majina(fname, lname):
    print(fname+""+lname)
majina("Victor","6y7y")

def greetings(name,greetings="Hello"):
    print(greetings+" "+name)
greetings ("Victor")
greetings("Niaje","nana")

def colour(rangi,remarks="My favourite colour is"):
    print(remarks+" "+rangi)
colour("Blue")
colour("Blue","my watch is")

def maxvalue(a,b,c,d,e,f):
    return max(a,b,c,d,e,f )
result=maxvalue(6,7,4,56,7,8)
print(result)

def minvalue(h,f,g,y,t,r):
    return min(h,f,g,y,t,r)
result+minvalue(1,2,3,4,5,6)
print(result)

def sort_list(lst):
    return sorted(lst)
answer=sort_list([1,6,5,43,7,5,18])
print (answer)

def sort_list(lst):
    return sorted(lst)
answer=sort_list([5,6,4,3,2,9,1])
print(answer)

def sort_list(lst):
    return sorted(lst)
answer=sort_list([1,2,3,7,8,56])
print(answer)
def print_numbers(n):
    for i in range(n):
        print(i)
print_numbers(5)