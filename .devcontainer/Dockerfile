FROM "ubuntu:24.04"
RUN apt-get update

ARG USERNAME
ARG USER_UID
ARG USER_GID
ARG HOME
ENV HOME=${HOME}
ENV USERNAME=${USERNAME}

# Installing majority of packages
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
     && apt-get -y install --no-install-recommends \
     git \
     xdg-utils \
     locales \
     sudo \
     nano \
     vim \
     ca-certificates \
     apt-utils \
     curl \
     wget \
     gedit \
     dpkg \
     python3 \
     python3-pip \
     nodejs \
     npm \
     && rm -rf /var/lib/apt/lists/*
 
 # Install uvenv    
# Copy the script into the image
COPY .devcontainer/scripts/install.sh /tmp/install.sh

# Make it executable and run it
RUN chmod +x /tmp/install.sh && /tmp/install.sh
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="$HOME/.local/bin:${PATH}"

ENV PATH="/usr/local/bin:${PATH}"
# Make it executable and run it

 # Optional: Pre-install MCP servers (can also be deferred to runtime)
#  RUN uv install mcp-server-sqlite && \
#      uv install duckduckgo-mcp-server
 
 # Install @modelcontextprotocol/server-filesystem globally if preferred
 # or use npx at runtime instead
RUN npm install -g @modelcontextprotocol/server-filesystem

RUN locale-gen en_US.UTF-8

ENV \
     LANG=en_US.UTF-8 \
     LC_ALL=en_US.UTF-8 \
          #some packages will require this to be set. You can change this a rebuild
          #the image is needed
     TZ="America/Detroit" \
     LANGUAGE=en_US.UTF-8
# Download and install Go 1.24.3
RUN curl -LO https://go.dev/dl/go1.24.3.linux-amd64.tar.gz && \
    rm -rf /usr/local/go && \
    tar -C /usr/local -xzf go1.24.3.linux-amd64.tar.gz && \
    rm go1.24.3.linux-amd64.tar.gz

# Create the user
RUN if getent passwd $USER_UID > /dev/null; then userdel -r $(getent passwd $USER_UID | cut -d ':' -f 1); fi \ 
     && groupadd --force --gid $USER_GID $USERNAME \
     && useradd --no-log-init --uid $USER_UID --gid $USER_GID -m $USERNAME \
     && mkdir -p /etc/sudoers.d/ \
     # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
     && apt-get update \
     && apt-get install -y sudo \
     && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
     && chmod 0440 /etc/sudoers.d/$USERNAME
     
# Make Go available in PATH
ENV PATH="/usr/local/go/bin:${PATH}"

RUN go install github.com/mark3labs/mcphost@latest


USER $USERNAME

WORKDIR /home/${USERNAME}