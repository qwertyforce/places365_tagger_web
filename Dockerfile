FROM python:3.9-slim-buster

ARG USERNAME=app
ARG USER_UID=1000
ARG USER_GID=1000

WORKDIR /app
COPY ./ ./

RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu && pip install --no-cache-dir -r requirements.txt

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME 
RUN chown -R $USER_UID:$USER_GID /app

EXPOSE 33341
USER app
CMD ["python3", "image_tags_web.py"]