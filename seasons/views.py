from django.shortcuts import render
from rest_framework import generics
from .models import Season
from .serializers import SeasonSerializer

# Create your views here.

class SeasonApiView(generics.ListCreateAPIView):

    queryset = Season.objects

    serializer_class = SeasonSerializer


    def perform_create(self, serializer):

        # serializer.save(user=self.request.user)
        print(serializer)


        print(serializer.validated_data) # all that passed with request

        title = serializer.validated_data.get("title", "")
        
        description = serializer.validated_data.get("description", "Coming soon!")

        # IMPORTANT TO SAVE BECAUSE WE OVERRIDING!
        serializer.save(title=title, description=description)

        # send a Django signal
    

class SeasonDetailApiView(generics.RetrieveAPIView):

    queryset = Season.objects
    serializer_class = SeasonSerializer

    lookup_field = "number"   # for single item 

    # custom queryset
    # def get_queryset(self): pass



