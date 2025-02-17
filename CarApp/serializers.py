from rest_framework import serializers
from .models import Car,Showroom,Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'       

class CarSerializer(serializers.ModelSerializer):  # Inherit from ModelSerializer
    #REV=ReviewSerializer(many=True,read_only=True)
    REV=serializers.StringRelatedField(many=True)
   
    class Meta:
        model = Car  # Tell the serializer which model to use
        fields = '__all__'  # Or specify the fields you want to include: ['id', 'name', 'description', 'price', 'chassisnumber']
        read_only_fields = ['id', 'active'] #Fields that are read only


    # Field-level validation (if needed) - these remain the same
    def validate_price(self, value):
        if value <= 20000.00:
            raise serializers.ValidationError("Price must be greater than 20000")
        return value

    # Object-level validation (if needed) - these remain the same
    def validate(self, data):
        if data.get('name') == data.get('description'):  # Use .get() to avoid KeyError
            raise serializers.ValidationError("Name and description must be different")
        return data


class ShowroomSerializer(serializers.ModelSerializer):
   # cars = CarSerializer(many=True, read_only=True)  # Use 'cars' based on the related_name
    #cars=serializers.StringRelatedField(many=True)
    cars=serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='Car_details'
    )
    # cars=serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title'
    #  )
    # cars = CarSerializer(many=True, read_only=True)
    # cars = serializers.HyperlinkedIdentityField(view_name='Car_details')


    class Meta:
        model=Showroom
        fields='__all__'

