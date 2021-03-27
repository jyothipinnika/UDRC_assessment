FROM python:3.6-slim

ARG APP_HOME=/opt/deployment
ARG PROJECT_NAME="Date-time"
ENV APP_HOME=${APP_HOME} \
    PROJECT_NAME=${PROJECT_NAME} \
    PROJECT_HOME=${APP_HOME}/${PROJECT_NAME}



ADD requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
COPY *-server.sh ${APP_HOME}/
RUN pip3 install -r requirements.txt && \
    mkdir -p ${PROJECT_HOME}/logs && \
    mkdir -p ${PROJECT_HOME}/conf && \
    mkdir -p ${PROJECT_HOME}/resources && \
    chmod a+x ${APP_HOME}/start-server.sh

COPY src ${PROJECT_HOME}/src
COPY conf ${PROJECT_HOME}/conf
COPY resources ${PROJECT_HOME}/resources
COPY app.py ${PROJECT_HOME}/
WORKDIR ${PROJECT_HOME}
ENTRYPOINT ["/opt/deployment/start-server.sh"]