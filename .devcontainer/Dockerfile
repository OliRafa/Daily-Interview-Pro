FROM python:3.13-slim


ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
# RUN olduser=$(getent passwd ${USER_UID} | cut -d: -f1) \
#     && groupmod -n ${USERNAME} "$olduser" \
#     && usermod -l ${USERNAME} "$olduser" \
#     && usermod -d /home/${USERNAME} -m ${USERNAME}
RUN groupadd --gid $USER_GID $USERNAME \
	&& useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
	#
	# [Optional] Add sudo support. Omit if you don't need to install software after connecting.
	&& apt-get update \
	&& apt-get install -y sudo \
	&& echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
	&& chmod 0440 /etc/sudoers.d/$USERNAME

# Install and configure Poetry and iPython
RUN pip install --no-cache-dir -U pip \
	&& pip install --no-cache-dir poetry \
	&& poetry config virtualenvs.create false

