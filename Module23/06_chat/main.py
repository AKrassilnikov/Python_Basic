import sys
print("Hello, welcome to the chat, to Exit type 'end'")
name = input("Input your name: ")
while True:
    action = input("""1 - Type message
2 - Read chat list
END - for exit
> """)
    if action == '1':
        with open("chat_file.txt",'a',encoding='utf-8') as chat:
            while True:
                print('Type end for exit')
                string = input('{} > '.format(name))
                chat.write(name + '> ' + string + '\n')
                if string == 'end':
                    break
    elif action == '2':
        with open("chat_file.txt", 'r', encoding='utf-8') as chat:
            for line in chat.readlines():
                print(line,end="")
    elif action == 'END':
        sys.exit("Exit chat")
