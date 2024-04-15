import logging
from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)

footer = """
    <footer>
        <hr>
        <div>
            <p>All rights reserved &copy;</p>
        </div>
    </footer>
"""


def index(request):
    html = """
    <body>
        <h1>Добро пожаловать!</h1>
            <p>Интернет-магазин</p>
        <hr>
        <div>
            <h2>Меню</h2>
            <p><a href=''>Главная</a></p>
            <p><a href='about'>О вас</a></p>
            <p><a href='products'>Продукция</a></p>
        </div>
    </body>
    """ + footer
    logger.info(f'Посещение страницы {__name__}: index')
    return HttpResponse(html)


def about(request):
    html = """
    <h1>О нас</h1>
    <p>Какая то информация</p>
    <hr>
    <div>
        <h2>Меню</h2>
        <p><a href='../'>Главная</a></p>
        <p><a href=''>О нас</a></p>
    </div>
    """ + footer
    logger.info(f'Посещение страницы {__name__}: about')
    return HttpResponse(html)