from django.contrib import admin

from .models import booksignuptbl, Review, enquiryTbl, Newsletter, Contact, Book, category

# Register your models here.
admin.site.register(booksignuptbl)
admin.site.register(Review)
admin.site.register(enquiryTbl)
admin.site.register(Newsletter)
admin.site.register(Contact)

admin.site.register(category)
admin.site.register(Book)