from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import SubCourseDetailView





urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("allCategory/", views.allCategoryView.as_view(),  name="allCategory"),
    path('books/<int:category_id>/', views.course_list, name='course_list'),
    path('course_list/', views.course_list, name='course_list'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('study/', views.study, name='study'),
    path("lecture_new/", views.lecture_new, name="lecture_new"),
    path('study2/', views.study2, name='study2'),
    path("lecture_new2/", views.lecture_new2, name="lecture_new2"),
    path('study3/', views.study3, name='study3'),
    path("lecture_new3/", views.lecture_new3, name="lecture_new3"),
    path('study4/', views.study4, name='study4'),
    path("lecture_new4/", views.lecture_new4, name="lecture_new4"),
                  # update post
    path('update_lecture/<int:post_id>/', views.update_lecture, name='update_lecture'),

                  # Delete post
    path('study/delete/<int:pk>/', views.delete_lecture, name='delete_lecture'),

                  # Confirm delete post
    path('study/delete/<int:pk>/confirm/', views.confirm_delete_lecture, name='confirm_delete_lecture'),
   # path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    #path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path("blog/", views.blog, name="blog"),
    path("post_new/", views.post_new, name="post_new"),
                  # update post
    path('update_post/<int:post_id>/', views.update_post, name='update_post'),

                  # Delete post
    path('blog/delete/<int:pk>/', views.delete_post, name='delete_post'),

                  # Confirm delete post
    path('blog/delete/<int:pk>/confirm/', views.confirm_delete_post, name='confirm_delete_post'),
    path('my-view/', views.my_view, name='my_view'),
    path('search/', views.search, name='search'),
    path('subcourse/<int:pk>/', SubCourseDetailView.as_view(), name='subcourse_detail'),

    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:book_id>/',views.add_to_cart, name='add_to_cart'),

    #=================payment=================================
    path('checkout/', views.checkout, name='checkout'),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)