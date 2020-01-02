#!/bin/bash

NAME="stern"                              #Name of the application (*)
DJANGODIR=/stern             # Django project directory (*)
SOCKFILE=/run/gunicorn.sock        # we will communicate using this unix socket (*)
USER=nginx                                        # the user to run as (*)
GROUP=webdata                                     # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=ourcase.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=ourcase.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
conda activate stern

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /var/www/test/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE