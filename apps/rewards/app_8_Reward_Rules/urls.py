from django.urls import path
from app_8_Reward_Rules.Views__Files.reward_rule_view import Reward_Rule_Public_View

urlpatterns = [
    path("reward-rule/", Reward_Rule_Public_View.as_view()),

]