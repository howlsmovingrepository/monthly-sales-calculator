import csv
import sys

FILENAME = "monthly_sales.csv"

def read():
    sales = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            sales.append(row)
    return sales

def write(sales):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sales)

def view_yearly(sales):
    sum = 0
    for months in sales:
        sum += int(months[1])
    print("Yearly total: " + str(sum) )
    average = sum/len(sales)
    print("Monthly average: " + str(round(average,2)) )
  

def view_monthly(sales):
    for months in sales:
        print(months[0] + " - " + months[1])


##############
def edit(sales):
    while True:
        month = input("Three-letter Month:")
        month = month.title()
        if not any(month in sublist for sublist in sales):
            print("Please enter 3-letter abbreviation for the month.")
            continue
        break

    while True:
        try:
            amount = int(input("Sales Amount: "))
        except ValueError:
            print("Please enter an integer.")
            continue
      
        if (amount <= 0):
            print("Please enter amount greater than zero.")
            continue
        break
    for months in sales:
        if months[0] == month:
            months[1] = amount
            write(sales)
            print("Sales amount for " + month + " was modified")
################


def display_menu():
    print("Monthly Sales program")
    print()
    print("COMMAND MENU")
    print("monthly - View monthly sales")
    print("yearly - View yearly summary")
    print("edit -  Edit sales for a month")
    print("exit - Exit program")
    print()

def main():
    display_menu()
    sales = read()
    while True:
        command = input("Command: ")
        if command == "monthly":
            view_monthly(sales)
        elif command == "yearly":
            view_yearly(sales)
        elif command == "edit":
            edit(sales)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Calc-you-later!")

if __name__ == "__main__":
    main()
