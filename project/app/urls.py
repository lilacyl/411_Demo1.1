from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('a/', views.get_all_user_name, name='get_user_name'),
    path('ret/', views.redirect_to_admin),
    path('database/', views.runoob),
    path('insert/', views.insert),
    path('update/', views.update),
    path('delete/', views.delete),
    path('view/', views.view),

    path('viewStock/', views.runStock),
    path('viewStockDatabase/', views.viewStockDatabase),
    path('insertStock/', views.insertStock),
    path('deleteStock/', views.deleteStock),

    path('viewSFIDatabase/', views.viewSFIDatabase),
    path('insertSFI/', views.insertSFI),
    path('deleteSFI/', views.deleteSFI),
    path('updateSFI/', views.updateSFI),
    path('searchSFI/', views.searchSFI),
    path('viewSFI/', views.runSFI),

    path('viewFPDatabase/', views.viewFPDatabase),
    path('insertFP/', views.insertFP),
    path('viewFP/', views.runFP),
]