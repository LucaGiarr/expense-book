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

    base_categ = ['days', 'income']

    num_rows = 31
    months = [0, 2, 4, 6, 7, 9, 11]
    for ind in months:
        df = pd.DataFrame(
            0, index=range(num_rows), columns=range(len(base_categ)))
        df.columns = base_categ
        exp_months[ind] = df

    # months with 30 days
    num_rows = 30
    months = [1, 3, 5, 8, 10]
    for ind in months:
        df = pd.DataFrame(
            0, index=range(num_rows), columns=range(len(base_categ)))
        df.columns = base_categ
        exp_months[ind] = df

    # month with 28 days
    num_rows = 28
    exp_months[1] = pd.DataFrame(
        0, index=range(num_rows), columns=range(len(base_categ)))
    exp_months[1].columns = base_categ


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
    # global categories

    strg = strg.capitalize()

    cat_length = len(categories)
    if strg == 'categories' and cat_length == 10:
        print('Are present 10 categories. You can:')
        print(f'1 - Rename {strg}')
        print(f'2 - Delete {strg}')
        print('3 - Go Back\n')
    elif strg == 'categories':
        print(f'0 - Add {strg}')
        print(f'1 - Rename {strg}')
        print(f'2 - Delete {strg}')
        print('3 - Go Back\n')
    else:
        print(f'0 - Add {strg}')
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
    print(f'\n0 - {opt_str} of a month')
    print(f'1 - {opt_str} of the year')
    print('2 - Go Back\n')


# Delete Expense book menus
def del_exp_book_menu():
    """
    Shows the menu of Delete Expense book
    """
    print('\n0 - Delete Categories (included Expenses and Income)')
    print('1 - Delete Expense')
    print('2 - Delete Income')
    print('3 - Go Back\n')


def delete_sub_menu(opt_str):
    """
    Shows the sub-menu of Delete Expense book
    """
    print(f'\n0 - Delete {opt_str} of a month')
    print(f'1 - Delete {opt_str} of the year')
    print('2 - Go Back\n')


def delete_sub_sub_menu():
    """
    Shows the sub-menu of the sub-menu of Delete Expense book
    """
    print(f'\n0 - Delete Expense of ALL categories')
    print(f'1 - Delete Expense of ONE category')
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


# Return days in a month function
def days_in_month(y, m):
    """
    Returns the number of days in a month
    https://www.tutorialspoint.com/number-of-days-in-a-month-in-python#:~:text=Practical%20Data%20Science%20using%20Python&text=Suppose%20we%20have%20one%20year,then%20the%20result%20is%2029.&text=if%20m%20is%20in%20the,31%2C%20otherwise%2C%20return%2030.
    """
    leap = 0
    if y% 400 == 0:
        leap = 1
    elif y % 100 == 0:
        leap = 0
    elif y% 4 == 0:
        leap = 1
    if m==2:
        return 28 + leap
    list = [1,3,5,7,8,10,12]
    if m in list:
        return 31
    return 30


# Validation inputs
def validate_categ_strg(categ_list, remaining_categ):
    """
    Validates category names strings (used in the categories function)
    Inside the try: the total number of categories < 10, no spaces between category names - Numbers allowed as category names.
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
            raise ValueError('there is a space at the beginning, end or between category names')
        elif True in dot_present:
            raise ValueError('there is a "." in a category name')

    except ValueError as e:
        print(f'Invalid data: {e}, please try again.')
        return False

    return True


def validate_strg(str_item):
    """
    Validates data (string) raising a ValueError if a dot, comma or a space is present in a category name
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
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True


def validate_numb_int(str_item, num_min, num_max):
    """
    Validates data (number) raising a ValueError if the input is not a number or in the range provided in the argument.
    """
    try:
        if str_item.isdecimal() == False:
            raise ValueError('the input is not allowed')
        elif int(str_item) < num_min or int(str_item) > num_max:
            raise ValueError('option out of range')

    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True


def validate_numb_float(str_item, num_min, num_max):
    """
    Validates data (float number) raising a ValueError if the input is not a number or in the range provided in the argument.
    """
    try:
        if float(str_item) == False:
            raise ValueError('the input is not allowed')
        elif float(str_item) <= num_min or float(str_item) >= num_max:
            raise ValueError('value out of range')

    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True


def validate_date(date_str):
    """
    Validates data (date) raising a ValueError if the input is not as shown in the input.
    """

    try:
        if len(date_str) != 5:
            raise ValueError('a number or "/" missing in the input')
        elif date_str[:2].isnumeric() == False:
            raise ValueError('the "DD" numbers are not allowed')
        elif date_str[3:].isnumeric() == False:
            raise ValueError('the "MM" numbers are not allowed')
        elif int(date_str[:2]) < 1 or int(date_str[:2]) > days_in_month(2023,int(date_str[3:])):
            raise ValueError(f'"DD" out of range. This month has {days_in_month(2023,int(date_str[3:]))} days')
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
    Validates data (just month) raising a ValueError if the input from the user is not as suggested of the text printed in the terminal.
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
        
        remaining_categ = 10-len(categories)
        print(
                f'\nInsert max {remaining_categ} categories separated by a comma and with no spaces.\n')
        print('Example: restaurant,supermarket,bills,investments,other \n')
        print(f'{categ_present}')
        print('are the categories present.\n')

        categ_items = str.lower(
                input('Enter your categories of the expenses here: \n'))

        categ_list = categ_items.split(',')

        # validate category names

        for categ in categ_list:
            categories.append(categ)

            for ind in range(len(exp_months)):
                exp_months[ind][categ] = 0

    elif sub_menu_option == 1 or sub_menu_option == 2:

        while True:
            print(f'{categ_present}')
            print('are the categories present.\n')

            sub_menu_opt_str = numb_selection_to_string(
                sub_menu_option, 'categories')

            edit_del_str = str.lower(
                input(f'Insert the category you want to {sub_menu_opt_str}: '))

            # Check if this category is existing
            categ_already_present = edit_del_str in categories
            if categ_already_present == True:
                print('\nData is valid!\n')
                break
            else:
                print('Category name not present.\n')

        ind = categories.index(edit_del_str)
        if sub_menu_option == 1:
            # Rename one category

            
            new_name_categ = input(
                    'Insert the new category name (insert just one category name): ')
            # validate category
            if new_name_categ in categories:
                print('\nCategory name already present.')
                print('Choose a category name not already present.\n')

            else:
                print('\nData is valid!\n')
                

            categories[ind] = new_name_categ

            # Apply the changes to the expense DataFrame
            for month in range(len(exp_months)):
                for item in range(len(categories)):
                    exp_months[month].columns.values[item +
                                                     2] = categories[item]

            print(exp_months[0])
            print('\nChanges also applied to the expense DataFrame (rename)\n')
        else:
            # Delete one category
            categories.pop(ind)

            # Apply the changes to the expense DataFrame
            for month in range(len(exp_months)):
                exp_months[month] = exp_months[month].drop(
                    edit_del_str, axis=1)

            print(exp_months[11])

            print('\nChanges also applied to the expense DataFrame (delete)\n')

        print(f'Category {sub_menu_opt_str}d successfully!\n')
        print(f'The categories present are:\n{", ".join(categories)}\n')


def sub_menu_categories():
    """
    Function/Sub-menu to add, rename or delete a category
    """
    # Global variables
    # global categories, exp_months

    while True:
        add_edit_menu('categories')
        categories_menu_opt = int(input('Enter your option: '))
        # Validate menu option

        if categories_menu_opt == 0:
            print('\nAdd a Category')

            add_edit_delete_categories(categories_menu_opt)

            print(f'\n{", ".join(categories)}')
            print('are the categories present.\n')
            
        elif categories_menu_opt == 1 or categories_menu_opt == 2:

            add_edit_delete_categories(categories_menu_opt)
            print('Edit or delete')
            
        elif categories_menu_opt == 3:
            break
        else:
            print('\nWrong number! Choose a correct one.\n')


# Expense and Income
def add_edit_delete_exp_income(income_expense_str, option_str):
    """
    Adds, edit and delete an expenses or an income. 
    """
    # Globar variables
    # global categories, exp_months

    date_str = input(f'\nEnter the date of {income_expense_str} (DD/MM): ')
    # validate date

    if income_expense_str == 'income':
        categ_name = 'income'
        categ_column = 0
    else:
        while True:
            print(f'The categories present are:\n{" ,".join(categories)}')
            categ_name = input(f'\nEnter the category name of which you want to {option_str} the {income_expense_str}: ')

            if categ_name in categories:
                print('\nData is valid!\n')
                break
            else:
                print(
                    f'{categ_name} is not in categories. Please enter a valid category name.\n')

        categ_column = categories.index(categ_name)

    if option_str == 'delete':
        exp_inc_val = 0
    else:

        exp_inc_str = input(
            f'\nEnter the new value of the {income_expense_str}: ')
        # validate expense (number)

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
    print(f'\n{exp_inc_val}euro')
    print(f'{option_str}ed successfully to the category {categ_name} on the day {date_str}\n')

    print(exp_months[month-1])


def sub_menu_exp_income(income_expense_str):
    """
    Function/Sub-menu to add, rename or delete an expense or an income
    """
    # Global variables
    # global categories

    while True:

        add_edit_menu(income_expense_str)
        menu_opt = int(input('Enter your option: '))
        # Validate menu option

        option_str = numb_selection_to_string(menu_opt, income_expense_str)

        if menu_opt == 0 or menu_opt == 1 or menu_opt == 2:
            print(f'\n{option_str.capitalize()} an {income_expense_str}')
            add_edit_delete_exp_income(income_expense_str, option_str)
            pass
        else:
            break


# Calculations
def sub_menu_calcs():
    """
    Does calculations with the expenses and prints the values the user chooses to see
    """
    # Global variables
    global categories, exp_months

    while True:
        calcs_menu()
        menu_opt = input('Enter your option: ')
        # validate option (calcs_menu)
        menu_opt = int(menu_opt)
        if menu_opt == 3:
            # Go Back
            break
        else:
            menu_opt_str = numb_selection_to_string(menu_opt, 'calcs')
            print(f'\nSpent in {menu_opt_str}:')

            calcs_sub_menu()
            sub_menu_opt = input('Enter your option: ')
            #  validate option (calcs_sub_menu)
            sub_menu_opt = int(sub_menu_opt)

        if menu_opt == 0:
            # Spent in a day
            if sub_menu_opt == 2:
                # Go Back
                pass
            else:
                date_str = input(f'\nEnter the date of expense (DD/MM): ')
                # validate date

                date = date_str.split('/')
                day = int(date[0])
                month = int(date[1])

            if sub_menu_opt == 0:
                # Spent in 1 day in 1 category
                while True:
                    print(f'\nThe categories present are:\n{" ,".join(categories)}')
                    categ_name = input(f'\nEnter the category name of which you want to find the expense: ')
                    # validate name of the category
                    if categ_name in categories:
                        print('\nData is valid!\n')
                        break
                    else:
                        print(f'{categ_name} is not in categories.')

                result = exp_months[month - 1].at[day - 1, categ_name]
                print(f'\nThe {date_str} you spent {result} euro in the category {categ_name}')

            elif sub_menu_opt == 1:
                # Spent in 1 day in all categories
                result = 0
                for item in categories:
                    result += (exp_months[month - 1].at[day - 1, item])

                print(f'\nThe {date_str} you spent {result} euro.')

        elif menu_opt == 1:
            # Spent in 1 month

            if sub_menu_opt == 2:
                # Go Back
                pass
            else:
                date_str = input(f'\nEnter the month of expense (MM): ')
                # validate date
                month = int(date_str)

            if sub_menu_opt == 0:
                # Spent in 1 month in 1 category
                while True:
                    print(f'The categories present are:\n{" ,".join(categories)}')
                    categ_name = input(f'\nEnter the category name of which you want to find the expense: ')
                    # validate name of the category
                    if categ_name in categories:
                        print('\nData is valid!\n')
                        break
                    else:
                        print(f'{categ_name} is not in categories.\n')

                result = exp_months[month - 1][categ_name].sum()
                print(
                    f'\nThe {date_str} you spent {result} euro in the category {categ_name}.')

            elif sub_menu_opt == 1:
                # Spent in 1 month in all categories
                result = 0
                for item in categories:
                    value = (exp_months[month - 1][item].sum())
                    result += value
                    print(f'{item}: {value} euro')

                print(f'\nThe {date_str} you spent {result} euro.')

        elif menu_opt == 2:
            # Spent in the whole year
            if sub_menu_opt == 0:
                # Spent in 1 year in 1 category
                while True:
                    print(f'The categories present are:\n{" ,".join(categories)}')
                    categ_name = input(f'\nEnter the category name of which you want to find the expense: ')
                    # validate name of the category
                    if categ_name in categories:
                        print('\nData is valid!\n')
                        break
                    else:
                        print(f'{categ_name} is not in categories.\n')

                result = 0
                for month in range(len(exp_months)):
                    result += exp_months[month][categ_name].sum()

                print(
                    f'\nIn the whole 2023 you spent {result} euro in the category {categ_name}.')

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
        show_menu()
        menu_opt = input('Enter your option: ')
        # validate option (calcs_menu)
        menu_opt = int(menu_opt)

        if menu_opt == 2:
            # Go Back
            break
        elif len(categories) == 0 and menu_opt == 0:
            print('\nNo expense because there are no categories.')
            print('Add first a category.')
        else:

            menu_opt_str = numb_selection_to_string(menu_opt, 'show')

            show_sub_menu(menu_opt_str)
            sub_menu_opt = input('Enter your option: ')
            #  validate option (calcs_sub_menu)
            sub_menu_opt = int(sub_menu_opt)

            if sub_menu_opt == 0:
                # Expense or Income of one month

                month_str = input(f'\nEnter the month of {menu_opt_str} (MM): ')
                # Validate month
                month = int(month_str)

                if menu_opt == 0:
                    # Expense of one month
                    df_exp = exp_months[month - 1]
                    del df_exp['income']
                    print(df_exp)
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
    Deletes Expense or Income of a whole month or year
    """
    # Global variables
    global categories, exp_months

    while True:
        del_exp_book_menu()
        menu_opt = input('Enter your option: ')
        # validate option (calcs_menu)
        menu_opt = int(menu_opt)

        if menu_opt == 3:
            # Go Back
            break
        elif menu_opt == 0:
            if len(categories) == 0:
                print('There are no categories present.')
            else:
                print(
                    'Are you sure you want to delete all the categories included the expenses and income?\n')
                while True:
                    sub_menu_opt = input('Enter your option (Y/N): ')
                    # convert the input to lower case to be able to validate the input (validation is case-sensitive)
                    sub_menu_opt_low = sub_menu_opt.lower()
                    # validate yes or no
                    if sub_menu_opt_low == 'y' or sub_menu_opt == 'n':
                        print('\nData is valid!\n')
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
            delete_sub_menu(menu_opt_str)
            sub_menu_opt = input('Enter your option: ')
            #  validate menu option
            sub_menu_opt = int(sub_menu_opt)

        if sub_menu_opt == 0:
            # Delete Expense or Income of one month
            month_str = input(f'\nEnter the month you want to delete the {menu_opt_str} (MM): ')
            # Validate month
            month = int(month_str)

            if menu_opt == 1:
                # Delete Expense of one month
                delete_sub_sub_menu()
                sub_sub_menu_opt = input('Enter your option: ')
                # Validate option
                sub_sub_menu_opt = int(sub_sub_menu_opt)

                if sub_sub_menu_opt == 0:
                    # Delete Expenses of a month of ALL categories
                    for categ in categories:
                        exp_months[month - 1][categ] = 0

                    print(exp_months[month - 1])

                elif sub_sub_menu_opt == 1:
                    # Delete Expense of a month of ONE category
                    while True:
                        print(f'\n{", ".join(categories)}')
                        print('are the categories present.\n')
                        categ_name = input(f'\nEnter the category name of which you want to delete the expense: ')
                        # validate name of the category
                        if categ_name in categories:
                            print('\nData is valid!\n')
                            break
                        else:
                            print(f'{categ_name} is not in categories. Please enter a valid category name.\n')

                    exp_months[month - 1][categ_name] = 0
                    print(exp_months[month - 1])

                else:
                    pass

            elif menu_opt == 2:
                # Delete Income of one month
                exp_months[month - 1]['income'] = 0
                print(exp_months[month - 1].loc[:, 'days':'income'])
                print(f'\nIncome of {month - 1} deleted successfully!')

        elif sub_menu_opt == 1:
            # Delete Expense or Income of the year
            if menu_opt == 1:
                # Delete Expense of the year
                delete_sub_sub_menu()
                sub_sub_menu_opt = input('Enter your option: ')
                # Validate menu option
                sub_sub_menu_opt = int(sub_sub_menu_opt)

                if sub_sub_menu_opt == 0:
                    # Delete Expenses of the whole year of ALL categories
                    for month in range(len(exp_months)):
                        for categ in categories:
                            exp_months[month][categ] = 0

                    print(
                        'Expense of the whole year of ALL categories deleted successfully.')

                elif sub_sub_menu_opt == 1:
                    # Delete Expense of the whole year of ONE category
                    while True:
                        print(f'\n{", ".join(categories)}')
                        print('are the categories present.\n')

                        categ_name = input(f'\nEnter the category name of which you want to delete the expense: ')
                        # validate name of the category
                        if categ_name in categories:
                            print('\nData is valid!\n')
                            break
                        else:
                            print(f'{categ_name} is not in categories. Please enter a valid category name.\n')

                    for month in range(len(exp_months)):
                        exp_months[month][categ_name] = 0

                    print(
                        f'Expense of the whole year of the category {categ_name} deleted successfully.')

                else:
                    # Go back
                    pass

            else:
                # Delete Income of the year
                for month in range(len(exp_months)):
                    exp_months[month]['income'] = 0

                print(exp_months[7])
                print('Expense of the whole year deleted successfully.')

        else:
            # Go back
            pass


def main():
    """
    Main function from which the Expense book runs
    """
    # Generate the monthly expense DataFrame
    month_expense()

    while True:
        main_menu()
        main_menu_opt = input('Enter your option: ')
        main_menu_opt = int(main_menu_opt)

        if main_menu_opt == 0:
            print('\n------------ MENU ADD/EDIT CATEGORIES ------------\n')
            sub_menu_categories()

        elif main_menu_opt == 1:
            print('\n------------- MENU ADD/EDIT EXPENSES -------------\n')
            sub_menu_exp_income('expense')

        elif main_menu_opt == 2:
            print('\n-------------- MENU ADD/EDIT INCOME --------------\n')
            sub_menu_exp_income('income')

        elif main_menu_opt == 3:
            print('\n------------------- SHOW LIST --------------------\n')
            if len(categories) == 0:
                print('No categories are present.')
            else:
                print(f'The categories present are:\n{" ,".join(categories)}')

        elif main_menu_opt == 4:
            print('\n------------------ CALCULATIONS ------------------')
            sub_menu_calcs()

        elif main_menu_opt == 5:
            print('\n----------------- PRINT TO SCREEN ----------------')
            sub_menu_print()

        elif main_menu_opt == 6:
            print('\n--------------- DELETE EXPENSE BOOK --------------\n')
            del_exp_book()

        else:
            print('\nGoodbye.\n')
            break


main()
