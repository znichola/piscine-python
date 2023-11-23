CONTAINERS = $(shell docker ps -a -q)
TIDY=2>/dev/null ; true

up :
	docker compose up

down :
	docker compose down

clean : down
	yes | docker container prune
	yes | docker image     prune
	yes | docker network   prune
	yes | docker volume    prune

fclean :
	docker stop       $(CONTAINERS)                  $(TIDY)
	docker rm         $(CONTAINERS)                  $(TIDY)
	docker network rm $(shell docker network ls -q)  $(TIDY)
	docker image rm   $(shell docker image ls -q)    $(TIDY)
	docker volume rm  $(shell docker volume ls -q)   $(TIDY)

re : fclean up

ls :
	docker container ls
	docker image     ls
	docker network   ls
	docker volume    ls

ip :
	docker ps -q | xargs -I{} docker inspect -f '{{.Name}} {{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {}

CN = py

$(CN) :
	docker exec -it $@ /bin/zsh