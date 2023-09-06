#implementation of stack in python 
stack = []
def push():
  elements = int(input("enter the element you want to push"))
  stack.append(elements)
  print(stack)
                 
def pop():
  if not stack:
      print(" stack is empty")
  else:
      stack.pop()
      print(stack)     
while True:
    choice = int(input( "1.push 2.pop 3.stop "))

    if choice == 1 :
        push()
    elif choice == 2 :
        pop()
    elif choice == 3 :
        break
    else:
          print("invalid choice")       
