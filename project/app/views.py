from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Test

from django.db import connection
from django.shortcuts import redirect


def home(request):
    # test1 = Test(name='haro 3')
    # test1.save()

    #select clause
    tempt_test = Test.objects.raw('SELECT * FROM app_test')[0]

    #insert clause
    lname = 'hsdishdishdishd'
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO app_test (name) VALUES (%s)",
            [lname])

    # update clause
    lname = 'new_name'
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE app_test SET name = %s where name = 'hsdishdishdishd'",
            [lname])

    # delete clause
    lname = 'haro 3'
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM app_test WHERE name = %s",
            [lname])

    return HttpResponse("welcome to FINDO")



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


    # if request.method == 'POST' and request.POST:
    #     lname = request.POST.get('name')
    #     with connection.cursor() as cursor:
    #         cursor.execute(
    #             "INSERT INTO app_test (name) VALUES (%s)",
    #             [lname])


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

    if request.method == 'POST' and request.POST:
        insert1 = request.POST.get('update_to')
        delete1 = request.POST.get('update_from')
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM app_test WHERE name = %s",
                [delete1])
            cursor.execute(
                "INSERT INTO app_test (name) VALUES (%s)",
                [insert1])


    # if request.method == 'POST' and request.POST:
    #     update_f = request.POST.get('update_from')
    #     update_t = request.POST.get('update_to')
    #     with connection.cursor() as cursor:
    #         cursor.execute(
    #             "UPDATE app_test SET name = %s where name = %s",
    #             [update_f, update_t])


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
