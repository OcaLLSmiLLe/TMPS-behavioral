from behavioral.abstractions.publisher import Publisher
from creational.builder import CrustDirector


class FactoryAccountant(Publisher):
    def __init__(self):
        self.factory = CrustDirector

    def update(self, subscriber):
        print("Pizzeria Accountant " + self.factory + " was notified about coming of the Revenue Service. " + subscriber)
