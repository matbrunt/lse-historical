#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = lse-historical

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Clean downloaded data files
clean-all:
	rm -f src/data/**/*

clean:
	rm -f src/data/interim/* src/data/processed/*

build-explore:
	docker-compose build explore

prophet:
	docker-compose up -d prophet

explore:
	docker-compose up -d explore

build-rprophet:
	docker build -f docker/rprophet/rprophet.dockerfile -t honir/rprophet:latest ./docker/rprophet

shell:
	docker-compose run --rm -w /usr/src/app prophet /bin/bash

shell-explore:
	docker-compose run --rm -w /usr/src/app explore /bin/bash