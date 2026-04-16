import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassowrd",
    database="expense_db"
)

cursor = conn.cursor()
def get_limits():
    cursor.execute("SELECT daily_limit, monthly_limit, yearly_limit FROM limits_table WHERE id=1")
    return cursor.fetchone()


def add_profit():
    n=int(input("enter number of profit entries:"))
    for i in range(n):
        Income=int(input("enter today's profit:"))
        sources=input("enter profit sources:")
        date=datetime.now().date()
        cursor.execute("INSERT INTO profits (Income,sources,date) VALUES (%s,%s,%s)",
                    (Income,sources,date))
        conn.commit()

def add_expense():
    amount = int(input("Enter amount: "))
    category = input("Enter category: ")
    today = datetime.now().date()

    # Insert expense
    cursor.execute("INSERT INTO expenses (amount, category, date) VALUES (%s, %s, %s)",
                   (amount, category, today))
    conn.commit()

    print("✅ Expense Added!")

    check_limits(today)

def check_limits(today):
    daily_limit, monthly_limit, yearly_limit = get_limits()

    # Daily total
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE date=%s", (today,))
    daily_total = cursor.fetchone()[0] or 0

    # Monthly total
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE MONTH(date)=MONTH(%s) AND YEAR(date)=YEAR(%s)", (today, today))
    monthly_total = cursor.fetchone()[0] or 0

    # Yearly total
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE YEAR(date)=YEAR(%s)", (today,))
    yearly_total = cursor.fetchone()[0] or 0

    print(f"\n📊 Daily: {daily_total}/{daily_limit}")
    print(f"📊 Monthly: {monthly_total}/{monthly_limit}")
    print(f"📊 Yearly: {yearly_total}/{yearly_limit}")

    # Alerts
    if daily_total > daily_limit:
        print("⚠️ Daily limit exceeded!")
    if monthly_total > monthly_limit:
        print("⚠️ Monthly limit exceeded!")
    if yearly_total > yearly_limit:
        print("⚠️ Yearly limit exceeded!")


def profit_summary():
    today = datetime.now().date()

    cursor.execute("SELECT SUM(Income) FROM profits")
    total_profit = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(Income) FROM profits WHERE MONTH(date)=MONTH(%s)", (today,))
    monthly_profit = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(Income) FROM profits WHERE YEAR(date)=YEAR(%s)", (today,))
    yearly_profit = cursor.fetchone()[0] or 0

    print(f"\n💰 Total Profit: {total_profit}")
    print(f"📅 Monthly Profit: {monthly_profit}")
    print(f"📆 Yearly Profit: {yearly_profit}\n")

def view_summary():
    today = datetime.now().date()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM expenses WHERE MONTH(date)=MONTH(%s)", (today,))
    monthly = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM expenses WHERE YEAR(date)=YEAR(%s)", (today,))
    yearly = cursor.fetchone()[0] or 0

    print(f"\n💰 Total Spending: {total}")
    print(f"📅 Monthly Spending: {monthly}")
    print(f"📆 Yearly Spending: {yearly}\n")

def weekly_report():
    cursor.execute("""
        SELECT WEEK(date), SUM(amount)
        FROM expenses
        GROUP BY WEEK(date)
    """)
    result = cursor.fetchall()

    print("\n📊 Weekly Spending:")
    for week, total in result:
        print(f"Week {week}: {total}")

def update_limits():
    d = int(input("Enter new daily limit: "))
    m = int(input("Enter new monthly limit: "))
    y = int(input("Enter new yearly limit: "))

    cursor.execute("UPDATE limits_table SET daily_limit=%s, monthly_limit=%s, yearly_limit=%s WHERE id=1",
                   (d, m, y))
    conn.commit()

    print("✅ Limits Updated!")

# ---------- MAIN MENU ---------- #

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Profit")
    print("2. Profit summary")
    print("3. Add Expense")
    print("4. View Summary")
    print("5. Weekly Report")
    print("6. Update Limits")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_profit()
    elif choice == 2: 
        profit_summary()
    elif choice == 3:
        add_expense()
    elif choice == 4:
        view_summary()
    elif choice == 5:
        weekly_report()
    elif choice == 6:
        update_limits()
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

conn.close()
