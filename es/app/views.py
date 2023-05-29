from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views import View
from . models import allCategory, subCourse, Post,  Lecture, Cart, Orders, OrderUpdate,ContactMessage,Lecture2,Lecture3,Lecture4
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django import forms
from django.db.models import Q
from django.views.generic import DetailView


from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
# Create your views here.

MERCHANT_KEY = 'Your-Merchant-Key-Here'


def home(request):
    categorys = allCategory.objects.all()[:8]  # Retrieve the first six authors
    return render(request, "app/home.html", {'categorys': categorys})
def about(request):
    categorys = allCategory.objects.all()[:8]  # Retrieve the first six authors
    return render(request, "app/about.html", {'categorys': categorys} )
#def contact(request):
    #categorys = allCategory.objects.all()[:8]  # Retrieve the first six authors
    #return render(request, "app/contact.html", {'categorys': categorys})

class allCategoryView(View):
    def get(self,request):
        categorys = allCategory.objects.all()
        return render(request, "app/allCategory.html", {'categorys': categorys})



def course_list(request, category_id=None):

    categorys = allCategory.objects.all()  # Retrieve all authors
    global bookcounts
    if category_id:
        books = subCourse.objects.filter(category_id=category_id)
        bookcounts = subCourse.objects.all()
    else:
        books = subCourse.objects.all()


    popular_books = subCourse.objects.order_by('-popularity')[:4]  # Retrieve top 4 popular books
    featured_books = subCourse.objects.filter(featured=True)

    context = {
        'books': books,
        'popular_books': popular_books,
        'featured_books': featured_books,
        'bookcounts' :  bookcounts,
        'categorys': categorys,  # Include the 'authors' variable in the context

    }

    return render(request, 'app/course_list.html', context)




def registerPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect(reverse('login'))

    return render(request, 'app/register.html')
@login_required(login_url='login')
def my_view(request):
    if request.user.groups.filter(name='teacher').exists():
        template_name = 'app/teacher_dashboard.html'
    elif request.user.groups.filter(name='student').exists():
        template_name = 'app/student_dashboard.html'
    else:
        return HttpResponse("Invalid user role!")

    return render(request, template_name)
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('my_view')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'app/login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')


#=====================blog====================
@login_required
def blog(request):

    posts = Post.objects.all()

    return render(request, 'app/blog.html',{'posts': posts})


def post_new(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        youtube_link = request.POST['youtube_link']
        zoom_link = request.POST['zoom_link']

        new_post = Post(title=title, content=content, youtube_link=youtube_link, zoom_link=zoom_link)
        new_post.author = request.user
        new_post.save()

        return HttpResponseRedirect('/blog')

    else:
        return render(request, 'app/post_new.html')


#===============================delete post======================
def confirm_delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app/confirm_delete_post.html', {'post': post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect('/blog')
    else:
        return HttpResponseRedirect(reverse('confirm_delete_post', args=[post.pk]))

#==================update post ====================================

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'youtube_link', 'zoom_link']

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post_id': post_id
    }
    return render(request, 'app/update_post.html', context)

#==================================teacher dashboard content==========


def study(request):
    lectures = Lecture.objects.all()
    return render(request, 'app/study.html',{'lectures': lectures})

def lecture_new(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        youtube_link = request.POST['youtube_link']
        zoom_link = request.POST['zoom_link']
        pdf_file = request.FILES['pdf_file']
        word_file = request.FILES['word_file']
        internet_link = request.POST['internet_link']

        new_lecture = Lecture(title=title, content=content, youtube_link=youtube_link, zoom_link=zoom_link, pdf_file= pdf_file ,word_file= word_file,internet_link=internet_link)
        new_lecture.author = request.user
        new_lecture.save()

        return HttpResponseRedirect('/study')

    else:
        return render(request, 'app/lecture_new.html')

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'content', 'youtube_link', 'zoom_link', 'pdf_file', 'word_file', 'internet_link']

    # ==================================teacher dashboard content==========


def study2(request):
    lectures = Lecture2.objects.all()
    return render(request, 'app/study2.html', {'lectures': lectures})


def lecture_new2(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        youtube_link = request.POST['youtube_link']
        zoom_link = request.POST['zoom_link']
        pdf_file = request.FILES['pdf_file']
        word_file = request.FILES['word_file']
        internet_link = request.POST['internet_link']

        new_lecture = Lecture2(title=title, content=content, youtube_link=youtube_link, zoom_link=zoom_link,
                              pdf_file=pdf_file, word_file=word_file, internet_link=internet_link)
        new_lecture.author = request.user
        new_lecture.save()

        return HttpResponseRedirect('/study2')

    else:
        return render(request, 'app/lecture_new2.html')


class LectureForm2(forms.ModelForm):
    class Meta:
        model = Lecture2
        fields = ['title', 'content', 'youtube_link', 'zoom_link', 'pdf_file', 'word_file', 'internet_link']

    # ==================================teacher dashboard content==========


def study3(request):
    lectures = Lecture3.objects.all()
    return render(request, 'app/study3.html', {'lectures': lectures})


def lecture_new3(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        youtube_link = request.POST['youtube_link']
        zoom_link = request.POST['zoom_link']
        pdf_file = request.FILES['pdf_file']
        word_file = request.FILES['word_file']
        internet_link = request.POST['internet_link']

        new_lecture = Lecture3(title=title, content=content, youtube_link=youtube_link, zoom_link=zoom_link,
                               pdf_file=pdf_file, word_file=word_file, internet_link=internet_link)
        new_lecture.author = request.user
        new_lecture.save()

        return HttpResponseRedirect('/study3')

    else:
        return render(request, 'app/lecture_new3.html')


class LectureForm3(forms.ModelForm):
    class Meta:
        model = Lecture3
        fields = ['title', 'content', 'youtube_link', 'zoom_link', 'pdf_file', 'word_file', 'internet_link']


 # ==================================teacher dashboard content==========


def study4(request):
    lectures = Lecture4.objects.all()
    return render(request, 'app/study4.html', {'lectures': lectures})


def lecture_new4(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        youtube_link = request.POST['youtube_link']
        zoom_link = request.POST['zoom_link']
        pdf_file = request.FILES['pdf_file']
        word_file = request.FILES['word_file']
        internet_link = request.POST['internet_link']

        new_lecture = Lecture4(title=title, content=content, youtube_link=youtube_link, zoom_link=zoom_link,
                              pdf_file=pdf_file, word_file=word_file, internet_link=internet_link)
        new_lecture.author = request.user
        new_lecture.save()

        return HttpResponseRedirect('/study4')

    else:
        return render(request, 'app/lecture_new4.html')


class LectureForm4(forms.ModelForm):
    class Meta:
        model = Lecture4
        fields = ['title', 'content', 'youtube_link', 'zoom_link', 'pdf_file', 'word_file', 'internet_link']


#============================ no use code =======================================================================================
@login_required
def update_lecture(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)

    if request.method == 'POST':
        form = LectureForm(request.POST, instance=lecture)
        if form.is_valid():
            form.save()
            return redirect('study')
    else:
        form = LectureForm(instance=lecture)

    context = {
        'form': form,
        'lecture_id': lecture_id
    }
    return render(request, 'app/update_lecture.html', context)

def confirm_delete_lecture(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    return render(request, 'app/confirm_delete_post.html', {'lecture': lecture})

def delete_lecture(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    if request.method == 'POST':
        lecture.delete()
        return HttpResponseRedirect('/study')
    else:
        return HttpResponseRedirect(reverse('confirm_delete_lecture', args=[lecture.pk]))
#====================================== code is not in use =======================================================================


def search(request):
    query = request.GET.get('q')  # Get the search query from the request's GET parameters

    # Perform the search query on the allCategory and subCourse models
    categories = allCategory.objects.filter(name__icontains=query)
    courses = subCourse.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {
        'query': query,
        'categories': categories,
        'courses': courses,
    }

    return render(request, 'search_results.html', context)
#=================================course details====================================================================================
def subcourse_details(request, pk):
    subcourse = subCourse.objects.get(pk=pk)
    return render(request, 'subcourse_details.html', {'subcourse': subcourse})


class SubCourseDetailView(DetailView):
    model = subCourse
    template_name = 'app/subcourse_details.html'  # Replace 'subcourse_details.html' with the actual template name for displaying subcourse details
    context_object_name = 'subcourse'  # Replace 'subcourse' with the desired context object name in your template
#=====================================================add to cart===================================================================

def view_cart(request):
    cart_items = Cart.objects.all()
    context = {
        'cart_items': cart_items
    }
    return render(request, 'app/cart.html', context)
def add_to_cart(request, category_id):
    category = subCourse.objects.get(pk=category_id)
    cart_item, created = Cart.objects.get_or_create(category=category)
    # Perform cart-related operations...
    return redirect('view_cart')
#==================================payment=====================================================================================================

def checkout(request):
    if request.method=="POST":
        course_name = request.POST.get('course_name', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(course_name=course_name, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {

            'MID': 'WorldP64425807474247',
            'ORDER_ID': 'order.order_id',
            'TXN_AMOUNT': '1',
            'CUST_ID': 'email',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlepayment/',

        }
        return render(request, 'app/paytm.html', {'param_dict': param_dict})
    return render(request, 'app/checkout.html')


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'app/paymentstatus.html', {'response': response_dict})


#============================================
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('phone')  # Use 'phone' instead of 'number'
        message = request.POST.get('message')

        # Create a new instance of the ContactMessage model and save it
        con = ContactMessage(name=name, email=email, number=number, message=message)
        con.save()

        return render(request, 'app/contact.html', {'success': True})  # Pass a success flag to the template

    return render(request, 'app/contact.html')