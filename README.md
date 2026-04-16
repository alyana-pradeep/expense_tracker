# 💰 Expense Tracker (Python + MySQL)

## 📌 Project Overview

This project is a simple Expense Tracker developed using Python and MySQL. It helps users track their daily, monthly, and yearly expenses and monitor spending limits.

The project is based on a real-world use case to manage expenses efficiently.

---

## 🚀 Features

* Add daily expenses with category and date
* View total expenses (daily, monthly, yearly)
* Set and update spending limits
* Get alerts when limits are exceeded
* Data stored in MySQL database
* Uses SQL queries like SUM, GROUP BY

---

## 🛠️ Technologies Used

* Python
* MySQL
* mysql-connector-python

---

## 📂 Database Structure

### Table: expenses

* id (Primary Key)
* amount
* category
* date

### Table: limits

* daily_limit
* monthly_limit
* yearly_limit

---

## ⚙️ How It Works

1. User enters expense details
2. Data is stored in MySQL database
3. System calculates totals using SQL queries
4. Compares with predefined limits
5. Displays summary and alerts

---

## ▶️ How to Run

1. Install dependencies:

```
pip install mysql-connector-python
```

2. Setup MySQL database:

* Create database
* Create required tables

3. Run the program:

```
python app.py
```

---

## 📊 Example Output

* Daily: 250 / 200
* Monthly: 5000 / 6000
* Yearly: 30000 / 72000
* ⚠️ Daily limit exceeded

---

## 🎯 Key Concepts Used

* CRUD Operations
* SQL Aggregate Functions (SUM)
* Date Functions (MONTH, YEAR)
* Python + MySQL Integration

---

## 💡 Future Improvements

* Add graphical dashboard
* Export data to Excel
* Add user authentication

---

## 👨‍💻 Author

Alyana Pradeep Kumar
