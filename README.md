
# FOOD BUDDY!

## Table of Contents

1. [Description](#description)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Demo](#demo)


## Description

`Food Buddy` is a Python project that allows users to filter restaurants from a list of restaurants available in the CSV file - Zomato-mini.csv

The program will greet the user and depending on the current time, will refer to the meal like breakfast, lunch, or dinner.

Based on the data taken from the CSV, in the console, the user can filter the restaurants through command-line inputs based on their preferred
1. Cuisine
2. Rating
3. Budget

The user can be careless with their inputs as the exceptions are being handled(for the most part) in this project.

Ultimately, the program would display the restaurants' name, rating(out of 5), phone number, cuisines, and cost for 2 persons.

The program could be improved further with other preferences like multiple cuisines or dining/takeaway, etc., for which the data is already available in the CSV file.


### Project.py
The program has only one file - project.py within which it contains all the following functions to filter and find the restaurants based on the user input:

1. **greet_user()**:

    * Returns greetings based on the current time using datetime.now() passed from main()


2. **get_course()**:

    * Returns the name of the meal based on the current time using datetime.now() passed from main()


3. **avail_cuisines()**:

    * Fetches all the non-duplicate cuisines from the list of dictionaries which was imported from the `Zomato-mini.csv`
    * Also returns all the cuisines in the Zomato-mini.csv without duplicates


4. **get_cuisine_and_rating()**:

    * Gets the user's preferred cuisine by displaying all the non-duplicate cuisines acquired from the avail_cuisines().
    * Gets the user's minimum rating(out of 5) to filter the restaurants and appends the restaurants that satisfy the above preferences in a new list.
    * Returns the new list.


5. **budgetter()**:

    * Filters restaurants(new list from get_cuisine_and_rating()) based on the user's budget and appends the respective restaurants to a new list.
    * Returns the new list.


6. **print_in_table()**:

    * Prints the new list(from budgetter()) in table(grid) format



### Design Choice
I have added blank line(s) between one process and the other even within a function to make the code look spacious and more readable.


## Features

- Import restaurant data from a CSV file.
- Filter restaurants based on user's input for cuisine, rating, and budget
- An exclusive method for each to filter for each preference.
- Everything is done in the command-line interface.


## Requirements

- Python 3.6+
- Libraries listed in `requirements.txt` (install using `pip install -r requirements.txt`)
- The CSV file containing restaurant data - `Zomato-mini.csv`


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/krish-e/food-buddy.git

2. Navigate to the project directory:

    ```bash
    cd food-buddy

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt


## Usage

1. Ensure you have a CSV file containing restaurant data- `Zomato-mini.csv` in the project directory.

2. Run the project from the command line:

    ```bash
    python project.py

3. Follow the on-screen prompts to filter and search for restaurants to your preference.

4. The filtered results will be displayed on the console with the phone number to contact the restaurant to order food or reserve a table.


## Demo
![](project_example.gif)
