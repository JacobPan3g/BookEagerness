# coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import Enagerness

def index(request):
    return render_to_response('login.html')

@csrf_exempt
def result(request):
    username = request.POST['username']
    userpw = request.POST['userpw']
    recommend, userInfo = Enagerness.recommend(username, userpw);
    hotbook = Enagerness.getTopBooks();
    user = { 'name' : '振坚_Jacob',
        'status' : '唉呀唉呀唉呀唉呀咿呀咿呀哟～～～～～～',
        'img' : 'http://tp1.sinaimg.cn/2136410524/180/5599650163/1' }
    return render_to_response('result.html', { 'user' : userInfo,
        'result' : recommend,
        'dayrecommend' : hotbook})

@csrf_exempt
def logout(request):
    return render_to_response('logout.html');
