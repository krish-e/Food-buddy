from tabulate import tabulate
import datetime
import sys
import csv


try:
    open("Zomato-mini.csv")

except FileNotFoundError:
    sys.exit("Could not read Zomato-mini.csv")



def main():

    restaurants = []
    # Read file to load all restaurants with necessary features
    with open("Zomato-mini.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:
            restaurants.append({"Name": row["name"], "Rating": row["rate"], "Phone": row["phone"], "Cuisines": row["cuisines"].lower().split(', '), "Cost for 2": row["budget(for_two)"].strip()})

    now = datetime.datetime.now()
    current_hour = int(now.time().hour)
    print("\n", greet_user(current_hour), " Hi! I'm Food Buddy.", sep="")
    course = get_course(current_hour)

    # Acquire available cuisine from data set (without duplicates)
    available_cuisines = avail_cuisines(restaurants)

    # Filter restaurants based on the user slected cuisine and preferred rating
    res_cus_and_rev, cuisine, rating = get_cuisine_and_rating(restaurants, available_cuisines)


    # Check whether the user opt to have a budget
    budget_opt = input("\nAre you on budget? ").lower()
    is_budget = False
    if budget_opt == "y" or budget_opt == "yes" or budget_opt == "yeah":
        while True:
            try:
                budget = int(input("\nWhat's your budget?(in INR) ₹."))
                break
            except ValueError:
                print("Enter your budget in numbers!")
                pass
        is_budget = True

        # Filter restaurants based on the user's budget
        res_cus_rev_bud = budgetter(res_cus_and_rev, budget)
    else:
        res_cus_rev_bud = res_cus_and_rev


    # Check if the final list has any restaurant to print
    if len(res_cus_rev_bud) > 0:

        print(f"\nI got {len(res_cus_rev_bud)} '{cuisine}' restaurant(s) for your {course}.")

        list_res_opt = input("\nShall I tell them all now? ").lower()
        if list_res_opt == 'y' or list_res_opt == 'yes' or list_res_opt == 'yeah' or list_res_opt == 'okay' or list_res_opt == 'ok':

            if is_budget:
                print(f"\n'{cuisine.title()}' restaurants with {rating} & above ratings within ₹.{budget} budget:")
            else:
                print(f"\n'{cuisine.title()}' restaurants with {rating} & above ratings without any budget limitations:")

            print(print_in_table(res_cus_rev_bud))
            print("\nYou may now call the restaurant to order food or reserve table. Thank you!\n")
        else:
            sys.exit("\nOKAY Bye!\n")
    else:
        sys.exit("\n***Sorry! No restaurants available to your preference.***\n")



# Return Greetings based on the current time
def greet_user(current_hour):

    if 1 <= current_hour <= 12:
        return ("\nGood Morning!")
    elif 12 <= current_hour <= 15:
        return ("\nGood Afternoon!")
    elif 16 <= current_hour < 24:
        return ("\nGood Evening!")


# Return the name of the meal based on the current time
def get_course(current_hour):

    if 7 <= current_hour <= 11:
        return "breakfast"
    elif 12 <= current_hour <= 16:
        return "lunch"
    elif 17 <= current_hour < 24:
        return "dinner"


# Fetch and return all the cuisines in the restaurants.csv without duplicates
def avail_cuisines(restaurants):
    avail_cuisines = set()
    for key in restaurants:
        for cuisine in key["Cuisines"]:
            avail_cuisines.add(cuisine)

    count = 1
    print("\nAvailable Cuisines: ")

    for cuisine in sorted(avail_cuisines):
        print(str(count)+'. '+cuisine.title())

        count += 1
        if count == len(avail_cuisines)+1:
            print("\n-----End of Cuisines-----")
        if count %10 == 1 and count != 1:
            page = input("\nProceed to see next page? ").lower()
            if page == "ok" or page == "okay" or page == "yeah" or page == "y" or page == "yes":
                continue
            else:
                break
    return avail_cuisines



# Get user's preferred cuisine and minimum rating
def get_cuisine_and_rating(restaurants, available_cuisines):
    res_cus_and_rev = []

    while True:
        try:
            cuisine = input("\nSo, which cuisine you are in the mood for? ").strip().lower()
            if cuisine.isnumeric() or cuisine not in available_cuisines:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please enter a valid cuisine's name!(not a number)\n")
            continue

    while True:
        try:
            rating = float(input("\nEnter your preferred minimum rating(out of 5): "))
            if rating > 5:
                raise ValueError
            else:
                break
        except ValueError:
            print("\nPlease enter your preferred minimum rating in numbers.\n")
            continue

    for restaurant in restaurants:
        if cuisine in restaurant["Cuisines"] and float(restaurant["Rating"].rstrip("/5")) >= rating:
            res_cus_and_rev.append({"Name": restaurant["Name"], "Rating": restaurant["Rating"], "Phone": restaurant["Phone"], "Cuisines": restaurant["Cuisines"], "Cost for 2": restaurant["Cost for 2"]})

    return res_cus_and_rev, cuisine, rating



# Filter restaurants based on the user's budget
def budgetter(res_cus_and_rev, budget):
    res_cus_rev_bud = []

    for restaurant in res_cus_and_rev:
        if int(restaurant["Cost for 2"])/2 <= budget:
            res_cus_rev_bud.append({"Name": restaurant["Name"], "Rating": restaurant["Rating"], "Phone": restaurant["Phone"], "Cuisines": restaurant["Cuisines"], "Cost for 2": restaurant["Cost for 2"]})

    return res_cus_rev_bud



# Print the filtered restaurants in table(grid) format
def print_in_table(res_cus_rev_bud):
    headers = res_cus_rev_bud[0].keys()
    rows = [restaurant.values() for restaurant in res_cus_rev_bud]
    return tabulate(rows, headers, tablefmt="grid")



if __name__ == '__main__':
    main()