# NewsBoard
Assessment project to DevelopsToday.

## How to run
1. Download repository `git clone https://github.com/Velx/NewsBoard.git`
2. Choose which config you want to run:
   - For production version with PostgreSQL add `.env.prod` file to root directory with envirements:
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      - POSTGRES_DB
      - SQL_HOST
      - SQL_PORT
      - REDIS_HOST
      - DEBUG
      - SECRET_KEY
   - For development version with SQLite3 go to the next step
3. Run it with docker-compose `docker-compose up -d`
4. Now server is running on port 8000

## Postman collection
All API endpoints in this [Postman collection](https://documenter.getpostman.com/view/5958867/TVK75zkw)

## Deployed version
Server deployed on on this [domain](http://ec2-18-222-204-247.us-east-2.compute.amazonaws.com:8000)
