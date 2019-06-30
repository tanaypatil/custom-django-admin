from django.db import models
from django.db.models import Count


class Tag(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField(max_length=300)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


class User(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    middle_name = models.CharField(max_length=10, blank=True, null=True)
    last_name = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(help_text="Date Of Birth", null=True, blank=True)
    alt_name = models.CharField(max_length=40, blank=True, null=True)
    phone1 = models.CharField(max_length=13, blank=False, null=False, unique=True)
    phone2 = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True)
    pincode = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    type_choices = (('Customer', 'Customer'), ('Prospect', 'Prospect'))
    user_type = models.CharField(blank=True, null=True, max_length=9, choices=type_choices)
    # Persona Fields
    gender_choices = (('m', 'male'), ('f', 'female'))
    age_ranges = (('10-15', '10-15'), ('15-18', '15-18'), ('18-20', '18-20'), ('20-25', '20-25'), ('25-30', '25-30'),
                  ('30-35', '30-35'), ('35-40', '35-40'), ('40-45', '40-45'), ('45-50', '45-50'), ('50-55', '50-55'))
    income_choices = (('affluent', 'affluent'), ('UpperMiddle', 'UpperMiddle'), ('LowerMiddle', 'LowerMiddle'))
    occupation_choices = (('student', 'student'), ('Working', 'Working'), ('Housewife', 'Housewife'),
                          ('Other', 'Other'))
    marital_choices = (('married', 'married'), ('unmarried', 'unmarried'), ('divorced', ' divorced'))
    rating_choices = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    age_range = models.CharField(choices=age_ranges, max_length=7, default='0', null=True, blank=True)
    gender = models.CharField(choices=gender_choices, max_length=7, default='m', null=True, blank=True)
    income_level = models.CharField(choices=income_choices, max_length=20, null=True, blank=True)
    places_lived = models.ManyToManyField(City, blank=True)
    occupation = models.CharField(choices=occupation_choices, max_length=15, null=True, blank=True)
    occupation_details = models.TextField(max_length=300, null=True, blank=True)
    marital_status = models.CharField(choices=marital_choices, max_length=12, null=True, blank=True)
    spouse_and_children = models.TextField(max_length=300, null=True, blank=True)
    user_persona = models.TextField(max_length=1000, null=True, blank=True)
    rating = models.CharField(choices=rating_choices, null=True, max_length=1, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Consumer"
        verbose_name_plural = "Consumers"

    @staticmethod
    def autocomplete_search_fields():
        return 'phone1', 'name', 'phone2'


class AlternateAddress(models.Model):
    address = models.CharField(max_length=500, null=True)
    city = models.CharField(max_length=20)
    pincode = models.IntegerField()
    state = models.CharField(max_length=15)
    user = models.ForeignKey(User, related_name='alternate_address')

    def __str__(self):
        return self.city

    def __unicode__(self):
        return self.city

    class Meta:
        verbose_name = "AlternateAddress"
        verbose_name_plural = "Alternate Addresses"


class UserImage(models.Model):
    img = models.ImageField(upload_to='user_images/', blank=True, null=True)
    user = models.ForeignKey(User, related_name='user_image')
    alt_text = models.CharField(blank=False, max_length=10)

    def __str__(self):
        return self.alt_text

    def __unicode__(self):
        return self.alt_text

    def image_tag(self):
        return u'<img width="160" height="160" src="%s" />' % self.img.url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = "User Image"
        verbose_name_plural = "User Images"

    @staticmethod
    def autocomplete_search_fields():
        return 'user__phone1', 'user__name', 'user__phone2'


class Log(models.Model):
    mode_choices = (('call', 'call'), ('whatsapp', 'whatsapp'), ('email', 'email'))
    employee_name = models.CharField(blank=False, max_length=35)
    date_time = models.DateTimeField()
    mode = models.CharField(choices=mode_choices, blank=False, max_length=15)
    user = models.ForeignKey(User, related_name='user_log')
    interaction = models.TextField(max_length=5000)

    def __str__(self):
        return self.mode

    def __unicode__(self):
        return self.mode

    @staticmethod
    def autocomplete_search_fields():
        return 'user__phone1', 'user__name', 'user__phone2'


class Order(models.Model):
    user = models.ForeignKey(User)
    payment_choices = (('pp', 'Prepaid'), ('cod', 'Cash on Delivery'), ('c', 'cash'))
    portal = models.CharField(max_length=25)
    order_id = models.CharField(max_length=50)
    order_date = models.DateField(blank=True, null=True)
    method = models.CharField(choices=payment_choices, max_length=25, default=None)
    shipping_cost = models.FloatField()
    dispatch_date = models.DateField(blank=True, null=True)
    delivery_vendor = models.CharField(max_length=25, blank=True)
    tracking_id = models.CharField(max_length=35, blank=True)
    delivery_date = models.DateField(blank=True, null=True)
    note = models.TextField(max_length=300, blank=True)
    review = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.order_id

    def __unicode__(self):
        return self.order_id

    def getcount(self):
        count = Order.objects.values('user').annotate(dcount=Count('user'))
        return count

    @staticmethod
    def autocomplete_search_fields():
        return 'user__phone1', 'user__name', 'user__phone2', 'order_id'


class Sku(models.Model):
    idn = models.CharField(max_length=15)
    quantity = models.IntegerField()
    price = models.FloatField()
    discount = models.IntegerField()
    order = models.ForeignKey(Order, related_name='product_ordered')

    def __str__(self):
        return self.idn

    def __unicode__(self):
        return self.idn


class SocialLink(models.Model):
    url = models.URLField(blank=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.url

    def __unicode__(self):
        return self.url


class InstaAlbum(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, help_text="Consumer Object. Attach if exists.")
    username = models.CharField(max_length=25, blank=False, null=True, help_text="User Name")
    insta_id = models.CharField(max_length=50, blank=False, null=True, help_text="Instagram ID")
    type_choices = (('Customer', 'Customer'), ('Prospect', 'Prospect'))
    user_type = models.CharField(blank=True, null=True, max_length=9, choices=type_choices)

    def album_name(self):
        return self.username+"_InstaAlbum"

    def __str__(self):
        return self.username+"_InstaAlbum"

    class Meta:
        verbose_name = "Instagram Album"
        verbose_name_plural = "Instagram Albums"


class InstaPic(models.Model):
    img = models.ImageField(upload_to='insta/', blank=False, null=True)
    album = models.ForeignKey(InstaAlbum)
    name = models.CharField(max_length=25, blank=False, null=True)
    caption = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    def image_large(self):
        return u'<img width="150" height="100" src="%s" />' % self.img.url

    def img_url(self):
        return self.img.url

    image_large.short_description = 'Image'
    image_large.allow_tags = True

    class Meta:
        verbose_name = "Instagram Pic"
        verbose_name_plural = "Instagram Pics"


class InstaComments(models.Model):
    comment = models.CharField(max_length=150, blank=False, null=True)
    pic = models.ForeignKey(InstaPic)

    def __str__(self):
        return str(self.pic)

    class Meta:
        verbose_name = "Instagram Comment"
        verbose_name_plural = "Instagram Comments"


class FbProfile(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    link = models.URLField(verbose_name="Profile Link", unique=True, blank=False)
    hometown = models.CharField("Home Town", max_length=30, blank=True, null=True)
    current_city = models.CharField("Current City", max_length=30, blank=True, null=True)
    profile_pic = models.ImageField("Profile Picture", upload_to="fb/", null=True)
    cover_pic = models.ImageField("Cover Picture", upload_to="fb/", null=True)
    type_choices = (('Customer', 'Customer'), ('Prospect', 'Prospect'))
    user_type = models.CharField(blank=True, null=True, max_length=9, choices=type_choices)

    def __str__(self):
        return self.name

    def pname(self):
        return self.name+"_FacebookProfile"

    def pp_large(self):
        return u'<img width="100" height="100" src="%s" />' % self.profile_pic.url

    def cp_large(self):
        return u'<img width="250" height="100" src="%s" />' % self.cover_pic.url

    pp_large.short_description = 'Image'
    pp_large.allow_tags = True

    cp_large.short_description = 'Image'
    cp_large.allow_tags = True

    class Meta:
        verbose_name = "Facebook Profile"
        verbose_name_plural = "Facebook Profiles"


class FbProfileLink(models.Model):
    profile = models.ForeignKey(FbProfile)
    url = models.URLField(blank=False, null=True)

    def __str__(self):
        return self.profile.name


class FbFavourite(models.Model):
    text = models.CharField(max_length=100, blank=False, null=True)
    label = models.CharField(max_length=60, blank=False, null=True)
    profile = models.ForeignKey(FbProfile)

    def name(self):
        return self.profile.name+"_"+self.label

    def __str__(self):
        return self.profile.name+"_"+self.label


class FbEducation(models.Model):
    title = models.TextField(max_length=500, blank=False, null=True)
    text = models.TextField(max_length=500, blank=False, null=True)
    additional = models.TextField(max_length=500, blank=False, null=True)
    profile = models.ForeignKey(FbProfile)

    def name(self):
        return self.profile.name+"_Education"

    def __str__(self):
        return self.profile.name+"_Education"


class FbWork(models.Model):
    title = models.TextField(max_length=500, blank=False, null=True)
    text = models.TextField(max_length=500, blank=False, null=True)
    additional = models.TextField(max_length=500, blank=False, null=True)
    profile = models.ForeignKey(FbProfile)

    def name(self):
        return self.profile.name+"_Work"

    def __str__(self):
        return self.profile.name+"_Work"





