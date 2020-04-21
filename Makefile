PY = python3
MODULE = manage.py

# COMMANDS
RUN_SERVER = runserver
CHECK = check
MIGRATE = migrate
MAKE_MIGRATIONS = makemigrations

RUN = $(PY) $(MODULE)

all:
	$(RUN) $(RUN_SERVER)

check:
	$(RUN) $(CHECK)

migrate:
	$(RUN) $(MIGRATE)

makemigrations:
	$(RUN) $(MAKE_MIGRATIONS)

update_db:
	make makemigrations
	make migrate
