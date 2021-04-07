from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from author.models import Author
# Register your models here.



class AuthorAdmin(UserAdmin):
    filter_horizontal = ('admirers',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                       'rock_type',
                       'interested_in',
                       'admirers',
                       'bio',
                       'created_at',
                       'birthday',
                       'profilepic')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": (
                       'rock_type',
                       'interested_in',
                       'admirers',
                       'bio',
                       'created_at',
                       'birthday',
                       'profilepic')
        }),
    )


admin.site.register(Author, AuthorAdmin)
