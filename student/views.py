
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import Student
from .serializer import StudentSerializer, UserSerializer


# USER SIGNUP
class SignUpView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):

        serializer_instance = UserSerializer(
            data=request.data
        )

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(
                {"message": "User created successfully"},
                status=201
            )

        return Response(
            serializer_instance.errors,
            status=400
        )

class LogoutView(APIView):

    authentication_classes = [
        authentication.TokenAuthentication
    ]

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request):

        request.user.auth_token.delete()

        return Response(
            {
                "message": "User Logged Out Successfully"
            },
            status=200
        )


# USER LIST
class UserListView(APIView):

    authentication_classes = [
        authentication.TokenAuthentication
    ]

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):

        users = User.objects.all()

        serializer_instance = UserSerializer(
            users,
            many=True
        )

        return Response(
            serializer_instance.data,
            status=200
        )


# STUDENT CREATE AND LIST
class StudentCreateView(APIView):

    authentication_classes = [
        authentication.TokenAuthentication
    ]

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):

        students = Student.objects.all()

        serializer_instance = StudentSerializer(
            students,
            many=True
        )

        return Response(
            serializer_instance.data,
            status=200
        )

    def post(self, request):

        serializer_instance = StudentSerializer(
            data=request.data
        )

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(
                {
                    "message": "Student Created Successfully",
                    "Student Details": serializer_instance.data
                },
                status=201
            )

        return Response(
            serializer_instance.errors,
            status=400
        )


# STUDENT RETRIEVE, UPDATE AND DELETE
class StudentRetrieveUpdateDeleteView(APIView):

    authentication_classes = [
        authentication.TokenAuthentication
    ]

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request, pk):

        student_object = get_object_or_404(
            Student,
            id=pk
        )

        serializer_instance = StudentSerializer(
            student_object
        )

        return Response(
            serializer_instance.data,
            status=200
        )

    def put(self, request, pk):

        student_object = get_object_or_404(
            Student,
            id=pk
        )

        serializer_instance = StudentSerializer(
            student_object,
            data=request.data
        )

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(
                {
                    "message": "Student Updated Successfully",
                    "Student Details": serializer_instance.data
                },
                status=200
            )

        return Response(
            serializer_instance.errors,
            status=400
        )

    def patch(self, request, pk):

        student_object = get_object_or_404(
            Student,
            id=pk
        )

        serializer_instance = StudentSerializer(
            student_object,
            data=request.data,
            partial=True
        )

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(
                {
                    "message": "Student Partially Updated Successfully",
                    "Student Details": serializer_instance.data
                },
                status=200
            )

        return Response(
            serializer_instance.errors,
            status=400
        )

    def delete(self, request, pk):

        student_object = get_object_or_404(
            Student,
            id=pk
        )

        student_object.delete()

        return Response(
            {
                "message": "Student Deleted Successfully"
            },
            status=200
        )
