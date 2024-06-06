def ask_name():
    name = input("What is your name? ").capitalize()
    return name

def calculate_expenses(expenses): 
    expenses_list = [float(expense) for expense in expenses.split(",")]
    sum_total = sum(expenses_list)
    return sum_total

def calculate_savings(income, expenses):
    income = float(income)
    expenses = float(expenses)
    savings = income - expenses
    return f"Total savings: ${savings:.2f}"

def simple_interest(principal, rate, time):
    principal = float(principal)
    rate = float(rate)
    time = float(time)
    interest = principal * (rate / 100) * time 
    return f"Simple interest: ${interest:.2f}"

def compound_interest(principal, rate, times_compounded, years):
    principal = float(principal)
    rate = float(rate)
    times_compounded = float(times_compounded)
    years = float(years)
    interest = principal * (1 + (rate / times_compounded)) ** (times_compounded * years)
    return f"Compound interest: ${interest:.2f}"

command = input("Which command would you like to run? Options: expenses, ask_name, calculate_savings, simple_interest, compound_interest: ")

if command == "expenses":
    exp = input("List your expenses inside [] comma-separated list: ")
    total_expenses = calculate_expenses(exp)
    print(f"Total expenses: ${total_expenses:.2f}")
elif command == "ask_name":
    name = ask_name()
    print(f"Hello, {name}!")
elif command == "calculate_savings":
    income = input("What is your income? ")
    expenses = input("What are your expenses? ")
    savings = calculate_savings(income, expenses)
    print(savings)
elif command == "simple_interest":
    principal = input("Principal? ")
    rate = input("Rate? ")
    time = input("Time? ")
    interest = simple_interest(principal, rate, time)
    print(interest)
elif command == "compound_interest":
    principal = input("Principal? ")
    rate = input("Rate? ")
    times_compounded = input("Times compounded? ")
    years = input("Years? ")
    interest = compound_interest(principal, rate, times_compounded, years)
    print(interest)
else: 
    print("Unknown command")
