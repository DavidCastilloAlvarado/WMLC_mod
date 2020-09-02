# coding: utf-8

"""
    IBM Watson Machine Learning REST API

    ## Authorization  ### IBM Watson Machine Learning Credentials  To start working with API one needs to generate an `access token` using the `username` and `password` available on the Service Credentials tab of the IBM Watson Machine Learning service instance or also available in the VCAP environment variable.  Example of the Service Credentials:  ```json {     \"url\": \"https://ibm-watson-ml.mybluemix.net\",     \"access_key\": \"ERY9vcBfE4sE+F4g8hcotF9L+j81WXWeZv\",     \"username\": \"c1ef4b80-2ee2-458e-ab92-e9ca97ec657d\",     \"password\": \"030528d4-5a3e-4d4c-9258-5d553513be6f\" } ```  Example of obtaining `access token` from Token Endpoint using HTTP Basic Auth (for details please refer to Token section below):  ` curl --basic --user username:password https://ibm-watson-ml.mybluemix.net/v2/identity/token `   ### Apache Spark Service Credentials  The IBM Watson Machine Learning co-operates with the Apache Spark as a Service to deploy pipeline models. For API methods requiring Apache Spark Service instance a custom header: `X-Spark-Service-Instance` with Service Credentials must be specified. The header value is a **base64 encoded** string with the Service Credentials JSON data.  [Example of API method requiring Apache Spark Service](https://console.ng.bluemix.net/docs/services/PredictiveModeling/index-gentopic1.html#pm_service_api_spark_batch) 

    OpenAPI spec version: 2.0.0
    
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


class PipelineInput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, author=None, type=None, runtime_environment=None):
        """
        PipelineInput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'author': 'ArtifactAuthor',
            'type': 'PipelineType',
            'runtime_environment': 'RuntimeEnvironment'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'author': 'author',
            'type': 'type',
            'runtime_environment': 'runtimeEnvironment'
        }

        self._name = name
        self._description = description
        self._author = author
        self._type = type
        self._runtime_environment = runtime_environment

    @property
    def name(self):
        """
        Gets the name of this PipelineInput.
        Name of the pipeline

        :return: The name of this PipelineInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PipelineInput.
        Name of the pipeline

        :param name: The name of this PipelineInput.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PipelineInput.
        Description of the pipeline

        :return: The description of this PipelineInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PipelineInput.
        Description of the pipeline

        :param description: The description of this PipelineInput.
        :type: str
        """

        self._description = description

    @property
    def author(self):
        """
        Gets the author of this PipelineInput.
        Author of the pipeline

        :return: The author of this PipelineInput.
        :rtype: ArtifactAuthor
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this PipelineInput.
        Author of the pipeline

        :param author: The author of this PipelineInput.
        :type: ArtifactAuthor
        """

        self._author = author

    @property
    def type(self):
        """
        Gets the type of this PipelineInput.
        Type of the pipeline

        :return: The type of this PipelineInput.
        :rtype: PipelineType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PipelineInput.
        Type of the pipeline

        :param type: The type of this PipelineInput.
        :type: PipelineType
        """

        self._type = type

    @property
    def runtime_environment(self):
        """
        Gets the runtime_environment of this PipelineInput.
        runtime environment of caller

        :return: The runtime_environment of this PipelineInput.
        :rtype: RuntimeEnvironment
        """
        return self._runtime_environment

    @runtime_environment.setter
    def runtime_environment(self, runtime_environment):
        """
        Sets the runtime_environment of this PipelineInput.
        runtime environment of caller

        :param runtime_environment: The runtime_environment of this PipelineInput.
        :type: RuntimeEnvironment
        """

        self._runtime_environment = runtime_environment

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
