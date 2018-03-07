from flask import Flask

app = Flask(__name__)



# CRUD Application so 4 routes per entity 
############################# RESTAURANTS ######################################

# Create
@app.route('/restaurants/new/')
def add_restaurant():
    """Create a new restaurant"""


# Read (Home Page)
@app.route('/')
@app.route('/restaurants/')
def restaurants():
    """Display list of all restaurants"""


# Update
@app.route('/restaurants/<int:restaurant_id>/edit/')
def edit_restaurant(restaurant_id):
    """Edit information of a particular restaurant"""


# Delete
@app.route('/restaurants/<int:restaurant_id>/delete/')
def delete_restaurant(restaurant_id):
    """Remove a particular restaurant"""


############################# MENU ITEMS #######################################

# Create
@app.route('/restaurants/<int:restaurant_id>/menu_items/new/')
def add_menu_item():
    """Create a new menu_item for particular restaurant"""


# Read
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu_items/')
def restaurant_menu(restaurant_id):
    """Display all menu items of particular restaurant"""


# Update
@app.route('/restaurants/<int:restaurant_id>/<int:item_id>/edit/')
def edit_menu_item(restaurant_id, item_id):
    """Edit information of a particular item on the menu"""


# Delete
@app.route('/restaurants/<int:restaurant_id>/<int:item_id>/delete/')
def delete_menu_item(restaurant_id, item_id):
    """Remove a particular item from the menu"""



################################################################################

if __name__ == '__main__':
    app.run()
    app.debug = True