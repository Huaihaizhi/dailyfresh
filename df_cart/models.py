from django.db import models

class CartInfo(models.Model):
	user=models.ForeignKey('df_user.UserInfo',on_delete=models.CASCADE)
	goods=models.ForeignKey('df_goods.GoodsInfo',on_delete=models.CASCADE)
	count=models.IntegerField()