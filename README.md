# By Eliud Munyala

# Credits to : Software Development Book

# Software implimentations should achieve : Robustness,Adaptability,Reusability

## Objects --> Instance of class --> Each class Represents the outside world -->

***
Syntactically, self identifies the instance upon which a method is invoked. For example, assume that a user of our class has a variable, my card, that identifies an instance of the CreditCard class. When the user calls my card.get balance(),
identifier self, within the definition of the get balance method, refers to the card
known as my card by the caller. The expression, self. balance refers to an instance
variable, named balance, stored as part of that particular credit card’s state.
***
class              // CreditCard //

Fields :   _customer    _balance
           _bank        _limit
           _account

Behaviors : get_customer()  get_balance()
            get_bank()      get_limit()
            get_account()   charge(price)
            make_payment(amount) withdraw(amount)
