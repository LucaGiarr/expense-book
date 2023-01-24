

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


def main():
    """
    Main function from which the Expense book runs
    """
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
