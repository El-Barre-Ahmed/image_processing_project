from django.shortcuts import render
from .forms import ImageUploadForm
from .services.basic_ops import *
from .services.segmentation import *
from .services.region_growing import *
import cv2
import os
from django.conf import settings

def upload_image(request):
    result_url = None
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            operation = form.cleaned_data['operation']
            param = form.cleaned_data.get('param') or 0

            # sauvegarder image
            path = os.path.join(settings.MEDIA_ROOT, 'uploads', image_file.name)
            with open(path, 'wb+') as f:
                for chunk in image_file.chunks():
                    f.write(chunk)

            # lire avec OpenCV
            image = cv2.imread(path)
            if operation == 'inversion':
                result = inversion(image)
            elif operation == 'decalage':
                result = decalage(image, int(param))
            elif operation == 'mise_echelle':
                result = mise_echelle(image, float(param) if param else 1.5)
            elif operation == 'rotation':
                result = rotation(image, int(param) if param else 90)
            elif operation == 'miroir':
                result = miroir(image)
            elif operation == 'kmeans':
                result = kmeans(image, int(param) if param else 2)
            elif operation == 'seuillage':
                result = seuillage(image, int(param) if param else 128)
            elif operation == 'region_growing':
                result = region_growing(image, seed=(0,0), threshold=int(param) if param else 10)
            
            # sauvegarder résultat
            result_path = os.path.join(settings.MEDIA_ROOT, 'results', image_file.name)
            cv2.imwrite(result_path, result)
            result_url = settings.MEDIA_URL + 'results/' + image_file.name
    else:
        form = ImageUploadForm()
    return render(request, 'image_app/upload.html', {'form': form, 'result_url': result_url})