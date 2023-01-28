import pandas as pd


# Global variables
categories = []
exp_months = [pd.DataFrame()] * 12


# Create the month expense data frames
def month_expense():
    """
    Generates the month expenses list
    """
    # Global variables
    global exp_months

    # base_categ = ['days', 'income']

    # delete from here
    base_categ = ['days', 'income', 'ciao', 'come', 'bene']
    # to here

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


# ------------ Menus ------------
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
    print('7 - Exit\n')


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
        while True:
            remaining_categ = 10 - len(categories)
            print(
                f'Insert max {remaining_categ} '
                f'categories separated by a comma and with no spaces.')
            print('Example: restaurant,supermarket,bills,investments,other\n')
            print('The categories present are:')
            print(f'{categ_present}\n')

            categ_items = str.lower(
                input('Enter your categories of the expenses here: '))

            categ_list = categ_items.split(',')

            # validate category names
            if validate_categ_strg(categ_list, remaining_categ):
                break

        for categ in categ_list:
            categories.append(categ)

            for ind in range(len(exp_months)):
                exp_months[ind][categ] = 0

        print(f'{categ} added successfully to the categories!\n')

    elif sub_menu_option == 1 or sub_menu_option == 2:

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
                    break

            categories[ind] = new_name_categ

            # Apply the changes to the expense DataFrame
            for month in range(len(exp_months)):
                for item in range(len(categories)):
                    exp_months[month].columns.values[item + 2] =\
                        categories[item]

        else:
            # Delete one category
            categories.pop(ind)

            # Apply the changes to the expense DataFrame
            for month in range(len(exp_months)):
                exp_months[month] = exp_months[month].drop(
                    edit_del_str, axis=1)

        print(f'Category {sub_menu_opt_str}d successfully!\n')


def sub_menu_categories():
    """
    Function/Sub-menu to add, rename or delete a category
    """
    # Global variables
    global categories, exp_months

    while True:
        while True:
            add_edit_menu('categories')
            categories_menu_opt = input('Enter your option: ')
            # Validate menu option
            if validate_numb_int(categories_menu_opt, 0, 3):
                categories_menu_opt = int(categories_menu_opt)
                break
        if categories_menu_opt == 3:
            break
        else:
            sub_menu_opt_str = numb_selection_to_string(
                categories_menu_opt, 'categories')
            print(f'\n/// {sub_menu_opt_str.capitalize()} a Category ///')
            add_edit_delete_categories(categories_menu_opt)

            print('The categories present are:')
            print(f'{", ".join(categories)}\n')


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
    df = exp_months[month-1]

    if income_expense_str == 'expense':
        ind = 2
    else:
        ind = 1

    if option_str == 'add':
        df.iat[day-1, categ_column + ind] += exp_inc_val
    else:
        df.iat[day-1, categ_column + ind] = exp_inc_val
        exp_months[month-1] = df

    # Print confirmation of expense/income added
    month_text = date_numb_to_text(date[1])
    if option_str == 'delete':
        print(f'\n{income_expense_str.capitalize()} deleted successfully '
              f'to the category {categ_name} on the {day} of {month_text}.\n')
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
            add_edit_menu(income_expense_str)
            menu_opt = input('Enter your option: ')
            # Validate menu option
            if validate_numb_int(menu_opt, 0, 3):
                menu_opt = int(menu_opt)
                break

        option_str = numb_selection_to_string(menu_opt, income_expense_str)

        if menu_opt == 0 or menu_opt == 1 or menu_opt == 2:
            print(f'\n/// {option_str.capitalize()} an {income_expense_str} ///')
            add_edit_delete_exp_income(income_expense_str, option_str)

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
            calcs_menu()
            menu_opt = input('Enter your option: ')
            # validate option (calcs_menu)
            if validate_numb_int(menu_opt, 0, 3):
                menu_opt = int(menu_opt)
                break

        if menu_opt == 3:
            # Go Back
            break
        else:
            menu_opt_str = numb_selection_to_string(menu_opt, 'calcs')

            while True:
                print(f'\n/// Spent in {menu_opt_str} ///')
                calcs_sub_menu()
                sub_menu_opt = input('Enter your option: ')
                #  validate menu option
                if validate_numb_int(sub_menu_opt, 0, 2):
                    sub_menu_opt = int(sub_menu_opt)
                    break

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

                result = exp_months[month - 1].at[day - 1, categ_name]
                month_text = date_numb_to_text(date[1])
                print(f'\nThe {day} of {month_text} you spent {result} euro '
                      f'in the category {categ_name}.')

            elif sub_menu_opt == 1:
                # Spent in 1 day in all categories
                result = 0
                for item in categories:
                    result += (exp_months[month - 1].at[day - 1, item])

                month_text = date_numb_to_text(date[1])
                print(f'\nThe {day} of {month_text} you spent {result} euro.')

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

                result = exp_months[month - 1][categ_name].sum()
                month_text = date_numb_to_text(date_str)
                print(
                    f'\nIn {month_text} you spent {result} euro'
                    f' in the category {categ_name}.')

            elif sub_menu_opt == 1:
                # Spent in 1 month in all categories
                result = 0
                for item in categories:
                    value = (exp_months[month - 1][item].sum())
                    result += value
                    print(f'{item}: {value} euro')

                month_text = date_numb_to_text(date_str)
                print(f'\nIn {month_text} you spent {result} euro.')

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

                result = 0
                for month in range(len(exp_months)):
                    result += exp_months[month][categ_name].sum()

                print(
                    f'\nIn the whole 2023 you spent {result} euro '
                    f'in the category {categ_name}.')

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
            print('\nNo expense because there are no categories.')
            print('Add first a category.')
        else:

            menu_opt_str = numb_selection_to_string(menu_opt, 'show')

            while True:
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
                    print(f'\n{df_exp}')
                else:
                    # Income of one month
                    print(exp_months[month - 1].loc[:, 'days':'income'])

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

                    print(result)
                    print(f'\nIn total you spent {exp_year} euro this year.')

                else:
                    # Income of the year
                    result = pd.DataFrame()
                    for month in range(len(exp_months)):
                        res = exp_months[month]['income'].sum()
                        result.at[month + 1, 'income'] = res

                    inc_year = result.sum().tolist()
                    print(result)
                    print(f'\nThe income of the year is {inc_year[0]} euro.')
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
                print('There are no categories present.')
            else:
                print('Are you sure you want to delete all the categories '
                      'included the expenses and incomes?\n')
                while True:
                    sub_menu_opt = input('Enter your option (Y/N): ')
                    # convert the input to lower case to be able to
                    # validate the input (validation is case-sensitive)
                    sub_menu_opt_low = sub_menu_opt.lower()
                    # validate yes or no
                    if sub_menu_opt_low == 'y' or sub_menu_opt == 'n':
                        sub_menu_opt = sub_menu_opt.upper()
                        break
                    else:
                        print(f'\n{sub_menu_opt} is not valid.\n')
                if sub_menu_opt == 'N':
                    print('Data NOT deleted.')
                else:
                    for month in range(len(exp_months)):
                        exp_months[month].drop(
                            exp_months[month].iloc[:, 2:], inplace=True, axis=1)
                        exp_months[month]['income'] = 0

                    categories = []
                    print('Expense book deleted successfully!')

        elif menu_opt == 1 and len(categories) == 0:
            print('There are no categories present.')

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

                    exp_months[month - 1][categ_name] = 0
                    print(f'Expenses of the category {categ_name} of '
                          f'{month_text} deleted successfully!')

                else:
                    pass

            elif menu_opt == 2:
                # Delete Income of one month
                exp_months[month - 1]['income'] = 0
                print(f'Incomes of {month_text} deleted successfully!')

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

                    for month in range(len(exp_months)):
                        exp_months[month][categ_name] = 0

                    print(f'Expenses of the whole year of the category '
                          f'{categ_name} deleted successfully!')

                else:
                    # Go back
                    pass

            else:
                # Delete Income of the year
                for month in range(len(exp_months)):
                    exp_months[month]['income'] = 0

                print('Expenses of the whole year deleted successfully!')

        else:
            # Go back
            pass


def main():
    """
    Main function from which the Expense book runs
    """
    # Global variables
    global categories

    # delete this form here
    categories = ['ciao', 'come', 'bene']
    # to here

    # Generate the monthly expense DataFrame
    month_expense()

    # delete from here
    global exp_months

    exp_months[0].iat[0, 2] = 100.2
    exp_months[0].iat[30, 2] = 1000.75
    exp_months[7].iat[24, 3] = 500
    exp_months[7].iat[13, 3] = 100.5
    exp_months[11].iat[30, 2] = 200
    exp_months[7].iat[24, 1] = 2000.20
    exp_months[0].iat[10, 1] = 1000.20
    # to here

    while True:
        while True:
            main_menu()
            main_menu_opt = input('Enter your option: ')
            # Validate main menu option
            if validate_numb_int(main_menu_opt, 0, 7):
                main_menu_opt = int(main_menu_opt)
                break

        if main_menu_opt == 0:
            print('\n------------ MENU ADD/EDIT CATEGORIES ------------')
            sub_menu_categories()

        elif main_menu_opt == 1:
            print('\n------------- MENU ADD/EDIT EXPENSES -------------')
            sub_menu_exp_income('expense')

        elif main_menu_opt == 2:
            print('\n-------------- MENU ADD/EDIT INCOME --------------')
            sub_menu_exp_income('income')

        elif main_menu_opt == 3:
            print('\n------------------- SHOW LIST --------------------')
            if len(categories) == 0:
                print('No categories are present.')
            else:
                print(f'The categories present are:\n{", ".join(categories)}')

        elif main_menu_opt == 4:
            print('\n------------------ CALCULATIONS ------------------')
            sub_menu_calcs()

        elif main_menu_opt == 5:
            print('\n----------------- PRINT TO SCREEN ----------------')
            sub_menu_print()

        elif main_menu_opt == 6:
            print('\n--------------- DELETE EXPENSE BOOK --------------')
            del_exp_book()

        else:
            print('\nGoodbye.\n')
            break


main()
