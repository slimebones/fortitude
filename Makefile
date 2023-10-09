export t=Main

build:
	@g++ Source/*.cpp -o bin/main

run: build
	@./bin/main
