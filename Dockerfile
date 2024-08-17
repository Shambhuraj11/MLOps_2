FROM python:3.8-slim-buster
USER root
RUN mkdir /app
COPY . /app/
WORKDIR /app/
RUN pip3 install -r requirements.txt
RUN python setup.py install

ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True
RUN airflow db init
# RUN airflow users create -e sunny.savita@ineuron.ai -f sunny -l savita -p admin -r Admin -u admin
RUN airflow users create -e shambhurajpatil11@gmail.com -f shambhuraj -l patil -p admin -r Admin -u admin

RUN chmod 777 start.sh
RUN apt update -y
ENTRYPOINT [ "/bin/sh" ]
CMD ["start.sh"]

# FROM python:3.8-slim-bookworm AS backend-builder
# RUN mkdir /app
# WORKDIR /app
# COPY ./requirements.txt /app/requirements.txt
# RUN pip install -r /app/requirements.txt

# # # Create final image
# # FROM python:3.8-slim-bookworm
# # WORKDIR /app/

# # # copy dependencies
# # COPY --from=backend-builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
# # COPY --from=backend-builder /usr/local/bin /usr/local/bin

# # # Ensure PATH is set correctly
# # ENV PATH=/usr/local/bin:$PATH

# COPY . /app/
# USER root
# ENV AIRFLOW_HOME = "/app/airflow"
# ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT = 1000
# ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING = True
# RUN airflow db init
# RUN airflow users create -e shambhurajpatil11@gmail.com -f shambhuraj -l patil -p admin -r Admin -u admin
# RUN chmod 777 start.sh
# RUN apt update -y
# ENTRYPOINT [ "bin/sh" ]
# CMD [ "start.sh" ]