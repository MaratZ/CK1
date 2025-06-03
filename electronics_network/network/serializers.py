from rest_framework import serializers
from .models import Supplier, Contact, Product

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ('debt',)

    def update(self, instance, validated_data):
        if 'debt' in validated_data:
            raise serializers.ValidationError("You cannot update debt via API!")
        return super().update(instance, validated_data)