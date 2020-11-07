from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Test, StockInfo

from django.db import connection
from django.shortcuts import redirect


def home(request):
    views_database = "<a href='http://127.0.0.1:8000/database/'>database</a>"      #link that go to viewstock page
    view_Stock = "<a href='http://127.0.0.1:8000/viewStock/'>viewStock</a>"  # link that go to database page
    return render(request, "home.html", {"view_Stock": view_Stock, "views_database": views_database})



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
    views_view = "<a href='http://127.0.0.1:8000/view/'>view</a>"           #link that go to view page

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
    view_stock = "<a href='http://127.0.0.1:8000/viewStockDatabase/'>viewStockDatabase</a>"           #link that go to viewStockDatabase page

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
                [insert1, insert2,insert3])

    view_stock = "<a href='http://127.0.0.1:8000/viewStockDatabase/'>viewStockDatabase</a>"           #link that go to viewStockDatabase page
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

#view stock database
def viewStockDatabase(request):
    tmp = StockInfo.objects.raw('SELECT * FROM app_stockinfo')
    return HttpResponse(tmp)