import pickle as pf
import sys

from tabulate import tabulate

import pushup_tables as put
import text_blocks as tb


class Person:
    """A 100 pushup challenger"""

    def __init__(self):
        self.name = ''
        self.age = 0
        self.initial_test = 0
        self.w2d3_test1 = 0
        self.w4d3_test2 = 0
        self.w5d3_test3 = 0
        self.final_test = 0
        self.initial_test_rank = 0
        self.test1_rank = 0
        self.test2_rank = 0
        self.test3_rank = 0
        self.final_test_rank = 0

    def calculate_rank(self, t):
        if t == 'initial_test':
            test_name = self.initial_test
            if int(self.age) < 40:
                if test_name < 6:
                    rank = 1
                elif test_name < 15:
                    rank = 2
                elif test_name < 30:
                    rank = 3
                elif test_name < 50:
                    rank = 4
                elif test_name < 100:
                    rank = 5
                elif test_name < 150:
                    rank = 6
                elif test_name >= 150:
                    rank = 7

                self.initial_test_rank = rank

            elif int(self.age) < 56:
                if test_name < 6:
                    rank = 1
                elif test_name < 13:
                    rank = 2
                elif test_name < 25:
                    rank = 3
                elif test_name < 45:
                    rank = 4
                elif test_name < 75:
                    rank = 5
                elif test_name < 125:
                    rank = 6
                elif test_name >= 125:
                    rank = 7

                self.initial_test_rank = rank

            elif int(self.age) > 55:
                if test_name < 6:
                    rank = 1
                elif test_name < 10:
                    rank = 2
                elif test_name < 20:
                    rank = 3
                elif test_name < 35:
                    rank = 4
                elif test_name < 65:
                    rank = 5
                elif test_name < 100:
                    rank = 6
                elif test_name >= 100:
                    rank = 7

                self.initial_test_rank = rank

        if t == 'test1':
            test_name = self.w2d3_test1
            if int(self.age) < 40:
                if test_name < 6:
                    rank = 1
                elif test_name < 15:
                    rank = 2
                elif test_name < 30:
                    rank = 3
                elif test_name < 50:
                    rank = 4
                elif test_name < 100:
                    rank = 5
                elif test_name < 150:
                    rank = 6
                elif test_name >= 150:
                    rank = 7

                self.test1_rank = rank

            elif int(self.age) < 56:
                if test_name < 6:
                    rank = 1
                elif test_name < 13:
                    rank = 2
                elif test_name < 25:
                    rank = 3
                elif test_name < 45:
                    rank = 4
                elif test_name < 75:
                    rank = 5
                elif test_name < 125:
                    rank = 6
                elif test_name >= 125:
                    rank = 7
                self.test1_rank = rank

            elif int(self.age) > 55:
                if test_name < 6:
                    rank = 1
                elif test_name < 10:
                    rank = 2
                elif test_name < 20:
                    rank = 3
                elif test_name < 35:
                    rank = 4
                elif test_name < 65:
                    rank = 5
                elif test_name < 100:
                    rank = 6
                elif test_name >= 100:
                    rank = 7

                self.test1_rank = rank

        if t == 'test2':
            test_name = self.w4d3_test2
            if int(self.age) < 40:
                if test_name < 6:
                    rank = 1
                elif test_name < 15:
                    rank = 2
                elif test_name < 30:
                    rank = 3
                elif test_name < 50:
                    rank = 4
                elif test_name < 100:
                    rank = 5
                elif test_name < 150:
                    rank = 6
                elif test_name >= 150:
                    rank = 7

                self.test2_rank = rank

            elif int(self.age) < 56:
                if test_name < 6:
                    rank = 1
                elif test_name < 13:
                    rank = 2
                elif test_name < 25:
                    rank = 3
                elif test_name < 45:
                    rank = 4
                elif test_name < 75:
                    rank = 5
                elif test_name < 125:
                    rank = 6
                elif test_name >= 125:
                    rank = 7

                self.test2_rank = rank

            elif int(self.age) > 55:
                if test_name < 6:
                    rank = 1
                elif test_name < 10:
                    rank = 2
                elif test_name < 20:
                    rank = 3
                elif test_name < 35:
                    rank = 4
                elif test_name < 65:
                    rank = 5
                elif test_name < 100:
                    rank = 6
                elif test_name >= 100:
                    rank = 7

                self.test2_rank = rank

        if t == 'test3':
            test_name = self.w5d3_test3
            if int(self.age) < 40:
                if test_name < 6:
                    rank = 1
                elif test_name < 15:
                    rank = 2
                elif test_name < 30:
                    rank = 3
                elif test_name < 50:
                    rank = 4
                elif test_name < 100:
                    rank = 5
                elif test_name < 150:
                    rank = 6
                elif test_name >= 150:
                    rank = 7

                self.test3_rank = rank

            elif int(self.age) < 56:
                if test_name < 6:
                    rank = 1
                elif test_name < 13:
                    rank = 2
                elif test_name < 25:
                    rank = 3
                elif test_name < 45:
                    rank = 4
                elif test_name < 75:
                    rank = 5
                elif test_name < 125:
                    rank = 6
                elif test_name >= 125:
                    rank = 7
                self.test3_rank = rank

            elif int(self.age) > 55:
                if test_name < 6:
                    rank = 1
                elif test_name < 10:
                    rank = 2
                elif test_name < 20:
                    rank = 3
                elif test_name < 35:
                    rank = 4
                elif test_name < 65:
                    rank = 5
                elif test_name < 100:
                    rank = 6
                elif test_name >= 100:
                    rank = 7

                self.test3_rank = rank

        if t == 'final_test':
            rank = 0
            test_name = self.final_test
            if int(self.age) < 40:
                if test_name < 6:
                    rank = 1
                elif test_name < 15:
                    rank = 2
                elif test_name < 30:
                    rank = 3
                elif test_name < 50:
                    rank = 4
                elif test_name < 100:
                    rank = 5
                elif test_name < 150:
                    rank = 6
                elif test_name >= 150:
                    rank = 7

                self.final_test_rank = rank

            elif int(self.age) < 56:
                if test_name < 6:
                    rank = 1
                elif test_name < 13:
                    rank = 2
                elif test_name < 25:
                    rank = 3
                elif test_name < 44:
                    rank = 4
                elif test_name < 74:
                    rank = 5
                elif test_name < 125:
                    rank = 6
                elif test_name >= 125:
                    rank = 7

                self.final_test_rank = rank

            elif int(self.age) > 55:
                if test_name < 6:
                    rank = 1
                elif test_name < 10:
                    rank = 2
                elif test_name < 20:
                    rank = 3
                elif test_name < 35:
                    rank = 4
                elif test_name < 65:
                    rank = 5
                elif test_name < 100:
                    rank = 6
                elif test_name >= 100:
                    rank = 7

                self.final_test_rank = rank

    def user_dict(self):
        user_dict = {'name':              self.name,
                     'age':               self.age,
                     'initial_test':      self.initial_test,
                     'test_1':            self.w2d3_test1,
                     'test_2':            self.w4d3_test2,
                     'test_3':            self.w5d3_test3,
                     'final_test':        self.final_test,
                     'initial_test_rank': self.initial_test_rank,
                     'test1_rank':        self.test1_rank,
                     'test2_rank':        self.test2_rank,
                     'test3_rank':        self.test3_rank,
                     'final_test_rank':   self.final_test_rank}

        return user_dict


p1 = Person()


def main():
    """Entry point and intro text"""
    tb.main_text()
    menu()


def menu():
    """List of and access point to the apps options """

    print("""
1 - Sign Up
2 - Login
3 - Save progress
4 - Go to week/day
5 - Test results
6 - Exit
""")

    choice = input()

    if choice not in ['1', '2', '3', '4', '5', '6']:
        menu()
    elif choice == '1':
        create_user_and_access_initial_test()
    elif choice == '2':
        login()
    elif choice == '3':
        save()
    elif choice == '4':
        choose_day_week()
    elif choice == '5':
        show_user_details()
    elif choice == '6':
        save_and_exit()


def choose_day_week():
    """Takes week/day input. Dictionary keys(week, day): values = corresponding push up table. Displays table to
    match entry then goes to test if applicable for the day. """
    week_dictionary = {
        (1, 1): put.week_one_day_one,
        (1, 2): put.week_one_day_two,
        (1, 3): put.week_one_day_three,
        (2, 1): put.week_two_day_one,
        (2, 2): put.week_two_day_two,
        (2, 3): put.week_two_day_three,
        (3, 1): put.week_three_day_one,
        (3, 2): put.week_three_day_two,
        (3, 3): put.week_three_day_three,
        (4, 1): put.week_four_day_one,
        (4, 2): put.week_four_day_two,
        (4, 3): put.week_four_day_three,
        (5, 1): put.week_five_day_one,
        (5, 2): put.week_five_day_two,
        (5, 3): put.week_five_day_three,
        (6, 1): put.week_six_day_one,
        (6, 2): put.week_six_day_two,
        (6, 3): put.week_six_day_three,
    }
    # Initial test must be completed before other tests for rank to be calculated. >0 means the process has been
    # completed.
    if p1.age == 0:
        print('Complete the initial test first.')
        input('Press any key and go to the initial test page.')
        create_user_and_access_initial_test()

    # Get week. Check and deal with UI errors
    week = input('Week (1 - 6): ')
    while week not in ['1', '2', '3', '4', '5', '6']:
        week = input('Week (1 - 6): ')

    # Get day. Check and deal with UI errors
    day = input('Day (1 - 3): ')
    while day not in ['1', '2', '3']:
        day = input('Day (1 - 3): ')

    print(week_dictionary[int(week), int(day)]())

    # option to take or omit test on the given week/day
    if week == '2' and day == '3':
        cont_or_test = input('Perform test(y/N): ')
        if cont_or_test in 'nN':
            menu()
        else:
            exhaustion_test('test1')
    elif week == '4' and day == '3':
        cont_or_test = input('Perform test(y/N): ')
        if cont_or_test in 'nN':
            menu()
        else:
            exhaustion_test('test2')
    elif week == '5' and day == '3':
        cont_or_test = input('Perform test(y/N): ')
        if cont_or_test in 'nN':
            menu()
        else:
            exhaustion_test('test3')
    elif week == '6' and day == '3':
        cont_or_test = input('Perform test(y/N): ')
        if cont_or_test in 'nN':
            menu()
        else:
            exhaustion_test('final_test')
    else:
        menu()


def show_user_details():
    """Displays user details and result of each test"""
    print(f'\nTest results - {p1.name} | Age: {p1.age}')
    user_details_table = [
        ['Initial Test', p1.initial_test, p1.initial_test_rank],
        ['Test 1 (week 2)', p1.w2d3_test1, p1.test1_rank],
        ['Test 2 (week 4)', p1.w4d3_test2, p1.test2_rank],
        ['Test 3 (week 5)', p1.w5d3_test3, p1.test3_rank],
        ['Final Test (week 6)', p1.final_test, p1.final_test_rank],

    ]
    col_names = ["Test", "Pushups Completed", "Rank"]
    print(tabulate(user_details_table, headers=col_names, tablefmt='pretty'))
    menu()


def create_user_and_access_initial_test():
    """Prompts for username and age. Age is used to calculate rank for each test."""
    if not p1.name:
        tb.intro()
        p1.name = input('Name: ')
        while p1.age == 0:
            try:
                p1.age = int(input('Age: '))
            except ValueError:
                p1.age = 0
        exhaustion_test('initial_test')
    else:
        print(f'You are logged in as "{p1.name}"!')
        menu()


def exhaustion_test(test_name):
    """Process results of each pushup test. Passes result to the rank function of the class. Displays ranking table
    user details and the menu."""
    tb.perform_test()
    result = 0
    while result == 0:
        try:
            result = int(input('\nNo. of pushups completed: '))
        # to deal with no user input
        except ValueError:
            result = 0

    if test_name == 'initial_test':
        p1.initial_test = result
        p1.calculate_rank('initial_test')
        print(put.initial_test_table())
        show_user_details()
        print(tb.post_first_test())
        menu()
    elif test_name == 'test1':
        p1.w2d3_test1 = result
        p1.calculate_rank('test1')
        print(put.initial_test_table())
        show_user_details()
    elif test_name == 'test2':
        p1.w4d3_test2 = result
        p1.calculate_rank('test2')
        print(put.initial_test_table())
        show_user_details()
    elif test_name == 'test3':
        p1.w5d3_test3 = result
        p1.calculate_rank('test3')
        print(put.initial_test_table())
        show_user_details()
    elif test_name == 'final_test':
        p1.final_test = result
        p1.calculate_rank('final_test')
        print(put.initial_test_table())
        show_user_details()


def save():
    # open a file where data is to be stored (value = username entered).
    try:
        file = open(p1.name, 'wb')
    # Prompt to create via initial test if username has been entered (error).
    except FileNotFoundError:
        print('Signup and complete the initial test first! Press any key to continue.')
        menu()

    # dump information to the file
    pf.dump(p1.user_dict(), file)

    # close the file
    file.close()
    print(f'Username: {p1.name} - progress is saved. ')
    menu()


def save_and_exit():
    # open a file where data is to be stored
    try:
        file = open(p1.name, 'wb')
    # exit without creating/saving any user details and completing the initial test
    except FileNotFoundError:
        sys.exit('Goodbye!')

    # dump information to the file
    pf.dump(p1.user_dict(), file)

    # close the file
    file.close()
    sys.exit(f'Goodbye {p1.name}. Your progress was saved.')


def login():
    # open the file where data is dumped
    try:
        open_file = open(input('User Name: '), 'rb')
    except FileNotFoundError:
        print(f'The user name does not exit!')
        menu()

    # loading data
    user_details = pf.load(open_file)
    setattr(p1, 'name', user_details['name'])
    setattr(p1, 'age', user_details['age'])
    setattr(p1, 'initial_test', user_details['initial_test'])
    setattr(p1, 'w2d3_test1', user_details['test_1'])
    setattr(p1, 'w4d3_test2', user_details['test_2'])
    setattr(p1, 'w5d3_test3', user_details['test_3'])
    setattr(p1, 'final_test', user_details['final_test'])
    setattr(p1, 'initial_test_rank', user_details['initial_test_rank']),
    setattr(p1, 'test1_rank', user_details['test1_rank']),
    setattr(p1, 'test2_rank', user_details['test2_rank']),
    setattr(p1, 'test3_rank', user_details['test3_rank']),
    setattr(p1, 'final_test_rank', user_details['final_test_rank'])
    open_file.close()
    show_user_details()

# The following functions enable simple testing to meet CS50P submission requirement. 'Your 3 required custom functions
# other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under
# any classes or functions).'


def name():
    return p1.name


def age():
    return p1.age


def initial_test_rank():
    return p1.initial_test_rank


if __name__ == "__main__":
    main()
