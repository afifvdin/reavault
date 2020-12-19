def createUser(ready=0):
    if ready > 0:
        return None
    print("Creating User...")
    while True:
        username = input("Input your username: ")
        password = input("Input your password: ")
        repass = input("Input your password again: ")
        if password == repass:
            print("\nProfile Created!\n")
            break
        print("\nPassword not match!\n")
    while True:
        print("After this you'll ask for some question and password provided within.\nThis will be usefull when you forget your identity to loged in in this application.\n")
        ques_a = input("Input first question: ")
        ans_a = input("Input first question answer: ")
        ques_b = input("Input second question: ")
        ans_b = input("Input second question answer: ")
        ques_c = input("Input third question: ")
        ans_c = input("Input third question answer: ")
        sure = input("Are you sure to continue with provided password? Any changes made will be saved: ")
        if sure == "y":
            print("\nProfile completion done!\n")
            break
        print("\nRedoing...\n")
    return {
        "username": username,
        "password": password,
        "ques": {
            "a": ques_a,
            "b": ques_b,
            "c": ques_c
        },
        "ans": {
            "a": ans_a,
            "b": ans_b,
            "c": ans_c
        }
    }