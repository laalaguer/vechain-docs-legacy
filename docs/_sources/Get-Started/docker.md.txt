# Docker
## Run VeChainThor Authority Masternode in docker

**This method needs running all commands by docker with the data directory mapped to the container.**


### Pull image

``` shell
docker pull vechain/thor
```

###Export Master Key

First, start an interactive shell by docker:

```
docker run -it --rm\
-v {path-to-your-data-directory}:/root/.org.vechain.thor\
--entrypoint /bin/sh vechain/thor
```

Then export master key in the shell:

```
thor master-key --export > /root/.org.vechain.thor/keystore.json
```

Enter your password and check the generated file, then exit.


### Import Master Key

``` shell
docker run -it --rm\
-v {path-to-your-data-directory}:/root/.org.vechain.thor\
vechain/thor master-key --import
```

Follow the instruction by the program, input the `KeyStore` and also the password.

### Check Master Key

``` shell
docker run -it --rm\
-v {path-to-your-data-directory}:/root/.org.vechain.thor\
vechain/thor master-key
```

This command will print the Master Key.

### Start the Authority Masternode

``` shell
docker run -d\
-v {path-to-your-data-directory}:/root/.org.vechain.thor\
-p 127.0.0.1:8669:8669 -p 11235:11235 -p 11235:11235/udp\
--name thor-node vechain/thor --network main --skip-logs
```




## Run node in docker

Docker is one quick way for running a vechain node:
```
docker run -d\
  -v {path-to-your-data-directory}/.org.vechain.thor:/root/.org.vechain.thor\
  -p 127.0.0.1:8669:8669 -p 11235:11235 -p 11235:11235/udp\
  --name thor-node vechain/thor --network test
```

Do not forget to add the `--api-addr 0.0.0.0:8669` flag if you want other containers and/or hosts to have access to the RESTful API. `Thor`binds to `localhost` by default and it will not accept requests outside the container itself without the flag.

The [Dockerfile](https://github.com/vechain/thor/blob/master/Dockerfile) is designed to build the last release of the source code and will publish docker images to [dockerhub](https://hub.docker.com/r/vechain/thor/) by release, feel free to fork and build Dockerfile for your own purpose.

You can also refer to a tutorial created by VeChainInsider [How to install a VeChainThor node locally using Docker](https://vechaininsider.com/development/development-guides/how-to-install-a-vechain-thor-node-using-docker/).