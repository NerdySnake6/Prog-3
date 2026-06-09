"""Контроллер главной страницы и страницы автора."""

from jinja2 import Environment

from myapp.controllers.data import MAIN_APP, MAIN_AUTHOR, NAVIGATION


def show_index(env: Environment) -> str:
    """Сформировать HTML главной страницы."""
    template = env.get_template("index.html")
    return template.render(
        app=MAIN_APP,
        author=MAIN_AUTHOR,
        navigation=NAVIGATION,
    )


def show_author(env: Environment) -> str:
    """Сформировать HTML страницы автора."""
    template = env.get_template("author.html")
    return template.render(
        app=MAIN_APP,
        author=MAIN_AUTHOR,
        navigation=NAVIGATION,
    )

