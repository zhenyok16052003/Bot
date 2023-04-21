FROM python:3.11.3
WORKDIR /pythonProject
COPY requirements.txt /pythonProject/
RUN pip install -r requirements.txt
COPY . /pythonProject/
CMD ["python", "main.py"]