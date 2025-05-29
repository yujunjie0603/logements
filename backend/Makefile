help:
	@echo " Commandes disponibles :"
	@echo "  make build             Construire l'image Docker à partir du Dockerfile"
	@echo "  make up                Démarrer les conteneurs en arrière-plan"
	@echo "  make down              Arrêter et supprimer les conteneurs, réseaux et volumes"
	@echo "  make logs              Afficher les journaux en temps réel des conteneurs"
	@echo "  make shell             Ouvrir un shell interactif dans le conteneur Django"
	@echo "  make exec              Exécuter une commande arbitraire dans le conteneur Django (params='commande')"
	@echo "  make test              Lancer les tests pytest dans le conteneur (params='options pytest')"
	@echo "  make migrate           Appliquer les migrations de la base de données"
	@echo "  make makemigrations    Créer de nouvelles migrations selon les modèles"
	@echo "  make createsuperuser   Créer un super-utilisateur Django"
	@echo "  make celery            Démarrer un worker Celery pour les tâches asynchrones"
	@echo "  make worker            Alias pour démarrer le worker Celery"
	@echo "  make beat              Démarrer Celery beat pour les tâches périodiques planifiées"
	@echo "  make createprojet      Créer une nouvelle application Django (app=nom_app)"

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

exec:
	docker compose exec web $(params) 

test:
	docker compose exec web pytest $(params)

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