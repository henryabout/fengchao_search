from django.db import models

class Category(models.Model):
	class Meta:
		db_table = 'category'

	keyword = models.CharField(max_length=80)
	weight = models.DecimalField(max_digits=20, decimal_places=10)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)




