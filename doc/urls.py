from django.urls import path,include
from rest_framework import routers
# from .views
# from doc.views import auth
# from doc.views import documentViewset
import doc.views as views

router=routers.DefaultRouter()
router.register(r'documents',views.document.DocumentViewset)
router.register(r'groups',views.group.GroupViewset)
router.register(r'permissions',views.permissions.PermissionViewset)
router.register(r'users',views.user.UserViewset)
# router.register(r'')
urlpatterns = router.urls

urlpatterns += [
    path('auth/authorize/', views.auth.OAuthAuthorizeView.as_view(), name='oauth-authorize'),
    path('auth/callback/', views.auth.oauth2_callback.as_view(), name='oauth-callback'),
    path('get_user_data/', views.auth.GetUserDataView.as_view(), name='get_user_data'),
    # path('new_document/',doc.views.document.DocumentViewset.as_view({'get': 'list'}),name='document'),
    # path('groups/',doc.views.group.GroupViewset.as_view({'get': 'list'},name='group'))

]

