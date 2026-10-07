from urllib import request

from django.http import HttpResponse
from django.shortcuts import render

from .models import booksignuptbl, Newsletter, Contact, Book, Review, enquiryTbl, Order
from django.contrib import messages
from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    books=Book.objects.filter(is_mainpage=True)

    return render(request, 'index.html',  {'books':books})
def home(request):
    books=Book.objects.filter(is_mainpage=True)

    return render(request, 'home.html',{'books':books})

def about(request):
    return render(request, 'about.html')


def Books(request):

    books = Book.objects.filter(is_mainpage=True)

    return render(request, 'Books.html', {
        'books': books
    })

def story(request):
    books=Book.objects.filter(categories__name__iexact="story")
    return render(request, 'story.html',{"books":books})
def self(request):
    books=Book.objects.filter(categories__name__iexact="self")

    return render(request, 'self.html',{"books":books})
def science(request):
    books=Book.objects.filter(categories__name__iexact="science")

    return render(request, 'science.html',{"books":books})
def psychology(request):
    books=Book.objects.filter(categories__name__iexact="psychology")

    return render(request, 'psychology.html',{"books":books})
def programming(request):
    books=Book.objects.filter(categories__name__iexact="programming")

    return render(request, 'programming.html',{"books":books})
def Novels(request):
    books=Book.objects.filter(categories__name__iexact="novels")

    return render(request, 'Novels.html',{"books":books})
def medical(request):
    books=Book.objects.filter(categories__name__iexact="medical")

    return render(request, 'medical.html',{"books":books})
def law(request):
    books=Book.objects.filter(categories__name__iexact="law")

    return render(request, 'law.html',{"books":books})

def history(request):
     books = Book.objects.filter(categories__name__iexact="history")

     return render(request, 'history.html', {
        'books': books
     })
def free(request):
    books=Book.objects.filter(is_free=True)

    return render(request, 'free.html',{ "books":books})
def frpre(request):
    return render(request, 'free&premiumbook.html')
def finance(request):
    books=Book.objects.filter(categories__name__iexact="finance")

    return render(request, 'finance.html',{"books":books})
def exam(request):
    books=Book.objects.filter(categories__name__iexact="exam")

    return render(request, 'exam.html',{"books":books})
def english(request):
    books=Book.objects.filter(categories__name__iexact="english")

    return render(request, 'english.html',{"books":books})
def competetive(request):
    books=Book.objects.filter(categories__name__iexact="comptetive")

    return render(request, 'competetive.html',{"books":books})
def child(request):
    books=Book.objects.filter(categories__name__iexact="children")

    return render(request, 'child.html',{"books":books})
def bookdetailself(request):
    return render(request, 'bookdetailself.html')
def bookdetailnovel1(request):
    return render(request, 'bookdetailnovel1.html')
def bookdetailhistory(request):
    return render(request, 'bookdetail.html')
def academic(request):
    books=Book.objects.filter(categories__name__iexact="academic")

    return render(request, 'academic.html',{"books":books})
def bio(request):
    books=Book.objects.filter(categories__name__iexact="Bio")

    return render(request, 'bio.html',{"books":books})
def bookcategories(request):
    return render(request, 'bookcategories.html')
def bookdetaillaw(request):
    return render(request, 'bookdetaillaw.html')
def bookdetailacademic(request):
    return render(request, 'bookdetailacademic.html')
def bookdetailfinance(request):
    return render(request, 'bookdetailfinance.html')
def bookdetailexam(request):
    return render(request, 'bookdetailexam.html')
def bookdetailenglish(request):
    return render(request, 'bookdetailenglish.html')
def bookdetailcomptetive(request):
    return render(request, 'bookdetailcomptetive.html')
def bookdetailchild(request):
    return render(request, 'bookdetailchild.html')
def bookdetailbio(request):
    return render(request, 'bookdetailbio.html')
def bookdetailstory(request):
    return render(request, 'bookdetailstory.html')
def booksignup(request):
    return render(request,'books.html')
def bookdetailprograamming(request):
    return render(request, 'bookdetailprograamming.html')
def booksignupcode(request):
    a = request.POST.get("name")
    b = request.POST.get("email")
    c = request.POST.get("password")
    d = request.POST.get("confirm password")

    data = booksignuptbl.objects.filter(email=b).first()

    if not data:
        booksignuptbl.objects.create(
            name=a,
            email=b,
            password=c,
            confirm_password=d
        )

        messages.success(request, "Signup Successfully!")
        return redirect("index")

    else:
        messages.error(request, "Signup already exists!")
        return redirect("index")
def login(request):

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]

        user = booksignuptbl.objects.filter(
            email=email,
            password=password
        ).first()

        if user:
            request.session["user_id"] = user.id
            if "buy_book_id" in request.session:
                book_id = request.session["buy_book_id"]
                del request.session["buy_book_id"]
                return redirect("buy_now",book_id=book_id)
            return redirect("home")

        else:
            return render(
                request,
                "login.html",
                {"msg":"Invalid Email or Password"}
            )

    return render(request,"index.html")
def logincode(request):
    a=request.POST.get("email")
    b=request.POST.get("password")
    data=booksignuptbl.objects.filter(email=a).first()
    if not data:
        return HttpResponse("enter emailid wrong")

    else:
        if data.password == b:
            request.session['user'] = a


            next_page=request.POST.get("next")
            if next_page:
                return redirect(next_page)
            else:

                return redirect("index")
        else:
            return HttpResponse("password wrong")



def review(request):
    if request.method == "POST":
        name = request.POST.get("name")
        rating = request.POST.get("rating")
        message = request.POST.get("message")

        Review.objects.create(
            name=name,
            rating=rating,
            message=message
        )

        return redirect("review")

    reviews = Review.objects.all().order_by("-created_at")

    return render(request, "review.html", {
        "reviews": reviews
    })
from .models import enquiryTbl
def enquiry(request):
    return render(request,'enquiry.html')

def enquirycode(request):

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        book_name = request.POST.get("book_name")
        category = request.POST.get("category")
        enquiry = request.POST.get("enquiry")

        enquiryTbl.objects.create(
            name=name,
            phone=phone,
            book_name=book_name,
            category=category,
            enquiry=enquiry
        )

        return redirect("contact")

    return redirect("contact")


def newsletter(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, "This email is already subscribed.")
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, "You have subscribed successfully!")

        return redirect("index")

    return redirect("index")



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect("contact")

    return render(request, "contact.html")



def bookdetail(request, id):

    book = Book.objects.get(id=id)

    related_books = Book.objects.filter(
        categories__in=book.categories.all()
    ).exclude(id=book.id).distinct()

    return render(request, 'bookdetail.html', {
        'book': book,
        'related_books': related_books
    })
def buy_now(request, book_id):

    if "user_id" not in request.session:
        request.session['buy_now'] =True
        request.session["buy_book_id"] = book_id
        return redirect("login")


    return redirect('checkout',book_id=book_id)
def checkout(request, book_id):

    book = Book.objects.get(id=book_id)

    # Book ko session me save kar do
    request.session["book_id"] = book_id

    if request.method == "POST":

        request.session["checkout_name"] = request.POST.get("name")
        request.session["checkout_email"] = request.POST.get("email")
        request.session["checkout_mobile"] = request.POST.get("mobile")
        request.session["checkout_address"] = request.POST.get("address")
        request.session["checkout_city"] = request.POST.get("city")
        request.session["checkout_pincode"] = request.POST.get("pincode")

        return redirect("payment")

    return render(request, "checkout.html", {
        "book": book,
        "total": book.price
    })
def payment(request):

    book_id = request.session.get("book_id")

    if not book_id:
        return redirect("index")

    book = Book.objects.get(id=book_id)

    total = book.price

    return render(request, "payment.html", {
        "book": book,
        "total": total
    })
def make_payment(request):


        if request.method != "POST":
            return redirect("payment")

        book_id = request.session.get("book_id")

        if not book_id:
            return redirect("index")

        book = Book.objects.get(id=book_id)

        payment_method = request.POST.get("payment_method")

        # Payment method select nahi kiya
        if not payment_method:
            return redirect("payment")

        Order.objects.create(
            name=request.session.get("checkout_name", ""),
            email=request.session.get("checkout_email", ""),
            mobile=request.session.get("checkout_mobile", ""),
            book=book,
            address=request.session.get("checkout_address", ""),
            city=request.session.get("checkout_city", ""),
            pincode=request.session.get("checkout_pincode", ""),
            total_amount=book.price,
            payment_method=payment_method,
            payment_status="Paid"
        )

        return redirect("order_success")
def order_success(request):
    return render(request, 'order.html')