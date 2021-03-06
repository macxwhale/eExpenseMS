from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('add-expenses', views.add_expense, name="add-expenses"),
    path('edit-expense/<int:id>', views.expense_edit, name="expense-edit"),
    path('expense-delete/<int:id>', views.delete_expense, name="expense-delete"),
    path('search-expenses', csrf_exempt(views.search_expenses), name="search_expenses"),
   
    path('expenses', views.expense, name="expenses"),
    path('add-expenses', views.add_expense, name="add-expenses"),
    path('edit-expense/<int:id>', views.expense_edit, name="expense-edit"),
    path('expense-delete/<int:id>', views.delete_expense, name="expense-delete"),
    
    path('float', views.float, name="float"),
    path('add-float', views.add_float, name="add-float"),
    path('edit-float/<int:id>', views.float_edit, name="edit-float"),
    path('float-delete/<int:id>', views.delete_float, name="float-delete"),

    path('category', views.category, name="category"),
    path('add-category', views.add_category, name="add-category"),
    path('edit-category/<int:id>', views.category_edit, name="edit-category"),
    path('category-delete/<int:id>', views.delete_category, name="category-delete"),

    path('expense_summary', views.expense_summary, name="expense_summary"),
    path('float_vs_expense', views.float_vs_expense, name="float_vs_expense"),

]
