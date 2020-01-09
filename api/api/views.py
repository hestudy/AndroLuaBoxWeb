from django.http import JsonResponse
from django.core.serializers import serialize
from dhjz.models import classification,tutorial
from jxwd.models import jxwd_context,jxwd_fenlei
import json

# Create your views here.
def api(request):
    data = {}
    anime_class = classification.objects.all()
    anime_class = serialize('json',anime_class)
    anime_class = json.loads(anime_class)
    for i in anime_class:
        anime_code = tutorial.objects.filter(classification=i['pk'])
        anime_code = serialize('json', anime_code)
        anime_code = json.loads(anime_code)
        data[i['pk']] = anime_code
    teach_class = jxwd_fenlei.objects.all()
    teach_class = serialize('json',teach_class)
    teach_class = json.loads(teach_class)
    for i in teach_class:
        teach_code = jxwd_context.objects.filter(fenlei=i['pk'])
        teach_code = serialize('json',teach_code)
        teach_code = json.loads(teach_code)
        data[i['pk']] = teach_code
    return JsonResponse(data,safe=False)