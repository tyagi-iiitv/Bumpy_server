from .models import Files, Bumps
# from .serializers import FileSerializer, BumpSerializer
from serializers import BumpSerializer
# from rest_framework import mixins
from rest_framework import generics
from .tasks import analyser
from django.views.decorators.csrf import csrf_exempt
from .forms import FileForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

@csrf_exempt
def file_list(request):
    # Handle file upload
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Files(docfile = request.FILES['docfile'])
            newdoc.save()
            filename = str(request.FILES['docfile'])
            print filename
            analyser.delay(filename)
            return HttpResponseRedirect(reverse('files.views.file_list'))
    else:
        form = FileForm() # A empty, unbound form

    # Load documents for the list page
    documents = Files.objects.all()
    print documents

    # Render list page with the documents and the form
    return render_to_response(
        'files/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

class BumpDetail(generics.ListAPIView):
    queryset = Bumps.objects.all()
    serializer_class = BumpSerializer

    def get_queryset(self):
        my_readings = str(self.kwargs['readings'])
        fields = my_readings.split(':')
        my_long = fields[1]
        my_latt = fields[0]
        return Bumps.objects.all()
        #return Bumps.objects.filter(longitude=my_long, lattitude=my_latt)
        # get_long = self.kwargs['longitude']
        # return Bumps.objects.filter(lattitude=get_lat, longitude=get_long)




# --------------------------------------------------------------------------------------- #

# class FileList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Files.objects.all()
#     serializer_class = FileSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#       filename = str(request.FILES['files'])
#       analyser.delay(filename)
#         return self.create(request, *args, **kwargs)



            
# class FileDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Files.objects.all()
#     serializer_class = FileSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# ------------------------------------------------------------------------------------------- #