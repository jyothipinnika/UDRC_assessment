


import time

import cherrypy
import json



cherrypy.config.update("conf/app.conf")
# from src.utils.logging_util import Logger
from src.processing_data.process_data import Process_data_frame


# from src.connectivity.kafka_connection import KafkaConnection
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

cherrypy.config.update("conf/app.conf")
# LOGGER = Logger.get_instance()
class Date_time_controller(object):
    '''
    SPX candidate Controller
    that creates url
    '''

    @cherrypy.expose()
    @cherrypy.tools.json_out()
    def index(self):
        '''
        returns if service is up and running
        '''
        return {"status": "200", "message": "service is up and running"}



    @cherrypy.expose("SendData")
    @cherrypy.tools.json_out()
    def currentbuild(self):
        """
        to retrieve current build-version in prod
        :param req:
        :return:
        """
        try:

            df = Process_data_frame.read_data(cherrypy.config["data_path"],cherrypy.config["json_path"])
            # df = df.dropna()
            df.to_csv("output_file.csv",index=False)
            return {"message":"File Processed successfully"}
        except FileNotFoundError:
            # LOGGER.log_err.exception("no build-info file not found")
            return {"message":"File Processed failed"}




if __name__ == '__main__':
    # LOGGER.logger.info("Starting cherrypy")
    print("Starting cherrypy")
    cherrypy.tree.mount(Date_time_controller(), "/")
    cherrypy.engine.start()
    # cherrypy.engine.block()


    # LOGGER.logger.info("Stopping cherrypy")
