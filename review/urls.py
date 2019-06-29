
from django.urls import path

from . import views

urlpatterns = [
    path('', views.search_text, name='index'),
]



from .helpers.data_management.doc_handler import DocHandler
DocHandler.create_index_from_db()


