"""Module providing start handler"""
from handler import start
from handler import create
from handler import price

ROUTERS = [
    start.dp,
    create.dp,
    price.dp
]