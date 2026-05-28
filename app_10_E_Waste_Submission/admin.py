# from django.contrib import admin
# from .E_Waste_Submission__API__1.models import E_Waste_Submission_Model

# @admin.register(E_Waste_Submission_Model)
# class E_Waste_Submission_Admin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'user',
#         'category',
#         'brand_name',
#         'model_name',
#         'status',
#         'pickup_type',
#         'created_at'
#     )
#     list_filter = ('status', 'pickup_type', 'category')
#     search_fields = ('address', 'phone', 'user__username', 'notes')
#     ordering = ('-created_at',)

#     def brand_name(self, obj):
#         return obj.category_brand_mapping.brand.brand_name
#     brand_name.short_description = 'Brand'

#     def model_name(self, obj):
#         return obj.model.model_name
#     model_name.short_description = 'Model'
