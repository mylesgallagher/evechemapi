# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class NewTower(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cycles_at: int=None, fuel_count: int=None, fuel_last_udpate: int=None, name: str=None, system: str=None, planet: int=None, moon: int=None, online: bool=None, sov: bool=None, type: int=None):
        """
        NewTower - a model defined in Swagger
        
        :param cycles_at: The cycles_at of this NewTower.
        :type cycles_at: int
        :param fuel_count: The fuel_count of this NewTower.
        :type fuel_count: int
        :param fuel_last_udpate: The fuel_last_udpate of this NewTower.
        :type fuel_last_udpate: int
        :param name: The name of this NewTower.
        :type name: str
        :param system: The system of this NewTower.
        :type system: str
        :param planet: The planet of this NewTower.
        :type planet: int
        :param moon: The moon of this NewTower.
        :type moon: int
        :param online: The online of this NewTower.
        :type online: bool
        :param sov: If tower has sov bonus.
        :type sov: bool
        :param type: The type of this NewTower.
        :type type: int
        """
        self.swagger_types = {
            'cycles_at': int,
            'stront_count': int,
            'fuel_count': int,
            'fuel_last_udpate': int,
            'name': str,
            'system': str,
            'planet': int,
            'moon': int,
            'online': bool,
            'sov': bool,
            'type': int
        }

        self.attribute_map = {
            'cycles_at': 'cycles_at',
            'stront_count': 'stront_count',
            'fuel_count': 'fuel_count',
            'fuel_last_udpate': 'fuel_last_udpate',
            'name':'name',
            'system': 'system',
            'planet': 'planet',
            'moon': 'moon',
            'online': 'online',
            'sov': 'sov',
            'type': 'type'
        }

        self._cycles_at = cycles_at
        self._stront_count = stront_count
        self._fuel_count = fuel_count
        self._fuel_last_udpate = fuel_last_udpate
        self._name = name
        self._system = system
        self._planet = planet
        self._moon = moon
        self._online = online
        self._sov = sov
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'NewTower':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The new_tower of this NewTower.
        :rtype: NewTower
        """
        return deserialize_model(dikt, cls)

    @property
    def cycles_at(self) -> int:
        """
        Gets the cycles_at of this NewTower.
        Minute (0-59) in which this tower processes all fuel and silo/reaction cycles. 

        :return: The cycles_at of this NewTower.
        :rtype: int
        """
        return self._cycles_at

    @cycles_at.setter
    def cycles_at(self, cycles_at: int):
        """
        Sets the cycles_at of this NewTower.
        Minute (0-59) in which this tower processes all fuel and silo/reaction cycles. 

        :param cycles_at: The cycles_at of this NewTower.
        :type cycles_at: int
        """
        if cycles_at is not None and cycles_at > 59:
            raise ValueError("Invalid value for `cycles_at`, must be a value less than or equal to `59`")
        if cycles_at is not None and cycles_at < 0:
            raise ValueError("Invalid value for `cycles_at`, must be a value greater than or equal to `0`")

        self._cycles_at = cycles_at

    @property
    def stront_count(self) -> int:
        """
        Gets the stront_count of this TowerDetails.

        :return: The stront_count of this TowerDetails.
        :rtype: int
        """
        return self._stront_count

    @stront_count.setter
    def stront_count(self, stront_count: int):
        """
        Sets the stront_count of this TowerDetails.

        :param stront_count: The stront_count of this TowerDetails.
        :type stront_count: int
        """

        self._stront_count = stront_count

    @property
    def fuel_count(self) -> int:
        """
        Gets the fuel_count of this NewTower.

        :return: The fuel_count of this NewTower.
        :rtype: int
        """
        return self._fuel_count

    @fuel_count.setter
    def fuel_count(self, fuel_count: int):
        """
        Sets the fuel_count of this NewTower.

        :param fuel_count: The fuel_count of this NewTower.
        :type fuel_count: int
        """

        self._fuel_count = fuel_count

    @property
    def fuel_last_udpate(self) -> int:
        """
        Gets the fuel_last_udpate of this NewTower.

        :return: The fuel_last_udpate of this NewTower.
        :rtype: int
        """
        return self._fuel_last_udpate

    @fuel_last_udpate.setter
    def fuel_last_udpate(self, fuel_last_udpate: int):
        """
        Sets the fuel_last_udpate of this NewTower.

        :param fuel_last_udpate: The fuel_last_udpate of this NewTower.
        :type fuel_last_udpate: int
        """

        self._fuel_last_udpate = fuel_last_udpate

    @property
    def name(self) -> str:
        """
        Gets the name of this NewTower.

        :return: The name of this NewTower.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this NewTower.

        :param name: The name of this NewTower.
        :type name: str
        """

        self._name = name

    @property
    def system(self) -> str:
        """
        Gets the system of this NewTower.

        :return: The system of this NewTower.
        :rtype: str
        """
        return self._system

    @system.setter
    def system(self, system: str):
        """
        Sets the system of this NewTower.

        :param system: The system of this NewTower.
        :type system: str
        """

        self._system = system

    @property
    def planet(self) -> int:
        """
        Gets the planet of this NewTower.

        :return: The planet of this NewTower.
        :rtype: int
        """
        return self._planet

    @planet.setter
    def planet(self, planet: int):
        """
        Sets the planet of this NewTower.

        :param planet: The planet of this NewTower.
        :type planet: int
        """

        self._planet = planet

    @property
    def moon(self) -> int:
        """
        Gets the moon of this NewTower.

        :return: The moon of this NewTower.
        :rtype: int
        """
        return self._moon

    @moon.setter
    def moon(self, moon: int):
        """
        Sets the moon of this NewTower.

        :param moon: The moon of this NewTower.
        :type moon: int
        """

        self._moon = moon

    @property
    def online(self) -> bool:
        """
        Gets the online of this NewTower.
        Online/offline status boolean. 

        :return: The online of this NewTower.
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online: bool):
        """
        Sets the online of this NewTower.
        Online/offline status boolean. 

        :param online: The online of this NewTower.
        :type online: bool
        """

        self._online = online

    @property
    def sov(self) -> bool:
        """
        Gets the sov of this NewTower.

        :return: The sov of this NewTower.
        :rtype: bool
        """
        return self._sov

    @sov.setter
    def sov(self, sov: bool):
        """
        Sets the sov of this NewTower.

        :param sov: The sov of this NewTower.
        :type sov: bool
        """

        self._sov = sov

    @property
    def type(self) -> int:
        """
        Gets the type of this NewTower.

        :return: The type of this NewTower.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type: int):
        """
        Sets the type of this NewTower.

        :param type: The type of this NewTower.
        :type type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

