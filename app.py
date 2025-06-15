import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import os

st.set_page_config(page_title="Budget Tracker", layout="wide")
st.title("💸 Personal Budget Tracker")

DATA_FILE = "data/expenses.csv"
os.makedirs("data", exist_ok=True)

# ✅ Read CSV safely and parse mixed date formats
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE, parse_dates=["Date"])
else:
    df = pd.DataFrame(columns=["Amount", "Category", "Date", "Description"])

st.sidebar.header("➕ Add Expense")
with st.sidebar.form("expense_form"):
    amount = st.number_input("Amount", min_value=0.0, step=1.0)
    category = st.selectbox("Category", ["Food", "Transport", "Rent", "Shopping", "Utilities", "Others"])
    exp_date = st.date_input("Date", value=date.today())
    description = st.text_input("Description (optional)")
    submitted = st.form_submit_button("Add Expense")

    if submitted and amount:
        new_data = pd.DataFrame([[amount, category, exp_date, description]], columns=df.columns)
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success("Expense added!")

st.sidebar.header("📅 Filter")
if not df.empty:
    # ✅ FIXED: Handle inconsistent date formats
    df["Date"] = pd.to_datetime(df["Date"], format='mixed', errors='coerce')
    df = df.dropna(subset=["Date"])  # Remove any rows with unparseable dates

    selected_month = st.sidebar.selectbox(
        "Month", 
        options=df['Date'].dt.to_period('M').astype(str).unique()
    )
    filtered_df = df[df['Date'].dt.to_period('M').astype(str) == selected_month]
else:
    selected_month = None
    filtered_df = df

st.subheader("📋 Expense Table")
st.dataframe(filtered_df.sort_values(by="Date", ascending=False), use_container_width=True)

if not filtered_df.empty:
    st.subheader("📊 Monthly Summary")
    total = filtered_df["Amount"].sum()
    st.metric("Total Spend", f"₹ {total:,.2f}")

    cat_summary = filtered_df.groupby("Category")["Amount"].sum()
    fig, ax = plt.subplots()
    ax.pie(cat_summary, labels=cat_summary.index, autopct='%1.1f%%', startangle=90)
    ax.axis("equal")
    st.pyplot(fig)
else:
    st.info("No expenses to show for this month.")

st.sidebar.download_button("📥 Download CSV", data=df.to_csv(index=False), file_name="expenses.csv")
# ─────────────────────────────────────────────────────────────
# 👨‍💻 Made by Sridhar Reddy
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <p>Made with ❤️ by <strong>Sridhar Reddy</strong></p>
        <p>
            🔗 <a href="https://github.com/THATTEPALLY-SRIDHAR-REDDY-11" target="_blank">GitHub</a> | 
            🌐 <a href="https://sridhar-budget-tracker.streamlit.app/" target="_blank">Live Streamlit App</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


