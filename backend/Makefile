help:
	@echo "🛠️ 可用命令："
	@echo "  make build             构建 Docker 镜像"
	@echo "  make up                启动容器服务"
	@echo "  make down              停止并移除容器"
	@echo "  make logs              查看日志"
	@echo "  make shell             进入 Django 容器"
	@echo "  make migrate           执行数据库迁移"
	@echo "  make createsuperuser   创建超级用户"
	@echo "  make celery            启动 Celery worker"
	@echo "  make worker            同上"
	@echo "  make beat              启动 Celery beat"
	@echo "  make createprojet      creer le projet"

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

shell:
	docker compose exec web bash

migrate:
	docker compose exec web python manage.py migrate

install:
	docker compose exec web pip install $(app)

makemigrations:
	docker compose exec web python manage.py makemigrations

createsuperuser:
	docker compose exec web python manage.py createsuperuser

celery:
	docker compose exec web celery -A cefhome worker --loglevel=info

worker: celery

beat:
	docker compose exec web celery -A cefhome beat --loglevel=info

createprojet:
	@if [ -z "$(app)" ]; then \
		echo "Usage: make createprojet app=your_app_name"; \
		exit 1; \
	else \
		docker compose exec web python manage.py startapp $(app); \
	fi