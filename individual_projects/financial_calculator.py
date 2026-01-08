# CB 1st Financial Calculator

# define function save_goal():
    # get total saving goal from user
    # get weekly deposit from user (the time will be calculated in weeks, but will be turned into months if it is big enough)
    # return total saving goal/weekly deposit

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

# define function sale_price()

# define function tip_calculator()

