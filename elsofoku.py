def fuggveny(param1):
    """Ez egy függvény"""
    # ... jelenleg nem sokat csinál
    print "semmi"
    return None
def hello():
     print("Hello, World!")
hello()
def triangle(a,b,c):
    print("perimeter: ",a+b+c)
triangle(3,4,5)
def triangle(a,b,c):
    print("ker: ",a+b+c)
a = input("a oldal: ")
b = input("b oldal: ")
c = input("c oldal: ")
triangle(a,b,c)
a = float(input("a oldal: "))
b = float(input("b oldal: "))
c = float(input("c oldal: "))
triangle(a,b,c)
def absolute_value(num):
  """This function returns the absolute
  value of the entered number"""
  if num >= 0:
    return num
  else:
    return -num
num = float(input("enter a number: "))
print(absolute_value(num))
#...ez egy másik példa lesz:
def add_numbers(x,y):
   sum = x + y
   return sum
num1 = float(input("num1: "))
num2 = float(input("num2: "))
print("The sum is", add_numbers(num1, num2))
def add_numbers(x,y):
   sum = x + y
   return sum
def subt_numbers(x,y):
    subt = x - y
    return subt
def multi_numbers(x,y):
    multi = (x*y)
    return multi
def div_numbers(x,y):
    div = (x/y)
    return div
num1 = float(input("num1: "))
num2 = float(input("num2: "))
op = int(input("operation: 1:sum, 2:subtract, 3:multiplication, 4:divison  "))
if op == 1:
    print("The sum is", add_numbers(num1, num2))
elif op == 2:
    print("The subt. is", subt_numbers(num1, num2))
elif op == 3:
    print("The multi. is", multi_numbers(num1, num2))
elif op == 4:
    print("The div. is", div_numbers(num1, num2))
else:
    print("unknown operation")



