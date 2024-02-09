from flask import Blueprint, flash, redirect, render_template, request

# Internal imports
from rangers_shop.models import Product, Customer, Order, db
from rangers_shop.forms import ProductForm

#bInstantiate our blueprint class
                                        # Location of html files
site = Blueprint('site', __name__,template_folder= 'site_templates')


# Use our site blueprint object to create our routes
@site.route('/')
def shop():

    # Grab all of hte products in our database via query
    allprods = Product.query.all()
    allcustomers = Customer.query.all()
    allorders = Order.query.all()

    shop_stats = {
        'products': len(allprods),
        'customers': len(allcustomers),
        'sales': sum([order.order_total for order in allorders])
    }

# Looking inside site_templates folder fpr a file called shop.html to render
    return render_template('shop.html', shop=allprods, stats=shop_stats) 





@site.route('/shop/create', methods= ['GET', 'POST'])
def create():

    #instantiate our productform

    createform = ProductForm()

    if request.method == 'POST' and createform.validate_on_submit():
        #grab our data from our form
        name = createform.name.data
        image = createform.image.data
        description = createform.description.data
        price = createform.price.data
        quantity = createform.quantity.data 

        #instantiate that class as an object passing in our arguments to replace our parameters 
        
        product = Product(name, price, quantity, image, description)

        db.session.add(product) #adding our new instantiating object to our database
        db.session.commit()

        flash(f"You have successfully created product {name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("We were unable to process your request", category='warning')
        return redirect('/shop/create')
    

    return render_template('create.html', form=createform )


@site.route('/shop/update/<id>', methods=['GET', 'POST'])
def update(id):

    # Grab our specifc product based on the id 
    product = Product.query.get(id) # Same as SELECT * FROM product WHERE product_id = id

    # Instantiate our form
    updateform = ProductForm()
    
    if request.method == 'POST' and update.validate_on_submit():
        product.name = updateform.name.data 
        product.image = product.set_image(updateform.image.data, updateform.name.data)
        product.description = updateform.description.data 
        product.price = updateform.price.data 
        product.quantity = updateform.quantity.data 

        #commit our changes
        db.session.commit()

        flash(f"You have successfully updated product {product.name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("We were unable to process your request", category='warning')
        return redirect(f'/shop/update/{product.prod_id}')
    
                                            # Left of = is html, right of = is what its referencing in the function
    return render_template('update.html', form=updateform, product=product )

@site.route('/shop/delete/<id>')
def delete(id):

    # Quary the database to find the product
    product = Product.quary.get(id)

    db.session.delete(product)
    db.session.commit
    return redirect('/')