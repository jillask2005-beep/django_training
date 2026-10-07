from django.shortcuts import render
from django.http import HttpResponse
from .serializers import Studentserializers
from rest_framework.response import Response 
from rest_framework.views import APIView
from .serializers import*
from rest_framework import status
from django.db.models import  Sum, Count, Avg, Max, Min
from django.db.models import F, ExpressionWrapper, IntegerField




# Create your views here.

def home (request):
    return HttpResponse("hello world") 

from .models import Student
class StudentView(APIView):
    # def get(self,request):
    #     studentList= Student.objects.all()
    #     serializer=Studentserializers(studentList,many=True)

    #     return Response({
    #         "data":serializer.data  
    #     })
    def post(self,request):
        serializer=Studentserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
               "msg":"data added sucessfully",
               "data":serializer.data
            },status=status.HTTP_201_CREATED)
        return Response({
            "error":serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        students=Student.objects.all()
        city=request.query_params.get("city")
        age=request.query_params.get("age")


        if city:
            students=students.filter(city__exact=city)
        if age:
            students=students.filter(age__gte=20)

        result=students.aggregate(
            max_age=Max('age'),
            min_age=Min('age'),
            total_stud=Count('age'),
            avg_age=Avg('age'),
            sum_age=Sum('age')
        )
        students=students.annotate(
            age_afterten=ExpressionWrapper(
                F('age')+10-7,
                output_field=IntegerField()
            )
        )

        grpby=students.values('course').annotate(
            total_price=Count('id')
        )
        


        serializer=Studentserializers(students,many=True)
        return Response({
                'data':serializer.data,
                'result':result,
                'namebycount':grpby
            },status=status.HTTP_201_CREATED)


    
from .models import Employee,Movie,Product
class EmployeeView(APIView):
    # def get(self,request):
    #     employeeList=Employee.objects.all()
    #     serializer=Employeeserializers(employeeList,many=True)
    #     return Response({
    #       "data":serializer.data  
    #     })
    def post(self,request):
        serializer=Employeeserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "mes":"data added succussfully",
                'data':serializer.data
            },status=status.HTTP_201_CREATED)
        return Response({
            "error":serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        employee=Employee.objects.all()
        age=request.query_params.get("a")
        order=request.query_params.get('order')

        if age:
            employee=employee.filter(age__gte=20)

        if order:
            employee=employee.order_by(order)

        seralizer=Employeeserializers(employee,many=True)    

        results=employee.aggregate(
            max_age=Max('age'),
            min_age=Min('age'),
            total_age=Count('age'),
            avg_age=Avg('age'),
            sum_age=Sum('age')
        )
        employee = employee.annotate(
            age_ofteen=ExpressionWrapper(
            F("age") + 10 - 2,
            output_field=IntegerField()
                )
            )
        seralizer=Employeeserializers(employee,many=True)
        return Response({
            'data':seralizer.data,
            'res':results,
            'emp':seralizer.data
        })
    
    

    
class MovieView(APIView):
    def get(self,request):
        movielist=Movie.objects.all()
        serializer=Movieserializers(movielist,many=True)
        return Response({
            "data":serializer.data
        })
    def post(self,request):
        serializer=Movieserializers(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({
               "mes":"data added successful",
               "data":serializer.data
           },status=status.HTTP_201_CREATED)
        return Response({
            "error":serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        Movies = Movie.objects.all()

        name = request.query_params.get("n")

        if name:
            Movies = Movies.filter(Directer_name__icontains=name)

        serializer = Movieserializers(Movies, many=True)

        return Response({
            "data": serializer.data
        })
class productView(APIView):
    # def get(self,request):
    #     productlist=Product.objects.all()
    #     serializer=Productserializers(productlist,many=True)


    #     return Response({
    #         "data":serializer.data
    #     })
    def post(self,request):
        serializer=Productserializers(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response({
                "mes":"data added succussfully",
                'data':serializer.data
            },status=status.HTTP_201_CREATED)
        return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        product = Product.objects.all()

        name = request.query_params.get("name")
        price = request.query_params.get("price")

        if name:
            product = product.filter(name__icontains=name)
            product=product.filter(name__exact=name)
        if price:
            product = product.filter(price__gte=price)

            
            res=product.aggregate(
                max_price=Max('price'),
                min_price=Min('price'),
                avg_price=Avg('price'),
                total_price=Count('price'),
                sum_price=Sum('price')
            )
            product=product.annotate(
                price_afterten=ExpressionWrapper(
                    F('price')+8000-2000,
                    output_field=IntegerField()
                )
            )

        serializer = Productserializers(product, many=True)

        return Response({
            "data": serializer.data,
            'result':res,
        })
from .models import Book

class BookView(APIView):
    # def get(self,request):
    #     booklist=Book.objects.all()
    #     serializers=Bookserializers(booklist,many=True)
    #     return Response({
    #         "data":serializers.data
    #     })
    def post(self,request):
        serializer=Bookserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'mes':"data added succussfully",
                'data':serializer.data
            },status=status.HTTP_201_CREATED)
        return Response({
            'error':serializer.data
        },status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        Books=Book.objects.all()
        name=request.query_params.get('n')
        genre=request.query_params.get('g')

        if name:
            Books=Books.filter(Author_name__icontains=name)
        if genre:
           Books = Books.filter(genre__icontains=genre)

        result = Books.aggregate(
         max_published_year=Max('published_year'),
         min_published_year=Min('published_year'),
         total_published_year=Count('published_year'),
         avg_published_year=Avg('published_year'),
         sum_published_year=Sum('published_year')
         )
        Books=Books.annotate(
                published_year_afterten=ExpressionWrapper(
                    F('published_year')+10-1,
                    output_field=IntegerField()
                )
            )

        gryby=Books.values('Book_title').annotate(
            total_Author_name=Count('id')
        )


              
        
        seializer=Bookserializers(Books,many=True)
        return Response({
            'data':seializer.data,
            'result':result,
            'grupby':gryby
        })
   


from .models import Student,Employee,Book,Movie
class StudentdetailsView(APIView):
    def get(self,request,pk):
        try:
            student=Student.objects.get(id=pk)
            serializer=Studentserializers(student)
            return Response({
                "data":serializer.data
            },status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({
                'error':'Student not found'
            },status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        try:
            student= Student.objects.get(id=pk )
            serializer=Studentserializers(student,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'data':serializer.data
                },status=status.HTTP_200_OK)
            return Response({
                'error':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({
                'error':'student not found'
            },status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        try:
             student=Student.objects.get(id=pk)
             Serializer=Studentserializers(student,data=request.data)
             if Serializer.is_valid():
                        Serializer.save()
                        return Response({
                            'data':Serializer.data,
                            'data':'data added successfully '
                        },status=status.HTTP_200_OK)
             return Response({
                        'error':Serializer.errors
                    },status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({
                'error':'srudent not found'
            },status=status.HTTP_400_BAD_REQUEST)
       
    
    def delete(self,request,pk):
        try:
            student=Student.objects.get(id=pk)
            student.delete()
            return Response({
                'mes':'delete succussfully',

            },status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({
                "error":"student not found"
            },status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(APIView):

    def get(self, request, pk):
        try:
            employee = Employee.objects.get(id=pk)

            serializer = Employeeserializers(employee)

            return Response({
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        except Employee.DoesNotExist:
            return Response({
                'error': 'Employee not found'
            }, status=status.HTTP_404_NOT_FOUND)
    def patch(self,request,pk):
        try:
             employeee=Employee.objects.get(id=pk)
             serializer= Employeeserializers(employeee,data=request.data,partial=True)
             if serializer.is_valid():
                 serializer.save()
                 return Response({
                     'data':serializer.data,
                     'data':"data added successfully"
                 },status=status.HTTP_200_OK)
             return Response({
                 'error':serializer.errors
             },status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response({
                'error':"employee not found"
            },status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        try:
             Employeee=Employee.objects.get(id=pk)
             serializer=Employeeserializers(Employeee,data=request.data)
             if serializer.is_valid():
                        serializer.save()
                        return Response({
                            'data':serializer.data,
                            'data':'data added successfully'
                        },status=status.HTTP_200_OK)
             return Response({
                        'error':serializer.errors
                    },status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response({
                'error':'employee not found'
            },status=status.HTTP_400_BAD_REQUEST)
       
    
            
       
    def delete(self, request, pk):
        try:
            employee = Employee.objects.get(id=pk)

            employee.delete()

            return Response({
                'mes': 'Delete successful'
            }, status=status.HTTP_200_OK)

        except Employee.DoesNotExist:
            return Response({
                'error': 'Employee not found'
            }, status=status.HTTP_404_NOT_FOUND)



class BookDetailsView(APIView):
    def get(self,request,pk):
        try:
            Books=Book.objects.get(id=pk)
            serializer=Bookserializers(Books)
            return Response({
                'data':serializer.data
            },status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"error":'Book is not found'},status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
            try:
                Books=Book.objects.get(id=pk)
                serializer=Bookserializers(Books,data=request.data,partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'data':serializer.data
                    },status=status.HTTP_200_OK)
                return Response({
                                    'error':serializer.error
                                },status=status.HTTP_400_BAD_REQUEST)

            
            except Book.DoesNotExist:
                return Response({"error":'Book is not found'},status=status.HTTP_400_BAD_REQUEST)

        
    def delete(self,request,pk):
        try:
            books=Book.objects.get(id=pk)
            books.delete()
            return Response({'mes':'delete successful'},status=status.HTTP_200_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({'error':'Book not found'},status=status.HTTP_400_BAD_REQUEST)

class MovieDetailsView(APIView):
    def get(self,request,pk):
        try:
            Movies=Movie.objects.get(id=pk)
            serializer=Movieserializers(Movies)
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
        except Movie.DoesNotExist:
            return Response({"movie not found"},status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        try:
            moviese=Movie.objects.get(id=pk)
            serializer=Movieserializers(moviese,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
            return Response({
                'error':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        except Movie.DoesNotExist:
            return Response({
                'error':'book not found'
            },status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        try:
            Moviese=Movie.objects.get(id=pk)
            serializer=Movieserializers(Moviese,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                     "message": "Student updated successfully",
                     'data':serializer.data
                },status=status.HTTP_200_CONTINUE)
            return Response({
                'error':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        except Movie.DoesNotExist:
            return Response({
                'error':"movies not found"
            },status=status.HTTP_400_BAD_REQUEST)
             
    def delete(self,request,pk):
        try:
            Movies=Movie.objects.get(id=pk)
            Movies.delete()
            return Response({'mes':'delete succussfully'},status=status.HTTP_201_CREATED)
        except Movie.DoesNotExist:
            return Response({'error':'movie not found'},status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):

    def get(self, request, pk):
        try:
            products = Product.objects.get(id=pk)
            serializer = Productserializers(products)

            return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
            )

        except Product.DoesNotExist:
            return Response(
                {'error': 'Product not found'},
                status=status.HTTP_404_NOT_FOUND
            )
    def patch(self,request,pk):
        try:
            productss=Product.objects.get(id=pk)
            serializer=Productserializers(productss,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'data':serializer.data
                },status=status.HTTP_201_CREATED)
            return Response({
                'error':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({
                'error':'product not found'
            },status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        try:
             products=Product.objects.get(id=pk)
             serializer=Productserializers(products,data=request.data)
             if serializer.is_valid():
                        serializer.save()
                        return Response({
                            'data':serializer.data,
                            'data ':'data added succefully'
                        },status=status.HTTP_201_CREATED)
             return Response({
                        'error':serializer.errors
                    },status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({
                'error':"product not found"
            },status=status.HTTP_400_BAD_REQUEST)  
        
       
    
            

    def delete(self, request, pk):
        try:
            products = Product.objects.get(id=pk)
            products.delete()

            return Response(
                {'mess': 'Deleted successfully'},
                status=status.HTTP_204_NO_CONTENT
            )

        except Product.DoesNotExist:
            return Response(
                {'error': 'Product not found'},
                status=status.HTTP_404_NOT_FOUND
            )
from django.db.models import Q

class filterView(APIView):

    def get(self, request):

        employee = Employee.objects.all()

        name = request.query_params.get("name")
        a = request.query_params.get("age")
        b = request.query_params.get("age")
        serach=request.query_params.get("serach")


        if name:
            employee = employee.filter(name__icontains=name)

        if a:
            employee = employee.filter(age__gte=a)

        if b:
            employee=employee.filter(age__lte=b)

        if a and b:
            employee=employee.filter(age__range=(a,b))
        if serach:
            employee=employee.filter(
                Q(name__icontains=serach)|
                Q(age__icointains=serach)
            )


        serializer = Employeeserializers(employee, many=True)

        return Response({
            "data": serializer.data
        })

class Imageview(APIView):
    serializer_class=imageseralizer
    def get(self,request):
        image=Images.objects.all()
        serializer=imageseralizer(image,many=True,context={'request':request})
        return Response({
            'data':serializer.data
        },status=status.HTTP_200_OK)
    def post(self,request):
        serializer=imageseralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data':serializer.data,
                'data':'data added sus'
            },status=status.HTTP_200_OK)
        return Response({
            'error':serializer.errors,

        },status=status.HTTP_400_BAD_REQUEST)

class ImageViewDeails(APIView):
    def get(self,request,pk):
        try:
            image=Images.objects.get(id=pk)
            serializer=imageseralizer(image)
            return Response({
                'data':serializer.data
            },status=status.HTTP_200_OK)
        except Images.DoesNotExist:
            return Response({
                'error':serializer.errors,
                'data':'image not found'
            },status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        try:
            image=Images.objects.get(id=pk) 
            seralizer=imageseralizer(image,data=request.data,partial=True)
            if seralizer.is_valid():
               seralizer.save()
               return Response(
            {
                'data':seralizer.data
            },status=status.HTTP_200_OK
        )
            return Response({
            'error':seralizer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        except Images.DoesNotExist:
            return Response({
                'error':'image not found'
            },status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        try:
            image=Images.objects.get(id=pk)
            serializer=imageseralizer(image,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'data':serializer.data
                },status=status.HTTP_200_OK)
            return Response({
                'error':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        except Images.DoesNotExist:
            return Response({
                'error':'image not found'
            },status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            image=Images.objects.get(id=pk)
            image.delete()
            return Response({
                'data':'deleye sus'
            },status=status.HTTP_200_OK)
        except Images.DoesNotExist:
            return Response({
                'error':'image not found'
            },status=status.HTTP_400_BAD_REQUEST)

from .serializers import SignupSerializer  
class Signup(APIView):
    def post(self,request):
        serializer=SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'mes':'Accound created','data':serializer.data
            },status=status.HTTP_201_CREATED)
        return Response({
            'error':serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import authenticate
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            return Response({
                'mes': "Login successful",
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            })

        return Response({
            'mes': "Invalid username or password"
        })

    
    
    