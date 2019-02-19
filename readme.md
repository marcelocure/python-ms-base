## Getting Started
* To create the virtual env: `virtualenv <name>`
* To use the virtual env: `source <nome>/bin/activate`
* To install dependencies: `pip install -r requirements.txt`
### For MacOS only:
* Install MySQL 5.7: `brew install mysql@5.7`
* To install dependencies: `LDFLAGS=-L/usr/local/opt/openssl/lib pip install -r requirements.txt`
## How to run
`python api.py`

## How to generate a migration
`alembic revision`

It will create a new script under ~/alembic/versions

Docs: https://alembic.sqlalchemy.org/en/latest/ops.html#ops

## How to run migrations
`alembic upgrade head`

It'll take the migrations that are still pending

If you inform a revision instead of `head`, it'll rerun that revision
