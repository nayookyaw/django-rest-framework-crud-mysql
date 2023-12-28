    Author
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com

# setup virtual env in window
    $ pip install virtualenv 

`navigate to root project path and run below command to create virtual env`

    $ python -m venu wmenv 

`activate the env in window`

    $ .\wmenv\Scripts\activate

# install the dependencies
*
    - all dependencies should be in requirements.txt <br>
    - if you want to add new dependency, make sure add into requirement.txt and install using "-r" <br>

# run server [navigate to ROOT path of project]
 $ python manage.py runserver

# create new app
`if you want to create new app, just use below command` <br>
    $ python manage.py startapp src/`your_app_name`

# migrate
`create migrate file` <br>
    $ python manage.py makemigrations src/`your_app_name` <br>

`after creating migration file and run makemigrations from ROOT path of project`
    $ python manage.py makemigrations
    $ python manage.py migrate

`after you create migrate file, just run migrate command as below`
    $ python manage.py migrate

# References
https://testdriven.io/blog/drf-basics/
https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
https://www.django-rest-framework.org/tutorial/3-class-based-views/

# encrypt and decrypt 
https://chat.openai.com/share/0060e397-75ab-47f4-b9d2-715af5ee3a50