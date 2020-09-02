################################################################################
#
# Licensed Materials - Property of IBM
# (C) Copyright IBM Corp. 2017
# US Government Users Restricted Rights - Use, duplication disclosure restricted
# by GSA ADP Schedule Contract with IBM Corp.
#
################################################################################


from .spark_pipeline_reader import SparkPipelineReader
from watson_machine_learning_client.libs.repo.mlrepository import MetaNames, MetaProps
from watson_machine_learning_client.libs.repo.mlrepository import ModelArtifact
from watson_machine_learning_client.libs.repo.util import SparkUtil,Json2ObjectMapper
from .version_helper import VersionHelper
from watson_machine_learning_client.libs.repo.util.library_imports import LibraryChecker
from watson_machine_learning_client.libs.repo.base_constants import *
from .spark_version import SparkVersion

lib_checker = LibraryChecker()
if lib_checker.installed_libs[PYSPARK]:
    from pyspark.ml.pipeline import Pipeline, PipelineModel
    from pyspark.sql import DataFrame
    import json
    from pyspark.sql.types import *

class SparkPipelineModelArtifact(ModelArtifact):
    """
    Class of model artifacts created with MLRepositoryCLient.

    :param pyspark.ml.PipelineModel ml_pipeline_model: Pipeline Model which will be wrapped
    :param DataFrame training_data: training_data compatible with Pipeline Model
    :param SparkPipelineArtifact pipeline_artifact: optional, pipeline artifact which Pipeline was used to generate Pipeline Model for this artifact

    :ivar pyspark.ml.PipelineModel ml_pipeline_model: Pipeline Model associated with this artifact
    :ivar DataFrame training_data: training_data compatible with Pipeline Model of this artifact
    """
    def __init__(self, ml_pipeline_model, training_data, uid=None, name=None, pipeline_artifact=None, meta_props=MetaProps({})):
        super(SparkPipelineModelArtifact, self).__init__(uid, name, meta_props)

        type_identified = False
        type_sparkmodel = False
        lib_checker.check_lib(PYSPARK)
        if issubclass(type(ml_pipeline_model), PipelineModel):
            type_identified = True
            type_sparkmodel = True

        if not type_identified and lib_checker.installed_libs[MLPIPELINE]:
            from mlpipelinepy.mlpipeline import MLPipelineModel
            if issubclass(type(ml_pipeline_model), MLPipelineModel):
                type_identified = True

        if not type_identified:
            raise ValueError('Invalid type for ml_pipeline: {}'.format(ml_pipeline_model.__class__.__name__))

        if not isinstance(training_data, DataFrame):
            raise ValueError('Invalid type for training_data: {}'.format(training_data.__class__.__name__))

        self.ml_pipeline_model = ml_pipeline_model
        self.training_data = training_data
        self._pipeline_artifact = pipeline_artifact

        if self._pipeline_artifact is not None:
            self.ml_pipeline = self._pipeline_artifact.pipeline_instance()
        else:
            if not type_sparkmodel:
                try:
                    from mlpipelinepy.mlpipeline import MLPipelineModel
                    if issubclass(type(ml_pipeline_model), MLPipelineModel):
                        self.ml_pipeline = ml_pipeline_model.parent
                except:
                    raise ValueError('Invalid type for ml_pipeline: {}'.format(ml_pipeline_model.__class__.__name__))
            else:
                self.ml_pipeline = None


        if meta_props.prop(MetaNames.RUNTIMES) is None and meta_props.prop(MetaNames.RUNTIME) is None and meta_props.prop(MetaNames.FRAMEWORK_RUNTIMES) is None:
            ver = SparkVersion.significant()
            runtimes = '[{"name":"spark","version": "'+ ver + '"}]'
            self.meta.merge(
                MetaProps({MetaNames.FRAMEWORK_RUNTIMES: runtimes})
            )

        # # TODO : Check and fix do we need to the merge training data ref
        self.meta.merge(
            MetaProps({
                MetaNames.FRAMEWORK_VERSION: VersionHelper.getFrameworkVersion(ml_pipeline_model),
                MetaNames.FRAMEWORK_NAME: VersionHelper.model_type(ml_pipeline_model),
                MetaNames.TRAINING_DATA_SCHEMA: Json2ObjectMapper.to_dict(self.training_data.schema.json()),
                MetaNames.LABEL_FIELD: SparkUtil.get_label_col(ml_pipeline_model) if meta_props.prop(MetaNames.LABEL_FIELD) is None else meta_props.prop(MetaNames.LABEL_FIELD)
            })
        )
        try:
            next(field for field in self.meta.prop(MetaNames.TRAINING_DATA_SCHEMA)['fields'] if field['name'] == self.meta.prop(MetaNames.LABEL_FIELD))
        except StopIteration:
            raise ValueError("Label \"{}\" cannot be found in training data schema.".format(self.meta.prop(MetaNames.LABEL_FIELD)))
        #get the label field and values  and update training_data_schema
        label_field = next(field for field in meta_props.prop(MetaNames.TRAINING_DATA_SCHEMA)['fields'] if field['name'] == meta_props.prop(MetaNames.LABEL_FIELD))
        label_field['metadata']['modeling_role'] = 'target'

        if meta_props.prop(MetaNames.LABEL_VALUES) is not None:
         label_field['metadata']['values'] = meta_props.prop(MetaNames.LABEL_VALUES)

        output_schema_present = False  # Flag to make sure that output_schema is merged to other meta only if either it is passed by user or PREDICTION_FIELD etc. fields are set.

        if meta_props.prop(MetaNames.OUTPUT_DATA_SCHEMA) is not None:
            output_schema_present = True
            if issubclass(type(meta_props.prop(MetaNames.OUTPUT_DATA_SCHEMA)), dict):
                inputfields = meta_props.prop(MetaNames.OUTPUT_DATA_SCHEMA)['fields']
            else:
                inputfields = Json2ObjectMapper.to_dict(meta_props.prop(MetaNames.OUTPUT_DATA_SCHEMA))['fields']
            output_schema = StructType([StructField.fromJson(f) for f in inputfields])  # this will be of type StructType
        else:
            output_schema = StructType()
            inputfields = filter(lambda f: f['name'] != meta_props.prop(MetaNames.LABEL_FIELD),
                                 meta_props.prop(MetaNames.TRAINING_DATA_SCHEMA)['fields'])
            # based on the meta props set, update output_data_schema
        if meta_props.prop(MetaNames.PREDICTION_FIELD) is not None and (
            self._found_field(inputfields, 'prediction') == False):
            output_schema.add(meta_props.prop(MetaNames.PREDICTION_FIELD), DoubleType(), False,
                              {'modeling_role': 'prediction'})
            output_schema_present = True
        if meta_props.prop(MetaNames.PROBABILITY_FIELD) is not None and (
            self._found_field(inputfields, 'probability') == False):
            output_schema.add(meta_props.prop(MetaNames.PROBABILITY_FIELD), ArrayType(DoubleType(), True), False,
                              {'modeling_role': 'probability'})
            output_schema_present = True
        if meta_props.prop(MetaNames.TRANSFORMED_LABEL_FIELD) is not None and (
            self._found_field(inputfields, 'transformed-target') == False):
            output_schema.add(meta_props.prop(MetaNames.TRANSFORMED_LABEL_FIELD), DoubleType(), False,
                              {'modeling_role': 'transformed-target'})
            output_schema_present = True
        if meta_props.prop(MetaNames.DECODED_LABEL) is not None and (
            self._found_field(inputfields, 'decoded-target') == False):
            output_schema.add(meta_props.prop(MetaNames.DECODED_LABEL), DoubleType(), False,
                              {'modeling_role': 'decoded-target', 'values': meta_props.prop(MetaNames.LABEL_VALUES)})
            output_schema_present = True

        if (output_schema_present != False):
            self.meta.merge(
                MetaProps({
                    MetaNames.OUTPUT_DATA_SCHEMA: Json2ObjectMapper.to_dict(output_schema.json())}))

    def pipeline_artifact(self):
        """
        Returns Pipeline artifact associated with this model artifact.

        If pipeline artifact was provided by user during creation - it will be returned. Otherwise will be created new pipeline artifact and returned.

        :return: Pipeline artifact associated with this Model artifact
        :rtype: SparkPipelineArtifact
        """
        if self._pipeline_artifact is None:

            from .ml_repository_artifact import MLRepositoryArtifact
            if self.ml_pipeline is not None:
                self._pipeline_artifact = MLRepositoryArtifact(ml_artifact=self.ml_pipeline, name=self.name, meta_props=self.meta)
            else:
                pass

        return self._pipeline_artifact

    def reader(self):
        """
        Returns reader used for getting pipeline model content.

        :return: reader for pyspark.ml.PipelineModel
        :rtype: SparkPipelineReader
        """
        try:
            return self._reader
        except:
            self._reader = SparkPipelineReader(self.ml_pipeline_model, 'model')
            return self._reader

    def _copy(self, uid=None, pipeline_artifact=None, meta_props=None):
        if uid is None:
            uid = self.uid

        if pipeline_artifact is None:
            pipeline_artifact = self.pipeline_artifact()

        if meta_props is None:
            meta_props = self.meta

        return SparkPipelineModelArtifact(
            self.ml_pipeline_model,
            training_data=self.training_data,
            uid=uid,
            name=self.name,
            pipeline_artifact=pipeline_artifact,
            meta_props=meta_props
        )

    def _found_field(self, inputfields, field):
        found = False
        for f in inputfields:
         if 'metadata' in f:
          if 'modeling_role' in f['metadata']:
            if f['metadata']['modeling_role'] == field:
                found = True
                break
        return found