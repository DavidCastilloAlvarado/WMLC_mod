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


class TrainingStatusExperiments(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, training_guid=None, training_url=None, training_reference_name=None, training_definition_url=None, submitted_at=None, finished_at=None, current_at=None, current_iteration=None, total_iterations=None, state=None, message=None, metrics=None, hyper_parameters=None, result=None, failure=None):
        """
        TrainingStatusExperiments - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'training_guid': 'str',
            'training_url': 'str',
            'training_reference_name': 'str',
            'training_definition_url': 'str',
            'submitted_at': 'datetime',
            'finished_at': 'datetime',
            'current_at': 'datetime',
            'current_iteration': 'float',
            'total_iterations': 'float',
            'state': 'str',
            'message': 'str',
            'metrics': 'ArrayModelVersionMetricsExperiments',
            'hyper_parameters': 'HyperParametersForStatusExperiments',
            'result': 'TrainingStatusExperimentsResult',
            'failure': 'ErrorSchemaExperiments'
        }

        self.attribute_map = {
            'training_guid': 'training_guid',
            'training_url': 'training_url',
            'training_reference_name': 'training_reference_name',
            'training_definition_url': 'training_definition_url',
            'submitted_at': 'submitted_at',
            'finished_at': 'finished_at',
            'current_at': 'current_at',
            'current_iteration': 'current_iteration',
            'total_iterations': 'total_iterations',
            'state': 'state',
            'message': 'message',
            'metrics': 'metrics',
            'hyper_parameters': 'hyper_parameters',
            'result': 'result',
            'failure': 'failure'
        }

        self._training_guid = training_guid
        self._training_url = training_url
        self._training_reference_name = training_reference_name
        self._training_definition_url = training_definition_url
        self._submitted_at = submitted_at
        self._finished_at = finished_at
        self._current_at = current_at
        self._current_iteration = current_iteration
        self._total_iterations = total_iterations
        self._state = state
        self._message = message
        self._metrics = metrics
        self._hyper_parameters = hyper_parameters
        self._result = result
        self._failure = failure

    @property
    def training_guid(self):
        """
        Gets the training_guid of this TrainingStatusExperiments.


        :return: The training_guid of this TrainingStatusExperiments.
        :rtype: str
        """
        return self._training_guid

    @training_guid.setter
    def training_guid(self, training_guid):
        """
        Sets the training_guid of this TrainingStatusExperiments.


        :param training_guid: The training_guid of this TrainingStatusExperiments.
        :type: str
        """

        self._training_guid = training_guid

    @property
    def training_url(self):
        """
        Gets the training_url of this TrainingStatusExperiments.
        Currently, this is link to current /V3 training API, so to the /v3/models.

        :return: The training_url of this TrainingStatusExperiments.
        :rtype: str
        """
        return self._training_url

    @training_url.setter
    def training_url(self, training_url):
        """
        Sets the training_url of this TrainingStatusExperiments.
        Currently, this is link to current /V3 training API, so to the /v3/models.

        :param training_url: The training_url of this TrainingStatusExperiments.
        :type: str
        """

        self._training_url = training_url

    @property
    def training_reference_name(self):
        """
        Gets the training_reference_name of this TrainingStatusExperiments.


        :return: The training_reference_name of this TrainingStatusExperiments.
        :rtype: str
        """
        return self._training_reference_name

    @training_reference_name.setter
    def training_reference_name(self, training_reference_name):
        """
        Sets the training_reference_name of this TrainingStatusExperiments.


        :param training_reference_name: The training_reference_name of this TrainingStatusExperiments.
        :type: str
        """

        self._training_reference_name = training_reference_name

    @property
    def training_definition_url(self):
        """
        Gets the training_definition_url of this TrainingStatusExperiments.


        :return: The training_definition_url of this TrainingStatusExperiments.
        :rtype: str
        """
        return self._training_definition_url

    @training_definition_url.setter
    def training_definition_url(self, training_definition_url):
        """
        Sets the training_definition_url of this TrainingStatusExperiments.


        :param training_definition_url: The training_definition_url of this TrainingStatusExperiments.
        :type: str
        """

        self._training_definition_url = training_definition_url

    @property
    def submitted_at(self):
        """
        Gets the submitted_at of this TrainingStatusExperiments.


        :return: The submitted_at of this TrainingStatusExperiments.
        :rtype: datetime
        """
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, submitted_at):
        """
        Sets the submitted_at of this TrainingStatusExperiments.


        :param submitted_at: The submitted_at of this TrainingStatusExperiments.
        :type: datetime
        """

        self._submitted_at = submitted_at

    @property
    def finished_at(self):
        """
        Gets the finished_at of this TrainingStatusExperiments.


        :return: The finished_at of this TrainingStatusExperiments.
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """
        Sets the finished_at of this TrainingStatusExperiments.


        :param finished_at: The finished_at of this TrainingStatusExperiments.
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def current_at(self):
        """
        Gets the current_at of this TrainingStatusExperiments.


        :return: The current_at of this TrainingStatusExperiments.
        :rtype: datetime
        """
        return self._current_at

    @current_at.setter
    def current_at(self, current_at):
        """
        Sets the current_at of this TrainingStatusExperiments.


        :param current_at: The current_at of this TrainingStatusExperiments.
        :type: datetime
        """

        self._current_at = current_at

    @property
    def current_iteration(self):
        """
        Gets the current_iteration of this TrainingStatusExperiments.


        :return: The current_iteration of this TrainingStatusExperiments.
        :rtype: float
        """
        return self._current_iteration

    @current_iteration.setter
    def current_iteration(self, current_iteration):
        """
        Sets the current_iteration of this TrainingStatusExperiments.


        :param current_iteration: The current_iteration of this TrainingStatusExperiments.
        :type: float
        """

        self._current_iteration = current_iteration

    @property
    def total_iterations(self):
        """
        Gets the total_iterations of this TrainingStatusExperiments.


        :return: The total_iterations of this TrainingStatusExperiments.
        :rtype: float
        """
        return self._total_iterations

    @total_iterations.setter
    def total_iterations(self, total_iterations):
        """
        Sets the total_iterations of this TrainingStatusExperiments.


        :param total_iterations: The total_iterations of this TrainingStatusExperiments.
        :type: float
        """

        self._total_iterations = total_iterations

    @property
    def state(self):
        """
        Gets the state of this TrainingStatusExperiments.


        :return: The state of this TrainingStatusExperiments.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this TrainingStatusExperiments.


        :param state: The state of this TrainingStatusExperiments.
        :type: str
        """
        allowed_values = ["running", "completed", "failed", "canceled"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def message(self):
        """
        Gets the message of this TrainingStatusExperiments.


        :return: The message of this TrainingStatusExperiments.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this TrainingStatusExperiments.


        :param message: The message of this TrainingStatusExperiments.
        :type: str
        """

        self._message = message

    @property
    def metrics(self):
        """
        Gets the metrics of this TrainingStatusExperiments.


        :return: The metrics of this TrainingStatusExperiments.
        :rtype: ArrayModelVersionMetricsExperiments
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this TrainingStatusExperiments.


        :param metrics: The metrics of this TrainingStatusExperiments.
        :type: ArrayModelVersionMetricsExperiments
        """

        self._metrics = metrics

    @property
    def hyper_parameters(self):
        """
        Gets the hyper_parameters of this TrainingStatusExperiments.


        :return: The hyper_parameters of this TrainingStatusExperiments.
        :rtype: HyperParametersForStatusExperiments
        """
        return self._hyper_parameters

    @hyper_parameters.setter
    def hyper_parameters(self, hyper_parameters):
        """
        Sets the hyper_parameters of this TrainingStatusExperiments.


        :param hyper_parameters: The hyper_parameters of this TrainingStatusExperiments.
        :type: HyperParametersForStatusExperiments
        """

        self._hyper_parameters = hyper_parameters

    @property
    def result(self):
        """
        Gets the result of this TrainingStatusExperiments.


        :return: The result of this TrainingStatusExperiments.
        :rtype: TrainingStatusExperimentsResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this TrainingStatusExperiments.


        :param result: The result of this TrainingStatusExperiments.
        :type: TrainingStatusExperimentsResult
        """

        self._result = result

    @property
    def failure(self):
        """
        Gets the failure of this TrainingStatusExperiments.


        :return: The failure of this TrainingStatusExperiments.
        :rtype: ErrorSchemaExperiments
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        """
        Sets the failure of this TrainingStatusExperiments.


        :param failure: The failure of this TrainingStatusExperiments.
        :type: ErrorSchemaExperiments
        """

        self._failure = failure

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
