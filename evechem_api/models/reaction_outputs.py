# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ReactionOutputs(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, amount: int=None, type: int=None):
        """
        ReactionOutputs - a model defined in Swagger

        :param amount: The amount of this ReactionOutputs.
        :type amount: int
        :param type: The type of this ReactionOutputs.
        :type type: int
        """
        self.swagger_types = {
            'amount': int,
            'type': int
        }

        self.attribute_map = {
            'amount': 'amount',
            'type': 'type'
        }

        self._amount = amount
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'ReactionOutputs':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The reaction_outputs of this ReactionOutputs.
        :rtype: ReactionOutputs
        """
        return deserialize_model(dikt, cls)

    @property
    def amount(self) -> int:
        """
        Gets the amount of this ReactionOutputs.

        :return: The amount of this ReactionOutputs.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """
        Sets the amount of this ReactionOutputs.

        :param amount: The amount of this ReactionOutputs.
        :type amount: int
        """

        self._amount = amount

    @property
    def type(self) -> int:
        """
        Gets the type of this ReactionOutputs.

        :return: The type of this ReactionOutputs.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type: int):
        """
        Sets the type of this ReactionOutputs.

        :param type: The type of this ReactionOutputs.
        :type type: int
        """

        self._type = type
