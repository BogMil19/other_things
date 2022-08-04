from datetime import datetime
from jinja2 import Template

with open('jinja_template.html') as file:
    template = Template(file.read())

context = {
    'date': datetime.now(),
    'movies': ['Casablanca', 'Dźwięki muzyki', 'Zawrót głowy'],
    'total_minutes': 404,
}

with open('report.html', 'w') as file:
    file.write(template.render(context))