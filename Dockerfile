FROM waggle/plugin-base:1.1.1-base

# install sshpass
RUN apt-get update && apt-get install -y sshpass rsync

# For smartflux ssh
RUN echo "Ciphers aes128-cbc" >> /etc/ssh/ssh_config

COPY rsync_data.py /app/
WORKDIR /app
ENTRYPOINT ["python3", "/app/rsync_data.py"]
