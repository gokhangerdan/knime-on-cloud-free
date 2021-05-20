# knime-on-cloud-free
Wrapper to deploy knime as a web service using knime, docker, python, redis.

### Usage

```docker build -t knimedockerapi:v1 .```

```docker run -d -p 8080:8080 <IMAGE>```

### TODO

- Add rq support to the api.
