import streamlit as st
import re
import Registration as reg
from Bank import Bank
from Account import Account 


def Dashboard(username):
    #st.title("Dashboard")
    username = username.upper()
    st.header(f"Hello {username}, Welcome to your personal Banking!")

    # Retrieve the initial balance from the session state
    initial_balance = st.session_state.get("initial_balance", 0)
    
    # Retrieve the account number from the session state
    account_number = st.session_state.get("account_number", "")

    # Create an instance of the Account class
    account_instance = Account(username, initial_balance, account_number)
    
    #create as instance of the Bank class
    bank_instance = Bank(username, account_number)
    
    # Create separate menu items in the sidebar
    st.sidebar.header("Menu")
    menu_option = st.sidebar.radio("Select an option", ["Dashboard", "Profile", "Available Balance", "Deposit Money", "Withdraw Money", "Transaction History", "Logout"])

    account_number = account_instance.account_number
    masked_account_number = "X" * (len(account_number) - 4) + account_number[-4:]


    # Display the selected menu option
    if menu_option == "Dashboard":
        st.write(f"Account Number: {masked_account_number}")   
        st.write(f"Available Balance: £{account_instance.initial_balance}")
        
    if menu_option == "Profile":
        st.header("Personal Information")
        bank_instance.user_profile()
     
    elif menu_option == "Available Balance":
        st.header("Available Balance")
        account_instance.display_initial_balance()
        st.write(f"Your available balance is: £{initial_balance}")


    elif menu_option == "Deposit Money":
        st.header("Deposit Money")
        st.write("Want to deposit money into your account? Proceed with entering amount.")
        account_number = st.text_input("Your account number:", value=account_number, disabled=True)
        amount = st.number_input("Enter the amount to deposit:", min_value=0.0)

        if st.button("Deposit Money", type="primary"):
            if amount > 0:
                if account_number == account_number:
                    account_instance.deposit(amount)
                else:
                    st.error("Invalid account number.")
            else:
                st.warning("Please enter a valid amount to deposit.")
                 
    elif menu_option == "Withdraw Money":
        st.header("Withdraw Money")
        st.write("Want to withdraw money from your account? Proceed with amount you want to withdraw.")
        account_number = st.text_input("Your account number:", value=account_number, disabled=True)
        amount = st.number_input("Enter the amount to withdraw:", min_value=0.0)
        
        if st.button("Withdraw Money", type="primary"):
            if amount > 0:
                if account_number == account_number:
                    # Check if the withdrawal amount is less than or equal to the current balance
                    if amount <= account_instance.initial_balance:
                        account_instance.withdraw(amount)
                    else:
                        st.error("Insufficient balance. Your current balance is: £{:.2f}".format(account_instance.initial_balance))  
                else:
                    st.error("Invalid account number.")
            else:
                st.warning("Please enter a valid amount to withdraw.")
                         
    elif menu_option == "Transaction History":
        Account.show_transaction_history(account_number)
            
    elif menu_option == "Logout":
        reg.navigate_to_login(username)
        
