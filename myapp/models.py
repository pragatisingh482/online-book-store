from django.db import models

# Create your models here.
class booksignuptbl(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id},{self.name},{self.email},{self.password},{self.confirm_password}"


class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class enquiryTbl(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    book_name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    enquiry = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="books/")
    price = models.IntegerField()
    old_price = models.IntegerField()
    discount = models.IntegerField()
    rating = models.FloatField()
    reviews = models.IntegerField()
    offer = models.IntegerField(default=0)
    is_free=models.BooleanField(default=False)
    is_mainpage=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(category)
    description=models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    published_year = models.PositiveIntegerField(null=True, blank=True)
    importance = models.TextField(null=True, blank=True)





    def __str__(self):
        return self.title
class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(
        max_length=30,
        default="Pending"
    )

    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.book.title