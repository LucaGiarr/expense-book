import pandas as pd


# Global variables
categories = []
exp_months = [pd.DataFrame()] * 12

# Menus
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


def numb_selection_to_string(numb, menu_item):
    """
    Converts the number of a menu choice to a string.
    menu_item is a string (categories or expense or calcs)
    """
    numb = int(numb)
    if menu_item == 'delete':
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


# sub-menus (Calculations)
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


# Create the month expense data frames
def month_expense():
    """
    Generates the month expenses list
    """
    # Global variables
    # global exp_months

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


# Add/Edit Categories
# Categories
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

        elif main_menu_opt == 4:
            print('\n------------------ CALCULATIONS ------------------')
            sub_menu_calcs()

        elif main_menu_opt == 5:
            print('\n----------------- PRINT TO SCREEN ----------------')

        elif main_menu_opt == 6:
            print('\n--------------- DELETE EXPENSE BOOK --------------\n')

        else:
            print('\nGoodbye.\n')
            break


main()
