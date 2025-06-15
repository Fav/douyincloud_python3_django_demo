from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.core.cache import cache
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import logging
import json
import requests

logger = logging.getLogger('polls')

@csrf_exempt
def antidirt(request):
    concat = request.POST
    postBody = request.body
    # 获取响应内容
    json_result = json.loads(postBody)
    return JsonResponse(json_result)


@csrf_exempt
def openid(request):
    openid = request.META.get('HTTP_X_TT_OPENID')
    result_data = {
        'err_no': 0,
        'err_msg': 'success',
        'data': {
            'openid': openid
        }
    }
    return JsonResponse(result_data)
