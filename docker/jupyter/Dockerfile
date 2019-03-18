FROM jupyter/minimal-notebook

USER root

# libav-tools for matplotlib anim
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER jovyan

# Install Python 3 packages
RUN conda install --quiet --yes \
	'pandas=*' \
	'matplotlib=*' \
	'plotly=*' \
	'seaborn=0.7*' \
	'mysql-connector-python=*' \
	'ipywidgets=*' \
	'astropy=*' \
	'skyfield=*' \
	'mpld3=*' \
	'astral=*' \
	'scikit-learn=*' \
	'statsmodels=*'

# Add shortcuts to distinguish pip for python2 and python3 envs
RUN ln -s $CONDA_DIR/envs/python2/bin/pip $CONDA_DIR/bin/pip2 && \
    ln -s $CONDA_DIR/bin/pip $CONDA_DIR/bin/pip3

# Install XGBoost library
RUN git clone --recursive https://github.com/dmlc/xgboost && \
    cd xgboost && \
    make -j4 && \
    cd python-package; python setup.py install

#RUN pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o
RUN pip install 'h2o==3.22.1.1'

