# Hello World Static Page

A minimal, production-ready static HTML page served by Python's built-in HTTP server.

## Prerequisites

- Python 3.6 or higher

## Running Locally

1. Clone the repository.
2. Run the server:
   ```bash
   python3 server.py
   ```
3. Open your browser to `http://localhost:8000`.

## Deployment

You can use the provided Dockerfile to build and run a container:

```bash
docker build -t hello-world-static .
docker run -p 8000:8000 hello-world-static
```

## Architecture Decision

This project follows [ADR-001](./docs/adr-001.md) which chose a static HTML file with Python's http.server over a web framework for simplicity.

## License

MIT (or your preferred license)
