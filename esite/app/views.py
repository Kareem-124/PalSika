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

# Process: Registration Process


def reg_process(request):
    password = request.POST['password']
    ps_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=ps_hash
    )
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

# Process: New Product


def new_product_process(request):
    if request.POST['product_qty'] == '' :
        product_qty = None
    if request.POST['product_barcode'] == '' :
        product_barcode = None
    product = Product.objects.create(product_name=request.POST['product_name'],
                                    product_category=request.POST['product_category'],
                                    product_qty=product_qty,
                                    product_barcode=product_barcode,
                                    product_desc=request.POST['product_desc'],
                                    )
    return redirect('/products')
