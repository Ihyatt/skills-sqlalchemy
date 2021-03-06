"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# # Get the brand with the **id** of 8.
# Brand.query.get(8)

# # Get all models with the **name** Corvette and the **brand_name** Chevrolet.
# Model.query.filter(Model.name =='Corvette', Model.brand_name == 'Chevrolet').all()

# # Get all models that are older than 1960.
# Model.query.filter(Model.year > 1960).all()

# # Get all brands that were founded after 1920.
# Brand.query.filter(Brand.founded > 1920).all()

# # Get all models with names that begin with "Cor".
# Model.query.filter(Model.name.like('Cor%') ).all()

# # Get all brands that were founded in 1903 and that are not yet discontinued.
# Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# # Get all brands that are either 1) discontinued (at any time) or 2) founded 
# # before 1950.
# Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# # Get any model whose brand_name is not Chevrolet.
# Model.query.filter(Model.brand_name != 'Chevrolet').first()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_by_year = db.session.query(Model.name, Model.brand_name, Model.year, Brand.headquarters).join(Brand).all()

    for model, brand, model_year, headquarters in model_by_year:
    	if model_year == int(year):
    		print model + "-" +  brand + "-" + headquarters

get_model_info('1960') #test for code

def get_brands_summary(brand):
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands_summary = db.session.query(Model.brand_name, Model.name).filter(Model.brand_name == brand).all()

    for brand, name in brands_summary:
    	print brand + "-" + name
    


get_brands_summary("Hillman") 

    

    

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
""" Perhaps there may be an error in my code, but what is returned is: 
	<flask_sqlalchemy.BaseQuery object at 0x1027b3d90>

	However, once I typed in Brand.query.filter_by(name='Ford').first(), the following was returned: 
	<Brand id=1 name=Ford founded=1903 headquarters=Dearborn, MI discontinued=None>

	To my knowledge, what is returned is a base query object that points to the location of the object."""


# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

"""An association table is a mapping table that holds the foriegn keys that connects both tables, and models the relationship between the aforementioned tables.
   An association table's relationship is a many to many relationship. An example that really helped in my understanding of this is that of Dark Crystal. For ex. a skekski can 
   feed off of many prisoners, and a prisoner can be fed off of many skeksis. """ 
# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
	name_search = Brand.query.filter(Brand.name.like("%" + mystr + "%") ).all()
	print name_search

search_brands_by_name("or")


def get_models_between(start_year, end_year):
	between_start_and_end = Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
	print between_start_and_end

get_models_between(1900, 1910)

    
