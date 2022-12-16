from django.shortcuts import render, HttpResponse
import random # 접속이 들어올 때마다 랜덤한 정보를 동적으로 만들어주는 웹 애플리케이션을 만들어 줄 때에 필요함


# Create your views here.
def index(request):
    return HttpResponse('<h1>Random</h1>'+str(random.random())) # 실행할 때마다 랜덤 숫자 출력
# str로 바꿔주는 이유는 '+' 기준, 왼쪽으로는 문자형인데 오른쪽은 숫자형이라 문자형으로 바꿔주기 위함
def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!'+id)
