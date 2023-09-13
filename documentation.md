# API DOCUMENTATION

This document provides information about the API endpoints, including standard formats for requests and responses and sample usage.

## ENDPOINTS
### GET/API
Reads all the users from the database and returnd the data in a list.

Request:
```
url -X GET http://localhost:<api_port>/api/
```
Response: Status Code: 200 (OK)  and Body: json

```
[
  {
    "id": 1,
    "name": "John Lee"
  },
  {
    "id": 2,
    "name": "Smith Joe"
  },
  ...
]
```
### GET/API/<USER_ID>
Reads a specific user from the database using the user_id.

Request:
```
curl -X GET http://localhost:<api_port>/api/<user_id>
```
Response: Status Code: 200 (OK)  and Body: json
```
  {
    "name": "John Lee"
  }

```
### POST/API
Creates a new user.

Request: Url and Json body
```
curl -X POST -H "Content-Type: application/json" -d '{"name":"John Lee"}' http://localhost:<api_port>/api/
```
```
  {
    "id": 1,
    "name": "John Lee"
  }
```
Response: Status Code: 200 (OK)  and Body: json
```
  {
    "name": "John Lee"
  }
```
### PUT/API/<USER_ID>
Updates an existing user.

Request: Url and Json body
```
curl -X PUT -H "Content-Type: application/json" -d '{"name":"John Lee"}' http://localhost:<api_port>/api/<user_id>
```
```
  {
    "name": "John Lee"
  }
```
Response: Status Code: 200 (OK)  and Body: json
```
  {
    "name": "John Lee"
  }
```
### DELETE/API/<USER_ID>
Deletes a specific user from the database using the user_id.

Request:
```
curl -X DELETE http://localhost:<api_port>/api/<user_id>
```
Response: Status Code: 200 (OK)  and Body: json
```
  {
    "1": "deleted"
  }

```
