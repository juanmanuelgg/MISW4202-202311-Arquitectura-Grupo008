from locust import HttpUser, TaskSet, between


def transporte(l):
    l.client.get("/transporte")


def ordencompra(l):
    l.client.get("/ordencompra")


class UserTasks(TaskSet):
    tasks = [transporte, ordencompra]

class WebsiteUser(HttpUser):
    """
    User class that does requests to the locust web server running on localhost
    """

    host = "https://api.arquitecturaccp.com"
    wait_time = between(2, 5)
    tasks = [UserTasks]