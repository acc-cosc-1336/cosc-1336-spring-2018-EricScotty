from customer import Customer

class CustomerRepository:

    def __init__(self):

        self.customers = {}
        self.__init_account_data()

    def __init_account_data(self):

        self.customers[1] = Customer1()
        self.customers[2] = Customer2()
        self.customers[3] = Customer3()
        self.customers[4] = Customer4()
        self.customers[5] = Customer5()
        self.customers[6] = Customer6()
        self.customers[7] = Customer7()
        self.customers[8] = Customer8()
        self.customers[9] = Customer9()
        self.customers[10] = Customer10()
        self.customers[11] = Customer11()
        self.customers[12] = Customer12()
