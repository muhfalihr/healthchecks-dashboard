import os
from flask import Flask, render_template
from setting import settings

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        template_name_or_list='index.html', 
        title=settings.TITLE,
        projects=settings.PROJECTS,
        host=settings.HOST,
        port=settings.PORT,
        domain_name=settings.DOMAIN_NAME
    )

if __name__ == "__name__":
    app.run()