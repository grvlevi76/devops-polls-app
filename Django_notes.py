#                       <===== first Django app - part 1  =====>

#urls.py --> is url configuration (URLconf) and is mendatory in django app as its used to map the 'view.py' file to a url so that we can access 'view' on browser
    #exp - http://localhost:8000/poll - 

#flow of basic request and response with Django for ur "polls" app  when ran server with "python manage.py runserver"

    # global URLconf (mysite/urls.py) got implemeted then -> local polls's URLconf(polls/urls.py) which included -> views.py path -> httpresponse

#packages and modules =====>

    # "from django.http import HttpResponse" --> use to return httpresponse from view.py

    # "from django.urls import path, include" -->  use it inside urls.py
        # path() -->  expects at least two arguments: route and view
            #exp - path("polls/", include("polls.urls")

        # include() --> The include() function allows referencing other URLconfs.



#                        <===== first Django app - part 2 ======>

#db setup ==> migrations ------>
'''
The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables 
according to the database settings in your mysite/settings.py file and the database migrations shipped 
with the app (we’ll cover those later).

migrations r derived from ur models file
'''
# creating models =========>

#models = table name of database
#field = attribute(column) of database

'''
models r basically single definitive source of information about ur data.
It contains the essential fields and behaviors of the data you’re storing.
'''
#these classes(models inside of models.py) r nothing but just the table name with variables inside of classs as attribute(columns) of database with their datatype

# activating models ========>
'''
"python manage.py makemigrations polls" to create migrations for those changes
"python manage.py migrate" to apply those changes to the database.

# migrations =====>

-->'makemigration' stores the changes u made in ur models , u can checkout- 
    those changes in 'migrations' folder.
-->'makemigrations' compares the current known schema from all available migrations file with the -
    what expected schema should be based on ur models and creates new migrations file to achieve that model schema.

--->to go to models for expected schema , the 'migrations' looks at refrence of models which is avilable in INSTALLED_APPS-
    of setting.py.

--->'migrations' folder also sort of tells all the changes or commits history u did in database

# migrate =====>

-->'migrate' command takes all the migrations that haven’t been applied and runs them against your database.

"python manage.py sqlmigrate polls 0001" - sqlmigrate command tell u sql command its going to use-
 to create or update models from the code in 'migrations/' folder

"python manage.py check" - checks for any problems in ur project without migrating or touching the db

-->'django_migrations' named table in ur db.sqlite3 tells the 'migrate' command which 'migrations' r applied-
    in ur databse already with their publish data. u can check them out in sqlite db

'''
#lol basically the migrate command just makes db tables based on settings(db type) and models(columns of table)

# playing with api  =======>
'''
    ---> inserting data in db ->
                "from polls.models import Student"
                s1 = Student(roll_no =5,name ="laman",pass =True)
                s1.save()

    ---> accessing models's object -
                "Student.objects.all()"

    ---> get specifc onject(row)
                "st = Student.objects.get(name = "chaman")"

    # Retrieving objects ----->

    ---> * To retrieve objects from your database, construct a QuerySet via a Manager on your model class.
         * every class has a Manager and its called objects
         * "f = Student.objects.filter(Pass = True)" -- return sollection of object whoever's Pass is true
         * 'objects' command only works on class not object

    ---> "__str__" functions shows the objects into string u provide when printing

    # "choice_set" ---->

    ---> * this work when two models r connected through foriegn key
         * using "choice_set" we can add choices to the specific question object(q)
         * "q.choice_set.create(choice_text ="ok".vote=0)" - a entry got created in Choice model cause Questions-
            and Choice r connected through foriengn key
         * "q.choice_set.all()"  - to see all choice object of a question object
         * "q.choice_set.count()" - counts how many choice objects r of 1 question object or -
                counts how many rows of other table r connected to one row of different table

    # misc --->
    
    ---> * The API automatically follows relationships as far as you need.
         * "Choice.objects.filter(question__pub_date__year=current_year)"

         * use "delete()" function on list of objects or single object to delete that entry from db        

'''

# Django admin ==========>
'''
---> \\\\ django api is insertion, retrieval , update in db through python interactive shell

'python manage.py createsuperuser'--> creates a admin user for django admin

--> add the model in admin.py by 'admin.site.register(model_name)' to let it appear on admin site-
    test it on ur student model.

---> wow i just entered data through admin site in database its crazy ngl

--> authentication - identifying a user's identity against the db to provide him access to the system

'''

# testing for later--> do choice_set on Student model ,see if it wors cause there's no forien key in Student table



#                        <===== first Django app - part 3 ======>




#                      <============== misc ==============>

# views ======>
        # "django.shortcut imports render"
        
        # 'render()' --> render function sends httpresponse and the response is the matching template file it finds inside apps of INSTALLED_APPS's apps
