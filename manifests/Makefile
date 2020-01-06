.PHONY: all
all:
	helm del helloworld --purge
	az configure --defaults acr=akspochelloworld
	az acr helm repo add
	helm package helloworld
	# az acr helm push helloworld-0.1.15.tgz  > program.stdout 2> program.stderr
	helm repo update
	helm search hello
	helm upgrade --install --debug --install helloworld akspochelloworld/helloworld
