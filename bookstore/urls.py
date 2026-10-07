"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from myapp import views

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('Books/', views.Books, name='Books'),
    path('home/', views.home, name='home'),
    path('story/', views.story, name='story'),
    path('self/', views.self, name='self'),
    path('science/', views.science, name='science'),
    path('review/', views.review, name='review'),
    path('psychology/', views.psychology, name='psychology'),
    path('programming/', views.programming, name='programming'),
    path('Novels/', views.Novels, name='Novels'),
    path('medical/', views.medical, name='medical'),
    path('law/', views.law, name='law'),
    path('history/', views.history, name='history'),
    path('free/', views.free, name='free'),
    path('free&premiumbook/', views.frpre, name='free&premiumbook'),
    path('finance/', views.finance, name='finance'),
    path('exam/', views.exam, name='exam'),
    path('english/', views.english, name='english'),
    path('competetive/',views.competetive, name='competetive'),
    path('child/', views.child, name='child'),
    path('bookdetailnovel1/', views.bookdetailnovel1, name='bookdetailnovel1'),
path('bookdetail/<int:id>/', views.bookdetail, name='bookdetail'),
    path('academic/', views.academic, name='academic'),
    path('bio/',views.bio,name='bio'),
    path('bookcategories/',views.bookcategories,name='bookcategories'),
    path('bookdetaillaw/', views.bookdetaillaw, name='bookdetaillaw'),
    path('bookdetailacademic/', views.bookdetailacademic, name='bookdetailacademic'),
    path('bookdetailbio/',views.bookdetailbio, name='bookdetailbio'),
    path('bookdetailstory/',views.bookdetailstory, name='bookdetailstory'),
    path('bookdetailchild/',views.bookdetailchild, name='bookdetailchild'),
    path('bookdetailcomptetive/',views.bookdetailcomptetive, name='bookdetailcomptetive'),
    path('bookdetailenglish/',views.bookdetailenglish, name='bookdetailenglish'),
    path('bookdetailexam/',views.bookdetailexam, name='bookdetailexam'),
    path('bookdetailfinance/',views.bookdetailfinance, name='bookdetailfinance'),
    path('bookdetailprograamming/',views.bookdetailprograamming, name='bookdetailprograamming'),
    path('booksignup/', views.booksignup),
    path('booksignupcode/', views.booksignupcode,name='booksignupcode'),
    path('login/', views.login),
    path('logincode/', views.logincode, name='logincode'),
    path('enquiry/',views.enquiry, name='enquiry'),
    path('enquirycode/',views.enquirycode,name='enquirycode'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('bookdetailself/',views.bookdetailself, name='bookdetailself'),

    path('bookdetail/<int:id>/', views.bookdetail, name="bookdetail"),
    path('buy-now/<int:book_id>/', views.buy_now, name='buy_now'),
    path('checkout/<int:book_id>/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('make-payment/', views.make_payment, name='make_payment'),
    path('order-success/', views.order_success, name='order_success'),


]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
