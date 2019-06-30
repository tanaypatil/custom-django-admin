from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from django.contrib.admin.widgets import FilteredSelectMultiple
from import_export import resources
from jet.admin import CompactInline


class UserImageInline(admin.TabularInline):
    extra = 0
    model = UserImage
    show_change_link = True
    fields = ('img', 'alt_text', 'image_tag')
    readonly_fields = ['image_tag']


class SkuInline(admin.TabularInline):
    extra = 0
    model = Sku


class SocialLinkInline(admin.StackedInline):
    extra = 0
    model = SocialLink


class AlternateAddressInline(admin.TabularInline):
    extra = 0
    model = AlternateAddress
    show_change_link = True


class UserLogInline(CompactInline):
    extra = 0
    model = Log
    show_change_link = True


class OrderInline(admin.StackedInline):
    extra = 0
    model = Order
    show_change_link = True
    show_full_result_count = True


class InstaAlbumInline(admin.StackedInline):
    extra = 0
    model = InstaAlbum
    show_change_link = True
    show_full_result_count = True


class LogResource(resources.ModelResource):
    class Meta:
        model = Log
        exclude = ['']
        fields = ('id', 'user__name', 'user__phone1', 'employee_name', 'date_time', 'mode', 'interaction')


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        fields = ('id', 'user__name', 'user__phone1', 'portal', 'order_id', 'order_date', 'method', 'shipping_cost',
                  'dispatch_date', 'delivery_vendor', 'tracking_id', 'delivery_date', 'note', 'review')


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        exclude = ['tag', 'places_lived', 'date_added', 'orders']


class UserAdmin(ImportExportModelAdmin):
    inlines = [UserImageInline, SocialLinkInline, AlternateAddressInline, UserLogInline, OrderInline, InstaAlbumInline]
    readonly_fields = ['date_added']
    icon = '<i class="material-icons">person_outline</i>'
    ordering = ['-date_added']
    list_display = ['phone1', 'name', 'user_type', 'email', 'city', ]
    list_editable = ['user_type']
    search_fields = ['name', 'alt_name', 'phone1', 'phone2', 'email', 'pincode', 'dob']
    list_filter = ['tag', 'city', 'state', 'age_range', 'gender', 'income_level', 'occupation', 'marital_status',
                   'rating', 'dob', 'user_type']
    fieldsets = (
        ('BasicInfo', {
            'classes': ('wide',),
            'fields': ('name', 'middle_name', 'last_name', 'alt_name', 'dob', 'phone1', 'phone2', 'address', 'city', 'pincode',
                       'state', 'email', 'tag', 'user_type', 'date_added')
        }),
        ('Persona', {
            'classes': ('wide',),
            'fields': ('age_range', 'gender', 'income_level', 'places_lived', 'occupation', 'occupation_details',
                       'marital_status', 'spouse_and_children', 'user_persona', 'rating')
        })
    )

    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple("Selected", is_stacked=False)},
    }

    resource_class = UserResource

    class Meta:
        model = User
        verbose_name = "Consumer"
        verbose_name_plural = "Consumers"


class CityAdmin(admin.ModelAdmin):
    search_fields = ['name']
    icon = '<i class="material-icons">location_city</i>'


class LogAdmin(ImportExportModelAdmin):
    list_display = ['user', 'mode', 'date_time']
    search_fields = ['user__name', 'interaction', 'user__phone1', 'user__phone2', 'date_time']
    list_filter = ['date_time', 'employee_name', 'user__phone1', 'user__name']
    ordering = ['date_time']
    resource_class = LogResource


class SkuAdmin(admin.ModelAdmin):
    list_display = ['order', 'idn']
    list_filter = ['quantity']
    search_fields = ['price', 'idn', 'discount', 'order__order_id']
    icon = '<i class="material-icons">fingerprint</i>'


class SocialLinkAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">insert_link</i>'
    search_fields = ['user__phone1']


class TagAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_filter = ['active']
    icon = '<i class="material-icons">compare_arrows</i>'


class UserImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'alt_text']
    search_fields = ['user__phone1', 'alt_text', 'user__name', 'user__phone2']
    fields = ('img', 'user', 'alt_text', 'image_tag')
    readonly_fields = ['image_tag']
    icon = '<i class="material-icons">burst_mode</i>'


class OrderAdmin(ImportExportModelAdmin):
    list_display = ['user', 'order_id', 'order_date', 'shipping_cost']
    list_select_related = True
    list_filter = ['portal', 'method', 'order_date', 'delivery_vendor', 'user__phone1', 'user__name']
    search_fields = ['order_id', 'tracking_id', 'order_date', 'user__phone1']
    inlines = [SkuInline]
    resource_class = OrderResource


class InstaPicInline(admin.TabularInline):
    extra = 0
    model = InstaPic
    fields = ('name', 'img', 'image_large', 'caption')
    readonly_fields = ['image_large']
    show_change_link = True


class InstaCommentInline(admin.TabularInline):
    extra = 0
    model = InstaComments
    show_change_link = True


class InstaAlbumAdmin(admin.ModelAdmin):
    list_display = ['album_name', 'username', 'insta_id', 'user_type']
    search_fields = ['album_name', 'username', 'insta_id']
    inlines = [InstaPicInline]
    list_editable = ['user_type']


class InstaPicAdmin(admin.ModelAdmin):
    list_display = ['name', 'album']
    search_fields = ['name', 'album']
    fields = ['name', 'album', 'img', 'image_large', 'caption']
    readonly_fields = ['image_large']
    inlines = [InstaCommentInline]


class InstaCommentAdmin(admin.ModelAdmin):
    list_display = ['pic', 'comment']
    list_search = ['pic', 'comment']


class FbProfileLinkInline(admin.StackedInline):
    fields = ('url', )
    extra = 0
    show_change_link = True
    model = FbProfileLink


class FbWorkInline(admin.TabularInline):
    model = FbWork
    fields = ('title', 'text', 'additional')
    extra = 0
    show_change_link = True


class FbEducationInline(admin.TabularInline):
    model = FbEducation
    fields = ('title', 'text', 'additional')
    extra = 0
    show_change_link = True


class FbFavouriteInline(admin.StackedInline):
    model = FbFavourite
    fields = ('label', 'text')
    extra = 0
    show_change_link = True


class FbProfileAdmin(admin.ModelAdmin):
    list_display = ['pname', 'name', 'user_type', 'hometown', 'current_city']
    list_filter = ['hometown', 'current_city']
    list_editable = ['user_type']
    search_fields = ['name', 'link', 'hometown', 'current_city']
    readonly_fields = ['pp_large', 'cp_large']
    inlines = [FbProfileLinkInline, FbFavouriteInline, FbEducationInline, FbWorkInline]


admin.site.register(User, UserAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(UserImage, UserImageAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Sku, SkuAdmin)
admin.site.register(InstaAlbum, InstaAlbumAdmin)
admin.site.register(InstaPic, InstaPicAdmin)
admin.site.register(InstaComments, InstaCommentAdmin)
admin.site.register(FbProfile, FbProfileAdmin)
"""admin.site.register(FbProfileLink)
admin.site.register(FbWork)
admin.site.register(FbEducation)
admin.site.register(FbFavourite)"""

