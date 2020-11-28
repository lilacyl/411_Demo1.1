from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from .models import Test, StockInfo
from .models import Users, UserClicks

from django.db import connection
from django.shortcuts import redirect

"""
Global Variable
"""
current_user = "No User"
stock_id = 0
sfi_id = 0

"""
Stock Functions
"""


def home(request):
    views_database = "<a href='http://127.0.0.1:8000/database/'>database</a>"  # link that go to viewstock page
    view_Stock = "<a href='http://127.0.0.1:8000/viewStock/'>viewStock</a>"  # link that go to database page
    view_users = "<a href='http://127.0.0.1:8000/all_users/'>all_users</a>"
    return render(request, "home.html",
                  {"view_Stock": view_Stock, "views_database": views_database, "all_users": view_users})


# print names
def get_all_user_name(request):
    name = request.path
    # print(name)
    tempt_test = Test.objects.raw('SELECT * FROM app_test')
    return HttpResponse(tempt_test)


# redirect to other page
def redirect_to_admin(request):
    return redirect(home)


# click then
def runoob(request):
    # views_insert = "<a href='http://127.0.0.1:8000/insert/'>insert </a>"      #link that go to insert page
    # views_update = "<a href='http://127.0.0.1:8000/update/'>update </a>"       #link that go to update page
    # views_delete = "<a href='http://127.0.0.1:8000/delete/'>delete </a>"      #link that go to delete page
    views_view = "<a href='http://127.0.0.1:8000/view/'>view</a>"  # link that go to view page

    # return render(request, "test.html", {"views_insert": views_insert, "views_update": views_update, "views_delete": views_delete, "views_view": views_view})
    return render(request, "test.html", {"views_view": views_view})


# view
def view(request):
    tempt_test = Test.objects.raw('SELECT * FROM app_test')
    return HttpResponse(tempt_test)


# insert
def insert(request):
    if request.method == 'POST' and request.POST:
        insert1 = request.POST.get('insert')
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO app_test (name) VALUES (%s)",
                [insert1])

    views_view = "<a href='http://127.0.0.1:8000/view/'>view</a>"
    return render(request, "test.html", {"views_view": views_view})


# update
def update(request):
    # if request.method == 'POST' and request.POST:
    #     insert1 = request.POST.get('update_to')
    #     delete1 = request.POST.get('update_from')
    #     with connection.cursor() as cursor:
    #         cursor.execute(
    #             "DELETE FROM app_test WHERE name = %s",
    #             [delete1])
    #         cursor.execute(
    #             "INSERT INTO app_test (name) VALUES (%s)",
    #             [insert1])

    if request.method == 'POST' and request.POST:
        update_f = request.POST.get('update_from')
        update_t = request.POST.get('update_to')
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE app_test SET name = %s where name = %s",
                [update_t, update_f])

    views_view = "<a href='http://127.0.0.1:8000/view/'>view</a>"
    return render(request, "test.html", {"views_view": views_view})


# delete
def delete(request):
    if request.method == 'POST' and request.POST:
        delete1 = request.POST.get('delete')
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM app_test WHERE name = %s",
                [delete1])

    views_view = "<a href='http://127.0.0.1:8000/view/'>view</a>"
    return render(request, "test.html", {"views_view": views_view})


###########################################################################################################################################

def runStock(request):
    view_stock = "<a href='http://127.0.0.1:8000/viewStockDatabase/'>viewStockDatabase</a>"  # link that go to viewStockDatabase page

    return render(request, "stock.html", {"view_stock": view_stock})


# insert
def insertStock(request):
    if request.method == 'POST' and request.POST:
        insert1 = request.POST.get('insertStockid')
        insert2 = request.POST.get('insertStockName')
        insert3 = request.POST.get('insertStockGR')
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO app_stockinfo (stock_id, company_name, growth_rate) VALUES (%s,%s,%s)",
                [insert1, insert2, insert3])

    view_stock = "<a href='http://127.0.0.1:8000/viewStockDatabase/'>viewStockDatabase</a>"  # link that go to viewStockDatabase page
    return render(request, "stock.html", {"view_stock": view_stock})


# delete
def deleteStock(request):
    if request.method == 'POST' and request.POST:
        delete1 = request.POST.get('deleteStock')
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM app_stockinfo WHERE stock_id = %s",
                [delete1])

    view_stock = "<a href='http://127.0.0.1:8000/viewStockDatabase/'>viewStockDatabase</a>"  # link that go to viewStockDatabase page
    return render(request, "stock.html", {"view_stock": view_stock})


# view stock database
def viewStockDatabase(request):
    tmp = StockInfo.objects.raw('SELECT * FROM app_stockinfo')
    return HttpResponse(tmp)


"""
MongoDB Section Pages & Functions
"""


def all_users(request):
    users = Users.object.using('mongo').all()
    stringval = "The following are all the users:<br>"
    count = 0
    for u in users:
        stringval += str(count) + ":" + u.use_name + "<br>"
    return HttpResponse(stringval)


def run_add_user(request):
    view_stock = "<a href='http://127.0.0.1:8000/viewStockDatabase/'>viewStockDatabase</a>"  # link that go to viewStockDatabase page
    return render(request, "user_login.html", {"view_stock": view_stock})


@csrf_exempt
def insertUser(request):
    if request.method == 'POST' and request.POST:
        use_name = request.POST.get('username')
        password = request.POST.get('password')
        user = Users(use_name=use_name, password=password)
        user.save(using='mongo')

    return HttpResponse("Inserted User")


def loginUser(request):
    result = "could not log in"

    use_name = request.POST.get('username_login')
    password = request.POST.get('password_login')

    try:
        user = Users.object.using('mongo').get(use_name=use_name)
    except Users.DoesNotExist:
        raise Http404("User has not register")

    if user.password == password:
        result = "welcome " + use_name
        current_user = use_name

    return HttpResponse(result)
