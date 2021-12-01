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

def determine_module_deadline():
    """The function determines the deadline date of module that user has chosen from 'modules' dictionary"""

    print(f"There are {len(modules)} modules that require to do Coursework in your 4BIS course for the first semester of 2021-2022 academic year.")
    
    number_modules()

    selected_number = int(input("Choose one of them to check your CW submission: "))-1

    selected_module = modules_list[selected_number]

    selected_module_deadline = modules[selected_module]
    loading()

    print(f'You are supposed to submit your CW till {selected_module_deadline}.')

    global module_deadline

    module_deadline = datetime.strptime(selected_module_deadline, "%d/%m/%Y %I:%M:%S %p")