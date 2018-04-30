class Action:

    def __init__(self, action_type, amount=1):

        self.action_type = action_type
        self.amount = amount

    def display(self):

        print('Super class display')
