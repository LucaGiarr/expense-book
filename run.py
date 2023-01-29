import pandas as pd
from time import sleep
from os import system, name
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('expense_book')

# Global variables
categories = []
exp_months = [pd.DataFrame()] * 12


# Headers
def head_menus(menu_str):
    """
    Shows the headers of the menus
    """
    if menu_str == "categories":
        print('\n------------ MENU ADD/EDIT CATEGORIES ------------')
    elif menu_str == "expense":
        print('\n------------- MENU ADD/EDIT EXPENSES -------------')
    elif menu_str == "income":
        print('\n-------------- MENU ADD/EDIT INCOME --------------')
    elif menu_str == "show_categ_list":
        print('\n-------------- SHOW CATEGORY LIST ----------------')
    elif menu_str == "calcs":
        print('\n------------------ CALCULATIONS ------------------')
    elif menu_str == "print_to_terminal":
        print('\n---------------- PRINT TO TERMINAL ---------------')
    elif menu_str == "del_exp_book":
        print('\n--------------- DELETE EXPENSE BOOK --------------')
    elif menu_str == "exp_book":
        print('\n------------------ EXPENSE BOOK ------------------')


# Create the month expense data frames
def month_expense():
    """
    Generates the month expenses list
    """
    # Global variables
    global exp_months

    base_categ = ['days', 'income']

    months_31_days = [0, 2, 4, 6, 7, 9, 11]
    months_30_days = [3, 5, 8, 10]

    for ind in range(12):
        if ind in months_31_days:
            num_rows = 31
        elif ind in months_30_days:
            num_rows = 30
        else:
            num_rows = 28

        df = pd.DataFrame(
            0, index=range(num_rows), columns=range(len(base_categ)))
        df.columns = base_categ
        for day in range(num_rows):
            df.iat[day, 0] = day + 1
        exp_months[ind] = df


# Expense book loaded from spreadsheet
def month_exp_load():
    """
    Loads the monthly expenses from a spreadsheet saved online
    """
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep',
              'octob', 'nov', 'dec']
    for month in range(len(months)):
        sprsheet = SHEET.worksheet(months[month])
        ws = sprsheet.get_all_values()
        col = sprsheet.row_values(1)
        rows = sprsheet.col_values(1)
        ws.pop(0)
        # Convert ws values in float
        ws_float = [] * (len(rows) - 1)
        for row in range(len(rows) - 1):
            ws_float.append([round(float(item), 3) for item in ws[row]])

        exp_months[month] = pd.DataFrame(ws_float, index=range(len(rows) - 1),
                                         columns=col)


# Main menu
def main_menu():
    """
    Shows the initial options and features of the Expense book
    """
    print('\n-------------------- MAIN MENU --------------------\n')
    print('Digit the correspondent number to choose an option:\n')
    print('0 - Add or Edit a Category')
    print('1 - Add or Edit an Expense')
    print('2 - Add or Edit an Income')
    print('3 - Show the List of Categories')
    print('4 - Do a Calculation')
    print('5 - Print to Terminal')
    print('6 - Delete Expense Book')
    print('7 - Save and Exit')
    print('8 - Discard changes and Exit\n')


# Add/Edit menu
def add_edit_menu(strg):
    """
    Shows the menu of the add/edit Categories, Expenses and Income
    """
    # Global variables
    global categories

    strg = strg.capitalize()

    cat_length = len(categories)
    if strg == 'categories' and cat_length == 10:
        print('Are present 10 categories. You can:')
        print(f'\n1 - Rename {strg}')
        print(f'2 - Delete {strg}')
        print('3 - Go Back\n')
    elif strg == 'categories':
        print(f'\n0 - Add {strg}')
        print(f'1 - Rename {strg}')
        print(f'2 - Delete {strg}')
        print('3 - Go Back\n')
    else:
        print(f'\n0 - Add {strg}')
        print(f'1 - Edit {strg}')
        print(f'2 - Delete {strg}')
        print('3 - Go Back\n')


# Do a Calculation menus
def calcs_menu():
    """
    Shows the menu of Calculations
    """
    print('\n0 - Spent in a day')
    print('1 - Spent in a month')
    print('2 - Spent in the whole year')
    print('3 - Go Back\n')


def calcs_sub_menu():
    """
    Shows the sub-menu of Calculations
    """
    print('\n0 - Spent in a specific Category')
    print('1 - Spent in all Categories')
    print('2 - Go Back\n')


# Print to terminal menus
def show_menu():
    """
    Shows the menu of Print to Terminal
    """
    print('\n0 - Expense')
    print('1 - Income')
    print('2 - Go Back\n')


def show_sub_menu(opt_str):
    """
    Shows the sub-menu of Print to Terminal
    """
    print(f'0 - {opt_str} of a month')
    print(f'1 - {opt_str} of the year')
    print('2 - Go Back\n')


# Delete Expense book menus
def del_exp_book_menu():
    """
    Shows the menu of Delete Expense book
    """
    print('\n0 - Delete Categories (included Expenses and Incomes)')
    print('1 - Delete Expenses')
    print('2 - Delete Incomes')
    print('3 - Go Back\n')


def delete_sub_menu(opt_str):
    """
    Shows the sub-menu of Delete Expense book
    """
    print(f'0 - Delete {opt_str}s of a month')
    print(f'1 - Delete {opt_str}s of the year')
    print('2 - Go Back\n')


def delete_sub_sub_menu():
    """
    Shows the sub-menu of the sub-menu of Delete Expense book
    """
    print(f'\n0 - Delete Expenses of ALL categories')
    print(f'1 - Delete Expenses of ONE category')
    print('2 - Go Back\n')


# Load Expense Book menus
def load_exp_book_menu():
    """
    Shows the menu when the user is asked to load or create a new Expense Book
    """
    print('\n0 - Load existing Expense Book')
    print('1 - Create a new Expense Book')
    print('2 - Quit\n')


# Other functions
def numb_selection_to_string(numb, menu_item):
    """
    Converts the number of a menu choice to a string.
    menu_item is a string (categories or expense or calcs)
    """
    numb = int(numb)
    selection = ''
    if menu_item == 'calcs':
        if numb == 0:
            selection = 'a day'
        elif numb == 1:
            selection = 'a month'
        else:
            selection = 'the whole year'

    elif menu_item == 'show':
        if numb == 0:
            selection = 'Expense'
        elif numb == 1:
            selection = 'Income'

    elif menu_item == 'delete':
        if numb == 1:
            selection = 'Expense'
        elif numb == 2:
            selection = 'Income'
    else:
        if numb == 0:
            selection = 'add'
        elif numb == 1:
            if menu_item == 'categories':
                selection = 'rename'
            else:
                selection = 'edit'
        elif numb == 2:
            selection = 'delete'
        elif numb == 3:
            selection = 'go_back'

    return selection


def date_numb_to_text(date_str):
    """
    Converts the month inserted as value in the name of the month
    """
    if date_str == '01':
        month = 'January'
    elif date_str == '02':
        month = 'February'
    elif date_str == '03':
        month = 'March'
    elif date_str == '04':
        month = 'April'
    elif date_str == '05':
        month = 'May'
    elif date_str == '06':
        month = 'June'
    elif date_str == '07':
        month = 'July'
    elif date_str == '08':
        month = 'August'
    elif date_str == '09':
        month = 'September'
    elif date_str == '10':
        month = 'October'
    elif date_str == '11':
        month = 'November'
    else:
        month = 'December'

    return month


# Return days in a month function
def days_in_month(y, m):
    """
    Returns the number of days in a month
    Taken from:
    https://www.tutorialspoint.com/number-of-days-in-a-month-in-python#:
    ~:text=Practical%20Data%20Science%20using%20Python&text=
    Suppose%20we%20have%20one%20year,then%20the%20result%20is%2029.
    &text=if%20m%20is%20in%20the,31%2C%20otherwise%2C%20return%2030.
    """
    leap = 0
    if y % 400 == 0:
        leap = 1
    elif y % 100 == 0:
        leap = 0
    elif y % 4 == 0:
        leap = 1
    if m == 2:
        return 28 + leap
    months_31_days = [1, 3, 5, 7, 8, 10, 12]
    if m in months_31_days:
        return 31
    return 30


# Erase and/or Save data in Google sheet
def erase_save_data(action):
    """
    Saves data in a spreadsheet
    """
    jan = SHEET.worksheet('jan')
    feb = SHEET.worksheet('feb')
    mar = SHEET.worksheet('mar')
    apr = SHEET.worksheet('apr')
    may = SHEET.worksheet('may')
    jun = SHEET.worksheet('jun')
    jul = SHEET.worksheet('jul')
    aug = SHEET.worksheet('aug')
    sep = SHEET.worksheet('sep')
    octob = SHEET.worksheet('octob')
    nov = SHEET.worksheet('nov')
    dec = SHEET.worksheet('dec')

    jan.clear()
    feb.clear()
    mar.clear()
    apr.clear()
    may.clear()
    jun.clear()
    jul.clear()
    aug.clear()
    sep.clear()
    octob.clear()
    nov.clear()
    dec.clear()

    if action == 'save':
        jan.update([exp_months[0].columns.values.tolist()] +
                   exp_months[0].loc[:].values.tolist())
        feb.update([exp_months[1].columns.values.tolist()] +
                   exp_months[1].loc[:].values.tolist())
        mar.update([exp_months[2].columns.values.tolist()] +
                   exp_months[2].loc[:].values.tolist())
        apr.update([exp_months[3].columns.values.tolist()] +
                   exp_months[3].loc[:].values.tolist())
        may.update([exp_months[4].columns.values.tolist()] +
                   exp_months[4].loc[:].values.tolist())
        jun.update([exp_months[5].columns.values.tolist()] +
                   exp_months[5].loc[:].values.tolist())
        jul.update([exp_months[6].columns.values.tolist()] +
                   exp_months[6].loc[:].values.tolist())
        aug.update([exp_months[7].columns.values.tolist()] +
                   exp_months[7].loc[:].values.tolist())
        sep.update([exp_months[8].columns.values.tolist()] +
                   exp_months[8].loc[:].values.tolist())
        octob.update([exp_months[9].columns.values.tolist()] +
                     exp_months[9].loc[:].values.tolist())
        nov.update([exp_months[10].columns.values.tolist()] +
                   exp_months[10].loc[:].values.tolist())
        dec.update([exp_months[11].columns.values.tolist()] +
                   exp_months[11].loc[:].values.tolist())


# Clear terminal
def clear():
    """
    Clears the terminal once is called
    Taken from:
    https://www.geeksforgeeks.org/clear-screen-python/
    """
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Validation inputs
def validate_categ_strg(categ_list, remaining_categ):
    """
    Validates category names strings (used in the categories function)
    Inside the try: the total number of categories < 10,
    no spaces between category names
    Numbers allowed as category names.
    """
    # Global variables
    global categories

    item_present = []
    for item in categ_list:
        item_present.append(item in categories)

    space_present = []
    for item in categ_list:
        space_present.append(" " in item)

    dot_present = []
    for item in categ_list:
        dot_present.append("." in item)

    just_alnum_present = []
    for item in categ_list:
        just_alnum_present.append(item.isalnum())

    try:
        if len(categ_list) > remaining_categ:
            raise ValueError('too many categories inserted')
        elif len(categories) > 0 and True in item_present:
            raise ValueError('category name already present')
        elif True in space_present:
            raise ValueError('there is a space at the beginning, '
                             'end or between category names')
        elif True in dot_present:
            raise ValueError('there is a "." in a category name')
        elif False in just_alnum_present:
            raise ValueError('only letters and numbers allowed '
                             'for the category name')

    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True


def validate_strg(str_item):
    """
    Validates data (string) raising a ValueError if a dot,
    comma or a space is present in a category name
    """
    try:
        if ',' in str_item:
            raise ValueError('"," not allowed in the category name')
        elif '.' in str_item:
            raise ValueError('"." not allowed in the category name')
        elif ' ' in str_item:
            raise ValueError('" " not allowed in the category name')
        elif '-' in str_item:
            raise ValueError('"-" not allowed in the category name')
        if not str_item.isalnum():
            raise ValueError('only letters and numbers allowed '
                             'for the category name')

    except ValueError as e:
        print(f'Invalid data: {e}, please try again.')
        return False

    return True


def validate_numb_int(str_item, num_min, num_max):
    """
    Validates data (number) raising a
    ValueError if the input is not a number
    or in the range provided in the argument.
    """
    try:
        if not str_item.isdecimal():
            raise ValueError('the input is not allowed')
        elif int(str_item) < num_min or int(str_item) > num_max:
            raise ValueError('option out of range')

    except ValueError as e:
        print(f'Invalid data: {e}, please try again.')
        sleep(2)
        return False

    return True


def validate_numb_float(str_item, num_min, num_max):
    """
    Validates data (float number) raising a
    ValueError if the input is not a number
    or in the range provided in the argument.
    """
    try:
        if not float(str_item):
            raise ValueError('the input is not allowed')
        elif float(str_item) <= num_min or float(str_item) >= num_max:
            raise ValueError('value out of range')

    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True


def validate_date(date_str):
    """
    Validates data (date) raising a
    ValueError if the input is not as shown in the input.
    """

    try:
        if len(date_str) != 5:
            raise ValueError('a number or "/" missing in the input')
        elif not date_str[:2].isnumeric():
            raise ValueError('the "DD" numbers are not allowed')
        elif not date_str[3:].isnumeric():
            raise ValueError('the "MM" numbers are not allowed')
        elif int(date_str[:2]) < 1 or \
                int(date_str[:2]) > days_in_month(2023, int(date_str[3:])):
            raise ValueError(f'"DD" out of range. This month has '
                             f'{days_in_month(2023, int(date_str[3:]))} days')
        elif int(date_str[3:]) < 1 or int(date_str[3:]) > 12:
            raise ValueError('"MM" out of range')
        elif date_str[2] != "/":
            raise ValueError('missing "/" between DD and MM')

    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True


def validate_date_just_month(date_str):
    """
    Validates data (just month) raising a
    ValueError if the input from the user is not as suggested.
    """
    try:
        if len(date_str) != 2:
            raise ValueError('the length of the input is not correct')
        elif not date_str.isnumeric():
            raise ValueError('the input is not allowed')
        elif int(date_str) < 1 or int(date_str) > 12:
            raise ValueError('"MM" out of range')

    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True


# Add/Edit Categories
def add_edit_delete_categories(sub_menu_option):
    """
    Adds, edit and delete a category
    """
    # Global variables
    global categories, exp_months

    if len(categories) == 0:
        categ_present = "None"
    else:
        categ_present = ", ".join(categories)

    if sub_menu_option == 0:
        # Add Categories
        while True:
            remaining_categ = 10 - len(categories)
            print(
                f'Insert max {remaining_categ} '
                f'categories separated by a comma and with no spaces.')
            print('Example: restaurant,supermarket,bills,investments,other\n')
            print('The categories present are:')
            print(f'{categ_present}\n')

            categ_items = str.lower(
                input('Enter the categories name of the expenses here: '))

            categ_list = categ_items.split(',')

            # validate category names
            if validate_categ_strg(categ_list, remaining_categ):
                break

        for categ in categ_list:
            categories.append(categ)

            for ind in range(len(exp_months)):
                exp_months[ind][categ] = 0

        print(f'{", ".join(categ_list)} added successfully '
              f'to the categories!\n')
        sleep(4)

    elif sub_menu_option == 1 or sub_menu_option == 2:
        # Rename or Delete a Category
        while True:
            print('The categories present are:')
            print(f'{categ_present}\n')

            sub_menu_opt_str = numb_selection_to_string(
                sub_menu_option, 'categories')

            edit_del_str = str.lower(
                input(f'Insert the category you want to {sub_menu_opt_str}: '))

            # Check if this category is existing
            categ_already_present = edit_del_str in categories
            if categ_already_present:
                break
            else:
                print('Category name not present.\n')

        ind = categories.index(edit_del_str)
        if sub_menu_option == 1:
            # Rename one category
            print('Renaming a category will change the name of a category in\n'
                  'the expense of each month.')
            print('Renaming a category will not change or delete\n'
                  'the expenses already present in this category.')
            print('They can be found under the new category name.')
            print('\nAre you sure to rename a category?')

            while True:
                choice_str = input('Enter your option (Y/N): ')
                # convert the input to lower case to be able to
                # validate the input (validation is case-sensitive)
                choice_str_low = choice_str.lower()
                # validate yes or no
                if choice_str_low == 'y' or choice_str_low == 'n':
                    choice_str = choice_str_low.upper()
                    break
                else:
                    print(f'\nInput not valid, please try again.\n')

            if choice_str == 'Y':
                while True:
                    new_name_categ = input(
                        'Insert the new category name '
                        '(insert just one category name): ')
                    # validate category
                    if new_name_categ in categories:
                        print('\nCategory name already present.')
                        print('Choose a category name not already present.\n')
                    elif validate_strg(new_name_categ) is False:
                        pass
                    else:
                        sleep(2.5)
                        break

                categories[ind] = new_name_categ

                # Apply the changes to the expense DataFrame
                for month in range(len(exp_months)):
                    for item in range(len(categories)):
                        exp_months[month].columns.values[item + 2] = \
                            categories[item]
                print(f'Category {sub_menu_opt_str}d successfully!\n')
                sleep(4)
            else:
                # Category not renamed
                print('Category not renamed.')
                sleep(2.5)

        else:
            # Delete one category
            print('Deleting a category will delete all the expenses stored\n'
                  'under that category in each month.')
            print('\nAre you sure to delete a category?')
            choice_str = input('Enter your option (Y/N): ')
            # convert the input to lower case to be able to
            # validate the input (validation is case-sensitive)
            choice_str_low = choice_str.lower()
            # validate yes or no
            while True:
                if choice_str_low == 'y' or choice_str_low == 'n':
                    choice_str = choice_str_low.upper()
                    break
                else:
                    print(f'\n{choice_str} is not valid.\n')

            if choice_str == 'Y':
                categories.pop(ind)

                # Apply the changes to the expense DataFrame
                for month in range(len(exp_months)):
                    exp_months[month] = exp_months[month].drop(
                        edit_del_str, axis=1)
                print(f'Category {sub_menu_opt_str}d successfully!\n')
                sleep(4)
            else:
                # Category not deleted
                print('Category not deleted.')
                sleep(2.5)


def sub_menu_categories():
    """
    Function/Sub-menu to add, rename or delete a category
    """
    # Global variables
    global categories, exp_months

    while True:
        while True:
            clear()
            head_menus('categories')
            add_edit_menu('categories')
            categories_menu_opt = input('Enter your option: ')
            # Validate menu option
            if validate_numb_int(categories_menu_opt, 0, 3):
                categories_menu_opt = int(categories_menu_opt)
                break
        if categories_menu_opt == 3:
            # Go back
            break
        else:
            # Add, Rename or Delete a Category
            sub_menu_opt_str = numb_selection_to_string(
                categories_menu_opt, 'categories')
            print(f'\n/// {sub_menu_opt_str.capitalize()} a Category ///')
            add_edit_delete_categories(categories_menu_opt)


# Expense and Income
def add_edit_delete_exp_income(income_expense_str, option_str):
    """
    Adds, edit and delete an expenses or an income. 
    """
    # Global variables
    global categories, exp_months

    while True:
        date_str = input(f'Enter the date of {income_expense_str} (DD/MM): ')
        # validate date
        if validate_date(date_str):
            break

    if income_expense_str == 'income':
        categ_name = 'income'
        categ_column = 0
    else:
        while True:
            print(f'\nThe categories present are:\n{" ,".join(categories)}')
            categ_name = input(
                f'\nEnter the category name of which you want to '
                f'{option_str} the {income_expense_str}: ')

            if categ_name in categories:
                break
            else:
                print(
                    f'{categ_name} is not in categories. '
                    f'Please enter a valid category name.')

        categ_column = categories.index(categ_name)

    if option_str == 'delete':
        exp_inc_val = 0
    else:
        while True:
            exp_inc_str = input(
                f'Enter the new value of the {income_expense_str}: ')
            # validate expense (number)
            max_val = 999999999999
            if validate_numb_float(exp_inc_str, 0, max_val):
                break

        exp_inc_val = round(float(exp_inc_str), 3)

    date = date_str.split('/')
    day = int(date[0])
    month = int(date[1])

    # Extract the expenses as DataFrame 
    # from the list of all expenses of all months
    df = exp_months[month - 1]

    if income_expense_str == 'expense':
        ind = 2
    else:
        ind = 1

    if option_str == 'add':
        df.iat[day - 1, categ_column + ind] += exp_inc_val
    else:
        df.iat[day - 1, categ_column + ind] = exp_inc_val
        exp_months[month - 1] = df

    # Print confirmation of expense/income added
    month_text = date_numb_to_text(date[1])
    if option_str == 'delete':
        if income_expense_str == 'expense':
            # Delete expense
            print(f'\n{income_expense_str.capitalize()} deleted successfully '
                  f'to the category {categ_name} on the {day} of '
                  f'{month_text}.\n')
        else:
            # Delete income
            print(f'\n{income_expense_str.capitalize()} deleted successfully '
                  f'on the {day} of {month_text}.\n')
    else:
        print(f'\n{exp_inc_val} euro {option_str}ed successfully '
              f'to the category {categ_name} on the {day} of {month_text}.\n')


def sub_menu_exp_income(income_expense_str):
    """
    Function/Sub-menu to add, rename or delete an expense or an income
    """
    # Global variables
    global categories

    while True:
        while True:
            clear()
            head_menus(income_expense_str)
            add_edit_menu(income_expense_str)
            menu_opt = input('Enter your option: ')
            # Validate menu option
            if validate_numb_int(menu_opt, 0, 3):
                menu_opt = int(menu_opt)
                break

        option_str = numb_selection_to_string(menu_opt, income_expense_str)

        if menu_opt == 0 or menu_opt == 1 or menu_opt == 2:
            print(f'\n/// {option_str.capitalize()} an '
                  f'{income_expense_str} ///')
            add_edit_delete_exp_income(income_expense_str, option_str)
            sleep(4)
        else:
            break


# Calculations
def sub_menu_calcs():
    """
    Does calculations with the expenses and
    prints the values the user chooses to see
    """
    # Global variables
    global categories, exp_months

    while True:
        while True:
            clear()
            head_menus('calcs')
            calcs_menu()
            menu_opt = input('Enter your option: ')
            # validate option (calcs_menu)
            if validate_numb_int(menu_opt, 0, 3):
                menu_opt = int(menu_opt)
                break
            clear()
            head_menus('calcs')

        if menu_opt == 3:
            # Go Back
            break
        else:
            menu_opt_str = numb_selection_to_string(menu_opt, 'calcs')

            while True:
                clear()
                print(f'\n/// Spent in {menu_opt_str} ///')
                calcs_sub_menu()
                sub_menu_opt = input('Enter your option: ')
                #  validate menu option
                if validate_numb_int(sub_menu_opt, 0, 2):
                    sub_menu_opt = int(sub_menu_opt)
                    break
                clear()
                head_menus('calcs')

        if menu_opt == 0:
            # Spent in a day
            if sub_menu_opt == 2:
                # Go Back
                pass
            else:
                while True:
                    date_str = input('Enter the date of expense (DD/MM): ')
                    # validate date
                    if validate_date(date_str):
                        break

                date = date_str.split('/')
                day = int(date[0])
                month = int(date[1])

            if sub_menu_opt == 0:
                # Spent in 1 day in 1 category
                while True:
                    print('\nThe categories present are:')
                    print(f'{" ,".join(categories)}')
                    categ_name = input('\nEnter the category name of '
                                       f'which you want to find the expense: ')
                    # validate name of the category
                    if categ_name in categories:
                        break
                    else:
                        print(f'{categ_name} is not in categories.')
                        sleep(2.5)

                result = exp_months[month - 1].at[day - 1, categ_name]
                month_text = date_numb_to_text(date[1])
                print(f'\nThe {day} of {month_text} you spent {result} euro '
                      f'in the category {categ_name}.')
                sleep(4)
                clear()

            elif sub_menu_opt == 1:
                # Spent in 1 day in all categories
                result = 0
                for item in categories:
                    result += (exp_months[month - 1].at[day - 1, item])

                month_text = date_numb_to_text(date[1])
                print(f'\nThe {day} of {month_text} you spent {result} euro.')
                sleep(4)
                clear()

        elif menu_opt == 1:
            # Spent in 1 month
            if sub_menu_opt == 2:
                # Go Back
                pass
            else:
                while True:
                    date_str = input('Enter the month of expense (MM): ')
                    # validate date
                    if validate_date_just_month(date_str):
                        month = int(date_str)
                        break

            if sub_menu_opt == 0:
                # Spent in 1 month in 1 category
                while True:
                    print('\nThe categories present are:')
                    print(f'{" ,".join(categories)}')
                    categ_name = input('\nEnter the category name of '
                                       f'which you want to find the expense: ')
                    # validate name of the category
                    if categ_name in categories:
                        break
                    else:
                        print(f'{categ_name} is not in categories.')
                        sleep(2.5)

                result = exp_months[month - 1][categ_name].sum()
                month_text = date_numb_to_text(date_str)
                print(
                    f'\nIn {month_text} you spent {result} euro'
                    f' in the category {categ_name}.')
                sleep(4)
                clear()

            elif sub_menu_opt == 1:
                # Spent in 1 month in all categories
                result = 0
                for item in categories:
                    value = (exp_months[month - 1][item].sum())
                    result += value
                    print(f'{item}: {value} euro')

                month_text = date_numb_to_text(date_str)
                print(f'\nIn {month_text} you spent {result} euro.')
                sleep(4)
                clear()

        elif menu_opt == 2:
            # Spent in the whole year
            if sub_menu_opt == 0:
                # Spent in 1 year in 1 category
                while True:
                    print('The categories present are:')
                    print(f'{" ,".join(categories)}')
                    categ_name = input(f'\nEnter the category name of '
                                       f'which you want to find the expense: ')
                    # validate name of the category
                    if categ_name in categories:
                        break
                    else:
                        print(f'{categ_name} is not in categories.\n')
                        sleep(2.5)

                result = 0
                for month in range(len(exp_months)):
                    result += exp_months[month][categ_name].sum()

                print(
                    f'\nIn the whole 2023 you spent {result} euro '
                    f'in the category {categ_name}.')
                sleep(4)
                clear()

            elif sub_menu_opt == 1:
                # Spent in 1 year in all categories
                result = 0
                for month in range(len(exp_months)):
                    result_month = 0
                    for item in categories:
                        value = (exp_months[month][item].sum())
                        result += value
                        result_month += value

                    print(f'{month + 1}: {result_month} euro')

                print(f'\nIn the whole 2023 you spent {result} euro.')
                sleep(4)
                clear()
                head_menus('calcs')
            else:
                pass


# Print to Terminal
def sub_menu_print():
    """
    Prints to terminal an expense or an income in a month or of the whole year
    """
    # Global variables
    global categories, exp_months

    while True:
        while True:
            clear()
            head_menus('print_to_terminal')
            show_menu()
            menu_opt = input('Enter your option: ')
            # validate option (calcs_menu)
            if validate_numb_int(menu_opt, 0, 2):
                menu_opt = int(menu_opt)
                break

        if menu_opt == 2:
            # Go Back
            break
        elif len(categories) == 0 and menu_opt == 0:
            print('\nThere are no expenses because no categories are present.')
            print('Add first a category.')
            sleep(4)
        else:

            menu_opt_str = numb_selection_to_string(menu_opt, 'show')

            while True:
                clear()
                head_menus('print_to_terminal')
                print(f'\n/// {menu_opt_str} ///')
                show_sub_menu(menu_opt_str)
                sub_menu_opt = input('Enter your option: ')
                #  validate option (calcs_sub_menu)
                if validate_numb_int(sub_menu_opt, 0, 2):
                    sub_menu_opt = int(sub_menu_opt)
                    break

            if sub_menu_opt == 0:
                # Expense or Income of one month
                while True:
                    month_str = input(
                        f'Enter the month of {menu_opt_str} (MM): ')
                    # Validate month
                    if validate_date_just_month(month_str):
                        month = int(month_str)
                        break

                if menu_opt == 0:
                    # Expense of one month
                    df_exp = exp_months[month - 1].copy()
                    del df_exp['income']
                    clear()
                    print(f'\n{df_exp}')
                    sleep(7)
                else:
                    # Income of one month
                    clear()
                    print(f'\n{exp_months[month - 1].loc[:, "days":"income"]}')
                    sleep(7)

            elif sub_menu_opt == 1:
                # Expense or Income of the year
                if menu_opt == 0:
                    # Expense of the year
                    result = pd.DataFrame()
                    for categ in categories:
                        for month in range(len(exp_months)):
                            res = exp_months[month][categ].sum()
                            result.at[month + 1, categ] = res

                    exp_list = result.sum().tolist()
                    exp_year = 0
                    for item in exp_list:
                        exp_year += (round(float(item), 2))

                    clear()
                    print(f'\n{result}')
                    print(f'\nIn total you spent {exp_year} euro this year.')
                    sleep(7)

                else:
                    # Income of the year
                    result = pd.DataFrame()
                    for month in range(len(exp_months)):
                        res = exp_months[month]['income'].sum()
                        result.at[month + 1, 'income'] = res

                    inc_year = result.sum().tolist()

                    clear()
                    print(f'\n{result}')
                    print(f'\nThe income of the year is {inc_year[0]} euro.')
                    sleep(7)
            else:
                # Go back
                pass


# Delete Expense book
def del_exp_book():
    """
    Deletes Expenses or Incomes of a whole month or year
    """
    # Global variables
    global categories, exp_months

    while True:
        while True:
            clear()
            head_menus('del_exp_book')
            del_exp_book_menu()
            menu_opt = input('Enter your option: ')
            # validate option (calcs_menu)
            if validate_numb_int(menu_opt, 0, 3):
                menu_opt = int(menu_opt)
                break

        if menu_opt == 3:
            # Go Back
            break
        elif menu_opt == 0:
            if len(categories) == 0:
                print('No categories are present. Please add a category first.')
                sleep(4)
            else:
                print('\nAre you sure you want to delete all the categories '
                      'included the expenses and incomes?\n')
                while True:
                    sub_menu_opt = input('Enter your option (Y/N): ')
                    # convert the input to lower case to be able to
                    # validate the input (validation is case-sensitive)
                    sub_menu_opt_low = sub_menu_opt.lower()
                    # validate yes or no
                    if sub_menu_opt_low == 'y' or sub_menu_opt_low == 'n':
                        sub_menu_opt = sub_menu_opt.upper()
                        break
                    else:
                        print(f'\n{sub_menu_opt} is not valid.\n')
                if sub_menu_opt == 'N':
                    print('Data NOT deleted.')
                    sleep(3)
                else:
                    for month in range(len(exp_months)):
                        exp_months[month].drop(
                            exp_months[month].iloc[:, 2:], inplace=True, axis=1)
                        exp_months[month]['income'] = 0

                    categories = []
                    print('Expense book deleted successfully!')
                    sleep(3)

        elif menu_opt == 1 and len(categories) == 0:
            print('No categories are present. Please add a category first.')
            sleep(3)

        else:
            menu_opt_str = numb_selection_to_string(menu_opt, 'delete')
            while True:
                print(f'\n/// {menu_opt_str}s ///')
                delete_sub_menu(menu_opt_str)
                sub_menu_opt = input('Enter your option: ')
                #  validate menu option
                if validate_numb_int(sub_menu_opt, 0, 2):
                    sub_menu_opt = int(sub_menu_opt)
                    break

        if sub_menu_opt == 0:
            # Delete Expense or Income of one month
            while True:
                month_str = input(f'Enter the month you want to '
                                  f'delete the {menu_opt_str}s (MM): ')
                # Validate month
                if validate_date_just_month(month_str):
                    month = int(month_str)
                    month_text = date_numb_to_text(month_str)
                    break

            if menu_opt == 1:
                # Delete Expense of one month
                while True:
                    delete_sub_sub_menu()
                    sub_sub_menu_opt = input('Enter your option: ')
                    # Validate option
                    if validate_numb_int(sub_sub_menu_opt, 0, 2):
                        sub_sub_menu_opt = int(sub_sub_menu_opt)
                        break

                if sub_sub_menu_opt == 0:
                    # Delete Expenses of a month of ALL categories
                    for categ in categories:
                        exp_months[month - 1][categ] = 0
                    print(f'Expenses of ALL categories of {month_text} '
                          f'deleted successfully!')
                    sleep(3)

                elif sub_sub_menu_opt == 1:
                    # Delete Expense of a month of ONE category
                    while True:
                        print('The categories present are:')
                        print(f'{", ".join(categories)}')
                        categ_name = input(f'\nEnter the category name of which'
                                           f' you want to delete '
                                           f'the expenses: ')
                        # validate name of the category
                        if categ_name in categories:
                            break
                        else:
                            print(f'{categ_name} is not in categories. '
                                  f'Please enter a valid category name.\n')
                            sleep(3)

                    exp_months[month - 1][categ_name] = 0
                    print(f'Expenses of the category {categ_name} of '
                          f'{month_text} deleted successfully!')
                    sleep(3)

                else:
                    pass

            elif menu_opt == 2:
                # Delete Income of one month
                exp_months[month - 1]['income'] = 0
                print(f'Incomes of {month_text} deleted successfully!')
                sleep(3)

        elif sub_menu_opt == 1:
            # Delete Expense or Income of the year
            if menu_opt == 1:
                # Delete Expense of the year
                while True:
                    delete_sub_sub_menu()
                    sub_sub_menu_opt = input('Enter your option: ')
                    # Validate menu option
                    if validate_numb_int(sub_sub_menu_opt, 0, 2):
                        sub_sub_menu_opt = int(sub_sub_menu_opt)
                        break

                if sub_sub_menu_opt == 0:
                    # Delete Expenses of the whole year of ALL categories
                    for month in range(len(exp_months)):
                        for categ in categories:
                            exp_months[month][categ] = 0

                    print('Expenses of the whole year of '
                          'ALL categories deleted successfully.')
                    sleep(3)

                elif sub_sub_menu_opt == 1:
                    # Delete Expense of the whole year of ONE category
                    while True:
                        print('The categories present are:')
                        print(f'{", ".join(categories)}')

                        categ_name = input(f'\nEnter the category name of which'
                                           f' you want to delete '
                                           f'the expenses: ')
                        # validate name of the category
                        if categ_name in categories:
                            break
                        else:
                            print(f'{categ_name} is not in categories. '
                                  f'Please enter a valid category name.\n')
                            sleep(3)

                    for month in range(len(exp_months)):
                        exp_months[month][categ_name] = 0

                    print(f'Expenses of the whole year of the category '
                          f'{categ_name} deleted successfully!')
                    sleep(3)

                else:
                    # Go back
                    pass

            else:
                # Delete Income of the year
                for month in range(len(exp_months)):
                    exp_months[month]['income'] = 0

                print('Expenses of the whole year deleted successfully!')
                sleep(3)

        else:
            # Go back
            pass


def main():
    """
    Main function from which the Expense book runs
    """
    # Global variables
    global categories, exp_months

    # Check if there is existing data saved in the spreadsheet
    head_menus('exp_book')
    print('\nChecking existing data...')
    exp_months[0] = SHEET.worksheet('jan')
    existing_categ = exp_months[0].row_values(1)

    if len(existing_categ) <= 2:
        print('No data existing.')

        # Generate the monthly expense DataFrame
        month_expense()

        print(f'\n/// Add a Category ///')
        add_edit_delete_categories(0)
    else:
        print('Found existing Expense book.')
        while True:
            load_exp_book_menu()
            sub_menu_opt = input('Enter your option: ')
            #  validate menu option
            if validate_numb_int(sub_menu_opt, 0, 2):
                sub_menu_opt = int(sub_menu_opt)
                break
            clear()
            head_menus('exp_book')
            print('\nFound existing Expense book.')

        if sub_menu_opt == 2:
            # Quit
            print('\nGoodbye.')
            quit()

        elif sub_menu_opt == 0:
            # Load existing Expense Book
            print('Loading data...')
            month_exp_load()
            categories = existing_categ[2:]
            print('Data loaded successfully!')
            sleep(3)
            clear()
        else:
            # Create a new Expense Book
            # Generate the monthly expense DataFrame
            month_expense()

            print(f'\n/// Add a Category ///')
            add_edit_delete_categories(0)

    while True:
        while True:
            clear()
            main_menu()
            main_menu_opt = input('Enter your option: ')
            # Validate main menu option
            if validate_numb_int(main_menu_opt, 0, 8):
                main_menu_opt = int(main_menu_opt)
                break
            sleep(2.5)

        if main_menu_opt == 0:
            # Categories
            sub_menu_categories()

        elif main_menu_opt == 1:
            # Expenses
            sub_menu_exp_income('expense')

        elif main_menu_opt == 2:
            # Incomes
            sub_menu_exp_income('income')

        elif main_menu_opt == 3:
            # Show category list
            clear()
            head_menus('show_categ_list')
            if len(categories) == 0:
                print('\nNo categories are present.')
            else:
                print(f'\nThe categories present are:\n{", ".join(categories)}')
            sleep(5)
        elif main_menu_opt == 4:
            # Do calculations
            sub_menu_calcs()

        elif main_menu_opt == 5:
            # Print to Terminal
            sub_menu_print()

        elif main_menu_opt == 6:
            # Delete Expense Book
            del_exp_book()

        elif main_menu_opt == 7:
            # Save and Exit
            print('\nUploading data...')
            erase_save_data('save')
            print('Data uploaded successfully!')
            print('Goodbye.')
            break

        else:
            # Exit without saving
            print('\nChanges discarded!')
            print('Goodbye.')
            break


main()
