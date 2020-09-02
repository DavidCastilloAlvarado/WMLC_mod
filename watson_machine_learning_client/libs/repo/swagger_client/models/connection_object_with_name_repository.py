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


class ConnectionObjectWithNameRepository(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self,name=None, connection=None, source=None):
        """
        ConnectionObjectWithNameRepository - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'connection': 'dict(str, str)',
            'source': 'dict(str, str)'
        }

        self.attribute_map = {
            'name': 'name',
            'connection': 'connection',
            'source': 'source'
        }

        self._name = name
        self._connection = connection
        self._source = source

    @property
    def name(self):
        """
        Gets the name of this ConnectionObjectWithNameRepository.
        Name which identifies this connection

        :return: The name of this ConnectionObjectWithNameRepository.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConnectionObjectWithNameRepository.
        Name which identifies this connection

        :param name: The name of this ConnectionObjectWithNameRepository.
        :type: str
        """
        self._name = name

    @property
    def connection(self):
        """
        Gets the connection of this ConnectionObjectWithNameRepository.
        Connections Map to the feedback data store

        :return: The connection of this ConnectionObjectWithNameRepository.
        :rtype: dict(str, str)
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """
        Sets the connection of this ConnectionObjectWithNameRepository.
        Connections Map to the feedback data store

        :param connection: The connection of this ConnectionObjectWithNameRepository.
        :type: dict(str, str)
        """
        self._connection = connection

    @property
    def source(self):
        """
        Gets the source of this ConnectionObjectWithNameRepository.
        Optional details of the data store

        :return: The source of this ConnectionObjectWithNameRepository.
        :rtype: dict(str, str)
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this ConnectionObjectWithNameRepository.
        Optional details of the data store

        :param source: The source of this ConnectionObjectWithNameRepository.
        :type: dict(str, str)
        """
        self._source = source

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

