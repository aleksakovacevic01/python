
print(
    """
    0 - quit
    1 - read
    2 - create
    3 - update
    4 - delte
    5 - search priority
    """
)


reminder_list = []
while True:
    message = input("Input: ")
    if message == '0':
        break

    elif message == '1':
        for i, r in enumerate(reminder_list):
            print(str(i) + ": " + str(r))


    elif message == '2':
        title = input("Title: ")
        content = input("Content: ")
        priority = int(input("Priority: "))
        reminder = {
            "title": title,
            "content": content,
            "priority": priority
        }
        reminder_list.append(reminder)
    elif message == '3':
        index = int(input("Update index: "))
        update_field = input("title - 1 / content - 2 / priority - 3: ")
        if update_field == '1':
            title = input("Enter title: ")
            reminder_list[index]["title"] = title
        elif update_field == '2':
            content = input("Enter content: ")
            reminder_list[index]["content"] = content
        elif update_field == '3':
            priority = input("Enter priority:")
            reminder_list[index]["priority"] = priority
    elif message == '4':
        index = int(input("Delete index: "))
        update_field = input("title - 1 / content - 2 / priority - 3: ")
        if update_field == '1':
            del reminder_list[index]["title"]
        elif update_field == '2':
            del reminder_list[index]["content"]
        elif update_field == '3':
           del reminder_list[index]["priority"]
    elif message == '5':
        value_priority = int(input("Enter value priority: "))
        for i in reminder_list:
            if i["priority"] == value_priority:
                print(i)
            else:
                print("ERROR")
















