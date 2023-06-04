build:
	docker build -t py-test-db . 

init:
	docker run --rm --name my-mongodb --publish 27017:27017  -d mongo 
	docker run --rm --name db-test -it -v /home/laxiflora/st-final:/app -w /app -p 80:5000 py-test-db

clean:
	docker stop my-mongodb
