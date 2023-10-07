from movies import Movies
a = Movies()
a.load()

def command():
    print('Enter your command:')
    while True:
        command = input("Command: ")
        commandList = command.split(" ")
        match commandList[0]:
            case 'show':
                print("About to show all")
                a.show()
            case 'delete':
                print(f'We will delete item {commandList[1]}')
                a.delete(commandList[1])
            case 'quit':
                print('Good bye!')
                break
            case 'seen':
                 print(f'Add to item {commandList[1]}')
                 a.mark_as_seen(commandList[1])
            case 'beenseen':
                 print(f'show already seen movies')
                 a.show_seen()    
            case 'notseen':
                print(f'show unseen movies')
                a.show_notseen()
                
            case _:
                print('Please enter a valid command')

                


command()       
