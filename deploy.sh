#!/bin/sh

docker build -t registry.heroku.com/perpay-backend/web .

docker push registry.heroku.com/perpay-backend/web

heroku container:release -a perpay-backend web