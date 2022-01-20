from .models import Product

from foodtruck.serializers import TruckSerializer

from main.utils import DynamicFieldsModelSerializer


class ProductSerializer(DynamicFieldsModelSerializer):
    """
    Serializer on the Product model.

    Lookup Field: slug.

    Fields: uuid, name, slug, info, image, price, quantity, is_available, truck,
    reviews, and likes.
    """
    truck = TruckSerializer(
        fields=('uuid', 'name', 'slug', 'images',), extra_fields=('profile_image',))

    class Meta:
        model = Product
        lookup_field = 'slug'
        fields = ('uuid', 'name', 'slug', 'info', 'image', 'price',
                  'quantity', 'is_available', 'truck',)
