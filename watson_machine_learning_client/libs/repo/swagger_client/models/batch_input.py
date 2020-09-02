# coding: utf-8

"""
    IBM Watson Machine Learning REST API

    ## Authorization  ### IBM Watson Machine Learning Credentials  To start working with API one needs to generate an `access token` using the `username` and `password` available on the Service Credentials tab of the IBM Watson Machine Learning service instance or also available in the VCAP environment variable.  Example of the Service Credentials:  ```json {     \"url\": \"https://ibm-watson-ml.mybluemix.net\",     \"access_key\": \"ERY9vcBfE4sE+F4g8hcotF9L+j81WXWeZv\",     \"username\": \"c1ef4b80-2ee2-458e-ab92-e9ca97ec657d\",     \"password\": \"030528d4-5a3e-4d4c-9258-5d553513be6f\" } ```  Example of obtaining `access token` from Token Endpoint using HTTP Basic Auth (for details please refer to Token section below):  ` curl --basic --user username:password https://ibm-watson-ml.mybluemix.net/v3/identity/token `   ### Apache Spark Service Credentials  The IBM Watson Machine Learning co-operates with the Apache Spark as a Service to deploy pipeline models. For API methods requiring Apache Spark Service instance a custom header: `X-Spark-Service-Instance` with Service Credentials must be specified. The header value is a **base64 encoded** string with the Service Credentials JSON data.  [Example of API method requiring Apache Spark Service](https://console.ng.bluemix.net/docs/services/PredictiveModeling/index-gentopic1.html#pm_service_api_spark_batch)

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


class BatchInput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, artifact_version_href=None, name=None, input=None, output=None):
        """
        BatchInput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'artifact_version_href': 'str',
            'name': 'str',
            'input': 'InternalInputBatch',
            'output': 'InternalOutputBatch'
        }

        self.attribute_map = {
            'artifact_version_href': 'artifactVersionHref',
            'name': 'name',
            'input': 'input',
            'output': 'output'
        }

        self._artifact_version_href = artifact_version_href
        self._name = name
        self._input = input
        self._output = output

    @property
    def artifact_version_href(self):
        """
        Gets the artifact_version_href of this BatchInput.
        Href to the artifact version that is going to be deployed

        :return: The artifact_version_href of this BatchInput.
        :rtype: str
        """
        return self._artifact_version_href

    @artifact_version_href.setter
    def artifact_version_href(self, artifact_version_href):
        """
        Sets the artifact_version_href of this BatchInput.
        Href to the artifact version that is going to be deployed

        :param artifact_version_href: The artifact_version_href of this BatchInput.
        :type: str
        """

        self._artifact_version_href = artifact_version_href

    @property
    def name(self):
        """
        Gets the name of this BatchInput.
        User-friendly name for this Execution

        :return: The name of this BatchInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BatchInput.
        User-friendly name for this Execution

        :param name: The name of this BatchInput.
        :type: str
        """

        self._name = name

    @property
    def input(self):
        """
        Gets the input of this BatchInput.


        :return: The input of this BatchInput.
        :rtype: InternalInputBatch
        """
        return self._input

    @input.setter
    def input(self, input):
        """
        Sets the input of this BatchInput.


        :param input: The input of this BatchInput.
        :type: InternalInputBatch
        """

        self._input = input

    @property
    def output(self):
        """
        Gets the output of this BatchInput.


        :return: The output of this BatchInput.
        :rtype: InternalOutputBatch
        """
        return self._output

    @output.setter
    def output(self, output):
        """
        Sets the output of this BatchInput.


        :param output: The output of this BatchInput.
        :type: InternalOutputBatch
        """

        self._output = output

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
