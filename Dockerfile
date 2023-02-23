FROM public.ecr.aws/lambda/python:3.9

# install dependencies for OpenCV
RUN yum install -y mesa-libGL

# Install the function's dependencies using file requirements.txt
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Set the CMD to handler 
CMD [ "app.lambda_handler" ]
