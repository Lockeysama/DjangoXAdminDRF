.PHONY: build update run generate-deploy

export VERSION = 2.0.1
export REGISTRY = registry.cn-shanghai.aliyuncs.com/affectivecloud

ifeq (${ENV}, test)
	export ENVFLAG = -test
else
	ifneq (${ENV}, release)
		$(error "Error: ENV(${ENV}) undefined.")
	endif
endif


_echo:
	@echo "Env: " ${ENV} "(" ${ENVFLAG} ")"
	@echo "Version: " ${VERSION}
	@echo "Registry: " ${REGISTRY}
	@echo "Project: " && pwd
	@echo "Git Branch: " && git branch | grep "*" | awk '{print $2}'
	@read -p "按任意键继续..."

build: _echo
	docker-compose build --build-arg ENVFLAG=${ENVFLAG} --build-arg VERSION=${VERSION}

update: build
	docker push ${REGISTRY}/acmanage${ENVFLAG}:${VERSION}
	docker push ${REGISTRY}/acmanage-nginx${ENVFLAG}:${VERSION}
