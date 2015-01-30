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

	def __unicode__(self):
		return self.name

class Genre(models.Model):
	class Meta:
		db_table = 'genre'

	DIMENSION_CHOICES = (
		(NATURE, u'自然风光'),
		(CULTURE, u'人文建筑'),
		(HISTORY, u'历史古迹'),
		(TIME, u'时间'),
		(PLACE, u'地理位置'),
		(FIGURE, u'人物'),
		(PRICE, u'价格'),
	)

	name = models.CharField(max_length=80)
	dimension = models.CharField(max_length=80, choices=DIMENSION_CHOICES)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class Category(models.Model):
	class Meta:
		db_table = 'category'

	name = models.CharField(max_length=80)
	genre = models.CharField(max_length=80)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class Keyword(models.Model):
	class Meta:
		db_table = 'keyword'

	keyword = models.CharField(max_length=80)
	weight = models.DecimalField(max_digits=20, decimal_places=3)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class UserGenre(models.Models):
	user = models.ForeignKey(User)
	genre = models.ForeignKey(Genre)
	preference = models.DecimalField(max_digits=20, decimal_places=3)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class UserCategory(models.Models):
	user = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	preference = models.DecimalField(max_digits=20, decimal_places=3)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class UserKeyword(models.Models):
	user = models.ForeignKey(User)
	keyword = models.ForeignKey(Keyword)
	preference = models.DecimalField(max_digits=20, decimal_places=3)
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

	name = models.CharField(max_length=80)
	description = models.TextField(null=True, blank=True)
	general_type = models.CharField(max_length=80, choices=TYPE_CHOICES)
	continent = models.CharField(max_length=20, choices=CONTINENT_CHOICES)
	country = models.ForeignKey(Country)
	city = models.ForeignKey(City)
	address = models.CharField(max_length=200, blank=True)
	currency_unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
	hit_count = models.IntegerField(null=True, blank=True)
	comment_count = models.IntegerField(null=True, blank=True)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class Hotel(Destination):
	class Meta:
		db_table = 'hotel'

	GRADE_CHOICES = None
	
	SINGLE = 'single room'
	DOUBLE = 'double room'
	STANDARD = 'standard room'
	SUIT = 'suit room'
	
	ROOM_GRADE_CHOICES = (
		(SINGLE, u'单人间'),
		(DOUBLE, u'双人间'),
		(STANDARD, u'标准间'),
		(SUIT, u'套间'),
	)

	grade = models.CharField(max_length=20, choices=GRADE_CHOICES)
	room_grade = models.CharField(max_length=20, choices=ROOM_GRADE_CHOICES)
	original_price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
	discount_price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class Resort(Destination):
	class Meta:
		db_table = 'resort'

	office_hours = models.ForeignKey(OfficeHours, null=True, blank=True)
	original_price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
	discount_price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class TourProduct(models.Model):
	class Meta:
		db_table = 'tour_product'

	CATEGORY_CHOICES =

	name = models.CharField(max_length=80)
	description = models.TextField(blank=True)
	resort = models.ForeignKey(Resort)
	category = models.CharField(max_length=80, choices=CATEGORY_CHOICES)
	expiration = models.SmallIntegerField(null=True, blank=True)
	vendor = models.ForeignKey(Vendor)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class PackageTour(models.Model):
	class Meta:
		db_table = 'package_tour'

	LANG_CHOICES = (
		(CHINESE, u'汉语'),
		(ENGLISH, u'英语'),
		(JAPANESE, u'日语'),
		(SPANISH, u'西班牙语'),
	)

	FREQUENCY_CHOICES = (
		(DAILY, u'每天'),
		(WEEKLY, u'每周'),
		(MONTHLY, u'每月'),
	)

	name = models.CharField(max_length=80)
	description = models.TextField(blank=True)
	start_place = models.ForeignKey(City)
	end_place = models.ForeignKey(City)
	num_of_days = models.SmallIntegerField()
	service_lang = models.CharField(max_length=20, choices=LANG_CHOICES)
	service_start_date = models.DateTimeField()
	service_end_date = models.DateTimeField()
	service_day_of_week = models.charField(max_length=20, choices=OfficeHours.DAY_OF_WEEK_CHOICES)
	service_frequency = models.charField(max_length=20, choices=FREQUENCY_CHOICES)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)


class ResortPackageTour(models.Model):
	class Meta:
		db_table = 'resort_package_tour'

	resort = models.ForeignKey(Resort)
	package_tour = models.ForeignKey(PackageTour)
	order = models.IntegerField()
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class ResortUserComment(models.Model):
	class Meta:
		db_table = 'resort_user_comment'

	content = models.CharField(max_length=2000)
	user = models.ForeignKey(User)
	resort = models.ForeignKey(resort)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)

class HotelUserComment(models.Model):
	class Meta:
		db_table = 'hotel_user_comment'

	content = models.CharField(max_length=2000)
	user = models.ForeignKey(User)
	hotel = models.ForeignKey(Hotel)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	remark = models.TextField(blank=True)



