from django.db import models

# Create your models here.
class TodoInfo(models.Model):
    """Todo信息模型"""
    __tablename__ = "tb_user"
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=10,verbose_name='用戶名')
    done = models.BooleanField(max_length=10,verbose_name='是否完成')

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'todoInfo'
        verbose_name = 'todo'

class ExcelInfo(models.Model):
    __tablename__ = "tb_excel"
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=50,verbose_name='用戶名')
    email = models.EmailField(max_length=254,verbose_name='電子郵件')
    company = models.CharField(max_length=50,verbose_name='公司名')
    birthdate = models.DateTimeField(verbose_name='生日')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'excelInfo'
        verbose_name = 'excel'
