#!/bin/bash

echo ""
echo "Welcome installer Boilerplate Django..."

# EnvFile
ENVFILE="./.env"

if [ ! -f "$ENVFILE" ]; then
  echo "File not found!"
  cp -v .env.sample .env
fi

if [ -f "$ENVFILE" ]
then

  # START
  echo "Settings vars environment"
  if [[($is_debug == "")]];
  then
    DEBUG=True
  else
    DEBUG=False
  fi

  # SECRET_KEY
  SECRET_KEY=$(openssl rand -base64 32)
  echo "New secret key generated: ${SECRET_KEY}"

  if [[($projectname == "")]];
  then
    APPNAME="Myapp"
  else
    APPNAME=$projectname
  fi

  if [[($urlwebsite == "")]];
  then
    URL_WEBSITE="http://localhost:8000"
  else
    URL_WEBSITE=$urlwebsite
  fi

  if [[($urlserver == "")]];
  then
    URL_SERVER="http://localhost:8000"
  else
    URL_SERVER=$urlserver
  fi

  if [[($timezone == "")]];
  then
    TIME_ZONE="UTC"
  else
    TIME_ZONE=$timezone
  fi

  if [[($pagination == "")]];
  then
    PAGE_SIZE="10"
  else
    PAGE_SIZE=$pagination
  fi

  if [[($dbhost == "")]];
  then
    DB_HOST="localhost"
  else
    DB_HOST=$dbhost
  fi

  if [[($dbname == "")]];
  then
    DB_NAME=""
  else
    DB_NAME=$dbname
  fi

  if [[($dbuser == "")]];
  then
    DB_USER="postgres"
  else
    DB_USER=$dbuser
  fi

  if [[($dbpassword == "")]];
  then
    DB_PASSWORD=""
  else
    DB_PASSWORD=$dbpassword
  fi

  if [[($dbport == "")]];
  then
    DB_PORT="5432"
  else
    DB_PORT=$dbport
  fi

  echo "DEBUG=$DEBUG" > "$ENVFILE"
  echo "SECRET_KEY=${SECRET_KEY}" >> "$ENVFILE"
  echo "APPNAME=${APPNAME}" >> "$ENVFILE"
  echo "URL_WEBSITE=${URL_WEBSITE}" >> "$ENVFILE"
  echo "URL_SERVER=${URL_SERVER}" >> "$ENVFILE"
  echo "TIME_ZONE=${TIME_ZONE}" >> "$ENVFILE"
  echo "PAGE_SIZE=${PAGE_SIZE}" >> "$ENVFILE"
  echo "FCM_SERVER_KEY=" >> "$ENVFILE"
  echo "CONEKTA_PRIVATE_KEY=" >> "$ENVFILE"
  echo "SMS_KEY=" >> "$ENVFILE"
  echo "AWS_ENABLE=False" >> "$ENVFILE"
  echo "AWS_REGION=" >> "$ENVFILE"
  echo "AWS_STORAGE_BUCKET_NAME=" >> "$ENVFILE"
  echo "AWS_CLOUD_FRONT_URL=" >> "$ENVFILE"
  echo "EMAIL_USE_TLS=True" >> "$ENVFILE"
  echo "DEFAULT_FROM_EMAIL=from@example.com" >> "$ENVFILE"
  echo "EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend" >> "$ENVFILE"
  echo "EMAIL_HOST=" >> "$ENVFILE"
  echo "EMAIL_HOST_USER=" >> "$ENVFILE"
  echo "EMAIL_HOST_PASSWORD=" >> "$ENVFILE"
  echo "EMAIL_PORT=587" >> "$ENVFILE"
  echo "DB_HOST=${DB_HOST}" >> "$ENVFILE"
  echo "DB_NAME=${DB_NAME}" >> "$ENVFILE"
  echo "DB_USER=${DB_USER}" >> "$ENVFILE"
  echo "DB_PASSWORD=${DB_PASSWORD}" >> "$ENVFILE"
  echo "DB_PORT=${DB_PORT}" >> "$ENVFILE"
fi
# echo ""
# if [[($collectsta == "y")]];
# then
#   echo "Creating collectstatics..."
#   python manage.py collectstatic --noinput
# fi


# Exit from the script with success (0)
exit 0

__ARCHIVE__
