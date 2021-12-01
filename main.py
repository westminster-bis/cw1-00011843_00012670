import datetime
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



def determine_module_deadline():
    """The function determines the deadline date of module that user has chosen from 'modules' dictionary"""

    print(f"There are {len(modules)} modules that require to do Coursework in your 4BIS course for the first semester of 2021-2022 academic year.")
    
    number_modules()

    selected_number = int(input("Choose one of them to check your CW submission: "))-1

    selected_module = modules_list[selected_number]

    selected_module_deadline = modules[selected_module]

    print(f'You are supposed to submit your CW till {selected_module_deadline}.')

    global module_deadline

    module_deadline = datetime.strptime(selected_module_deadline, "%d/%m/%Y %I:%M:%S %p")


def check_user_date_validity():
    """The function checks whether student is submitted right format of date and time that user have submitted his/her CW."""

    while True:
        try:
            submission_date_string = input("When did you submit it actually? Send it as a format of 'DD/MM/YYYY H:M:S' (e.g. 25/12/2021 19:45:26): ")
            global student_submission_date 
            student_submission_date = datetime.strptime(submission_date_string, "%d/%m/%Y %H:%M:%S")
            student_submission_date = student_submission_date
            break
                
        except: 
            print("You've entered wrong format of date and time. Please, try again.")