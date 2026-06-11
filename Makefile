.PHONY: run build docker-build docker-run

# Run the server locally
run:
	python3 server.py

# Build Docker image
docker-build:
	docker build -t hello-world-static .

# Run Docker container
docker-run:
	docker run -p 8000:8000 hello-world-static

# Show available targets
default:
	@echo "Targets: run, docker-build, docker-run"
