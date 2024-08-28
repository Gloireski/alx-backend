# 0x03-queuing_system_in_js

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* How to run a Redis server on your machine
* How to run simple operations with the Redis client
* How to use a Redis client with Node JS for basic operations
* How to store hash values in Redis
* How to deal with async operations with Redis
* How to use Kue as a queue system
* How to build a basic Express app interacting with a Redis server
* How to the build a basic Express app interacting with a Redis server and queue

## Tasks

+ [x] 0. **Install a redis instance**
  + Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - [https://redis.io/download](https://redis.io/download)):
    ```powershell
    wget http://download.redis.io/releases/redis-6.0.10.tar.gz
    tar xzf redis-6.0.10.tar.gz
    cd redis-6.0.10
    make MALLOC=libc # for Linux systems
    # make MALLOC=jemalloc # for Mac OS X systems
    ```
    + Start Redis in the background with `src/redis-server`.
    + Make sure that the server is working with a ping `src/redis-cli ping`.
    + Using the Redis client again, set the value `School` for the key `Holberton`.
    + Kill the server with the process id of the redis-server (hint: use ps and grep).
  + Copy the [`dump.rdb`](dump.rdb) from the `redis-6.0.10` directory into the root of this project.
  + **Requirements:**
    + Running `get Holberton` in the client, should return `School`.

