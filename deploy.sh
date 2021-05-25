docker build --pull --rm -f "DockerFile" -t tcp:latest "."
docker run --rm -it -d -p 127.0.0.1:65434:65434/tcp tcp:latest
python3 client.py --port 65434