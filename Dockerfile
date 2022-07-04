#Base Image to use
FROM python:3.10.3

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

#Expose port 8080
EXPOSE 8080

#Copy Requirements.txt file into app directory
# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./


#install all requirements in requirements.txt
RUN pip install --upgrade pip
# RUN pip install pipwin
# RUN pipwin install gdal
# RUN pipwin install fiona
RUN pip install geopandas
RUN pip install -r requirements.txt


#Change Working Directory to app directory
# WORKDIR /app

#Run the application on port 8080
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]