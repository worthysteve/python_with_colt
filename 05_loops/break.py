# while True:
#     command = input("Type 'exit' to exit: ")
#     if(command == 'exit'):
#         break

# for x in range(1, 101):
#     print(x)
#     if x == 3:
#         break

times = int(input("How many time do I have to tell you? "))

for time in range(times):
    print("CLEAN UP YOUR ROOM!")
    if time >= 4:
        print("do you even listen?")
        break