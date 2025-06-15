This project is a simple yet powerful expense tracking web app built using Streamlit. It's designed to help users keep track of their daily and monthly expenses, categorize them, and visualize their spending patterns in an easy-to-understand interface.

🎯 Objective
The goal of this app is to:

Make personal budgeting simple and interactive.

Allow users to record daily expenses quickly.

Provide monthly summaries with visual breakdowns.

Enable downloading expense logs for offline use.

🧱 Project Structure
The app runs entirely from a single Python script.

It saves data into a CSV file inside a data/ folder.

The data persists between sessions, making it practical for long-term use.

📌 Key Functionalities
1. User Interface (UI) with Streamlit
The app uses Streamlit to render a user-friendly UI in the browser:

Sidebar: For adding new expenses and filtering by month.

Main page: For showing a table of expenses and visual summaries.

2. Data Storage
All expense data is saved in a CSV file.

The data includes:

Amount spent

Category (e.g., Food, Rent, Transport)

Date of the expense

Optional Description

The data is automatically loaded each time the app runs.

3. Adding New Expenses
The user inputs details in a form.

Once submitted:

The data is appended to the existing CSV file.

The UI shows a success message.

This makes the app act like a live form that builds your expense database in real time.

4. Date Handling and Filtering
The app reads the expense date and intelligently converts it to datetime format.

It can handle inconsistencies in date formats (like YYYY-MM-DD vs YYYY-MM-DD HH:MM:SS) by using a flexible date parser.

The sidebar includes a month filter so the user can view data specific to any month.

5. Expense Table View
Once a month is selected, a table shows all expenses made in that month.

This table is sorted in reverse chronological order, meaning the most recent expenses appear at the top.

Users can scroll and inspect individual entries.

6. Monthly Summary Visualization
The app calculates the total amount spent in the selected month.

It generates a pie chart to visually represent the spending across different categories (e.g., how much was spent on food vs rent).

This visual representation helps users quickly understand where their money is going.

7. Downloadable Reports
The sidebar includes a Download CSV button.

Users can export their entire expense log as a CSV file for use in Excel or other tools.

This ensures portability and offline access to data.

⚙️ Technical Highlights
Streamlit handles the UI and interactivity.

Pandas is used for:

Reading/writing CSV files

Manipulating dates

Grouping data for analysis

Matplotlib is used to generate pie charts from category-wise spending.

The app uses os to ensure the required data/ directory exists.

🔒 Data Persistence
One key strength of this app is that it stores data locally. Once an expense is added, it remains saved even after closing the browser or restarting the app — because everything is stored in a CSV file.

🧩 Extendability
This app is a strong foundation and can be extended with:

Income tracking

Editable/deletable entries

Monthly budgeting limits and alerts

Bar charts for trends across months

User login and multi-user support

