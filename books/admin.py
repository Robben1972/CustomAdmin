from django.contrib import admin
from .models import Book, Author 

# Register your models here.
class BookInline(admin.StackedInline):
    model = Book
    fields = ['title', 'price','published_date', 'in_stock']
    extra = 1


admin.site.register(Book)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_books']
    inlines = [BookInline]

    def total_books(self, obj):
        return obj.books.count()

admin.site.register(Author, AuthorAdmin)