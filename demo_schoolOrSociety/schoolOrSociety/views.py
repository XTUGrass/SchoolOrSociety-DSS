# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from dss_model.brain import model1
# Create your views here.


def index(request, template_name):
    return render(request, template_name)


def questionary(request, template_name):
    return render(request, template_name)


def process(request):
    raw_arr = []
    input_dic = {}
    input_dic['two'] = request.POST['two']
    raw_arr.append(int(input_dic['two']))

    input_dic['three'] = request.POST['three']
    raw_arr.append(int(input_dic['three']))

    input_dic['four'] = request.POST['four']
    raw_arr.append(int(input_dic['four']))

    input_dic['five'] = request.POST.get('five', '-3')
    raw_arr.append(int(input_dic['five']))

    input_dic['six'] = request.POST['six']
    raw_arr.append(int(input_dic['six']))

    input_dic['seven'] = request.POST['seven']
    raw_arr.append(int(input_dic['seven']))

    input_dic['eight'] = request.POST['eight']
    raw_arr.append(int(input_dic['eight']))

    input_dic['nine'] = request.POST['nine']
    raw_arr.append(int(input_dic['nine']))

    input_dic['ten'] = request.POST['ten']
    raw_arr.append(int(input_dic['ten']))

    input_dic['eleven'] = request.POST['eleven']
    raw_arr.append(int(input_dic['eleven']))

    input_dic['twelve'] = request.POST['twelve']
    raw_arr.append(int(input_dic['twelve']))

    input_dic['thirteen'] = request.POST['thirteen']
    raw_arr.append(int(input_dic['thirteen']))

    input_dic['fourteen1'] = request.POST.get('friends', '-2')
    raw_arr.append(int(input_dic['fourteen1']))

    input_dic['fourteen2'] = request.POST.get('lover', '-2')
    raw_arr.append(int(input_dic['fourteen2']))

    input_dic['fourteen3'] = request.POST.get('policy', '-2')
    raw_arr.append(int(input_dic['fourteen3']))

    input_dic['fourteen4'] = request.POST.get('situation', '-2')
    raw_arr.append(int(input_dic['fourteen4']))

    input_dic['fourteen5'] = request.POST.get('job', '-2')
    raw_arr.append(int(input_dic['fourteen5']))

    input_dic['fourteen6'] = request.POST.get('chance', '-2')
    raw_arr.append(int(input_dic['fourteen6']))

    input_dic['fourteen7'] = request.POST.get('others', '-2')
    raw_arr.append(int(input_dic['fourteen7']))

    input_dic['fifteen'] = request.POST['fifteen']
    raw_arr.append(int(input_dic['fifteen']))

    input_dic['sixteen'] = request.POST['sixteen']
    raw_arr.append(int(input_dic['sixteen']))

    input_dic['seventeen1'] = request.POST.get('seventeen1', '0')
    raw_arr.append(int(input_dic['seventeen1']))

    input_dic['seventeen2'] = request.POST.get('seventeen2', '0')
    raw_arr.append(int(input_dic['seventeen2']))

    input_dic['seventeen3'] = request.POST.get('seventeen3', '0')
    raw_arr.append(int(input_dic['seventeen3']))

    input_dic['seventeen4'] = request.POST.get('seventeen4', '0')
    raw_arr.append(int(input_dic['seventeen4']))

    input_dic['seventeen5'] = request.POST.get('seventeen5', '0')
    raw_arr.append(int(input_dic['seventeen5']))

    input_dic['seventeen6'] = request.POST.get('seventeen6', '0')
    raw_arr.append(int(input_dic['seventeen6']))

    input_dic['seventeen7'] = request.POST.get('seventeen7', '0')
    raw_arr.append(int(input_dic['seventeen7']))

    input_dic['seventeen8'] = request.POST.get('seventeen8', '0')
    raw_arr.append(int(input_dic['seventeen8']))

    input_dic['seventeen9'] = request.POST.get('seventeen9', '0')
    raw_arr.append(int(input_dic['seventeen9']))

    input_dic['seventeen10'] = request.POST.get('seventeen10', '0')
    raw_arr.append(int(input_dic['seventeen10']))

    input_dic['seventeen11'] = request.POST.get('seventeen11', '0')
    raw_arr.append(int(input_dic['seventeen11']))

    input_dic['seventeen12'] = request.POST.get('seventeen12', '0')
    raw_arr.append(int(input_dic['seventeen12']))

    input_dic['seventeen13'] = request.POST.get('seventeen13', '0')
    raw_arr.append(int(input_dic['seventeen13']))

    input_dic['seventeen14'] = request.POST.get('seventeen14', '0')
    raw_arr.append(int(input_dic['seventeen14']))

    input_dic['eighteen'] = request.POST['eighteen']
    raw_arr.append(int(input_dic['eighteen']))

    input_dic['nineteen'] = request.POST['nineteen']
    raw_arr.append(int(input_dic['nineteen']))

    print raw_arr

    if len(raw_arr) == 37:
        model = model1()
        model_index = model.getResult(raw_arr)

        with open("e:\\python/django/demo_schoolOrSociety/dss_model/result.txt", 'w+') as f:
            f.write('考研' if model_index == 1 else '就业')

    return HttpResponseRedirect(reverse('result'))


def result(request):
    content = ""
    with open("e:\\python/django/demo_schoolOrSociety/dss_model/result.txt", 'r') as f:
        content = f.read()

    return render(request, 'schoolOrSociety/result.html', {'model_result': content})

