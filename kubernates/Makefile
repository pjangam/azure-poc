FILES = $(shell ls *.tgz)
chartname := helloworld
reponame := akspochelloworld
cartchart := shopping-cart

.PHONY:all
all:
	kubectl config current-context
	helm ls
	helm version
	kubectl get all

.PHONY: clean
clean:
	rm -rf *.tgz >> output.txt 2>&1 | true

.PHONY:restartmk
restartmk:
	minikube stop
	minikube start --kubernetes-version=1.15.4

.PHONY:clusterroles
clusterroles:
	kubectl apply -f clusterrole.yml
	kubectl apply -f clusterrolebinding.yml


.PHONY:helminit
helminit:
	kubectl apply -f tiller.yml
	helm init

.PHONY: push
push:package
push:login
push:
	echo $(FILES)
	az acr helm push $(FILES) >> output.txt 2>&1 | true

.PHONY: login
login:
	echo $(acrpassword) | docker login $(reponame).azurecr.io -u $(acruser) --password-stdin
	az configure --defaults acr=$(reponame)
	az acr helm repo add

####################### contexts   ####################

.PHONY: contexthello
contexthello:
	kubectl config use-context hello


.PHONY: contextminikube
contextminikube:
	kubectl config use-context minikube

###################### enviornments ##################




####################### helloworld ####################
.PHONY: package
package:clean
package:
	helm package $(chartname)

.PHONY: azure
azure:contexthello
azure:login
azure:
	helm repo update
	helm upgrade --install --debug --install $(chartname) $(reponame)/$(chartname)

.PHONY: minikube
minikube:restartmk
minikube:contextminikube
minikube:login
minikube:helminit
minikube:clusterroles
minikube:
	helm upgrade --install --debug --install $(chartname) $(reponame)/$(chartname)

###################### shopping-cart #################
.PHONY: cartpack
cartpack:clean
cartpack:
	helm package $(cartchart)

.PHONY: pushcart
pushcart:cartpack
pushcart:login
pushcart:
	echo $(FILES)
	az acr helm push $(FILES) >> output.txt 2>&1 | true

.PHONY:azcart

azcart:contexthello
azcart:login
azcart:
	helm repo update
	helm upgrade --install --debug --install $(cartchart) $(reponame)/$(cartchart)

.PHONY: mkcart
mkcart:restartmk
mkcart:contextminikube
mkcart:login
mkcart:helminit
mkcart:clusterroles
mkcart:
	helm upgrade --install --debug --install $(cartchart) $(reponame)/$(cartchart)


####################################################
-include User.mk
-include ../User.mk
-include ~/User.mk
