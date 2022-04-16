# App-Store
This repository is an appstore created for my IT 209 final project.

# Purpose:
The purpose of this project was to demonstrate an acceptable
level of expertise with the fundamental procedural and object-oriented concepts and Graphical
User Interface (GUI) implementation techniques introduced and refined in the lectures and labs
throughout the course of the semester.

# Program Structure:
1. Program starts by reading from an input file containing an id, apps name, price, user
rating and category of each item. (code provided). The information are separated by
comma and saved in a .csv file.
2. Once read, an apps item will be created and saved to a dictionary ‘category_dict’ of
apps per category. The key will be the category like: Games/Productivity etc. and the
values will be the apps item object.
3. The program needs to create one more dictionary ‘ratings_dict’ where the apps will be
saved by ratings. Key will be ratings and the values in the dictionary will be the apps
item object. The ratings are: 1, 2, 3, 4 and 5. So if an apps has a rating of 4.5 then it will
be saved under key 4, if an apps has a ratings of 2.1 , then it will be saved under key 2.
4. A testing code is provided to check the class file. You need to comment the testing code
once done checking the class file.
5. The GUI file imports the class file and use the Item and SmartCart class information.
6. User has the option of ordering apps from different category or choose by apps ratings.
Once user selects a category, s/he will be directed to the list of apps available to
purchase for that category.
7. Each list, loads the items from the corresponding category dict. If user selects Games,
then all the game apps will be loaded from the category_dict[‘Games’] from the class
file
8. For each apps, there will be some information that will be displayed to user.
a. A check box to select the apps to purchase
b. A label to show the name of the item
c. A label to display the price
d. A label to display user ratings
e. A label to display category of the apps
9. Once user selects item(s), and hits add to cart button then a subtotal label will appear.
10. User can then have the option of choosing more apps/checkout.
11. Checkout shows apps purchased, break-down of each apps and their information, tax
and total.

# GUI Requirements:
1. Welcome screen: This screen will be the first screen to display. It will contain following
widgets:
a. Welcome message: Label
b. Select by category: Button – will take user to different categories. Figure 1, #2
c. Select by rating: Button – will take user to select different ratings from 1-5 Figure 2
#2
d. Exit Application: Button – exit the program
2. Choose Category: If user presses start by category then the program will display another
frame with different categories of apps (Figure -1 #2). This window has one button widget
for each category of apps. For example: in figure -1 #2 user selects Games and then the
program will display all the game apps. Go Back: Button – will take to step 1 again. Selecting
the category will take user to all the apps currently in the apps store. For example: Figure- 1
#3 shows all the games available with ratings >=4.0 and <5.0. This window contains the
following widgets:

a. Name of the apps: check button – user selects which apps they want to buy

b. Price of an apps: Label

c. id: Label -id of an item

d. User rating: label of the apps rating

e. Category: Category of the apps.

f. Select by category/rating: Buttons will take again to main menu (Figure-1, #1)

g. Add to Cart: Button – Add selected items to cart

i. Will display a current subtotal as label after selecting an app and pressing this
button (Figure-1, #4)

h. Checkout: Button – After adding to cart, user can directly go to checkout window
