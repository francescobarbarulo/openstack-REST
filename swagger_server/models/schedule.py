# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Schedule(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, peak_start: str=None, peak_end: str=None, image: str=None):  # noqa: E501
        """Schedule - a model defined in Swagger

        :param id: The id of this Schedule.  # noqa: E501
        :type id: int
        :param peak_start: The peak_start of this Schedule.  # noqa: E501
        :type peak_start: str
        :param peak_end: The peak_end of this Schedule.  # noqa: E501
        :type peak_end: str
        :param image: The image of this Schedule.  # noqa: E501
        :type image: str
        """
        self.swagger_types = {
            'id': int,
            'peak_start': str,
            'peak_end': str,
            'image': str
        }

        self.attribute_map = {
            'id': 'id',
            'peak_start': 'peak-start',
            'peak_end': 'peak-end',
            'image': 'image'
        }

        self._id = id
        self._peak_start = peak_start
        self._peak_end = peak_end
        self._image = image

    @classmethod
    def from_dict(cls, dikt) -> 'Schedule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Schedule of this Schedule.  # noqa: E501
        :rtype: Schedule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Schedule.


        :return: The id of this Schedule.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Schedule.


        :param id: The id of this Schedule.
        :type id: int
        """

        self._id = id

    @property
    def peak_start(self) -> str:
        """Gets the peak_start of this Schedule.


        :return: The peak_start of this Schedule.
        :rtype: str
        """
        return self._peak_start

    @peak_start.setter
    def peak_start(self, peak_start: str):
        """Sets the peak_start of this Schedule.


        :param peak_start: The peak_start of this Schedule.
        :type peak_start: str
        """
        if peak_start is None:
            raise ValueError("Invalid value for `peak_start`, must not be `None`")  # noqa: E501

        self._peak_start = peak_start

    @property
    def peak_end(self) -> str:
        """Gets the peak_end of this Schedule.


        :return: The peak_end of this Schedule.
        :rtype: str
        """
        return self._peak_end

    @peak_end.setter
    def peak_end(self, peak_end: str):
        """Sets the peak_end of this Schedule.


        :param peak_end: The peak_end of this Schedule.
        :type peak_end: str
        """

        self._peak_end = peak_end

    @property
    def image(self) -> str:
        """Gets the image of this Schedule.


        :return: The image of this Schedule.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image: str):
        """Sets the image of this Schedule.


        :param image: The image of this Schedule.
        :type image: str
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image
