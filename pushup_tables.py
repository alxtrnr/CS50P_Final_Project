from tabulate import tabulate
import project
import text_blocks as tb


def initial_test_table():
    print('\nThe Hundred Pushups Training Program - Test/Rank Table')
    i_t_table = [

        ['Rank(!)', 'Number of pushups performed', 'Number of pushups performed', 'Number of pushups performed'],
        [1, '0 - 5', '0 - 5', '0 - 5'],
        [2, '6 - 14', '6 - 12', '6 - 10'],
        [3, '15 - 29', '13 - 24', '11 - 19'],
        [4, '30 - 49', '25 - 44', '20 - 34'],
        [5, '50 - 99', '45 - 74', '35 - 64'],
        [6, '100 - 149', '75 - 124', '65 - 99'],
        [7, '150 & above', '125 & above', '100 & above']
    ]
    col_names = ["Age", "< 40 years", "40 - 55 years", "> 56 years"]

    return tabulate(i_t_table, headers=col_names, tablefmt='pretty')


# table and format checked
def week_one_day_one():
    print('\nThe Hundred Pushups Training Program')
    print("""
So, you've completed your initial test and keen to start or carry on with the program? Excellent news!

* If you managed 5 or less pushups in the test, follow column 1.
* If you completed between 6 and 10 pushups, column 2 is for you.
* Between 11 and 20 consecutive pushups? Impressive! Column 3 is what you're looking for.
        
More than 20 pushups? I would suggest starting the program on Week 3.

For example: let's say you managed 8 pushups. Looking at the second column, Day 1 begins with Set 1 (6 pushups), a rest 
period of 60 seconds, before moving on to Set 2 (6 pushups). Rest for 60 seconds and continue with Set 3 (4 pushups) and
Set 4 (4 pushups), before finishing with Set 5 and as many consecutive pushups as you can comfortably manage (at least 
5, but not so many that you damage muscle tissue). The 60 seconds rest between each level should allow you to complete 
the workout, but I promise it will get tough towards the end.
""")
    print('Week 1: day 1')
    print('REST 60 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')
    w1d1_table = [
        ['SET 1', '2', '6', '10'],
        ['SET 2', '3', '6', '12'],
        ['SET 3', '2', '4', '7'],
        ['SET 4', '2', '4', '7'],
        ['SET 5', 'max (at least 3)', 'max (at least 5)', 'max (at least 9)'],
    ]
    col_names = ['PUSHUPS', 'up to 5 pushups', '6-10 push ups', '11-20 push ups']
    return tabulate(w1d1_table, headers=col_names, tablefmt='pretty')


# table and format checked
def week_one_day_two():
    print('\nThe Hundred Pushups Training Program')
    print('\nWeek 1: day 2')
    print('REST 90 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')
    w1d2_table = [
        ['SET 1', '3', '6', '10'],
        ['SET 2', '4', '8', '12'],
        ['SET 3', '2', '6', '8'],
        ['SET 4', '3', '6', '8'],
        ['SET 5', 'max (at least 4)', 'max (at least 7)', 'max (at least 12)'],
    ]
    col_names = ['PUSHUPS', 'up to 5 pushups', '6-10 push ups', '11-20 push ups']
    return tabulate(w1d2_table, headers=col_names, tablefmt='pretty')


# table and format checked
def week_one_day_three():
    print('\nThe Hundred Pushups Training Program')
    print('\nWeek 1: day 3')
    print('REST 120 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')
    w1d3_table = [
        ['SET 1', '4', '8', '11'],
        ['SET 2', '5', '10', '15'],
        ['SET 3', '4', '7', '9'],
        ['SET 4', '4', '7', '9'],
        ['SET 5', 'max (at least 5)', 'max (at least 10)', 'max (at least 13)'],
    ]
    col_names = ['PUSHUPS', 'up to 5 pushups', '6-10 push ups', '11-20 push ups']
    print(tabulate(w1d3_table, headers=col_names, tablefmt='pretty'))
    print(tb.w1d3_end_text())
    return ''

# table and format checked
def week_two_day_one():
    print('\nThe Hundred Pushups Training Program')
    print("""
Week 1 should now be comfortably behind you and it's time to start Week 2 of the hundred pushups program. Continue by
following the same column of exercises as you did in Week 1. Don't cut any corners, but feel free to take a little more
rest between each level if you need to. It's also important to be well hydrated before you start each workout.
    """)
    print('Week 2: day 1')
    print('REST 60 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w2d1_table = [
        ['SET 1', '4', '9', '14'],
        ['SET 2', '6', '11', '14'],
        ['SET 3', '4', '8', '10'],
        ['SET 4', '4', '8', '10'],
        ['SET 5', 'max (at least 6)', 'max (at least 11)', 'max (at least 15)']
    ]
    col_names = ['PUSHUPS', 'up to 5 pushups', '6-10 push ups', '11-20 push ups']
    return tabulate(w2d1_table, headers=col_names, tablefmt='pretty')


# table and format checked
def week_two_day_two():
    print('\nThe Hundred Pushups Training Program\n')
    print('Week 2: day 2')
    print('REST 90 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w2d2_table = [
        ['SET 1', '5', '10', '14'],
        ['SET 2', '6', '12', '16'],
        ['SET 3', '4', '9', '12'],
        ['SET 4', '4', '9', '12'],
        ['SET 5', 'max (at least 7)', 'max (at least 13)', 'max (at least 17)']
    ]
    col_names = ['PUSHUPS', 'up to 5 pushups', '6-10 push ups', '11-20 push ups']
    return tabulate(w2d2_table, headers=col_names, tablefmt='pretty')


# table and format checked
def week_two_day_three():
    print('\nThe Hundred Pushups Training Program')
    print(tb.w2d3_start_text())
    print('Week 2: day 3')
    print('REST 120 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w2d3_table = [
        ['SET 1', '5', '12', '16'],
        ['SET 2', '7', '13', '17'],
        ['SET 3', '5', '10', '14'],
        ['SET 4', '5', '10', '14'],
        ['SET 5', 'max (at least 8)', 'max (at least 15)', 'max (at least 20)']
    ]
    col_names = ['PUSHUPS', 'up to 5 pushups', '6-10 push ups', '11-20 push ups']
    print(tabulate(w2d3_table, headers=col_names, tablefmt='pretty'))
    print(tb.wk2d3_end_text())
    return ''


# table and format checked
def week_three_day_one():
    print('\nThe Hundred Pushups Training Program')
    tb.wk3d1_start_text()
    print('Week 3: day 1')
    print('REST 60 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w3d1_table = [
        ['SET 1', '10', '12', '14'],
        ['SET 2', '12', '17', '18'],
        ['SET 3', '7', '13', '14'],
        ['SET 4', '7', '13', '14'],
        ['SET 5', 'max (at least 9)', 'max (at least 17)', 'max (at least 20)']
    ]
    col_names = ['PUSHUPS', '16 - 20 pushups', '21 - 25 push ups', '> 25 push ups']
    print(tabulate(w3d1_table, headers=col_names, tablefmt='pretty'))
    return ''


def week_three_day_two():
    print('\nThe Hundred Pushups Training Program\n')
    print('Week 3: day 2')
    print('REST 90 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w3d2_table = [
        ['SET 1', '10', '14', '20'],
        ['SET 2', '12', '19', '25'],
        ['SET 3', '8', '14', '15'],
        ['SET 4', '8', '14', '15'],
        ['SET 5', 'max (at least 12)', 'max (at least 19)', 'max (at least 25)']
    ]
    col_names = ['PUSHUPS', '16 - 20 pushups', '21 - 25 push ups', '> 25 push ups']

    print(tabulate(w3d2_table, headers=col_names, tablefmt='pretty'))
    return ''


def week_three_day_three():
    print('\nThe Hundred Pushups Training Program\n')
    print('Week 3: day 3')
    print('REST 120 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w3d3_table = [
        ['SET 1', '11', '16', '22'],
        ['SET 2', '13', '21', '30'],
        ['SET 3', '9', '15', '20'],
        ['SET 4', '9', '15', '20'],
        ['SET 5', 'max (at least 13)', 'max (at least 21)', 'max (at least 28)']
    ]
    col_names = ['PUSHUPS', '16 - 20 pushups', '21 - 25 push ups', '> 25 push ups']
    print(tabulate(w3d3_table, headers=col_names, tablefmt='pretty') + tb.wk3d3_end_text())
    return ''


def week_four_day_one():
    print('\nThe Hundred Pushups Training Program')
    print(tb.wk4d1_start_text())
    print('Week 4: day 1')
    print('REST 60 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w4d1_table = [
        ['SET 1', '12', '18', '21'],
        ['SET 2', '14', '22', '25'],
        ['SET 3', '11', '16', '21'],
        ['SET 4', '11', '16', '21'],
        ['SET 5', 'max (at least 20)', 'max (at least 25)', 'max (at least 32)']
    ]
    col_names = ['PUSHUPS', '16 - 20 pushups', '21 - 25 push ups', '> 25 push ups']
    print(tabulate(w4d1_table, headers=col_names, tablefmt='pretty'))
    return ''


def week_four_day_two():
    print('\nThe Hundred Pushups Training Program\n')
    print('Week 4: day 2')
    print('REST 90 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w4d2_table = [
        ['SET 1', '14', '20', '25'],
        ['SET 2', '16', '25', '29'],
        ['SET 3', '12', '20', '25'],
        ['SET 4', '12', '20', '25'],
        ['SET 5', 'max (at least 18)', 'max (at least 28)', 'max (at least 36)']
    ]
    col_names = ['PUSHUPS', '16 - 20 pushups', '21 - 25 push ups', '> 25 push ups']
    print(tabulate(w4d2_table, headers=col_names, tablefmt='pretty'))
    return ''


def week_four_day_three():
    print('\nThe Hundred Pushups Training Program\n')
    print('Week 4: day 3')
    print('REST 120 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w4d3_table = [
        ['SET 1', '16', '23', '29'],
        ['SET 2', '18', '28', '33'],
        ['SET 3', '13', '23', '29'],
        ['SET 4', '13', '23', '29'],
        ['SET 5', 'max (at least 20)', 'max (at least 33)', 'max (at least 40)']
    ]
    col_names = ['PUSHUPS', '16 - 20 pushups', '21 - 25 push ups', '> 25 push ups']
    print(tabulate(w4d3_table, headers=col_names, tablefmt='pretty'))
    print(tb.wk4d3_end_text())
    return ''


def week_five_day_one():
    print('\nThe Hundred Pushups Training Program')
    print(tb.wk5d1_start_text())
    print('Week 5: day 1')
    print('REST 60 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w5d1_table = [
        ['SET 1', '17', '28', '36'],
        ['SET 2', '19', '35', '40'],
        ['SET 3', '15', '25', '30'],
        ['SET 4', '15', '22', '24'],
        ['SET 5', 'max (at least 20)', 'max (at least 35)', 'max (at least 40)']
    ]
    col_names = ['PUSHUPS', '31 - 35 pushups', '36 - 40 push ups', '> 40 push ups']
    print(tabulate(w5d1_table, headers=col_names, tablefmt='pretty'))
    return ''



def week_five_day_two():
    print('\nThe Hundred Pushups Training Program\n')
    print('Week 5: day 2')
    print('REST 45 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w5d2_table = [
        ['SET 1', '10', '18', '19'],
        ['SET 2', '10', '18', '19'],
        ['SET 3', '13', '20', '22'],
        ['SET 4', '13', '20', '22'],
        ['SET 5', '10', '14', '18'],
        ['SET 6', '10', '14', '18'],
        ['SET 7', '9', '16', '22'],
        ['SET 8', 'max (at least 25)', 'max (at least 40)', 'max (at least 45)']
    ]
    col_names = ['PUSHUPS', '31 - 35 pushups', '36 - 40 push ups', '> 40 push ups']
    print(tabulate(w5d2_table, headers=col_names, tablefmt='pretty'))
    return ''


def week_five_day_three():
    print('\nThe Hundred Pushups Training Program\n')
    print('Week 5: day 3')
    print('REST 45 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w5d3_table = [
        ['SET 1', '13', '18', '20'],
        ['SET 2', '13', '18', '20'],
        ['SET 3', '15', '20', '24'],
        ['SET 4', '15', '20', '24'],
        ['SET 5', '12', '17', '20'],
        ['SET 6', '12', '17', '20'],
        ['SET 7', '10', '20', '22'],
        ['SET 8', 'max (at least 30)', 'max (at least 45)', 'max (at least 50)']
    ]
    col_names = ['PUSHUPS', '31 - 35 pushups', '36 - 40 push ups', '> 40 push ups']
    print(tabulate(w5d3_table, headers=col_names, tablefmt='pretty'))
    print(tb.wk5d3_end_text())
    return ''


def week_six_day_one():
    print('\nThe Hundred Pushups Training Program')
    print(tb.wk6d1_start_text())
    print('Week 6: day 1')
    print('REST 60 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w6d1_table = [
        ['SET 1', '25', '40', '45'],
        ['SET 2', '30', '50', '55'],
        ['SET 3', '20', '25', '35'],
        ['SET 4', '15', '25', '30'],
        ['SET 5', 'max (at least 40)', 'max (at least 50)', 'max (at least 55)']
    ]
    col_names = ['PUSHUPS', '46 - 50 pushups', '51 - 60 push ups', '> 60 push ups']
    print(tabulate(w6d1_table, headers=col_names, tablefmt='pretty'))
    return ''


def week_six_day_two():
    print('\nThe Hundred Pushups Training Program\n')
    print('Week 6: day 2')
    print('REST 45 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w6d2_table = [
        ['SET 1', '14', '20', '22'],
        ['SET 2', '14', '20', '22'],
        ['SET 3', '15', '23', '30'],
        ['SET 4', '15', '23', '30'],
        ['SET 4', '14', '20', '24'],
        ['SET 4', '14', '20', '24'],
        ['SET 4', '10', '18', '18'],
        ['SET 4', '10', '18', '18'],
        ['SET 9', 'max (at least 44)', 'max (at least 53)', 'max (at least 58)']
    ]
    col_names = ['PUSHUPS', '46 - 50 pushups', '51 - 60 push ups', '> 60 push ups']
    print(tabulate(w6d2_table, headers=col_names, tablefmt='pretty'))
    return ''


def week_six_day_three():
    print('\nThe Hundred Pushups Training Program\n')
    print('Week 6: day 3')
    print('REST 45 SECONDS BETWEEN EACH SET (LONGER IF REQUIRED)')

    w6d3_table = [
        ['SET 1', '13', '22', '26'],
        ['SET 2', '13', '22', '26'],
        ['SET 3', '17', '30', '33'],
        ['SET 4', '17', '30', '33'],
        ['SET 4', '16', '25', '26'],
        ['SET 4', '16', '25', '26'],
        ['SET 4', '14', '18', '22'],
        ['SET 4', '14', '18', '22'],
        ['SET 9', 'max (at least 50)', 'max (at least 55)', 'max (at least 60)']
    ]
    col_names = ['PUSHUPS', '46 - 50 pushups', '51 - 60 push ups', '> 60 push ups']
    print(tabulate(w6d3_table, headers=col_names, tablefmt='pretty'))
    input('\npress any button to continue...')
    print(tb.wk6d3_end_text())
    input('\nready for the final test...')
    print(tb.final_test_start_text())
    return ''





