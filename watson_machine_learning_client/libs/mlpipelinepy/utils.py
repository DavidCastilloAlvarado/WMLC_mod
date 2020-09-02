################################################################################
# IBM Confidential
# OCO Source Materials
# (c) Copyright IBM Corp. 2017
# US Government Users Restricted Rights - Use, duplication disclosure restricted
# by GSA ADP Schedule Contract with IBM Corp.
################################################################################

'''
Created on Feb 17, 2017

@author: calin
'''
import logging

from pyspark.ml.param import Params
from pyspark.ml.pipeline import Pipeline
from pyspark.ml.wrapper import JavaEstimator
from pyspark.ml.wrapper import _jvm

__all__ = ['Learner', 'Target']

logger = logging.getLogger("mlpipelinepy")

def estimatorCopy(estimator, jvmObject, extra=None):
    if extra is None:
        extra = dict()
    if isinstance(estimator , Pipeline):
        that = Params.copy(estimator, extra)
        stages = [estimatorCopy(stage, jvmObject, extra) for stage in that.getStages()]
        return that.setStages(stages)
    elif (isinstance(estimator,JavaEstimator)):
        newJavaEstimator = estimator.copy(extra)
        paramMapConstructor = jvmObject.org.apache.spark.ml.param.ParamMap
        jParamMap = paramMapConstructor()
        newJavaEstimator._java_obj = newJavaEstimator._java_obj.copy(jParamMap)
        return newJavaEstimator
    else :
        return estimator.copy(extra)


def emptyParam():
    jvmObject = _jvm()
    return jvmObject.org.apache.spark.ml.param.ParamMap.empty()