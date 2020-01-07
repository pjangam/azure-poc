.PHONY:all
all:
	kubectl config current-context
	helm ls
	helm version
	kubectl get all

.PHONY: azure
azure:contexthello
azure:login
azure:
	helm repo update
	helm search hello
	helm upgrade --install --debug --install helloworld akspochelloworld/helloworld

.PHONY: minikube
minikube:restartmk
minikube:contextminikube
minikube:login
minikube:helminit
minikube:clusterroles
minikube:
	helm upgrade --install --debug --install helloworld akspochelloworld/helloworld

.PHONY:restartmk
restartmk:
	minikube stop
	minikube start --kubernetes-version=1.15.4

.PHONY:clusterroles
clusterroles:
	kubectl apply -f clusterrole.yml
	kubectl apply -f clusterrolebinding.yml

FILES = $(shell ls *.tgz)

.PHONY:helminit
helminit:
	kubectl apply -f tiller.yml
	helm init

.PHONY: push
push:login
push:
	echo $(FILES)
	az acr helm push $(FILES) >> output.txt 2>&1 | true

.PHONY: login
login:
	echo $(acrpassword) | docker login akspochelloworld.azurecr.io -u $(acruser) --password-stdin
	az configure --defaults acr=akspochelloworld
	az acr helm repo add

.PHONY: contexthello
contexthello:
	kubectl config use-context hello


.PHONY: contextminikube
contextminikube:
	kubectl config use-context minikube

-include User.mk
-include ../User.mk
-include ~/User.mk
