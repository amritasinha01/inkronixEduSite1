from django.contrib import admin
from .models import allCategory, subCourse, Post, Lecture, Cart, Orders, OrderUpdate, ContactMessage, Lecture2,Lecture3,Lecture4



class subCourseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'popularity', 'featured', 'bookcount', 'price', 'discounted_price']

class allCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'book_image']

admin.site.register(subCourse, subCourseModelAdmin)
admin.site.register(allCategory, allCategoryModelAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    pass

admin.site.register(Cart, CartAdmin)
admin.site.register(Orders)
admin.site.register(OrderUpdate)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number','message')
    search_fields = ('name', 'email', 'number','message')


# Register your models here.
#class subCourseModelAdmin(admin.ModelAdmin):
    #list_display = ['id', 'title', 'category', 'popularity', 'featured', 'bookcount','price','discounted_price']

#class allCategoryModelAdmin(admin.ModelAdmin):
    #list_display = ['id', 'name', 'book_image']

#admin.site.register(allCategory)



#admin.site.register(subCourse)

admin.site.register(Post)

admin.site.register(Lecture)
admin.site.register(Lecture2)
admin.site.register(Lecture3)
admin.site.register(Lecture4)
