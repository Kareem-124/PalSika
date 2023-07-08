from django.shortcuts import render, redirect
from app.models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def check_session(request):
    if request.session.has_key('user_session_id') == True:
        user_session = User.objects.get(id=request.session['user_session_id'])
    else:
        user_session = False
    return user_session
# Page: Home


def index(request):
    # Check if we a session is available
    user_session = check_session(request)
    context = {
        'user_session': user_session,
    }
    return render(request, 'index.html', context)

# Page: Registration


def registration(request):
    # Check if we a session is available
    user_session = check_session(request)
    context = {
        'user_session': user_session,
    }
    return render(request, 'registration.html', context)

# Page: Products


def products(request):
    # Check if we a session is available
    user_session = check_session(request)
    products = Product.objects.all()
    context = {
        'user_session': user_session,
        'products' : products,
    }
    return render(request, 'products.html', context)

# Page : New_Products


def new_product_page(request):
    # Check if we a session is available
    user_session = check_session(request)
    context = {
        'user_session': user_session,
    }
    return render(request, 'new_product.html', context)

# Page: Edit_product
def edit_product_page(request,product_id):
    product = Product.objects.get(id=product_id)
    user_session = check_session(request)
    context = {
        'user_session': user_session,
        'product' : product,
    }
    return render(request,'edit_product.html',context)

# Process: Registration Process


def reg_process(request):
    errors = User.objects.reg_validation(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/registration')
    password = request.POST['password']
    ps_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=ps_hash
    )
    messages.success(request,f"User {request.POST['first_name']} {request.POST['last_name']} Has Been Created Successfully")
    return redirect('/')

# Process: Login


def login_process(request):
    # see if the username provided exists in the database
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['user_session_id'] = logged_user.id
            messages.success(request, "You have Successfully logged in")

        else:
            # if we didn't find anything in the database by searching by username or if the passwords don't match,
            messages.error(request, "Email or Password incorrect")

    else:
        # if we didn't find anything in the database by searching by username or if the passwords don't match,
        messages.error(request, "Email or Password incorrect")

    return redirect('/')

# Process: Logout


def logout_process(request):
    # This will clear the massages from messages (error / success)
    list(messages.get_messages(request))
    request.session.flush()
    return redirect('/')

# Function: Check Quantity and Barcode
def check_qty_barcode(request):
    if request.POST['product_qty'] == '' :
        product_qty = None
    else:
        product_qty = request.POST['product_qty']
    if request.POST['product_barcode'] == '' :
        product_barcode = None
    else:
        product_barcode = request.POST['product_barcode']
    return product_qty,product_barcode

# Process : Add New Product
def new_product_process(request):
    product_qty,product_barcode = check_qty_barcode(request)
    product = Product.objects.create(product_name=request.POST['product_name'],
                                    product_category=request.POST['product_category'],
                                    product_qty=product_qty,
                                    product_barcode=product_barcode,
                                    product_desc=request.POST['product_desc'],
                                    )
    return redirect('/products')


# Process: Delete

def delete_product_process(request,product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect ('/products')

# Process: Edit Product

def edit_product_process(request, product_id):
    product=Product.objects.get(id=product_id)
    product_qty,product_barcode = check_qty_barcode(request)
    product.product_name=request.POST['product_name']
    product.product_category=request.POST['product_category']
    product.product_qty=product_qty
    product.product_barcode=product_barcode
    product.product_desc=request.POST['product_desc']
    product.save()
    return redirect('/products')