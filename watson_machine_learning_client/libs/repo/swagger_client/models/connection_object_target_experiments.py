# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class ConnectionObjectTargetExperiments(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, connection=None, target=None):
        """
        ConnectionObjectTargetExperiments - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'connection': 'dict(str, str)',
            'target': 'object'
        }

        self.attribute_map = {
            'type': 'type',
            'connection': 'connection',
            'target': 'target'
        }

        self._type = type
        self._connection = connection
        self._target = target

    @property
    def type(self):
        """
        Gets the type of this ConnectionObjectTargetExperiments.


        :return: The type of this ConnectionObjectTargetExperiments.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ConnectionObjectTargetExperiments.


        :param type: The type of this ConnectionObjectTargetExperiments.
        :type: str
        """

        self._type = type

    @property
    def connection(self):
        """
        Gets the connection of this ConnectionObjectTargetExperiments.


        :return: The connection of this ConnectionObjectTargetExperiments.
        :rtype: dict(str, str)
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """
        Sets the connection of this ConnectionObjectTargetExperiments.


        :param connection: The connection of this ConnectionObjectTargetExperiments.
        :type: dict(str, str)
        """

        self._connection = connection

    @property
    def target(self):
        """
        Gets the target of this ConnectionObjectTargetExperiments.


        :return: The target of this ConnectionObjectTargetExperiments.
        :rtype: object
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this ConnectionObjectTargetExperiments.


        :param target: The target of this ConnectionObjectTargetExperiments.
        :type: object
        """

        self._target = target

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