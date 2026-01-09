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

def save_goal():
    while True:
        saving_goal = input("How much money do you want to save? Do not include the currency sign in your answer.")
        if saving_goal.isnumeric() == False:
            print("Invalid answer")
            continue
        else:
            saving_goal = float(saving_goal)
            break
    while True:
        week_month = input("Are you depositing weekly or monthly? Enter number for answer. \n1. Weekly\n2. Monthly")
        if week_month != "1" and week_month != "2":
            print("Invalid answer")
            continue
        else:
            break
    while True:
        deposit_amount = input("How much are you depositing every week/month?")
        if deposit_amount.isnumeric() == False:
            print("Invalid answer")
            continue
        else:
            deposit_amount = float(deposit_amount)
            break
    saving_goal = round(saving_goal,2)
    deposit_amount = round(saving_goal,2)
    time_units = saving_goal/deposit_amount
    time_units = round(time_units,1)
    if week_month == "1":
        print(f"It will take {time_units} week(s) to save ${saving_goal} if you are depositing ${deposit_amount} per week.")
    else:
        print(f"It will take {time_units} month(s) to save ${saving_goal} if you are depositing ${deposit_amount} per month.")

def compound_interest():
    while True:
        starting_value = input("How much money are you starting with? Do not put currency sign into your answer.")
        if starting_value.isnumeric == False:
            print("Invalid answer")
            continue
        else:
            starting_value = float(starting_value)
            break
    while True:
        interest_rate = input("What is the interest rate? Do not enter the percent as a decimal. I.E: 5% would be entered as 5.")
        if interest_rate.isnumeric() == False:
            print("Invalid answer")
            continue
        else:
            interest_rate = float(interest_rate)
            interest_rate = interest_rate/100
            break
    while True:
        years_compounding = input("How many years will your money spend compounding?")
        if years_compounding.isnumeric() == False:
            print("Invalid answer")
            continue
        else:
            years_compounding = int(years_compounding)
            break
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
    pass

def sale_price():
    while True:
        og_price = input("What is the orginal price of the item you are buying?")
        discount = input("What is the discount on the item? Enter percent not as a decimal, but as a regular number. I.E: 5% would be entered as 5")
        discount = discount/100
        

def tip_calculator():
    pass
compound_interest()