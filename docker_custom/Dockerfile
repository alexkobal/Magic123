FROM nvidia/cuda:11.7.1-devel-ubuntu22.04

# Check if the nvidia runtima is active
RUN nvidia-smi

# To test if the nvidia runtime is installed run:
# # docker run --rm --runtime=nvidia nvidia/cuda:11.7.1-devel-ubuntu22.04 nvidia-smi

# Solution install older docker version Docker 20.10
# https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.8.1/install-guide.html

# If docker can not find the socket than you can fix it like in:
# https://superuser.com/questions/1741326/how-to-connect-to-docker-daemon-if-unix-var-run-docker-sock-is-not-available

# This command sets the default shell to be bash instead of sh
SHELL ["/bin/bash", "-c"]

RUN apt update && apt install -y \
    git \
    wget \
    libeigen3-dev \
    python3.10 \
    python3-pip \
    ffmpeg \
    libsm6 \
    libxext6 \
    python3.10-venv

RUN mkdir -p workdir
WORKDIR /workdir
RUN git clone https://github.com/alexkobal/Magic123.git

# In docker you need to use WORKDIR instead of cd
WORKDIR /workdir/Magic123

RUN git checkout multiview

# a100: 8.0; v100: 7.0; 2080ti: 7.5; titan xp: 6.1
ENV TORCH_CUDA_ARCH_LIST="7.0;7.5;8.0;6.1"

# use python venv
# https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV VIRTUAL_ENV=/workdir/Magic123/venv_magic123
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 install torch torchvision
RUN pip3 install -r requirements.txt
RUN bash scripts/install_ext.sh
