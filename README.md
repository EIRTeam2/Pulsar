![sad](GamePlanner/static/images/logo-eirteam-small.png)

# What is pulsar?
Pulsar is our internal project management tool, it's built to resemble Hack N Plan.

# Current Features
Pulsar at the time is heavily unfinished, but I am publishing the code because I am taking a two week break, and maybe someone can learn from this.

- REST API (WIP, powered by tastypie)
- Frontend code uses node.js packages and vue.js
- Uses bulma
- Hack n plan style game model

# Things that need work
- Markdown editor likes to break
- You can't save markdown fields
- Editing tasks is impossible (except from the django admin interface).

# Installation
Keep in mind this is untested, but generally this should be doable by:

- Creating a virtualenv and sourcing it
```bash
virtualenv env -p python3
source env/bin/activate
```

- Installing all the node packages
```bash
npm install
```

- Installing all the python packages
```bash
pip install -r requirements.txt
```

- Migratin the database and running the development server
```bash
python manage.py migrate
python manage.py runserver
```

First loads might be slow, because JS has to be compiled.
