FROM andrewosh/binder-base

USER root

# Add Julia dependencies
RUN apt-get update
RUN apt-get install -y git && apt-get clean

USER main

RUN pip install notebook
RUN pip install jupyter
RUN git clone https://github.com/damianavila/RISE.git
RUN cd RISE; python setup.py install