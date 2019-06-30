from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple
from import_export import resources
from jet.admin import CompactInline


class UserImageInline(admin.TabularInline):
    extra = 0
    model = UserImage
    show_change_link = True
    fields = ('img', 'alt_text', 'image_tag')
    readonly_fields = ['image_tag']


class UserLogInline(CompactInline):
    extra = 0
    model = Log
    show_change_link = True


class OrderInline(admin.StackedInline):
    extra = 0
    model = Order
    show_change_link = True
    show_full_result_count = True


class LogResource(resources.ModelResource):
    class Meta:
        model = Log
        exclude = ['']
        fields = ('id', 'user__salon_name', 'user__owner_phone', 'employee_name', 'mode', 'interaction')


class OrderResource(resources.ModelResource):

    class Meta:
        model = Order
        exclude = ['id']
        fields = ('id', 'salon__salon_name', 'salon__owner_phone', 'portal', 'order_id', 'order_date', 'method',
                  'shipping_cost', 'dispatch_date', 'delivery_vendor', 'tracking_id', 'delivery_date', 'note_review')


class UserResource(resources.ModelResource):
    class Meta:
        model = Salon
        exclude = ['tag', 'date_added', ]


class SalonAdmin(ImportExportModelAdmin):
    inlines = [UserImageInline, UserLogInline, OrderInline]
    list_display = ['owner_phone', 'salon_type', 'salon_name', 'owner_name', 'city', 'rating']
    list_filter = ['rating', 'city', 'app_installed', 'video_tutorial', 'salon_type']
    list_editable = ['salon_type']
    search_fields = ['salon_name', 'owner_name', 'owner_phone', 'city', 'pincode', 'website', 'address']
    readonly_fields = ['date_added']
    ordering = ['-date_added']

    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple("Selected", is_stacked=False)},
    }

    resource_class = UserResource


class SkuAdmin(admin.ModelAdmin):
    list_display = ['order', 'idn']
    list_filter = ['quantity']
    search_fields = ['price', 'idn', 'discount', 'order__order_id']


class SkuInline(admin.TabularInline):
    extra = 0
    model = Sku


class OrderAdmin(ImportExportModelAdmin):
    list_display = ['salon', 'order_id', 'order_date']
    list_filter = ['portal', 'method', 'order_date', 'delivery_vendor', 'salon__salon_name', 'salon__owner_phone']
    search_fields = ['order_id', 'tracking_id', 'order_date', 'user__phone1']
    inlines = [SkuInline]
    resource_class = OrderResource


class TagAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_filter = ['active']


class UserImageAdmin(admin.ModelAdmin):
    list_display = ['salon', 'alt_text']
    search_fields = ['salon__owner_phone', 'alt_text', 'salon__salon_name', ]
    fields = ('img', 'salon', 'alt_text', 'image_tag')
    readonly_fields = ['image_tag']
    icon = '<i class="material-icons">burst_mode</i>'


class LogAdmin(ImportExportModelAdmin):
    list_display = ['user', 'mode', 'date_time']
    search_fields = ['user__salon_name', 'interaction', 'user__owner_phone', 'date_time']
    list_filter = ['date_time', 'employee_name', 'user__owner_phone', 'user__salon_name']
    resource_class = LogResource


admin.site.register(Salon, SalonAdmin)
admin.site.register(Sku, SkuAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(UserImage, UserImageAdmin)
admin.site.register(Log, LogAdmin)
