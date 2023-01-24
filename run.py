import pandas as pd


# Global variables
exp_months = [pd.DataFrame()] * 12


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
        df = pd.DataFrame(0, index=range(num_rows), columns=range(len(base_categ)))
        df.columns = base_categ
        exp_months[ind] = df

    # months with 30 days
    num_rows = 30
    months = [1, 3, 5, 8, 10]
    for ind in months:
        df = pd.DataFrame(0, index=range(num_rows), columns=range(len(base_categ)))
        df.columns = base_categ
        exp_months[ind] = df

    # month with 28 days
    num_rows = 28
    exp_months[1] = pd.DataFrame(0, index=range(num_rows), columns=range(len(base_categ)))
    exp_months[1].columns = base_categ


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
