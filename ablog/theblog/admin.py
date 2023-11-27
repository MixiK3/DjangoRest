from django.contrib import admin
from .models import Post, Category, Profile, Comment, Reports, TypesOfArticles

from import_export.admin import ExportMixin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # метод list_display, отображает поле 'name'
    list_filter = ('name',)  # метод list_filter, позволяет фильтровать записи по полю 'name'
    search_fields = ('name',)  # атрибут search_fields, позволяет выполнять поиск по полю 'name'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    @admin.display(description='Пользователь')
    def user_display(self, obj):
        return obj.user.username  # метод @admin.display позволяет отображать данные из метода 'user_display' в админке

    list_display = (
        'user_display',
        'bio',
        'telegram_url',
    )  # метод list_display, отображает поля 'user_display', 'bio' и 'telegram_url'


@admin.register(Post)
class PostAdmin(ExportMixin, admin.ModelAdmin):
    @admin.display(description='Лайки')
    def total_likes_display(self, obj):
        return obj.total_likes()  # метод @admin.display позволяет отображать данные из метода 'total_likes_display' в админке

    list_display = ('title', 'author',
                    'total_likes_display')  # метод list_display, отображает поля 'title', 'author' и 'total_likes_display'
    list_filter = ('category',)  # метод list_filter, позволяет фильтровать записи по полю 'category'
    inlines = []  # атрибут inlines, позволяет добавить встраиваемые объекты (например, редактирование связанных объектов)
    date_hierarchy = 'post_date'  # атрибут date_hierarchy, позволяет навигацию по дате (группировка объектов по дате)
    filter_horizontal = (
    'likes',)  # атрибут filter_horizontal, позволяет отображать ManyToMany-связи в виде горизонтальных фильтров
    list_display_links = ('title',
                          'author')  # атрибут list_display_links, позволяет добавить ссылки на редактирование объектов из list_display
    raw_id_fields = ('author',)  # атрибут raw_id_fields, позволяет использовать строковые поля выбора без поиска
    search_fields = ('title',
                     'author__username')  # атрибут search_fields, позволяет выполнять поиск по полям 'title' и 'author__username'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','post')  # метод list_display, отображает поле 'name'
    list_filter = ('name',)  # метод list_filter, позволяет фильтровать записи по полю 'name'
    search_fields = ('name',)  # атрибут search_fields, позволяет выполнять поиск по полю 'name'


@admin.register(Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ('name_users', 'post')
    list_filter = ('post',)
    search_fields = ('name_users', 'post__title')

@admin.register(TypesOfArticles)
class TypesOfArticlesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)