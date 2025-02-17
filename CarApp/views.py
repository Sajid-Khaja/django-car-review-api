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
    if request.method == 'GET':  # Retrieve a list of cars
        cars = Car.objects.all()  # Database interaction: Retrieve all Car objects
        serializer = CarSerializer(cars, many=True)  # Serialization: Convert Car objects to JSON
        return Response(serializer.data)  # Response: Send serialized data (JSON)

    if request.method == 'POST':  # Create a new car
        serializer = CarSerializer(data=request.data)  # Deserialization: Convert incoming JSON to Python
        if serializer.is_valid():
            #serializer.is_valid():  The is_valid() method performs validation.  It checks if the data in the OrderedDict conforms to the field types and constraints defined in your serializer.  If the data is valid, the validated data is stored in the serializer.validated_data attribute, also as an OrderedDict.
              # Validation: Check if the data is valid
            serializer.save()  # Database interaction: Create and save the Car object

            #serializer.save(): When you call serializer.save(), the serializer uses the data from serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Response: Send serialized data (JSON) and 201 Created status
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Response: Send error messages and 400 Bad Request status

@api_view(['GET','PUT','DELETE'])
def Car_details(request, pk):  # pk: Primary key of the Car object
    if request.method == 'GET':  # Retrieve a specific car
        try:
            car = Car.objects.get(pk=pk)  # Database interaction: Retrieve a specific Car object
        except Car.DoesNotExist:  # Error handling: Car not found
            return Response({'Error': "Can not found"}, status=status.HTTP_404_NOT_FOUND)  # Response: 404 Not Found status
        serializer = CarSerializer(car)  # Serialization: Convert Car object to JSON
        return Response(serializer.data)  # Response: Send serialized data (JSON)

    if request.method == 'PUT':  # Update a specific car
        try:
            car = Car.objects.get(pk=pk)  # Database interaction: Retrieve the Car object to update
        except Car.DoesNotExist:  # Error handling: Car not found
            return Response({'Error': "Can not found"}, status=status.HTTP_404_NOT_FOUND)  # Response: 404 Not Found status
        serializer = CarSerializer(car, data=request.data)  # Deserialization: Convert incoming JSON to Python for update
        if serializer.is_valid():  # Validation: Check if the data is valid
            serializer.save()  # Database interaction: Update and save the Car object
            return Response(serializer.data)  # Response: Send serialized data (JSON)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Response: Send error messages and 400 Bad Request status

    if request.method == 'DELETE':  # Delete a specific car
        try:
            car = Car.objects.get(pk=pk)  # Database interaction: Retrieve the Car object to delete
        except Car.DoesNotExist:  # Error handling: Car not found
            return Response({'Error': "Can not found"}, status=status.HTTP_404_NOT_FOUND)  # Response: 404 Not Found status
        car.delete()  # Database interaction: Delete the Car object
        return Response(status=status.HTTP_204_NO_CONTENT)  # Response: 204 No Content status