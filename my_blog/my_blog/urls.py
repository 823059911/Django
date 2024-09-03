"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#不要忘了include
from django.urls import path, include
#url可以理解为访问网站时输入的网址链接，配置好url后Django才知道怎样定位app
# 新引入的模块
from django.conf import settings
from django.conf.urls.static import static
# 存放映射关系的列表
urlpatterns = [
    path('admin/', admin.site.urls),
     # 新增代码，配置app的url
    path('article/', include('article.urls', namespace='article')),
     # 用户管理
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
     # 密码重置
    path('password-reset/', include('password_reset.urls')),
    # 评论
    path('comment/', include('comment.urls', namespace='comment')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)