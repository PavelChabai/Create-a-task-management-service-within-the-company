from rest_framework import serializers
from .models import User, Customer, Employee, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phone')

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ('id', 'user')

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ('id', 'user')

class TaskSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    employee = EmployeeSerializer(required=False)

    class Meta:
        model = Task
        fields = (
            'id',
            'customer',
            'employee',
            'created_at',
            'updated_at',
            'closed_at',
            'status',
            'report',
        )
        read_only_fields = ('created_at', 'updated_at', 'closed_at')

class CreateTaskSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Task
        fields = (
            'customer',
            'employee',
            'status',
            'report',
        )

class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'status',
            'report',
        )

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def save(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        user.set_password(password)
        user.save()
        return user

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'type']

    def save(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            type=self.validated_data['type'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})

        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'type']