# django
### init
- python -m venv venv
- venv\Scripts\activate 進入虛擬環境
- python -m pip install --upgrade pip
- pip freeze > requirements.txt
- pip install django
- pip install python-dotenv
- pip install djangorestframework 
- https://www.django-rest-framework.org/#installation
### 1.django-admin startproject [項目名稱]
### 2.python manage.py startapp app01
- python manage.py runserver 啟動server
### 3.pip install djangorestframework 
- 註冊
    INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    'rest_framework'
]
- drf配置 REST_FRAMEWORK = {"UNAUTHENTICATED_USER": None} 不然會抱錯
### 4.urls.py 配置路由
### 5.app01/views.py 配置
- class drf用法
class InfoView(APIView):
    def get(self,request):
        return Response({'status':True,'message':'success'})
### FBV與CBV
### request對象(基於drf二次封裝)
- oop知識
- drf請求流程
### app(介紹)
- settings.py 項目配置        常常操作
- urls.py URL和函數的對應關係  常常操作
- asgi.py 接收網路請求 異步
- wsgi.py 接收網路請求 同步
- manage.py 項目的管理 啟動項目 創建app 數據管理
### 數據庫
--------------------------
- python manage.py makemigrations
- python manage.py migrate
INSTALLED_APPS = [
    # "django.contrib.admin",
    # "django.contrib.auth",
    # "django.contrib.contenttypes",
    # "django.contrib.sessions",
    # "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "app01"
] 要註冊app01
- 定義類型 https://docs.djangoproject.com/zh-hans/5.0/ref/models/fields/
### 使用python manage.py shell
- from app01.models import TodoInfo
- TodoInfo.objects.create(name='Jack',done=True) 直接添加數據

### Serializer 序列化器

### 遇到導包失敗
- deactivate
- Remove-Item -Recurse -Force C:\Users\User\Desktop\flask\flask_model\venv
- python -m venv venv 
- 重來


### sudo apt update
### sudo apt install docker-compose
### docker-compose build 
### docker-compose up -d

### ngrok
### http://localhost:4040/ 裡面訪問 

### git 設定隱私 token 圖片教學

### 佈署上gcp後 ngrok 要打開防火牆 4040