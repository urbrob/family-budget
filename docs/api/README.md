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
