<h1 align="center"> Todo-API </h1>
Endpoints: 

1. To create user, check swagger interface for all parameter of request
```
todoapiassign.herokuapp.com/auth/register
```

2. Pass credentials with request, access and refresh token will be returned add \
access token into authorization section in swagger as 'Bearer {access_token}'
```
todoapiassign.herokuapp.com/auth/login
```

3. To get all the task 
```
todoapiassign.herokuapp.com/todo/getall 
```

4. To get task (identified by id)
```
todoapiassign.herokuapp.com/todo/get/<id> 
```

5. to create task (refer swagger for field details)
```
todoapiassign.herokuapp.com/todo/create
```

6. to Update task (refer swagger for field details)
```
todoapiassign.herokuapp.com/todo/put/<id>
```

7. to delete task (provide id of task in query arguments)
```
todoapiassign.herokuapp.com/todo/delete/<id>
```