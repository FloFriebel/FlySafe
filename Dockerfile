#FROM tensorflow/tensorflow:2.10.0
FROM python:3.10.6

WORKDIR /prod

# First, pip install dependencies
COPY requirements.txt requirements.txt

# Then only, install taxifare!
#COPY taxifare taxifare
COPY jawp jawp
COPY api api
COPY tft_v1_1yeardata_3h tft_v1_1yeardata_3h
COPY tft_v1_1yeardata_3h.ckpt tft_v1_1yeardata_3h.ckpt
COPY setup.py setup.py
RUN pip install .

# We already have a make command for that!
COPY Makefile Makefile
#RUN make reset_local_files

#CMD ["uvicorn", "api.fast:app", "--host", "0.0.0.0", "--port", "$PORT"]
CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
