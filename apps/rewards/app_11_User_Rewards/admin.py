# from django.contrib import admin
# from .User_Rewards__API__1.models import User_Wallet_Model, Reward_Transaction_Model

# @admin.register(User_Wallet_Model)
# class User_Wallet_Admin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'total_points', 'created_at', 'updated_at')
#     search_fields = ('user__username',)

# @admin.register(Reward_Transaction_Model)
# class Reward_Transaction_Admin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'submission', 'points', 'type', 'created_at')
#     list_filter = ('type',)
#     search_fields = ('user__username', 'description')
