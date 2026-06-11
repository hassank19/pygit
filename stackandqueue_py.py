def stack_py():
    max = int(input("Enter max size of array: "))
    my_stack = [0] * max
    top = -1
    while True:
        print("1: Push")
        print("2: Pop")
        print("3: Display")
        print("4: Break") 
        ui = int(input("Choose an operation: "))

        if ui == 1:
            if top == max - 1:
                print("Stack overflow")
            else:
                top+=1
                value = int(input("Enter your element: "))
                my_stack[top] = value
                print("Element pushed")
        elif ui == 2:
            if top == -1:
                print("Stack underflow")
            else:
                print(f"Element popped {my_stack[top]}")
                top = top - 1
        elif ui == 3:
            if top == -1:
                print("Stack is empty")
            else:
                print(my_stack)
        elif ui == 4:
            break
#-----------------------------------------------
def queue_py():
    max = int(input("Enter max size of array: "))
    my_queue = [0] * max
    front = -1
    rear = -1
    while True:
        print("1: Enqueue")
        print("2: Dequeue")
        print("3: Display")
        ui = int(input("Choose an operation: "))

        if ui == 1:
            if rear == max - 1:
                print("Queue overflow")
            else:
                if (front == -1):
                    front+=1
                val = int(input("Enter the value to enqueue: "))
                rear+=1
                my_queue[rear] = val
                print(f"Enqueued {val}")
        elif ui == 2:
            if front == -1:
                print("Queue Underflow")
            else:
                print(f"Dequeued {my_queue[front]}")
                front+=1
            if front>rear:
                front = rear = -1
        elif ui == 3:
            if rear == -1:
                print("Queue is empty")
            else:
                for x in range(front, rear+1):
                    print(f"{my_queue[x]}")




print("1. Stack using python")
print("2. Queue using python")
user_in = int(input("Enter your choice: "))

if user_in == 1:
    stack_py()
if user_in == 2:
    queue_py()