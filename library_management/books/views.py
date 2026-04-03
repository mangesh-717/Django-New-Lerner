
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book, Category
from .forms import BookForm
from .scraper import scrape_books
from django.core.paginator import Paginator
from django.contrib.auth.models import Group


from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()

        group = Group.objects.get(name='User')
        user.groups.add(group)

        login(request, user)
        return redirect('book_list')

    return render(request, 'register.html', {'form': form})



@login_required
@permission_required('books.view_book', raise_exception=True)
def book_list(request):
    category_id = request.GET.get('category')
    books = Book.objects.all().order_by('id')

    if category_id:
        books = books.filter(category_id=category_id)

    paginator = Paginator(books, 10)  # 10 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    return render(request, 'book_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category_id
    })


@login_required
@permission_required('books.add_book', raise_exception=True)
def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'form': form})


@login_required
@permission_required('books.change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'form': form})


@login_required
@permission_required('books.delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')






@login_required
@permission_required('books.add_book', raise_exception=True)
def scrape_view(request):
    categories = Category.objects.all()

    if request.method == "POST":
        category_id = request.POST.get("category_id")
        category = Category.objects.get(id=category_id)

        scrape_books(category)

        return redirect('book_list')

    return render(request, "scrape.html", {"categories": categories})