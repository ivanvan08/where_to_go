# Where to go?

A personal list of favourite places to eat, walk or hang out. Browse the list,
open a place for the full description, add your own, or let the site pick one
for you - the higher the rating, the more likely a place is chosen.

The list is kept in the user session, so every visitor edits their own copy of
the default places.

## Local setup

Requires Python 3.12+. Run the commands from the directory containing
`manage.py`.

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv

   # linux/macos
   source .venv/bin/activate
   # windows
   .venv\Scripts\activate.ps1
   ```

2. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Apply migrations - sessions need the database tables:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Pages

| URL | What it does |
| --- | --- |
| `/` | Home page with the "Куди піти сьогодні?" button |
| `/places/` | All places, one preview card each |
| `/places/<id>/` | Full description of a single place |
| `/places/add/` | Form for adding a new place |
