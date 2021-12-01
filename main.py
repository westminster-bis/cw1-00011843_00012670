from data import modules, submitted_time, questions_reason, results

def greeting():
    name = input("First of all how can I call you: ")
    print(f"Hey {name} 👋. How are you doing? and your study in WIUT? \nLet's talk about your CW assignments.")

def answer_to_question(answer):
    """ 
    The function that if user enters "No", (alternatives for No: "NO", "nO", "N" or just "n") it will return False. 
    When the user enters "Yes" (alternatives for Yes: "YES", "YEs", "yES" "Y" or just "y") it will return True.
    In another case when the user enters the invalid answer it will repeat the question. 

    """
    while answer:
        answer = answer.lower()
        if answer == 'yes' or answer == 'y':
            return True
        elif answer == 'no' or answer == 'n':
            return False
        else:
            answer = input("Oops. Sorry I didn't get your answer. Please, write yes or no: ")

def number_modules():
    """Convert the modules dictionary to list and number each modules that given in dictionary 'modules'."""
    i=1
    global modules_list
    modules_list = list(modules)
    for module in modules_list:
        print(f'{i}. {module}')
        i+=1
