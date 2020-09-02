# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class MlAssetsCreateFunctionsOutputArray(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, first=None, next=None, limit=None, resources=None):
        """
        MlAssetsCreateLibrariesOutputArray - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'first': 'MlAssetsCreateFunctionsOutputArrayFirst',
            'next': 'MlAssetsCreateFunctionsOutputArrayFirst',
            'limit': 'float',
            'resources': 'list[MlAssetsCreateFunctionsOutput]'
        }

        self.attribute_map = {
            'first': 'first',
            'next': 'next',
            'limit': 'limit',
            'resources': 'resources'
        }

        self._first = first
        self._next = next
        self._limit = limit
        self._resources = resources

    @property
    def first(self):
        """
        Gets the first of this MlAssetsCreateLibrariesOutputArray.


        :return: The first of this MlAssetsCreateLibrariesOutputArray.
        :rtype: MlAssetsCreateLibrariesOutputArrayFirst
        """
        return self._first

    @first.setter
    def first(self, first):
        """
        Sets the first of this MlAssetsCreateLibrariesOutputArray.


        :param first: The first of this MlAssetsCreateLibrariesOutputArray.
        :type: MlAssetsCreateLibrariesOutputArrayFirst
        """
        self._first = first

    @property
    def next(self):
        """
        Gets the next of this MlAssetsCreateLibrariesOutputArray.


        :return: The next of this MlAssetsCreateLibrariesOutputArray.
        :rtype: MlAssetsCreateLibrariesOutputArrayFirst
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Sets the next of this MlAssetsCreateLibrariesOutputArray.


        :param next: The next of this MlAssetsCreateLibrariesOutputArray.
        :type: MlAssetsCreateLibrariesOutputArrayFirst
        """
        self._next = next

    @property
    def limit(self):
        """
        Gets the limit of this MlAssetsCreateLibrariesOutputArray.


        :return: The limit of this MlAssetsCreateLibrariesOutputArray.
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this MlAssetsCreateLibrariesOutputArray.


        :param limit: The limit of this MlAssetsCreateLibrariesOutputArray.
        :type: float
        """
        self._limit = limit

    @property
    def resources(self):
        """
        Gets the resources of this MlAssetsCreateLibrariesOutputArray.


        :return: The resources of this MlAssetsCreateLibrariesOutputArray.
        :rtype: list[MlAssetsCreateLibrariesOutput]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this MlAssetsCreateLibrariesOutputArray.


        :param resources: The resources of this MlAssetsCreateLibrariesOutputArray.
        :type: list[MlAssetsCreateLibrariesOutput]
        """
        self._resources = resources

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

