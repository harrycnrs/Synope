FROM andrewosh/binder-base

USER root

RUN /bin/bash -c 'wget https://github.com/jgm/pandoc/releases/download/1.17.0.2/pandoc-1.17.0.2-1-amd64.deb; dpkg -i pandoc-1.17.0.2-1-amd64.deb'
RUN apt-get update -y &&\
    apt-get install -y texlive-full

USER main

ADD environment.yml /home/main/

RUN conda env create -f environment.yml
RUN /bin/bash -c "source activate synope && ipython kernelspec install-self --user"
RUN pip install notebook
RUN pip install pypandoc
RUN mkdir $HOME/.jupyter
RUN ipython profile create
RUN git clone https://github.com/damianavila/RISE.git
RUN cd RISE; python setup.py install
ADD python/session-2016-03-idf/styles/custom.css /home/main/.ipython/profile_default/static/custom/
