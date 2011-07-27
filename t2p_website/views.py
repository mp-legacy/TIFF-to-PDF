# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
import os
import time
from subprocess import call


def index_page(request):
	if request.POST.has_key("submit"):
		id = str(time.time()).split(".")[0]
		
		##make directories
		os.makedirs('/home/tiff2pdf_online/media_folder/' + id)
		os.makedirs('/home/tiff2pdf_online/media_folder/' + id + "/uploads")
		os.makedirs('/home/tiff2pdf_online/media_folder/' + id + "/download")
	
		upload_path = '/home/tiff2pdf_online/media_folder/' + id + "/uploads"
	
		file = request.FILES['uploadedfile']
		filename = file.name
		
		fd = open('%s/%s' % (upload_path, filename), 'wb')
		
		for chunk in file.chunks():
			fd.write(chunk)
		fd.close()
	
		file_location = '%s/%s' % (upload_path, filename)
		file_output   = '/home/tiff2pdf_online/media_folder/' + id + "/download/output.pdf"	
	
		compiled_call ="tiff2pdf -j -o " + file_output + " " + file_location
	
		os.system(compiled_call)
	
		fd = open(file_output,'r')
	
		response = HttpResponse(fd, mimetype='application/pdf')
		response['Content-disposition'] = 'attachment'
		
		return response
		#response = HttpResponse(file(file_output).read())
		#response['Content-Type'] = ''
		#return response
	
	else:
		return render_to_response('index.html')