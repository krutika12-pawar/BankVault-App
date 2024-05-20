import streamlit as st
import os

class User:
    def __init__(self, username, account_number):
        self.username = username.capitalize()
        self.account_number = account_number

    def get_user_info(self, registration_file):
        if os.path.exists(registration_file):
            with open(registration_file, "r") as file:
                for line in file:
                    fields = line.strip().split(",")
                    if len(fields) >= 7 and fields[6] == self.account_number:
                        return {
                            "last_name": fields[1],
                            "email": fields[2],
                            "phone": fields[3],
                        }
        return None

class Bank(User):
    def __init__(self, username, account_number):
        super().__init__(username, account_number)

    def user_profile(self):
        # registration data file with user information
        registration_file = "registration_data.txt"
        user_info = self.get_user_info(registration_file)

        if user_info:
            st.write(f"Name: {self.username} {user_info['last_name']}")
            st.write(f"Email Id: {user_info['email']}")
            st.write(f"Phone Number: {user_info['phone']}")
            st.write(f"Account Number: {self.account_number}")
        else:
            st.warning("User information not found.")
