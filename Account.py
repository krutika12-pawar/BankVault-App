import streamlit as st
import random
from datetime import datetime
import os

class Account: 
          
    def __init__(self, username, initial_balance, account_number):
        self.username = username
        self.initial_balance = initial_balance
        self.account_number = account_number

                
    def display_initial_balance(self):
        initial_balance = self.initial_balance
        
    #To deposite money in account           
    def deposit(self, amount):
        # initial balance + amount to deposite 
        self.initial_balance += amount
        # Update the initial balance in the session state
        st.session_state["initial_balance"] = self.initial_balance 
        # Update the initial balance after deposit money in the text file
        update_initial_balance_in_file(self.account_number, self.initial_balance)
        st.success(f"£{amount} deposited into your account. Your new balance is: £{self.initial_balance}")
        # Call save_transaction
        Account.save_transaction(self.account_number, "Deposit", "£", amount)  

    #To withdraw money from account   
    def withdraw(self, amount):
        #initial balance - amount to withdraw
        self.initial_balance -= amount
        # Update the initial balance in the session state
        st.session_state["initial_balance"] = self.initial_balance
        # Update the initial balance after deposit money in the text file
        update_initial_balance_in_file(self.account_number, self.initial_balance)
        st.success(f"£{amount} withdrawn from your account. Your new balance is: £{self.initial_balance}")
        # Call save_transaction with negative amount
        Account.save_transaction(self.account_number, "Withdrawal", "£", -amount)  

            
    # Define a function to save a transaction to the user's file
    def save_transaction(account_number, transaction_type, currency_sign, amount):
        # Create the user's directory
        user_dir = os.path.join("transactions", str(account_number))
        os.makedirs(user_dir, exist_ok=True)

        # To Get the current date and time
        now = datetime.now()
        timestamp = now.strftime("%d-%m-%Y %H:%M:%S")

        # To Create the transaction record
        transaction_record = f"{timestamp} | {transaction_type} | {currency_sign}{amount}"

        # Open the user's transaction file in append mode
        file_path = os.path.join(user_dir, "transactions.txt")
        with open(file_path, "a") as file:
            file.write(transaction_record + "\n")

    def show_transaction_history(account_number):
        user_dir = os.path.join("transactions", str(account_number))
        file_path = os.path.join(user_dir, "transactions.txt")

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                transactions = file.readlines()
                st.subheader("Transaction History")
                for transaction in transactions:
                    st.write(transaction.strip())
        else:
            st.warning("No transaction history found for this account.")
                           
def update_initial_balance_in_file(account_number, new_balance):
        file_path = "/Users/aniket/Desktop/UCB/OOPS Lectures/BankVault App/registration_data.txt"
        updated_lines = []

        with open(file_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            fields = line.strip().split(",")
            if len(fields) >= 7 and fields[6] == account_number:
                # Update the initial balance field
                fields[4] = str(new_balance) 
            updated_lines.append(",".join(fields))

        with open(file_path, "w") as file:
            file.write("\n".join(updated_lines))

        print(f"Initial balance updated in the file for account number {account_number}")

     

