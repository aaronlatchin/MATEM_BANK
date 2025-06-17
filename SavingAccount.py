import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from savings_account import SavingsAccount

st.set_page_config(page_title="Maten bank", layout="centered")

savings = SavingsAccount(50000)

with st.form('savings_form'):
    amount = st.number_input("Enter amount", min_value=0)
    operation = st.selectbox("Select operation", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")

if submit:
    with st.spinner("Processing..."):
        if operation == "Withdraw":
            withdrawal_limit=10000
            if amount > savings.balance:
                st.error(f"Insufficient funds")

            elif amount > withdrawal_limit:
                st.error(f"Withdrawal amounts exceeds the limit.")
            
            else: 
                amount <= savings.balance
                savings.savingsWithdraw(amount)
                st.success(f"The transaction was successful and the New balance {savings.balance}")

                
        else:
            savings.deposit(amount)
            st.success(f"Transaction complete. New balance: {savings.balance}")
