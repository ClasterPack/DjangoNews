from django.contrib import admin
from .models import Post, PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage
    extra =0


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'status', 'created_on',
    )
    list_filter = ("status",)
    search_fields = ['title', 'content', ]
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PostImageAdmin]

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
