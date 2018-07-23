FROM pytorch/pytorch

MAINTAINER Arden Chew <achew4@jhu.edu>

RUN apt-get update

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
	cmake \
	python3-pip \
	vim \
	python-matplotlib \
	python-numpy \
	python-pil \
	python-scipy \
	build-essential \
	cython \
	python-pyqt5 \
	python-skimage

RUN pip install --no-cache-dir --upgrade pip setuptools \
	numpy \
	Pillow \
	opencv-python \
	scikit-image \
	render-python

EXPOSE 8888

CMD ["/bin/bash"]