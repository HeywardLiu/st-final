build:
	docker build -t py-test-db . 

init:
	docker run --rm --name my-mongodb --publish 27017:27017  -d mongo 
	docker run --rm --name db-test -it  -v .:/app -w /app -p 80:5000 py-test-db   # python3.8
	# docker run --name db-test -it --rm -v .:/app -w /app -p 80:5000 db-test    # Ububtu + python3.8m

clean:
	docker stop my-mongodb
	# docker stop py-test-db
