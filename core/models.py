from django.db import models


class CodeInfo(models.Model):
    value = models.CharField(max_length=100,null=True)
    class Meta:
        db_table = 'enum_code'
class UserInfo(models.Model):
    id = models.BigIntegerField(unique=True,primary_key=True)
    uid = models.CharField(max_length=100,null=True)
    pwd = models.CharField(max_length=100,null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    code = models.ForeignKey(CodeInfo,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'user_info'