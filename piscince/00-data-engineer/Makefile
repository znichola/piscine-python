
up :
	docker compose up -d

down : 
	docker compose down

ip :
	@docker ps -q | xargs -I{} docker inspect -f '{{.Name}} {{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {}

CONTAINERS = $(shell docker ps -a -q)
TIDY=2>/dev/null ; true

fclean : env-clean
	docker stop       $(CONTAINERS)                  $(TIDY)
	docker rm         $(CONTAINERS)                  $(TIDY)
	docker network rm $(shell docker network ls -q)  $(TIDY)
	docker image rm   $(shell docker image ls -q)    $(TIDY)
	docker volume rm  $(shell docker volume ls -q)   $(TIDY)

env :
	./gen_env.sh

dl_data :
	./download_data.sh

db :
	docker exec -it postgres psql -U znichola -d piscineds -h localhost -W