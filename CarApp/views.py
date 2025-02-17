from .models import Car,Showroom,Review
from .serializers import CarSerializer,ShowroomSerializer,ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class Review_view(APIView):
    def get(self,request):
        rev=Review.objects.all()
        serializer=ReviewSerializer(rev,many=True,context={'request' : request})
        return Response(serializer.data)
    def post(self,request):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Rev_Detail(APIView):

    def get(self,request,pk):
        try:
            rev = Review.objects.get(pk=pk)  
        except Review.DoesNotExist:  
            return Response({'Error': "OOPS!"}, status=status.HTTP_404_NOT_FOUND) 
        serializer = ReviewSerializer(rev)  
        return Response(serializer.data) 
     
    def put(self,request,pk):
        try:
            rev = Review.objects.get(pk=pk) 
        except Review.DoesNotExist:  
            return Response({'Error': "OOPS!"}, status=status.HTTP_404_NOT_FOUND)  
        serializer = ReviewSerializer(rev, data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data)  
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Response: Send error messages and 400 Bad Request status
    
    def delete(self,request,pk):
       rev=Review.objects.get(pk=pk)
       rev.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)    


class Showroom_View(APIView):
    def get(self,request,format=None):
        showroom=Showroom.objects.all()
        serializer=ShowroomSerializer(showroom,many=True,context={'request': request})
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serialzer=ShowroomSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class Showroom_Detail(APIView):

    def get(self,request,pk):
        try:
            showroom = Showroom.objects.get(pk=pk)  
        except Showroom.DoesNotExist:  
            return Response({'Error': "OOPS!"}, status=status.HTTP_404_NOT_FOUND) 
        serializer = ShowroomSerializer(showroom)  
        return Response(serializer.data) 
     
    def put(self,request,pk):
        try:
            showroom = Showroom.objects.get(pk=pk) 
        except Car.DoesNotExist:  
            return Response({'Error': "OOPS!"}, status=status.HTTP_404_NOT_FOUND)  
        serializer = ShowroomSerializer(showroom, data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data)  
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Response: Send error messages and 400 Bad Request status
    
    def delete(self,request,pk):
       showroom=Showroom.objects.get(pk=pk)
       showroom.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)


              

# function based views 
@api_view(['GET','POST'])
def Car_list(request):
    if request.method == 'GET': 
        cars = Car.objects.all()  
        serializer = CarSerializer(cars, many=True)  
        return Response(serializer.data)  

    if request.method == 'POST':  
        serializer = CarSerializer(data=request.data)  
        if serializer.is_valid():
           
            serializer.save()  

          
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET','PUT','DELETE'])
def Car_details(request, pk): 
    if request.method == 'GET': 
        try:
            car = Car.objects.get(pk=pk)  
        except Car.DoesNotExist:  
            return Response({'Error': "Can not found"}, status=status.HTTP_404_NOT_FOUND)  
        serializer = CarSerializer(car)  
        return Response(serializer.data)  

    if request.method == 'PUT': 
        try:
            car = Car.objects.get(pk=pk)  
        except Car.DoesNotExist:  
            return Response({'Error': "Can not found"}, status=status.HTTP_404_NOT_FOUND)  
        serializer = CarSerializer(car, data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data)  
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    if request.method == 'DELETE':  
        try:
            car = Car.objects.get(pk=pk)  
        except Car.DoesNotExist: 
            return Response({'Error': "Can not found"}, status=status.HTTP_404_NOT_FOUND)  
        car.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)  