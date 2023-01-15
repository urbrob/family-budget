# Api documentation
I am using readme docs just for simplicity of application. Normally i would use confluence or other app to write docs.
## Login
#### Date of contract: 11.01.2023
#### UR: api/v1/login
####  METHOD: POST
### BODY:
````
{
    "email": str,
    "password": str
}
````

### Example body:
````
{
    "email": "urb.rob@o2.pl",
    "password": "uaintgonnaguessit12345%$#@!
}
````

### Response:
````
{
    "refresh": str,
    "access": str
}
````

## User Registration
#### Date of contract: 11.01.2023
#### UR: api/v1/register
####  METHOD: POST
### BODY:
````
{
    "email": str,
    "password": str
    "username": str
}
````

### Example body:
````
{
    "email": "urb.rob@o2.pl",
    "password": "uaintgonnaguessit12345%$#@!,
    "username": "urb.rob"
}
````
### Response:
````
{
    "status": "OK"
}
````

## Budget creation
#### Date of contract: 11.01.2023
#### UR: api/v1/budget
####  METHOD: POST
### BODY:
````
{
    "name": str,
}
````

### Example body:
````
{
    "name": "House",
}
````
### Response:
````
{
    "status": "OK"
}
````
## Budget list
#### Date of contract: 11.01.2023
#### UR: api/v1/budget
####  METHOD: GET
### PARAMS:
````
{
    "limit": int,
    "offset": int,
}
````
### Example body:
````
{
    "limit": 1,
    "offset": 1,
}
````
### Response:
````
{
    "count": int,
    "next": Optional[str],
    "previous": Optional[str],
    "results": [
        {
            "id": int,
            "name": str,
        }
    ]
}
````
## Budget Delete
#### Date of contract: 11.01.2023
#### UR: api/v1/budget
####  METHOD: DELETE
### PARAMS:
````
{
    "id": int,
}
````
### Example body:
````
{
    "id": 1,
}
````
### Response:
````
{
    "status": "OK"
}
````

## Budget Update
#### Date of contract: 11.01.2023
#### UR: api/v1/budget
####  METHOD: PUT
### PARAMS:
````
{
    "id": int,
    "name": str,
}
````
### Example body:
````
{
    "id": 1,
    "name": "New name",
}
````
### Response:
````
{
    "status": "OK"
}
````
## Invite User to budget
#### Date of contract: 11.01.2023
#### UR: api/v1/invitation
####  METHOD: POST
### PARAMS:
````
{
    "email": str,
    "budget_id": int,
}
````
### Example body:
````
{
    "email": "urb.rob@o2.pl,
    "budget_id": 1,
}
````
### Response:
````
{
    "status": "OK"
}
````
## Accept invitation to budget
#### Date of contract: 11.01.2023
#### UR: api/v1/invitation
####  METHOD: PATCH
### PARAMS:
````
{
    "invitation_id": int,
}
````
### Example body:
````
{
    "invitation_id": int,
}
````
### Response:
````
{
    "status": "OK"
}
````
