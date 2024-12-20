start-docker:
	  @echo "Starting Docker Compose..."
	  docker-compose up 

start-docker-dev:
	  @echo "Starting Docker Compose in development mode..."
	  docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
	  
stop-docker:
	  @echo "Stopping Docker Compose..."
	  docker-compose -f docker-compose.yml down

make-migrations:
	  @echo "Creating Django migrations..."
	  poetry run python3 django_project/manage.py makemigrations

migrate:
	  @echo "Running Django migrations..."
	  poetry run python3 django_project/manage.py migrate

run-server:
	  @echo "Starting Django server..."
	  poetry run python3 django_project/manage.py runserver

redis-cli:
	  @echo "Connecting to Redis CLI..."
	  docker exec -it giaco-dev-backend-redis-1 redis-cli
