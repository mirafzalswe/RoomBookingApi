### RoomBookingAPI 😉
## Enjoy reading documentation 
The Room Booking API is a Django REST Framework (DRF) project designed to facilitate the booking and management of hotel rooms. The API allows clients to check room availability, book rooms for specific periods, retrieve details about individual rooms, and register new users.

* To get a list of all rooms `GET` `...api/rooms`
```
{
   "available": [<list of unoccupied rooms>],
   "reserved": [<list of occupied rooms>],
   "date": <today's date>,
}
```
> For instance: 
```JSON
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "available": [
        {
            "id": 1,
            "room_number": "facebook",
            "capacity": 4,
            "description": "smth smthing smthing"
        },
        {
            "id": 4,
            "room_number": "Somsaxona",
            "capacity": 2,
            "description": "somsalar issiq issiq"
        }
    ],
    "reserved": [
        {
            "id": 2,
            "room_number": "instagram",
            "capacity": 2,
            "description": "smthing smthing"
        },
        {
            "id": 3,
            "room_number": "Youtube",
            "capacity": 10,
            "description": "Somthing something"
        }
    ],
    "date": "2024-01-24"
}
```
* To book a room, `POST` → `…/api/book/room`
```JSON
HTTP 200 OK
Allow: GET, OPTION
Content-Type: application/json
  {
      "room_name":"facebook",
      "start":"2024-01-23",
      "end": "2023-01-25"
  }   

```
# Making POST Requests

To make POST requests to protected endpoints, such as booking a room, you need to obtain an authentication token, specifically a JSON Web Token (JWT). Follow the steps below:
1. **User Registration:**
   - Endpoint: `/api/register/`
   - Method: POST
   - Description: Register a new user to obtain authentication credentials.
   - Parameters:
     - `username` (string): Desired username for the new user.
     - `password` (string): Password for the new user.
   - Example:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}' http://your-domain/api/register/
     ```
   - Response:
     ```json
     {
        "username": "your_username",
        "id": 2
     }
     ```

2. **Token Acquisition:**
   - Endpoint: `/api/token/`
   - Method: POST
   - Description: Obtain a JSON Web Token (JWT) by providing the registered user's credentials.
   - Parameters:
     - `username` (string): Username of the registered user.
     - `password` (string): Password of the registered user.
   - Example:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}' http://your-domain/api/token/
     ```
   - Response:
     ```json
     {
        "access": "your_access_token",
        "refresh": "your_refresh_token"
     }
     ```

     3. **Use the Token for Booking:**
   - After obtaining the access token, include it in the Authorization header for subsequent requests.
   - Example:
     ```bash
     curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer your_access_token" -d '{"room_name": "101", "start": "2024-01-24", "end": "2024-01-26"}' http://your-domain/api/book/room/
     ```
   - Response:
     ```json
     {
        "message": "Booking successful for you",
        "room": 2,
        "room_name": "101",
        "start": "2024-01-24",
        "end": "2024-01-26"
     }
     ```

   
**Note:**
- Keep your tokens secure.
- Access tokens have a limited lifespan, but you can use the refresh token to obtain a new access token when needed.
- Only superuser can add(create) rooms 

### 3. Room Details

- **Endpoint:** `/api/room/{room_name}/`
- **Method:** GET
- **Description:** Retrieve details of a specific room.
- **Parameters:**
  - `room_number` (string): The room number.
- **Authentication:** None
> For intacne
`GET` -> `api/room/<room_name/`
```JSON
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "room_number": "facebook",
    "capacity": 4,
    "description": "smth smthing smthing",
    "is_available": true
}
```


![image](https://github.com/mirafzal114/RoomBookingApi/assets/136591233/82c952a3-c32d-431c-81b2-e3b1e2c67d8b)

![image](https://github.com/mirafzal114/RoomBookingApi/assets/136591233/74353893-fc21-4117-a357-fa2a0c56917c)

![image](https://github.com/mirafzal114/RoomBookingApi/assets/136591233/c03e92a6-d16c-445d-9695-992ecc96ee22)

![image](https://github.com/mirafzal114/RoomBookingApi/assets/136591233/a536a9ff-6c4a-43a4-87d1-6ece303cfae7)




### Install Docker

1. Make sure you have Docker installed on your computer.
2. If Docker is not installed, you can download it [from here](https://docs.docker.com/get-docker/) and install it according to the instructions for your operating system.

### Start the project
### We have already entered the repositories with `pipenv` before, now we will continue with the next one, but you first enter your `Docker Desktop` application if you do not have `Linux` of course:
1. Create a Docker image by running the command: 
    ```
    $ docker build -t BookingApi .
    ```
2. Once the image has been successfully created, start the container: 
    ```
    $ docker run -p 1212:8000 BookingApi
    ```
3. Check ``Dockerfile`` if you do not have an image download from ``Docker Hub``:
    ````bash
    $ docker pull python:3.11-alpine
    ````

Your project should now be available in your browser at `https://localhost:1212/api/rooms`. - Here `api/rooms` means this from application Django.

5. List of rooms:
    ```
    https://localhost:1212/api/rooms
    ```
## Project home page. ##
