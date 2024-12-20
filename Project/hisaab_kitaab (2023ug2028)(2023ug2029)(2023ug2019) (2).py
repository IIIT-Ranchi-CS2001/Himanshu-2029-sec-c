# CREATER OF HISAAB KITAAB

# CHAITANYA CHAURASIA (2023UG2028)
# HIMANSHU  GUPTA (2023UG2029)
# ROHIT PATEL (2023UG2019)


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

DATA_FILE = "hisaab_kitaab.csv"

def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=['Month', 'Income', 'Expenditure', 'Savings', 'Investment', 'Balance'])

def save_data(data):
    data.to_csv(DATA_FILE, index=False)

def calc_financials(data, month, inc, exp, inv):
    try:
        t_exp = sum(exp.values())
        sav = inc - t_exp
        bal = sav - inv

        if month not in data['Month'].values:
            new_row = pd.DataFrame({
                'Month': [month], 
                'Income': [inc], 
                'Expenditure': [t_exp], 
                'Savings': [sav], 
                'Investment': [inv], 
                'Balance': [bal]
            })
            data = pd.concat([data, new_row], ignore_index=True)
        else:
            data.loc[data['Month'] == month, ['Income', 'Expenditure', 'Savings', 'Investment', 'Balance']] = [
                inc, t_exp, sav, inv, bal
            ]
        return data, t_exp, sav, bal
    except:
        st.error("Something went wrong")
        return data, 0, 0, 0

def generate_bar_chart(data):
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        bar_width = 0.2
        months = data['Month']
        r1 = np.arange(len(months))
        r2 = [x + bar_width for x in r1]
        r3 = [x + bar_width for x in r2]
        r4 = [x + bar_width for x in r3]

        ax.bar(r1, data['Income'], color='green', width=bar_width, label='Income')
        ax.bar(r2, data['Expenditure'], color='red', width=bar_width, label='Expenditure')
        ax.bar(r3, data['Savings'], color='blue', width=bar_width, label='Savings')
        ax.bar(r4, data['Investment'], color='orange', width=bar_width, label='Investment')

        ax.set_xlabel('Month')
        ax.set_ylabel('Amount')
        ax.set_title('Overview')
        ax.set_xticks([r + bar_width * 1.5 for r in range(len(months))])
        ax.set_xticklabels(months)
        ax.legend()
        st.pyplot(fig)
    except:
        st.error("Couldn't generate chart")

def sidebar():
    st.sidebar.title("Options")
    return st.sidebar.selectbox("What do you want to do?", ["View Data", "Add Data"])

def main():
    data = load_data()
    option = sidebar()

    if option == "View Data":
        st.subheader("View Data")
        st.write(data)

        if st.button("Show Chart"):
            generate_bar_chart(data)

    elif option == "Add Data":
        st.subheader("Add Data")
        month = st.text_input("Month")
        income = st.number_input("Income", min_value=0.0)
        expenditures = {}
        num_exp = st.number_input("Number of expenditures", min_value=1, step=1, max_value=10)
        for i in range(int(num_exp)):
            name = st.text_input(f"Expenditure {i + 1} Name", "")
            value = st.number_input(f"Expenditure {i + 1} Amount", min_value=0.0)
            expenditures[name] = value
        investment = st.number_input("Investment", min_value=0.0)

        if st.button("Save"):
            data, t_exp, sav, bal = calc_financials(data, month, income, expenditures, investment)
            save_data(data)
            st.write(f"Total Expenditure: {t_exp}")
            st.write(f"Savings: {sav}")
            st.write(f"Balance: {bal}")
            generate_bar_chart(data)

        if st.button("Clear Data"):
            data = pd.DataFrame(columns=['Month', 'Income', 'Expenditure', 'Savings', 'Investment', 'Balance'])
            save_data(data)
            st.write("Data cleared")

if __name__ == "__main__":
    main()
