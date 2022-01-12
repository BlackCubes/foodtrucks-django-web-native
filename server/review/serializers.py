from rest_framework import serializers

from .models import Review
from product.models import Product
from user.models import CustomUser


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer on the Review model.

    Lookup Field: uuid.

    Fields: uuid, review, created_at, updated_at, product, and user.
    """
    product = serializers.SlugRelatedField(
        slug_field='slug', queryset=Product.objects.all(), error_messages={
            'required': 'The product is required.',
            'null': 'The product cannot be empty.',
            'does_not_exist': 'The product does not exist.'})
    review = serializers.CharField(
        max_length=280, error_messages={
            'required': 'The review is required',
            'blank': 'The review cannot be empty.',
            'max_length': 'The review should be no more than 280 characters.'})
    user = serializers.SlugRelatedField(
        slug_field='username', queryset=CustomUser.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        lookup_field = 'uuid'
        fields = ('uuid', 'review', 'created_at',
                  'updated_at', 'product', 'user',)
