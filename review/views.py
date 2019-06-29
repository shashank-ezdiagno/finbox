from django.shortcuts import render

# Create your views here.
from django import forms
from review.helpers.indexing import Indexer
from review.helpers.query import TermsQueryExecutor
from django.views.generic.edit import FormView



class SearchForm(forms.Form):
    search_text = forms.CharField()
    max_review_count = forms.IntegerField()

    def search(self):
        # send email using the self.cleaned_data dictionary
        #print(Indexer._max_len_index)
        query = self.cleaned_data["search_text"].split(',')
        values = {val.strip() for val in query}
        executor = TermsQueryExecutor(self.cleaned_data["max_review_count"])
        docs = executor.execute(["summary","text"], values)
        return [doc for doc in docs]


def search_text(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print('ghussa')
            data = form.search()
            return render(request, 'search_form.html', {'form': form.cleaned_data, 'data': data,
                          "query_text":form.cleaned_data["search_text"], 'data_length': len(data)})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'search_form.html', {'form': form})