from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.utils import timezone
from django.views import generic

# class IndexView(generic.ListView):
#     template_name = 'index.html'

#     def get_queryset(self):
# 	    """
# 	    Return the last five published questions (not including those set to be
# 	    published in the future).
# 	    """
# 	    return [0,1]

def index(request):
    return render(request, "index.html")