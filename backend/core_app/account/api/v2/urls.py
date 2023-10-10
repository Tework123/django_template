from django.urls import path

from account.api.v2.views import GetUserView

urlpatterns = [

    # path('', UsersView.as_view()),
    # re_path(r'^filter/(?P<email>[\w.@+-]+)/', UsersFilterView.as_view()),
    # re_path(r'^order_by/(?P<order_by>[\w.@+-]+)/', UsersOrderView.as_view()),
    # path('<int:pk>', UsersEditView.as_view()),
    # path('auth/', AuthUserView.as_view()),
    # path('logout/', UsersLogoutView.as_view()),
    path('', GetUserView.as_view()),
]
