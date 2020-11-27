from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import Test, StockInfo, FinancialProduct, StructuredFinancialInvestment

from django.db import connection
from django.shortcuts import redirect


def home(request):
    view_Stock = "<a href='http://127.0.0.1:8000/viewStock/'>Stock page</a>"  # link that go to database page
    view_FP = "<a href='http://127.0.0.1:8000/viewFP/'>FP page</a>"  # link that go to database page
    view_SFI = "<a href='http://127.0.0.1:8000/viewSFI/'>SFI page</a>"
    return render(request, "home.html", {"view_Stock": view_Stock,"view_FP": view_FP, "view_SFI": view_SFI})


##################################################################################################################

# print names
def get_all_user_name(request):
    name = request.path
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
#this is dedicated for the stock page
def runStock(request):
    view_stock = "<a href='http://127.0.0.1:8000/viewStockDatabase/'>viewStockDatabase</a>"           #link that go to viewStockDatabase page

    view_FP = "<a href='http://127.0.0.1:8000/viewFP/'>FP page</a>"

    home_page = "<a href='http://127.0.0.1:8000/'>home page</a>"

    view_SFI = "<a href='http://127.0.0.1:8000/viewSFI/'>SFI page</a>"

    return render(request, "stock.html", {"view_stock": view_stock, "view_FP": view_FP, "home_page":home_page, "view_SFI":view_SFI })

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


#search
def searchStockId(request):

    searchstock = request.POST.get('search_Stockid')

    for p in StockInfo.objects.raw('SELECT * FROM app_stockinfo where company_name = %s', [searchstock]):
        tmp = p

    return HttpResponse(tmp.stock_id)


def searchStockPrice(request):

    searchstockprice = request.POST.get('search_Stockprice')

    for p in StockInfo.objects.raw('SELECT * FROM app_stockinfo where company_name = %s', [searchstockprice]):
        tmp = p

    return HttpResponse(tmp.price)

def searchStockIdViaSFI(request):

    if request.method == 'POST' and request.POST:
        searchw = request.POST.get('search_StockIdViaSFI')

        with connection.cursor() as cursor:
            cursor.execute(
                'select * from app_stockinfo sto join app_structuredfinancialinvestment str on str.stock_id_id=sto.stock_id where sto.stock_id = %s',[searchw])
            results = cursor.fetchall()

        # 'select * from app_financialproduct f join app_structuredfinancialinvestment s on f.fp_id=s.SFI_id where s.SFI_id = %s', [
        #     searchw])

        # template = loader.get_template('.html')
        # context = {
        #     'jjj': results[0][0],
        #     'jjj': results[0][1]
        # }


    return HttpResponse(results)

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


###################################################################################################################################################################################
#this is dedicated for the structured financial investment page

def insertSFI(request):
    if request.method == 'POST' and request.POST:
        insert1 = request.POST.get('insert_fp_id')
        insert2 = request.POST.get('insert_stock_id')
        insert3 = request.POST.get('insert_SFI_id')
        insert4 = request.POST.get('insert_Knock_in')
        insert5 = request.POST.get('insert_Knock_out')
        insert6 = request.POST.get('insert_put_strike')

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO app_structuredfinancialinvestment (fp_id_id, stock_id_id, SFI_id, Knock_in, Knock_out, put_strike) VALUES (%s,%s, %s,%s,%s,%s)",
                [insert1, insert2,insert3,insert4, insert5,insert6])

    view_SFI = "<a href='http://127.0.0.1:8000/viewSFIDatabase/'>viewSFIDatabase</a>"
    return render(request, "StructuredFinancialInvestment.html", {"view_SFI": view_SFI})


def viewSFIDatabase(request):
    tmp = StructuredFinancialInvestment.objects.raw('SELECT * FROM app_structuredfinancialinvestment')
    return HttpResponse(tmp)

# delete
def deleteSFI(request):
    if request.method == 'POST' and request.POST:
        delete1 = request.POST.get('deleteSFI')
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM app_structuredfinancialinvestment WHERE SFI_id = %s",
                [delete1])

    view_SFI = "<a href='http://127.0.0.1:8000/viewSFIDatabase/'>viewSFIDatabase</a>"
    return render(request, "StructuredFinancialInvestment.html", {"view_SFI": view_SFI})


# update
def updateSFI(request):
    if request.method == 'POST' and request.POST:
        update_f = request.POST.get('update_SFI_from')
        update_t = request.POST.get('update_SFI_to')
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE app_structuredfinancialinvestment SET SFI_id = %s where SFI_id = %s",
                [update_t, update_f])


    view_SFI = "<a href='http://127.0.0.1:8000/viewSFIDatabase/'>viewSFIDatabase</a>"
    return render(request, "StructuredFinancialInvestment.html", {"view_SFI": view_SFI})

#search
def searchSFI(request):
    # if request.method == 'POST' and request.POST:
    #     search1 = request.POST.get('')
    #
    #     with connection.cursor() as cursor:
    #         cursor.execute(
    #             "SELECT * FROM app_structuredfinancialinvestment where SFI_id = %s",
    #             [search1])

    search1 = request.POST.get('search_SFI')

    for p in StructuredFinancialInvestment.objects.raw('SELECT * FROM app_structuredfinancialinvestment where SFI_id = %s', [search1]):
        tmp = p


    return HttpResponse(tmp.Knock_in)

    # view_SFI = "<a href='http://127.0.0.1:8000/searchSFI/'>searchSFI</a>"
    # return render(request, "StructuredFinancialInvestment.html", {"view_SFI": view_SFI})


def runSFI(request):
    view_SFI = "<a href='http://127.0.0.1:8000/viewSFIDatabase/'>viewSFIDatabase</a>"

    view_FP = "<a href='http://127.0.0.1:8000/viewFP/'>FP page</a>"

    home_page = "<a href='http://127.0.0.1:8000/'>home page</a>"

    return render(request, "StructuredFinancialInvestment.html", {"view_SFI": view_SFI, "home_page":home_page, "view_FP":view_FP})



######################################################################################################################
def insertFP(request):
    if request.method == 'POST' and request.POST:
        insert1 = request.POST.get('insert_fp_id')

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO app_financialproduct (fp_id) VALUES (%s)",
                [insert1])

    view_FP = "<a href='http://127.0.0.1:8000/viewFPDatabase/'>viewFPDatabase</a>"           #link that go to viewStockDatabase page
    return render(request, "financial_product.html", {"view_FP": view_FP})

#search
def searchFP(request):

    searchfp = request.POST.get('search_fp')

    for p in FinancialProduct.objects.raw('SELECT * FROM app_financialproduct where product_name = %s', [searchfp]):
        tmp = p

    return HttpResponse(tmp.fp_id)



def viewFPDatabase(request):
    tmp = FinancialProduct.objects.raw('SELECT * FROM app_financialproduct')

    return HttpResponse(tmp)

def runFP(request):
    view_FP = "<a href='http://127.0.0.1:8000/viewFPDatabase/'>view FP Database</a>"

    home_page = "<a href='http://127.0.0.1:8000/'>home page</a>"

    view_SFI = "<a href='http://127.0.0.1:8000/viewSFI/'>SFI page</a>"
    return render(request, "financial_product.html", {"view_FP": view_FP, "home_page": home_page, "view_SFI": view_SFI})