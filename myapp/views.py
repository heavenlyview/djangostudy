from django.shortcuts import render, HttpResponse
import random # 접속이 들어올 때마다 랜덤한 정보를 동적으로 만들어주는 웹 애플리케이션을 만들어 줄 때에 필요함
# topics = [
#     {'id':1, 'title':'routing', 'body':'Routing is ..'},
#     {'id':2, 'title':'view', 'body':'View is ..'},
#     {'id':3, 'title':'Model', 'body':'Model is ..'},
# ]

def index(request):
    # global topics # topics는 전역변수다라고 선언
    # ol = ''
    # for topic in topics:
    #     ol += f'<li>{topic["title"]}</li>'

    return HttpResponse('''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            <li>routing</li>
            <li>view</li>
            <li>model</li>
        <ol>
        <h2>welcome</h2>
        Hello, Django
    </body>
    </html>
    ''') 

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!'+id)
