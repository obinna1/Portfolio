This Java program features a Purse class designed to manage a simple monetary system based on traditional British currency, where 1 pound equals 240 pence and 1 shilling equals 12 pence. 
The Purse class allows for the creation of purse objects to handle monetary values in pounds, shillings, and pence. It includes methods to add or spend money, alongside getter methods to retrieve the current amounts of each currency unit.

Key functionalities include:

Adding Money: Users can add pounds, shillings, and pence to the purse. The class automatically handles conversions between these units, ensuring that adding shillings or pence beyond their thresholds (20 shillings to a pound, 12 pence to a shilling) correctly updates the total in pounds, shillings, and pence.


Spending Money: Users can spend money from the purse, with the class converting the specified amounts into pence for subtraction, updating the purse's balance accordingly. If there aren't enough funds, it notifies the user of insufficient funds.


Displaying Balance: The class provides a toString method to output the current balance in a readable format, showing the amounts of pounds, shillings, and pence.
The accompanying PurseMain2 class serves as a tester, offering a menu-driven console interface for interacting with Purse objects. Users can create purses for two fictional characters, Sophie and Sally, and perform operations like adding money to or querying the balance of these purses. The program loops until the user decides to exit, offering a practical example of managing and manipulating object states based on user input.

This program is a useful demonstration of object-oriented programming concepts such as class design, object instantiation, and encapsulation in a real-world scenario of managing a wallet or purse with traditional British currency. It's a fitting showcase for a GitHub portfolio, demonstrating proficiency in Java programming, problem-solving, and the application of historical knowledge in software development.
