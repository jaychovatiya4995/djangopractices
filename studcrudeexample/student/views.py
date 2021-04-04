from django.shortcuts import render,redirect
from student.models import Book
from student.models import Student
from student.models import Stream

from student.forms import BookForm
from student.forms import StudentForm
from student.forms import StreamForm


# ################  BOOK ###########################################
def show_book(request):  
    books = Book.objects.all()
    return render(request,"books\\show_book.html",{'books':books}) 

def add_book(request):
    if request.method == "POST":  
        form = BookForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_book')  
            except:
                pass
    else:  
        form = BookForm()  
    return render(request,'books\\add_book.html',{'form':form})

def delete_book(request, id):  
    book = Book.objects.get(id=id)  
    book.delete()
    return redirect("/show_book")

def edit_book(request, id):
    book = Book.objects.get(id=id)  
    return render(request,'books\\edit_book.html', {'book':book})  

def update_book(request, id):  
    book = Book.objects.get(id=id)  
    form = BookForm(request.POST, instance = book)  
    if form.is_valid():  
        form.save()  
        return redirect("/show_book")  
    return render(request, 'books\\edit_book.html', {'book': book})
#  ################  END BOOK ######################################



#  ############## STREAM ###########################################
def show_stream(request):  
    stream = Stream.objects.all()
    return render(request,"streams\\show_stream.html",{'streams':stream}) 

def add_stream(request):
    if request.method == "POST":  
        form = StreamForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_stream')  
            except:
                pass
    else:  
        form = StreamForm()  
    return render(request,'streams\\add_stream.html',{'form':form})

def delete_stream(request, id):  
    stream = Stream.objects.get(id=id)  
    stream.delete()
    return redirect("/show_stream")

def edit_stream(request, id):
    stream = Stream.objects.get(id=id)  
    return render(request,'streams\\edit_stream.html', {'stream':stream})  

def update_stream(request, id):  
    stream = Stream.objects.get(id=id)  
    form = StreamForm(request.POST, instance = stream)  
    if form.is_valid():  
        form.save()  
        return redirect("/show_stream")  
    return render(request, 'streams\\edit_stream.html', {'stream': stream})

# #################### END STREAM ####################################

    
# ################### Student ########################################
def show_student(request):  
    student = Student.objects.all()
    return render(request,"students\\show_students.html",{'students':student}) 

def add_student(request):
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_student')  
            except:
                pass
    else:  
        form = StudentForm()  
    return render(request,'students\\add_students.html',{'form':form})

def delete_student(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()
    return redirect("/show_student")

def edit_student(request, id):
    student = Student.objects.get(id=id)  
    return render(request,'students\\edit_students.html', {'student':student})  

def update_student(request, id):  
    student = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/show_student")  
    return render(request, 'students\\edit_students.html', {'student': student})

# ##################### END STUDENT ##########################################

