# knime-on-cloud-free
Wrapper to deploy knime as a web service using knime, docker, python, redis.

## Usage:

```docker build -t knimedockerapi:v1 .```

### Standalone run:

```docker run -d -p 8080:8080 <IMAGE>```

### Run with external server fo rq module:

Create server: ```docker network create web_server --driver bridge```

Run container: ```docker run -dit --name knimeserver --network web_server knimedockerapi:v1```

Get ip addresses: ```docker inspect webserver```

## Related Repositories:

[knime-workflows](https://github.com/gokhangerdan/knime-workflows)

[knime-rq-module](https://github.com/gokhangerdan/knime-rq-module)

## TODO:

- Will be merged with knime-rq-module using docker compose
- Needs optimization on Dockerfiles
