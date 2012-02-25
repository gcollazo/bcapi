# BarcampCheckin
A very simple backend to save data from the check-in app.

## Heroku URL
http://quiet-sky-9376.herokuapp.com

## Endpoints
### /event/[event_name]/
- GET Request will return a list of all the users that already checked in. It will return something like.

    ```
    http://barcampm12.herokuapp.com/event/BarcampM12
    ```
    
    ```
    [
        {"user":"1234567890", "checked_in": false},
        {"user":"2123456789", "checked_in": true}
    ]
    ```

- POST create a new user on the db. It has to be an Array. Send something like:

    ```
    [
        {"user": "1234567890", "checked_in": false},
        {"user": "238476", "checked_in": false}
    ]
    ```

### /event/[event_name]/[user_id]/
- GET will return user details
    ```
    {
        "user": "1234567890"
        "checked_in": true
    }
    ```

- PUT will update the user state. Just send something like:
    
    ```
    {
        "user": "1234567890"
        "checked_in": true
    }
    ```