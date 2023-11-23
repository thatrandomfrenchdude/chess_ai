docker compose -f docker-compose.test.yaml --verbose build
docker compose -f docker-compose.test.yaml --verbose run --rm test
