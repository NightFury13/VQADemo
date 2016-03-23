from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse

from .models import Image
from .forms import ImageUploadForm


import subprocess, os

image_url = ''

# Create your views here.
def index(request):
    global image_url
    if not image_url:
        image_url = '/static/images/cat.jpg'

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
                newImg = Image(photo = request.FILES['image'])
                image_url = newImg.photo.url
                print image_url
                newImg.save()
    else:
        form = ImageUploadForm()

    return render_to_response(
        'vqa/index.html',
        {'msg':'Visual Question Answering', 'image_url':image_url, 'form':form},
        context_instance=RequestContext(request)
    )

def compute_vqa(request):
    print "computing VQA answer"
    img_url = 'blank'
    question = 'blank'

    if request.method == 'GET':
        img_url = request.GET['image_url']
        img_url = os.getcwd()+img_url
        question = request.GET['question']

    print "Img-URL : %s, Question : %s" % (img_url, question)

    with open('out.txt','w') as outfile:
        p = subprocess.Popen(["th", "predict.lua", "-checkpoint_file", "checkpoints/vqa_epoch23.26_0.4610_cpu.t7", "-input_image_path", img_url, "-question", question], cwd='/home/mohit/research/cloudcv/GSoC2016/neural-vqa', stdout=outfile)
        p.wait()
    with open('out.txt','r') as f:
        answer = f.readlines()[-1]

    return HttpResponse('Answer : '+answer)

