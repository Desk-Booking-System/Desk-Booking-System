# Desk-Booking-System


## License

This project is licensed under the BSD 3-Clause License 

## Author

The attribution of this  project should be given to the author at [Saad Mir](https://github.com/Desk-Booking-System/Desk-Booking-System).  

## Business Model

This project uses the Freemium business model

## Description

The purpose of this project is to create a desk booking system for emloyees of a company in order to reserve a desk one day or a week before they arrive at the office.

## Technologies

The technologies that will used in this project are:

- Bootstrap - 5
- Python Django
- SQLite3

## Build - Docker

To run the Django application using Docker Compose, follow these steps:

1. Make sure you have Docker and Docker Compose installed on your machine.

2. Clone the project repository from GitHub.

3. Open a terminal window and navigate to the root directory of the project.

4. Run the following command to start the Docker container:

    `docker-compose up`
    
The application should now be running. Open a web browser and go to http://localhost:8000 to view the homepage.

## Progress

To stay updated with the projects process please look into the [Trello](https://trello.com/b/phcYRJtc/desk-booking-system) created for the project.

## Samples examples of code

### Example of views



``` 
from django.shortcuts import render

# create your views here

@csrf_exempt
@api_view(['GET', 'DELETE', 'PUT'])
def example_desk_function(request, id):
    try:
        ...
    except Desk.DoesNotExist:
        return JsonResponse({"message":"desk doesnt exist"}, status=status.HTTP_400_BAD_REQUEST)

```

## Example of Models

```
from django.db import models

# Create your models here.

class Desks(models.Model):

    id = models.CharField(max_length=250, default='')
    desk = models.CharField(max_length=250, default='')
    
    def __str__(self) -> str:
        return self.desk
        
```





