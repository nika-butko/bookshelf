import collections

from django.conf import settings
from django.views import generic

from .models import Book, Author


class IndexView(generic.ListView):
    template_name = 'books/index.djt'
    context_object_name = 'latest_books_list'

    def get_queryset(self):
        """Return the last five published books."""
        return Book.objects.order_by('-created_at')[:5]


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.djt'

    def get_queryset(self):
        """
        Get book.
        """
        return Book.objects

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['media'] = repr(settings.MEDIA_ROOT)
        return context


class AuthorsListView(generic.ListView):
    template_name = 'books/authors_list.djt'
    context_object_name = 'authors_list'

    def get_queryset(self):
        """Return the last five published books."""
        return Author.objects.order_by('-created_at')


class AuthorView(generic.DetailView):
    model = Author
    template_name = 'books/author_detail.djt'

    def get_queryset(self):
        return Author.objects

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AuthorView, self).get_context_data(**kwargs)
        author = super(AuthorView, self).get_object()
        books = Book.objects.filter(authors__id=author.id)
        context['grouped_books'] = self.group_books(books)
        return context

    def group_books(self, books):
        grouped_books = collections.defaultdict(dict)

        for book in books:
            for series in book.series.all():
                grouped_books[series.title] = {book}

        return dict(grouped_books)
