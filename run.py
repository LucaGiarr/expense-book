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

        elif main_menu_opt == 1:
            print('\n------------- MENU ADD/EDIT EXPENSES -------------\n')

        elif main_menu_opt == 2:
            print('\n-------------- MENU ADD/EDIT INCOME --------------\n')

        elif main_menu_opt == 3:
            print('\n------------------- SHOW LIST --------------------\n')

        elif main_menu_opt == 4:
            print('\n------------------ CALCULATIONS ------------------')

        elif main_menu_opt == 5:
            print('\n----------------- PRINT TO SCREEN ----------------')

        elif main_menu_opt == 6:
            print('\n--------------- DELETE EXPENSE BOOK --------------\n')

        else:
            print('\nGoodbye.\n')
            break


main()
