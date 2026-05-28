# import time
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import User_insert_model




# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     """
#     Jab bhi User create ho ya update ho:
#     - Create: profile table me Show_Password me original password save
#     - Update: agar password change hua ho to Show_Password update
#     """
#     if created:
#         User_insert_model.objects.create(
#             auth_user=instance,
#             firstname=instance.first_name,
#             lastname=instance.last_name,
#             # username=instance.username,
#             email=instance.email,
#             # profile.Show_Password = raw_password,

#             Show_Password=getattr(instance, "_raw_password", ""),  # signal me raw_password handle
#             user_type="User",
#             user_created_on=int(time.time()),
#             user_updated_on=0,
#         )
#     else:
#          # 🔹 Existing user update
#         profile = getattr(instance, "profile", None)
#         if profile:
#             profile.firstname = instance.first_name
#             profile.lastname = instance.last_name
#             profile.username = instance.username
#             profile.email = instance.email
#             profile.Show_Password = instance._raw_password
#              # 🔹 Update user_type if present on instance
#             if hasattr(instance, "_user_type_update"):
#                 profile.user_type = instance._user_type_update
#             profile.user_updated_on = int(time.time())
#             profile.save()
#         # # ✅ User update ke time password check
#         # if hasattr(instance, "_raw_password"):
#         #     try:
#         #         profile = instance.profile
#         #         profile.user_updated_on = int(time.time())
#         #         profile.save()
#         #     except User_insert_model.DoesNotExist:
#         #         pass
