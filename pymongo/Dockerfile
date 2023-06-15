FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7


RUN apt-get update \
  && apt-get -y install gcc \
  && apt-get -y install g++ \
  && apt-get -y install unixodbc unixodbc-dev \
  && apt-get clean
RUN apt-get install libgl1 -y

RUN pip install --upgrade pip setuptools wheel
RUN pip install spacy==2.3.7
RUN python -m spacy download en_core_web_sm
#RUN apt install uvicorn -y
#RUN apt install tesseract-ocr -y



COPY real.txt real.txt
# RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r real.txt
COPY ./app .