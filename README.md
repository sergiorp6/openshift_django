Django on OpenShift
===================

This git repository helps you get up and running quickly w/ a Django
installation on OpenShift.  The Django project name used in this repo
is 'mydjangoapp' but you can feel free to change it.  

I've set this up as MySQL 5.5 and included crispyforms (http://django-crispy-forms.readthedocs.org/en/latest/) because they are crispy.

Running on OpenShift
--------------------

Create an account at http://openshift.redhat.com/

Install the RHC client tools if you have not already done so:
    
    sudo gem install rhc

Create a python application

    rhc app create django python-2.7 mysql-5.5

Add this upstream repo

    cd django
    git remote add upstream -m master git://github.com/smocarski/openshift_django.git
    git pull -s recursive -X theirs upstream master

At the command line, type

    rhc app show

This will list your database name, username and password.  Update these values into your settings.py file.

Then push the repo upstream

    git push

Once this completes, run syncdb on openshift using the terminal.  Login using:

    rhc ssh

At the prompt:

    cd app-root/repo/wsgi/mydjangoapp
    manage.py syncdb
    manage.py collectstatic

That will create the tables and initial values in your database and grab the static files for the admin app.

That's it. You can now checkout your application at:

    http://django-$yournamespace.rhcloud.com


