import threading
import sys
from queue import Queue
from attr import attrs, attrib


@attrs
class Cutlery:
    knives = attrib(default=0)
    forks = attrib(default=0)

    def give(self, to: 'Cutlery', knives=0, forks=0):
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        self.knives += knives
        self.forks += forks


class ThreadBot(threading.Thread):
    def __init__(self, kitchen):
        super().__init__(target=self.manage_table)
        self.cutlery = Cutlery(knives=0, forks=0)
        self.tasks = Queue()
        self.kitchen = kitchen

    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == 'prepare table':
                self.kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == 'clear table':
                self.cutlery.give(to=self.kitchen, knives=4, forks=4)
            elif task == 'shutdown':
                return