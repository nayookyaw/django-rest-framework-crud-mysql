
# Rules
1. all variable must have data-type
    `except from validated_data`
2. follow the response data type and format
3. business logic should be in services.py
4. database logic should be in repositories.py
5. in views.py, must put try-catch
6. don't use request data before is_valid()
7. must validate request data in services.py
8. import module using `....`, DON'T import using absolute path

# variable declaration
sample - sample_variable <br>
    `except from Request Body` <br>
    request body sample - sampleVariable <br>

# method declaration
sample - sample_method_name <br>

# class declaration
sample - SampleClass <br>

# Response Status Defination
There are TWO types of status code
    - HTTP status code <br>
    - custom json status code (defined by us) <br>

1. Success - HTTP code[200], custom json code [200] 
2. Validation Failed - HTTP code[200], custom json code [400] 
3. Condition failure - HTTP code[200], custom json code [400] 
4. Code Error/Exception - HTTP code[500], custom json code [500] 
5. Unauthorized - HTTP code[401], custom json code [401]
6. Forbidden - HTTP code[403], custom json code [403]

# Important Notes
1. Even though validation, condition failed, just run HTTP code [200] and custom [400]
2. Only response [500] when code error/exception
3. Only response [401] when un-authorized condition