from tkinter import *
from Matthew_Crouse_final_project_CLASS import Item
from Matthew_Crouse_final_project_CLASS import SmartCart
from functools import partial
import random, string #used in random receipt no function

class MyFrame(Frame):
    def __init__(self, root):
        '''Constructor method'''
        Frame.__init__(self, root) #Frame class initialization
        self.init_container() #initialize all widget containers
        self.cart = SmartCart() #initialize SmartCart dict object - key = Item object item selected, value = quantity
        self.welcome() #start the application
        self.data = StringVar(self, 'Subtotal: $0.00') #Associated with subtotal label


    def init_container(self):
        '''Initialize widget containers'''
        self.states = [] #holds state if selected/not i-th list item holds selection for i-th item

    def clear_frame(self):
        '''Clears the previous frame'''
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        '''Exits the program'''
        root.destroy()

    def welcome(self):
        '''Welcome window - refer spec file for details'''
        self.clear_frame()
        Label(self, text = '****Welcome to AppsCart!****', background="gray70").pack(side = TOP)
        #your code here
        #Select by category: Button – start ordering, command = shop_by_apps_category
        Button(self, text = 'Select by Category', command = self.shop_by_apps_category).pack()
        #Select by rating: Button - start ordering, command = shop_by_apps_ratings
        Button(self, text = 'Select by Rating', command = self.shop_by_apps_ratings).pack()
        #Exit Application: Button – exit the program, command = exit_application
        Button(self, text = 'Exit Application', command = self.exit_application).pack()

    def shop_by_apps_category(self):
        '''2. Widget to display different category of apps - refer spec file for details'''
        self.clear_frame()
        self.init_container()
        categories = ['Games', 'Productivity', 'Weather', 'Shopping', 'Utilities', 'Finance', \
                      'Travel', 'Music', 'Health & Fitness']
        #your code here
        Label(self, text = 'Choose Apps Category', background="gray70").pack(side = TOP) 
        #Choose Apps Category: label
        #Iterate over each category in categories list
        #create a button for each category, set text = category and
        #command= partial(self.start,Item.category_dict[category])
        #partial is a special method to pass an argument during button command
        #layout button
        for category in categories:
            Button(self, text = category, command = partial(self.start, Item.category_dict[category])).pack()

        #Go Back: Button – command = welcome
        #layout manager for all the widgets
        Button(self, text = 'Go Back', command = self.welcome).pack()

    def shop_by_apps_ratings(self):
        self.clear_frame()
        self.init_container()
        ratings=[1, 2, 3, 4, 5]
        #yourcodehere
        Label(self, text = 'Choose Apps Rating', background="gray70").pack(side = TOP)
        for rating in ratings:
            Button(self, text = (rating,'--',rating*'*'), command = partial(self.start, Item.rating_dict[rating])).pack()

        Button(self, text = 'Go Back', command = self.welcome).pack()

    def start(self, current_items):
        ''''3. Start ordering from selected category,
        list passed by command will be used as current_items'''
        self.clear_frame()
        self.init_container()

        #creating widgets for items using a for loop
        #iterative over each item of current apps and
        #create that many checkbutton, price, ID, rating and category label
        row = 0#########
        for item in current_items:
            self.states.append(IntVar()) #keeps track if an item is selected
            checkbutton = Checkbutton(self, text=item.get_name(), variable=self.states[row])#create check buttons
            checkbutton.grid(row = row, column = 0)

            #your code here
            #create and layout a price label, set text to item.get_price()
            price_label = Label(self, text = '$' + item.get_price())
            price_label.grid(row = row, column = 1)
            #create and layout id label and set text to item.get_id() method
            id_label = Label(self, text = item.get_id())
            id_label.grid(row = row, column = 2)
            #similary create and layout rating and category label
            rating_label = Label(self, text = item.get_rating())
            rating_label.grid(row = row, column = 3)

            category_label = Label(self, text = item.get_category())
            category_label.grid(row = row, column = 4)

            row+=1


        #create and layout subtotal lable, set textvaribale = self.data so it changes
        self.subtotal_label = Label(self, textvariable = self.data, background="gray70") #set to self.data
        self.subtotal_label.grid(row = row, column = 0)
        #create and layout select by categories: button, command = shop_by_apps_category
        self.shop_by_apps_category_button = Button(self, text = 'Select by Categories', command = self.shop_by_apps_category)
        self.shop_by_apps_category_button.grid(row = row, column = 1)
        #create and layout select by ratings: button, command = shop_by_apps_ratings
        self.ratings_button = Button(self, text = 'Select by Ratings', command= self.shop_by_apps_ratings)
        self.ratings_button.grid(row = row, column = 3)
        #create and layout add_to_cart_button, command = partial(self.add_to_cart, current_items)
        self.add_to_cart_button = Button(self, text = 'Add to Cart', command= partial(self.add_to_cart, current_items))
        self.add_to_cart_button.grid(row = row+1, column = 2)
        #create and layout button: checkout, command = self.checkout
        self.checkout_button = Button(self, text = 'Checkout', command= self.checkout)
        self.checkout_button.grid(row = row+2, column = 2)

    def add_to_cart(self, current_items): #####
        self.current_subtotal = 0
        '''3. Added to cart, displays subtotal - see spec file for details layout'''
        for i in range(len(current_items)):
            #your code here
            #get() the value of i-th item of self.states -> returns 1 if selected otherwise 0
            #if item is selected:
            #add app item object to self.cart list

            if (self.states[i].get() == 1):
                if not(current_items[i] in self.cart):
                    self.cart.append(current_items[i])
                self.current_subtotal = self.cart.subtotal()
                
            else:
                if (current_items[i] in self.cart):
                    self.cart.remove(current_items[i])
                self.current_subtotal = self.cart.subtotal()
             

        self.data.set('Subtotal: ${:.2f}'.format(self.current_subtotal))

        #your code here
        #set the StringVar to be the current subtotal (SmartCart object self.cart has subtotal method)
        #refer to class file

    def get_receipt_number(self):
        '''Generate random receipt number'''
        return  ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=10))

    def checkout(self):
        '''4. Check out window '''
        self.clear_frame()
        #your code here to create and layout following widgets:
        #refer to receipt frame
        #    Your e-order: Label
        #    e-Order Number: Label - Randomly generated by program - text = get_receipt_number()
        #	Name Price Rating Category: Header Label
        #    Iterate over apps items from cart list
        #	   Genrate labels of 	name, price, rating, category and layout
        #	Subtotal: Label - get self.cart subtotal - new label
        #	Tax: Label - 4.3%
        #	Total: Label - subtotal + tax
        #	‘Thank you’ message: Label
        #	Exit application: Button – exit the program- command = exit_application

        Label(self, text = 'Your e-order:', background="gray70").pack(side = TOP)
        Label(self, text = ('e-order Number: '+self.get_receipt_number())).pack(side = TOP)
        Label(self, text = '--------------------------------------------').pack(side = TOP)
        Label(self, text = ('\tName\t\tPrice\tRating\tGenre\t')).pack(side = TOP)
        for item in self.cart:
            Label(self, text = (item.get_name() + '\t' + item.get_price() + '\t' + item.get_rating() +
                                '\t' + item.get_category())).pack(side = TOP)
        Label(self, text = ('Subtotal: ${:.2f}'.format(float(self.cart.subtotal())))).pack(side = TOP)
        Label(self, text = 'Tax: 4.30%').pack(side = TOP)
        Label(self, text = 'Total: ${:.2f}'.format(float(self.cart.subtotal())*0.043 + self.cart.subtotal())).pack(side = TOP)
        Label(self, text = ('Thanks for using Apps Cart!')).pack(side = TOP)
        Label(self, text = '--------------------------------------------').pack(side = TOP)
        Button(self, text = 'Exit Application', command = self.exit_application).pack()

#main driver code
#your code here
#create root window
root = Tk()
root.title("Apps Cart") #set window title
#your code here
#create a myframe object and layout
#call mainloop
frame = MyFrame(root)
frame.grid()
root.mainloop()
