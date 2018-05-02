#partially written by Arturo Gonzalez one of the best teachers in the WORLD!! lolz 
from main_menu_actions import MainMenuActions
from atm import ATM

class MainMenu:

    def __init__(self):

        self.atm = ATM()

    def __account_menu(self):

        print("Select account: ")
        print("1) Dealer")
        print("2) Player")
        print("3) Pot")

    def __display_menu0(self):
        print("Pot Menu")
        print("1) Display Pot")
        print("2) exit to account menu")

    def __display_menu(self):
        print("Dealer Menu")
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Distribute")
        print("4) Back")
        print("5) Next")
        print("6) End Round")
        print("7) End Hand")
        print("8) exit")

    def __display_menu1(self):
        print("Player Menu")
        print("1) Bet")
        print("2) Raise")
        print("3) Call")
        print("4) Fold")
        print("5) player exit")

    def __display_menu2(self):
        print("Player Select")
        print("1) Player 1")
        print("2) Player 2")
        print("3) Player 3")
        print("4) Player 4")
        print("5) Player 5")
        print("6) Player 6")
        print("7) Player 7")
        print("8) Player 8")
        print("9) Player 9")
        print("10) Player 10")
        print("11) Exit to Account Menu")

    def __display_menu3(self):
        print()

    def __display_menu4(self):

    def run_atm(self):

        choice = -1

        self.__account_menu()
        self.atm.account = int(input("Enter choice: "))

        while self.atm.account = 1:

            self.__display_menu()
            choice = int(input("What do you want to do?"))

            while choice != 8:
                self.__display_menu()
                choice = int(input("What do you want to do?"))

                    if choice == 1:
                        self.__display_menu2()
                        choice = int(input("What do you want to do?"))

                            while choice !=11:
                                self.main_menu_actions.__handle_deposit()
                        
                    elif choice == 2:
                        self.__display_menu2()
                        choice = int(input("What do you want to do?"))

                        while choice !=11:
                            self.main_menu_actions.__handle_withdraw()


                    elif choice == 3:
                        self.__display_menu2()
                        choice = int(input("What do you want to do?"))

                        while choice != 11
                            self.main_menu_actions.__handle_distribute()

                    elif choice == 4:
                        self.__display_menu2()
                        choice = int(input("What do you want to do?"))

                        while choice != 11:
                            self.main_menu_actions.__undo_last_action()

                    elif choice == 5:
                        self.main_menu_actions.__skip_action()
                               
                    elif choice == 6:
                        self.main_menu_actions.__end_round()

                    elif choice == 7:
                        self.main_menu_actions.__end_hand()


            choice = -1
            self.__account_menu()
            self.main_menu_actions.atm.account = int(input("Enter choice: "))

            if self.main_menu_actions.atm.account == 0:
                self.main_menu_actions.atm.account = 1
                self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[random.randint(1,4)]

        while self.atm.account = 2:

            self.__display_menu2()
            choice = int(input("What do you want to do?"))

            if choice = 1:
                self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[1]

            elif choice = 2:
                self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[2]

            elif choice = 3:
                self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[3]

            elif choice = 4:
                self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[4]

            elif choice = 5:
                self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[5]

            elif choice = 6:
                self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[6]

            elif choice = 7:
                self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[7]

            elif choice = 8:
                self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[8]

            elif choice = 9:
                self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[9]

            elif choice = 10:
                self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[10]


                while choice != 11:
                    self.__display_menu1()
                    choice = int(input("What do you want to do?"))

                        if choice == 1:
                            self.main_menu_actions.__bet()

                        elif choice == 2:
                            self.main_menu_actions.__raise()

                        elif choice == 3:
                            self.main_menu_actions.__call()
                            
                        elif choice == 4:
                            self.main_menu_actions.__fold()
                            
                choice = -1
                self.__account_menu()
                self.main_menu_actions.atm.account = int(input("Enter choice: "))

                if self.main_menu_actions.atm.account == 0:
                    self.main_menu_actions.atm.account = 1
                    self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[random.randint(1,4)]


        while self.atm.account = 3:

            self.__display_menu()
            choice = int(input("What do you want to do?"))

            while choice != 2:
                self.__display_menu1()
                choice = int(input("What do you want to do?"))

                    if choice == 1:
                        self.main_menu_actions.__display_pot()

            choice = -1
            self.__account_menu()
            self.main_menu_actions.atm.account = int(input("Enter choice: "))

            if self.main_menu_actions.atm.account == 0:
                self.main_menu_actions.atm.account = 1
                self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[random.randint(1,4)]

