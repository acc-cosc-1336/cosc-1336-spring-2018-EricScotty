from actions import action

class ActionTransaction(action):

    def __init__(self, trans_type):

        Transaction.__init__(self, trans_type)

    def display(self):

        print(self.trans_type, format(self.amount, '.2f'))

    
