# ***TMPS Laboratory Work #3***
# ***Behavioral Design Patterns***

### Author: Grecu Octavian

## Objectives:

* Get familiar with the Behavioral Design Patterns;
* As a continuation of the previous laboratory work, think about what communication between software entities might be involed in my system;
* Implement some additional functionalities using behavioral design patterns;
# Publisher:
...
from __future__ import annotations

from abc import ABCMeta, abstractmethod


class Subscriber(ABCMeta):
    @abstractmethod
    def attach(self, publisher: Publisher):
        pass

    @abstractmethod
    def detach(self, publisher: Publisher):
        pass

    @abstractmethod
    def notify(self):
        pass


class Publisher(ABCMeta):
    @abstractmethod
    def update(self, subscriber: Subscriber):
        pass
        ...
        
# Owner:
         ...
         from behavioral.abstractions.publisher import Publisher
from creational.builder import CrustDirector


class Owner(Publisher):
    factory: object

    def __init__(self) -> object:
        self.factory = CrustDirector

    def update(self, subscriber):
        print("The " + self.factory + " was notified. " + subscriber)
...
# Factory_check:
...
from behavioral.abstractions.publisher import Subscriber, Publisher
from abc import ABCMeta, abstractmethod
from typing import List


class FactoryOwner(Subscriber, ABCMeta):
    taxers = []
    accountants = []
    _publishers: List[Publisher] = []



    def notify(self, event):
        print("Subject: Notifying accountants...\n")
        for publisher in self._publishers: publisher.update(event)

    def new_manager(self, accountant):
        print("A new accountant for your block")
        self.accountants.append(accountant)
        event = accountant.restaurant + " is a new accountant\n"
        self.notify(event)

    def new_taxer(self, taxer):
        print("A new taxer has arrived to your restaurant")
        self.taxers.append(taxer)
        event = taxer.restaurant + " have come with new revenue checks\n"
        self.notify(event)

    def attach(self, publisher: Publisher):
        print("Subject: Attached a new taxer.")
        self._publishers.append(publisher)

    def detach(self, publisher: Publisher):
        self._publishers.remove(publisher)


...
# Revenue_Service:
...
from behavioral.abstractions.publisher import Publisher
from creational.builder import CrustDirector


class FactoryAccountant(Publisher):
    def __init__(self):
        self.factory = CrustDirector

    def update(self, subscriber):
        print("Pizzeria Accountant " + self.factory + " was notified about coming of the Revenue Service. " + subscriber)



...
## Behavioral Design Pattern:
 - [x] Publisher
