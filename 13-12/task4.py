import streamlit as st

class Bank:
    balance = 50000

    def deposit(self):
        # Remove the default deposit amount
        amount = st.number_input("Enter amount to deposit:", min_value=100, max_value=50000, step=100, value=None)
        if amount:
            if amount < 100 or amount > 50000:
                st.title("Minimum deposit is 100 and Maximum deposit is 50000")
            elif amount % 100 == 0:
                self.balance += amount
                st.title(f"{amount} is deposited.")
                self.bal_enquiry()
                st.title("************ Transaction Successful *********")
            else:
                st.title("Amount should be in multiples of 100.")

    def withdraw(self):
        # Remove the default withdrawal amount
        amount = st.number_input("Enter amount to withdraw:", min_value=100, value=None)
        min_bal = 500
        minacc = self.balance - min_bal
        if amount:
            if amount < 100 or amount > minacc:
                st.title(f"Minimum withdrawal is 100 and Maximum withdrawal is {minacc}, "
                         f"as there should be a minimum balance of 500 in your account.")
            elif amount % 100 == 0:
                self.balance -= amount
                st.title(f"{amount} is withdrawn.")
                self.bal_enquiry()
                st.title("************ Transaction Successful *********")
            else:
                st.title("Amount should be in multiples of 100.")

    def bal_enquiry(self):
        st.title(f"Balance: {self.balance}")

    def viewoptions(self):
        transac = 3
        while transac > 0:
            st.title("----------------Transaction---------------------")
            # Add a unique key to each selectbox
            option = st.selectbox("Choose your option:",
                                  ["1. Deposit", "2. Withdraw", "3. Balance Enquiry", "4. Exit"], key=f"option_{transac}")
            if option == "1. Deposit":
                self.deposit()
            elif option == "2. Withdraw":
                self.withdraw()
            elif option == "3. Balance Enquiry":
                self.bal_enquiry()
            elif option == "4. Exit":
                st.title("Thank you for using the bank. Goodbye!")
                break
            else:
                st.title("Invalid option. Please choose a valid option.")
            transac -= 1

    def validate(self):
        chance = 3
        while chance > 0:
            # Remove default PIN value
            pin = int(st.number_input("Enter your pin:"))
            actual_pin = 1234
            if pin == actual_pin:
                self.viewoptions()
                break
            else:
                if chance == 1:
                    st.title("Your card is blocked. Too many incorrect attempts.")
                else:
                    st.title("Incorrect pin. Try again...")
            chance -= 1

# Initialize the Bank class and start the app
obj = Bank()
obj.validate()
