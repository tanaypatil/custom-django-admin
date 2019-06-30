from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField(max_length=300)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Salon(models.Model):
    catg_choices = (('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C', 'C'))
    salon_name = models.CharField(max_length=20, blank=True)
    owner_name = models.CharField(max_length=40, blank=True)
    owner_phone = models.CharField(max_length=13, blank=False, unique=True)
    alt_name = models.CharField(max_length=40, blank=True)
    alt_phone1 = models.CharField(max_length=13, blank=True)
    alt_phone2 = models.CharField(max_length=13, blank=True)
    website = models.URLField(blank=True)
    email1 = models.EmailField(blank=True)
    email2 = models.EmailField(blank=True)
    type_choices = (('Customer', 'Customer'), ('Prospect', 'Prospect'))
    salon_type = models.CharField(blank=True, null=True, max_length=9, choices=type_choices)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=20, blank=True)
    pincode = models.IntegerField(blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    state = models.CharField(max_length=20, blank=True)
    rating = models.CharField(choices=catg_choices, max_length=3)
    app_installed = models.BooleanField()
    video_tutorial = models.BooleanField()
    date_added = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.owner_phone

    def __unicode__(self):
        return self.owner_phone

    class Meta:
        verbose_name = "Salon"
        verbose_name_plural = "Salons"


class Log(models.Model):
    mode_choices = (('call', 'call'), ('whatsapp', 'whatsapp'), ('email', 'email'))
    employee_name = models.CharField(blank=False, max_length=35)
    date_time = models.DateTimeField()
    mode = models.CharField(choices=mode_choices, blank=False, max_length=15)
    user = models.ForeignKey(Salon, related_name='salon_log')
    interaction = models.TextField(max_length=5000)

    def __str__(self):
        return self.mode

    def __unicode__(self):
        return self.mode

    @staticmethod
    def autocomplete_search_fields():
        return 'user__salon_name', 'user__owner_phone'


class UserImage(models.Model):
    img = models.ImageField(upload_to='user_images/', blank=True, null=True)
    salon = models.ForeignKey(Salon, related_name='salon_image')
    alt_text = models.CharField(blank=False, max_length=10)

    def __str__(self):
        return self.alt_text

    def __unicode__(self):
        return self.alt_text

    def image_tag(self):
        return u'<img width="160" height="160" src="%s" />' % self.img.url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Order(models.Model):
    salon = models.ForeignKey(Salon)
    payment_choices = (('pp', 'Prepaid'), ('cod', 'Cash on Delivery'), ('c', 'cash'))
    portal = models.CharField(max_length=25)
    order_id = models.CharField(max_length=50)
    order_date = models.DateField(null=True)
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

    @staticmethod
    def autocomplete_search_fields():
        return 'salon__salon_name', 'salon__owner_phone', 'order_id'


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
