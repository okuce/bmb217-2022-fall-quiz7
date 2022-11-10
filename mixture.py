"""
Name Surname = 
Number = 

"""

class Mixture:
    """Salt and water mixture manipulation class"""

    def __init__() -> None:
        """Mixture Constructor

        Args:
            total_amount (float): water + salt amount
            salt_amount (float): salt amount
        """



    def salt_ratio():
        """salt_ratio property getter

        Returns:
            float: salt_amount / total_amount
        """



    def salt_ratio():
        """salt_ratio property setter
        Calculates salt_amount with salt_ratio and total_amount 
        and sets salt_amount 

        Args:
            value (float): salt ratio
        """



    def water_amount():
        """water_amount property getter

        Returns:
            float: total_amount - salt_amount
        """   



    def water_amount():
        """water_amount property setter
        water_amount is a calculated property 
        it is read-only

        Args:
            value (float): water amount (but not used)

        Raises:
            AttributeError: "Cannot set water amount"
        """



    def water_ratio():
        """water_ratio property getter

        Returns:
            float: 1 - salt_ratio
        """



    def water_ratio():
        """water_ratio property setter
        water_ratio is a calculated property 
        it is read-only

        Args:
            value (float): water ratio (but not used)

        Raises:
            AttributeError: "Cannot set water ratio"
        """



    def from_salt_ratio():
        """from_salt_ratio is a classmethod 
        it is a alternative constructor
        it calls main constructor with total_amount and 0 salt_amount
        and creates a new instance
        it sets salt_ratio property of new instance

        Args:
            total_amount (float): water + salt amount
            salt_ratio (float): salt ratio

        Returns:
            Mixture: created new instance 
        """



    def from_water_ratio():
        """from_water_ratio is a classmethod 
        it is a alternative constructor
        it calls from_salt_ratio alternative constructor with total_amount and 1-water_ratio 

        Args:
            total_amount (float): water + salt amount
            water_ratio (float): water ratio

        Returns:
            Mixture: created new instance 
        """



    def from_water_amount():
        """from_water_amount is a classmethod 
        it is a alternative constructor
        it calls main constructor with total_amount and total_amount-water_amount
        and creates a new instance 

        Args:
            total_amount (float): water + salt amount
            water_amount (float): water amount

        Returns:
            Mixture: created new instance 
        """



    def from_amounts():
        """from_amounts is a classmethod 
        it is a alternative constructor
        it calls main constructor with water_amount+salt_amount and salt_amount
        and creates a new instance 

        Args:
            water_amount (float): water amount
            salt_amount (float): salt amount

        Returns:
            Mixture: created new instance 
        """


    def __add__():
        """Mixture class + operator overloader
        it creates a new instance with self.total_amount + rhs.total_amount and self.salt_amount + rhs.salt_amount


        Args:
            rhs (Mixture): right hand side object

        Returns:
            Mixture: created new instance
        """


    def __truediv__ ():
        """Mixture class / operator overloader
        it creates a new instance with self.total_amount / value and self.salt_amount / value


        Args:
            value (float): divider

        Returns:
            Mixture: created new instance
        """


    def __mul__():
        """Mixture class * operator overloader
        it creates a new instance with self.total_amount * value and self.salt_amount * value


        Args:
            value (float): multiplier

        Returns:
            Mixture: created new instance
        """


    def __eq__() -> bool:
        """Mixture class == operator overloader

        Args:
            rhs (Mixture): right hand side object

        Returns:
            bool: self.total_amount == rhs.total_amount and self.salt_amount == rhs.salt_amount
        """

        

    def __str__() -> str:
        """Mixture class to string method overloader

        Returns:
            str: 'SA:{:3.2f},WA:{:3.2f},SR:{:3.2f},WR:{:3.2f},TOTAL:{:3.2f}'
        """


    
