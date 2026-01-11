# CB 1st Financial Calculator

# define function save_goal():
    # get total saving goal from user
    # ask user if they are depositing weekly or monthly
    # get the deposit amount from user
    # time_units = saving_goal/deposit_amount
    # if user said weekly:
        # print(f"It will take {time_units} week(s) to save up ${saving_goal} depositing ${deposit amount} a week.")
     # if user said monthly:
        # print(f"It will take {time_units} months(s) to save up ${saving_goal} depositing ${deposit amount} a month.")

# define function compound_interest():
    # get starting amount from user
    # get interest rate from user
    # get amount of time spent collecting (years)
    # define function calc_total()
        # for i in range(years):
            # nonlocal starting amount
            # nonlocal interest rate
            # interest = starting amount * interest rate
            # starting amount += interest
    # calc_total()
    # return starting amount

# define function budget_allocator():
    # dictionary for storing budget items and allocation
    # list for storing percentages for allocation
    # ask user for total monthly income
    # while True:
        # ask user for budget item (type exit to continue)
        # add budget item to dictionary with value of 0
        # if exit, then break
    # for i in budget_dictionary:
        # ask what percentage of the budget user wants to give to each item
        # put percentage in allocation_list (same index as the dictionary item it is connected too)
        # automatically end function if sum of allocation_list is 100 (all of the budget is allocated)
    # define function calc_budget():
        # nonlocal budget_dictionary
        # nonlocal allocation_list
        # nonlocal monthly_income
        # list for storing money amounts
        # for i in range(budget_dictionary):
            # value = monthly_income * (allocation_list(i)/100)
            # money_list.append(value)
        # return money_list
    # money_list = calc_budget()
    # for i in range(money_list):
        # budget_dictionary(i) = money_list(i)
    # print("Final Budget")
        # for item,value in budget_dictionary.keys():
            # print(f"{item}: ${value})

# define function sale_price():
    # get the original item price
    # get discount amount
    # discount_amount = discount_amount / 100
    # final_price = original_price - (original_price * discount_amount)
    # return final_price


# define function tip_calculator():
    # get total of meal price from user
    # get how much they want to tip (percent)
    # tip_percent = tip_percent/100
    # tip_amount = tip_percent * total
    # final_price = tip_amount + meal_total
    # return meal_total, final_price, tip_amount


# define user_interface():
    # while True:
        # ask user what function they want to use
        # call that function
        # ask user if they want to continue
        # if user wants to continue:
            # continue
        # else:
            # break
functions = ["Calcuate a saving goal","Calcuate compounded interest","Calculate your monthly budget","Calcute sale price for an item","Calculate a tip"]
def save_goal():
    while True:
        saving_goal = input("How much money do you want to save? Do not include the currency sign in your answer.\n")
        if saving_goal.isnumeric() == False:
            print("Invalid answer")
            continue
        else:
            saving_goal = float(saving_goal)
            break
    while True:
        week_month = input("Are you depositing weekly or monthly? Enter number for answer. \n1. Weekly\n2. Monthly\n")
        if week_month != "1" and week_month != "2":
            print("Invalid answer")
            continue
        else:
            break
    while True:
        deposit_amount = input("How much are you depositing every week/month?\n")
        if deposit_amount.isnumeric() == False:
            print("Invalid answer")
            continue
        else:
            deposit_amount = float(deposit_amount)
            break
    saving_goal = round(saving_goal,3)
    deposit_amount = round(deposit_amount,3)
    time_units = saving_goal/deposit_amount
    time_units = round(time_units,1)
    if week_month == "1":
        print(f"It will take {time_units} week(s) to save ${saving_goal} if you are depositing ${deposit_amount} per week.")
    else:
        print(f"It will take {time_units} month(s) to save ${saving_goal} if you are depositing ${deposit_amount} per month.")

def compound_interest():
    while True:
        starting_value = input("How much money are you starting with? Do not put currency sign into your answer.\n")
        if starting_value.isnumeric == False:
            print("Invalid answer")
            continue
        else:
            starting_value = float(starting_value)
            break
    while True:
        interest_rate = input("What is the interest rate? Do not enter the percent as a decimal. I.E: 5% would be entered as 5.\n")
        if interest_rate.isnumeric() == False:
            print("Invalid answer")
            continue
        else:
            interest_rate = float(interest_rate)
            interest_rate = interest_rate/100
            break
    while True:
        years_compounding = input("How many years will your money spend compounding?\n")
        if years_compounding.isnumeric() == False:
            print("Invalid answer")
            continue
        else:
            years_compounding = int(years_compounding)
            break
    # this inner function calculates the final amount of money in the account after it has been compounded.
    def compound_total():
        nonlocal starting_value
        nonlocal interest_rate
        nonlocal years_compounding
        final_value = starting_value
        for i in range(years_compounding):
            final_value *= (1 + interest_rate)
        return final_value
    final_value = compound_total()
    final_value = round(final_value, 2)
    print(f"Starting value: ${starting_value}\n Interest Rate: {interest_rate * 100}%\n Years spent Compounding: {years_compounding}\n Final Value: ${final_value}")

def budget_calc():
    budget_dictionary = {}
    allocations = []
    percent_total = 0
    while True:
        monthly_income = input("What is your monthly income? Do not include the currency sign.\n")
        if monthly_income.isnumeric() == False:
            print("invalid answer")
            continue
        else:
            monthly_income = float(monthly_income)
            monthly_income = round(monthly_income,2)
            break
    while True:
        budget_item = input("Enter a budget item, or type 'continue' to continue on to the next step.\n").strip().capitalize()
        if budget_item == "Continue":
            break
        elif budget_item in budget_dictionary:
            print("You have already entered that item.")
            continue
        else:
            budget_dictionary[budget_item] = 0
            continue
    for i in budget_dictionary.keys():
        allocation = input(f"What percent of your budget do you want to allocate to {i}? Do not include the percent sign.\n")
        if allocation.isnumeric() == False:
            print("invalid answer")
        elif percent_total + float(allocation) > 100:
            print("Invalid answer; not enough money to allocate")
        else:
            allocation = float(allocation)
            allocation = round(allocation,2)
            percent_total += allocation
            allocations.append(allocation)
    # this inner function calculates how much money will be allocated to each budget item, and then stes the value of the buget item in the dictionary to that allocated amount of money.
    def calc_budget():
        nonlocal budget_dictionary
        nonlocal allocations
        nonlocal monthly_income
        for index,item in enumerate(budget_dictionary):
            money = monthly_income * (allocations[index]/100)
            budget_dictionary[item] = money
    calc_budget()
    for key,value in budget_dictionary.items():
        print(f"{key}: ${value}")

def sale_price():
    while True:
        og_price = input("What is the orginal price of the item you are buying?\n")
        if og_price.isnumeric() == False:
            print("Invalid answer")
            continue
        else:
            og_price = float(og_price)
            og_price = round(og_price,2)
            break
    while True:
        discount = input("What is the discount on the item? Enter percent not as a decimal, but as a regular number. I.E: 5% would be entered as 5\n")
        if discount.isnumeric() == False:
            print("Invalid answer")
            continue
        else:   
            discount = float(discount)
            discount = discount/100
            break
    final_price = og_price - (og_price * discount)
    print(f"Original Price: ${og_price}\nDiscount: {discount * 100}%\nFinal Price: ${final_price}")

def tip_calculator():
    while True:
        meal_cost = input("How much did the original meal cost? Do not include the currency sign.\n")
        if meal_cost.isnumeric() == False:
            print("Invalid answer")
        else:
            meal_cost = float(meal_cost)
            meal_cost = round(meal_cost,2)
            break
    while True:
        tip_percentage = input("What percent do you want to tip? Do not include the perce tage sign.\n")
        if tip_percentage.isnumeric() == False:
            print("Invalid answer")
            continue
        else:
            tip_percentage = float(tip_percentage)
            tip_percentage = round(tip_percentage,1)
            tip_percentage = tip_percentage/100
            break

    tip = meal_cost * tip_percentage
    final_cost = meal_cost + tip
    print(f"Orignal Cost: ${meal_cost}\n Tip: ${tip}\n Final Cost: ${final_cost}")

def user_interface():
    while True:
        print("This is a financial calculator! What would you like to do?")
        function_number = 0
        for i in functions:
            function_number += 1
            print(f"{str(function_number)}. {i}")
        while True:
            choice = input("Enter number of function you want to perform. I.E, to calculate a saving goal, enter 1.\n")
            match choice:
                case "1":
                    save_goal()
                    break
                case "2":
                    compound_interest()
                    break
                case "3":
                    budget_calc()
                    break
                case "4":
                    sale_price()
                    break
                case "5":
                    tip_calculator()
                    break
                case _:
                    print("Invalid answer")
                    continue
        repeat = input("Do you want to continue using the calculator? Yes/No\n").strip().capitalize()
        if repeat == "Yes":
            continue
        else:
            print("Goodbye!")
            break

user_interface()
