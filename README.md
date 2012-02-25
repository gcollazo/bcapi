# BarcampCheckin
A very simple backend to save data from the check-in app. Based on Flask, MongoDB and pusherapp.com.

## Heroku URL
http://barcampm12.herokuapp.com/

## Endpoints
### /event/[event_name]/
- GET Request will return a list of all the users that already checked in. It will return something like.

    ```
    http://barcampm12.herokuapp.com/event/BarcampM12
    ```
    
    ```
    [
        {
            _id: {
            	$oid: "4f4922165b25fa0007000000"
        	},
            checked_in: true,
            name: "Juan del Pueblo",
            event: "BarcampM12"
        },
        {
            _id: {
            	$oid: "4f4922165b25fa0007000001"
        	},
            checked_in: false,
            name: "Maria Rivera",
            event: "BarcampM12"
        }
    ]
    ```

- POST create a new user on the db. It has to be an Array. Send something like:

    ```
    [
        {"name": "Juan del Pueblo", "checked_in": false},
        {"name": "Maria Rivera", "checked_in": false}
    ]
    ```

### /event/[event_name]/[user_id]/
- GET will return user details

    ```
	{
	   _id: {
	   	$oid: "4f4922165b25fa0007000001"
	},
	   checked_in: false,
	   name: "Maria Rivera",
	   event: "BarcampM12"
	}
    ```

- PUT will update the user state. Just send something like:
    
    ```
    {
        "checked_in": true
    }
    ```