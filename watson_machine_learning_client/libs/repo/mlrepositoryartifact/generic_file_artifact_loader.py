################################################################################
#
# Licensed Materials - Property of IBM
# (C) Copyright IBM Corp. 2017
# US Government Users Restricted Rights - Use, duplication disclosure restricted
# by GSA ADP Schedule Contract with IBM Corp.
#
################################################################################


from watson_machine_learning_client.libs.repo.util.compression_util import CompressionUtil
from watson_machine_learning_client.libs.repo.util.unique_id_gen import uid_generate
from watson_machine_learning_client.libs.repo.mlrepository import MetaNames
import os, shutil

class GenericFileArtifactLoader(object):
    def load(self):
        return self.extract_content()

    def extract_content(self):
        directory_name = 'artifact_content'

        try:
            shutil.rmtree(directory_name)
        except:
            pass

        try:
            id_length = 20
            dir_id = uid_generate(id_length)
            model_dir_name = directory_name + dir_id
            file_name = '{}/model'.format(model_dir_name)
            os.makedirs(model_dir_name)
            input_stream = self.reader().read()
            file_content = input_stream.read()
            gz_f = open(file_name, 'wb+')
            gz_f.write(file_content)
            gz_f.close()
            self.reader().close()
            return os.path.abspath(file_name)
        except Exception as ex:
            raise ex
