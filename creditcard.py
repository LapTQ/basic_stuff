class CreditCard:
    """A customer credit card."""
    
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.
        
        The initial balance is zero.
        
        customer  the name of the customer (eg., 'Tran Quoc Lap')
        bank      the name of the bank (eg., 'VietinBank')
        acnt      the account identifier (eg., '1837 1932 3948 2994')
        limit     credit limit 
        """
        self._customer = customer
        self._bank     = bank
        self._acnt     = acnt
        self._limit    = limit
        self._balance  = 0
    
    def get_customer(self):
        """Return name of the customer."""
        return self._customer
        
    def get_bank(self):
        """Return name of the bank."""
        return self._bank
        
    def get_account(self):
        """Return the card identifing number."""
        return self._acnt
        
    def get_limit(self):
        """Return current credit limit."""
        return self._limit
        
    def get_balance(self):
        """Return current balance."""
        return self._balance
        
    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed, False if charge was denied.
        """
        if not isinstance(price, (int, float)):
            raise TypeError('price must be numeric')
        elif price < 0:
            raise ValueError('price must be positive')
            
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
            
    def make_payment(self, amount):
        """Process customer payment that reduce balance."""
        if not isinstance(amount, (int, float)):
            raise TypeError('payment must be numeric')
        elif price < 0:
            raise ValueError('payment must be positive')
            
        self._balance -= amount
        
        
class PredatoryCreditCard(CreditCard):
    """An extension to Creditcard that compound interest and fees."""
    
    def __init__(self, customer, bank, acnt, limit, apr):
        """
        Create a new predatory credit card instance.
        
        The initial balance is zero.
        
        customer  the name of the customer (eg., 'Tran Quoc Lap')
        bank      the name of the bank (eg., 'VietinBank')
        acnt      the account identifier (eg., '1837 1932 3948 2994')
        limit     credit limit
        apr       annual percentage rate
        """
        super().__init__(customer, bank, acnt, limit) # call super constructor
        self._apr = apr
        
    def charge(self, price): # override existing charge method
        """
        Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed
        Return False and assess $5 fee if charge is denied.
        """
        if not isinstance(price, (int, float)):
            raise TypeError('price must be numeric')
        elif price < 0:
            raise ValueError('price must be positive')
            
        success = super().charge(price)         # call inherited method
        if not success:
            self._balance += 5
        return success                          # caller expects return value
        
    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
        
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    
