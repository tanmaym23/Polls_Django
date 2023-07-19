from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def hello(requests):
    # html='<h1> hello! I am Tanmay Mahajan </h1>'
    return render(requests,'myapp/hello.html')

def info(requests):
    html='''
        <ul>
            <li> age 20</li>
            <li> ptk</li>
            <li> lpu</li>
        </ul>
    '''
    return HttpResponse(html)

class hi(View):
    def get(self,requests):
        return HttpResponse("<hi>class based view</hi>")