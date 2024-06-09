from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task, Customer, Employee

class TaskListTestCase(TestCase):
    def setUp(self):
        # Create test users and save them immediately
        self.customer_user = User.objects.create_user(username='testcustomer', password='testpassword')
        self.customer_user.save()

        self.employee_user = User.objects.create_user(username='testemployee', password='testpassword')
        self.employee_user.save()

        # Create test Customer and Employee objects
        self.customer = Customer.objects.create(user=self.customer_user)
        self.employee = Employee.objects.create(user=self.employee_user)

        # Create a test task
        self.task = Task.objects.create(
            customer=self.customer,
            employee=self.employee,
            description='This is a test task.'
        )

        # Set up the client and authenticate
        self.client = APIClient()
        self.client.force_authenticate(user=self.customer_user)

    def test_list_tasks(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the task is included in the response
        self.assertIn(self.task.id, [task['id'] for task in response.data])