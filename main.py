from data import modules, submitted_time, questions_reason, results
from loading import loading
from datetime import datetime, timedelta


def greeting():
    name = input("First of all how can I call you: ")
    print(f"Hey {name} 👋. How are you doing? and your study in WIUT? \nLet's talk about your CW assignments.")
    loading()



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

    loading()

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




def determine_user_late_submission(mark):
    """The function that checks and calculate the time that student has submitted lately or not."""
    
    if student_submission_date > module_deadline:
        if student_submission_date - module_deadline <= timedelta(hours=24):
            within_24_hours(mark)
            
        else:
            if student_submission_date - module_deadline <= timedelta(days=5):
                within_5_days(mark)
            
            else:
                more_than_5_days(mark)
            
    else:
        on_time()

def on_time(mark):
    """The function that gets the overall mark when student has submitted CW on time"""
    print(f'{submitted_time.get("on_time")}. \nYour overall mark is {mark}')



def within_24_hours(mark):
    """The function gets the overall mark when student has submitted CW within 24 hours after the deadline."""

    print(submitted_time.get("within_24"))
    valid_reason = input(questions_reason["is_valid_reason"]) 
    if answer_to_question(valid_reason):
        mc_claim = input(questions_reason.get("mc_claim_acceptance"))
        if answer_to_question(mc_claim):
            print(f'{results["full_mark"]}. \nYour overall mark is {mark}')
        else:
            if mark-10 < 40:
                mark == 40
                print(f'{results["minus_10"]}. \nYour overall mark is {mark}')
            else:
                mark = mark-10
                print(f'{results["minus_10"]}. \nYour overall mark is {mark}') 



def within_5_days(mark):
    """The function gets the overall mark when student has submitted CW within 5 days after the deadline."""

    print(submitted_time.get("within_5_days"))
    valid_reason = input(questions_reason["is_valid_reason"]) 
    if answer_to_question(valid_reason):
        mc_claim = input(questions_reason.get("mc_claim_acceptance"))
        if answer_to_question(mc_claim):
            print(f'{results["full_mark"]}. \nYour overall mark is {mark}')
        else:
            print(f'{results["zero_mark"]}. \nYour overall mark is {mark-mark}')
    else:
        print(f'{results["zero_mark"]}. \nYour overall mark is {mark-mark}')



def more_than_5_days(mark):
    """The function gets the overall mark when student has submitted CW more than 5 days after the deadline."""

    print(submitted_time.get("more_than_5_days"))
    valid_reason = input(questions_reason["is_valid_reason"])
    if answer_to_question(valid_reason):
        print(results["deferral"])
    else:
        print(f'{results["zero_mark"]}. \nYour overall mark is {mark-mark}')


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



def main():
    greeting()
    
    determine_module_deadline()
    
    check_user_date_validity()
    
    student_mark = int(input("Please enter your mark of that module that you chose: "))

    determine_user_late_submission(student_mark)