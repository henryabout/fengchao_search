from django.db import models

class User(models.Model):
	name = models.CharField(max_length=20)
	username = models.CharField(max_length=20, blank=True)
	password = models.CharField(max_length=80)
	phone_num = models.CharField(max_length=20, blank=True)
	email_address =models.CharField(max_length=80, blank=True)
	register_time = models.DateTimeField(auto_now_add=True)
	last_login_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class Category(models.Model):
	class Meta:
		db_table = 'dimension'

	name = models.CharField(max_length=80)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class Dimension(models.Model):
	class Meta:
		db_table = 'dimension'

	keyword = models.CharField(max_length=80)
	weight = models.DecimalField(max_digits=20, decimal_places=3)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class UserDimension(models.Models):
	user = models.ForeignKey(User)
	dimension = models.ForeignKey(Dimension)
	preference = models.DecimalField(max_digits=20, decimal_places=3)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class Destination(models.Model):
	HOTEL = 'hotel'
	RESORT = 'resort'

	TYPE_CHOICES = (
		(HOTEL, u'宾馆'),
		(RESORT, u'旅游景区'),
	)

	CONTINENT_CHOICES = (
		(ASIA, u'亚洲'),
		(NORTH_AMERICA, u'北美洲'),
		(SOUTH_AMERICA, u'南美洲'),
		(EUROPE, u'欧洲'),
		(AFRICA, u'非洲'),
		(OCEANIA, u'大洋洲'),
		(ANTARCTICA, u'南极洲'),
	)

	RMB = 'RMB'
	USD = 'USD'
	EUR = 'EUR'
	JPY = 'JPY'

	UNIT_CHOICES = (
		(RMB, u'人民币'),
		(USD, u'美元'),
		(EUR, u'欧元'),
		(JPY, u'日元'),
	)

	general_type = models.CharField(max_length=80, choices=TYPE_CHOICES)
	continent = models.CharField(max_length=20, choices=CONTINENT_CHOICES)
	country = models.ForeignKey(Country)
	city = models.ForeignKey(City)
	address = models.CharField(max_length=200, blank=True)
	price = models.SmallIntegerField(null=True, blank=True)
	currency_unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class Country(models.Model):
	name = models.CharField(max_length=20)
	continent = models.CharField(max_length=20, choices=CONTINENT_CHOICES)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class City(model.Model):
	name = models.CharField(max_length=20)
	continent = models.CharField(max_length=20, choices=CONTINENT_CHOICES)
	country = models.ForeignKey(Country)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class Hotel(Destination):
	class Meta:
		db_table = 'hotel'

	grade = models.CharField(max_length=20, choices=GRADE_CHOICES)
	room_grade = models.CharField(max_length=20, choices=ROOM_GRADE_CHOICES)
	original_price = models.SmallIntegerField(null=True, blank=True)
	discount_price = models.SmallIntegerField(null=True, blank=True)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class OfficeHours(models.Model):
	MON = 'Monday'
	TUE = 'Tuesday'
	WED = 'Wednesday'
	THU = 'Thursday'
	FRI = 'Friday'
	SAT = 'Saturday'
	SUN = 'Sunday'

	DAY_OF_WEEK_CHOICES = (
		MON, u''),
		TUE, u''),
		WED, u''),
		THU, u''),
		FRI, u''),
		SAT, u''),
		SUN, u''),
	)

	resort = models.ForeignKey(Resort)
	day_of_week = models.CharField(max_length=80, choices=DAY_OF_WEEK_CHOICES)
	office_hours_start = models.DateTimeField(null=True, blank=True)
	office_hours_end = models.DateTimeField(null=True, blank=True)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class Resort(Destination):
	class Meta:
		db_table = 'resort'

	description = models.TextField(null=True)
	office_hours = models.ForeignKey(OfficeHours, null=True, blank=True)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class TourProduct(models.Model):
	class Meta:
		db_table = 'tour_product'

	name = models.CharField(max_length=80)
	description = models.TextField(blank=True)
	resort = models.Foreignkey(Resort)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)


class PackageTour(models.Model):
	class Meta:
		db_table = 'package_tour'

	name = models.CharField(max_length=80)
	description = models.TextField(blank=True)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)










