FROM python:3.6

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
ADD . /app

#install dependencies:
RUN pip install -r requirements.txt

#RUN the application
CMD ["python","app.py"] 