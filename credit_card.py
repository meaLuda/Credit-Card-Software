
class CreditCard:
    """A consumer credit card. """

    def __init__(self, customer, bank, account, limit):
        """
            Create a new credit_card instance.
            The initial balance is 0

            customer : name of customer (i.e "Eliud Munyala")
            bank    : name of the bank(i.e 'Equity Bank')
            acnt    : account identifier number(i.e 123 456 789)
            limit   : credit card( measured in dollars/ksh/euros e.t.c), updates
            deposit : money sent to the bank account
        """
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = 0
        self.deposit = deposit

        if self.deposit != None:
            self.balance += self.balance + self.deposit

    def get_customer(self):
        """Return name of customer"""
        return self.customer

    def get_bank(self):
        """Return customers bank"""
        return self.bank

    def get_account(self):
        """Return the cards identifier number (typically stored as string) """
        return self.account

    def get_limit(self):
        """Return current credit cards limit"""
        return self.limit

    def get_balance(self):
        """Return balance"""
        return self.balance

    def charge(self, price):
        """
            Charge a given price to the card, assuming sufficient credit limit
            Return :
                true if charge was processed
                False is denied

        """
        if price + self.balance > self.limit:
            return False
        else:
            self.balance += price
            return True

    def make_payment(self, amount):
        """
        Process customer payment and reduce the balance

        """
        self.balance -= amount

    def withdraw(self, amount):
        """
            From the balance minus the request withdraw
            update the balance and limit

        """
        self.balance -= amount
        
        pass

    def __repr__(self) -> str:
        return "Customer : {} , Bank: {} ".format(self.get_customer(), self.get_bank())

c1  = CreditCard( 'John Doe', '1st Bank' ,'5391 0375 9387 5309' , 1000,)

print(c1)
