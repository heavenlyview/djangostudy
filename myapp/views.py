from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# CSRF 보안 기능 우회하기 (제외하기) 불러오기
import random # 접속이 들어올 때마다 랜덤한 정보를 동적으로 만들어주는 웹 애플리케이션을 만들어 줄 때에 필요함


topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'},
]

def HTMLTemplate(articleTag):
    global topics # topics는 전역변수다라고 선언
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        <ul>
        {articleTag}
        <ul>
            <a href="/create/">create</a>
        </ul> 
    </body>
    </html>
    '''
@csrf_exempt
def index(request):
    article = '''
    <h2>welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def create(request):
    article = '''
        <form action="/create/">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'

    return HttpResponse(HTMLTemplate(article))
