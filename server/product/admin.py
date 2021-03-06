from django.contrib import admin
from django.utils.html import format_html

from .models import Product
from review.admin import AddReviewInline, ViewReviewInline
from social.admin import AddLikeInline, ViewLikeInline


# PRODUCT INLINE
class ProductInline(admin.StackedInline):
    """
    Inline Model Admin for the Product model.
    """
    model = Product

    fieldsets = (
        (None, {'fields': ('name', 'image', 'image_tag', 'info', 'price',
         'quantity', 'is_available',)}),
    )
    readonly_fields = ('image_tag',)

    min_num = 1

    # Adding preview image.
    @admin.display(description='Preview')
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{0}" style="width: 45px; height: 45px" />'.format(obj.image.url))
        else:
            return '(No image)'


# PRODUCT ADMIN
class ProductAdmin(admin.ModelAdmin):
    """
    Model Admin for the Product model.
    """
    model = Product

    # Viewing all products
    list_display = ('name', 'truck', 'quantity', 'is_available',
                    'created_at', 'updated_at', 'image_tag',)
    list_display_links = ('name', 'truck',)
    list_filter = ('name', 'truck', 'is_available',)
    search_fields = ('name', 'truck__name',)
    ordering = ('slug',)

    # Viewing and changing on product
    fieldsets = (
        (None, {'fields': ('name', 'info', 'price',
         'quantity', 'is_available', 'truck',)}),
        ('Product Image', {'fields': ('image', 'image_tag')}),
        ('Additional Info', {
         'fields': ('uuid', 'slug', 'created_at', 'updated_at',)}),
    )
    readonly_fields = ('uuid', 'slug', 'created_at',
                       'updated_at', 'image_tag',)

    # Adding one new product
    add_fieldset = (
        (None, {'fields': ('name', 'info', 'price',
         'quantity', 'is_available', 'truck',)}),
    )

    # To be viewed on the product since these models have a foreign key.
    inlines = (AddLikeInline, ViewLikeInline,
               AddReviewInline, ViewReviewInline,)

    # Adding preview image.
    @admin.display(description='Preview')
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{0}" style="width: 45px; height: 45px;" />'.format(obj.image.url))
        else:
            return '(No image)'

    # To display the add_fielsets on the creation page.
    def get_fieldsets(self, request, obj=None):
        if not obj:
            self.inlines = []
            return self.add_fieldset

        self.inlines = (AddLikeInline, ViewLikeInline,
                        AddReviewInline, ViewReviewInline,)

        return super(ProductAdmin, self).get_fieldsets(request, obj)


admin.site.register(Product, ProductAdmin)
