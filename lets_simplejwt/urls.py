from django.contrib import admin
from django.urls import path, include
# 추가
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),

    # jwt토큰 발급을 위한 url 추가
    # simple-jwt 라이브러리에서 기본으로 제공하는 뷰로 사용하기 때문에 별도의 사용자 정의 뷰는 작성하지 않음
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('accounts.urls')),

]
