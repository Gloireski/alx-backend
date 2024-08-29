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

+ [x] 1. **1. Node Redis Client**
 + Install [node_redis](https://github.com/redis/node-redis) using yarn or npm.
  + Using Babel and ES6, write a script named [`0-redis_client.js`](0-redis_client.js). It should connect to the Redis server running on your machine:
    + It should log to the console the message `Redis client connected to the server` when the connection to Redis works correctly.
    + It should log to the console the message `Redis client not connected to the server: ERROR_MESSAGE` when the connection to Redis does not work.
  + **Requirements:**
    + To import the library, you need to use the keyword `import`.

+ [x] 2. **Node Redis client and basic operations**
  + In a file [`1-redis_op.js`](1-redis_op.js), copy the code you previously wrote ([`0-redis_client.js`](0-redis_client.js)).
  + Add two functions:
    + `setNewSchool`:
      + It accepts two arguments `schoolName`, and `value`.
      + It should set in Redis the value for the key `schoolName`.
      + It should display a confirmation message using `redis.print`.
    + `displaySchoolValue`:
      + It accepts one argument `schoolName`.
      + It should log to the console the value for the key passed as argument.
  + At the end of the file, call:
    + `displaySchoolValue('Holberton');`.
    + `setNewSchool('HolbertonSanFrancisco', '100');`.
    + `displaySchoolValue('HolbertonSanFrancisco');`.
  + **Requirements:**
    + Use callbacks for any of the operation, we will look at async operations later.

+ [x] 3. **Node Redis client and async operations**
  + In a file [`2-redis_op_async.js`](2-redis_op_async.js), copy the code from the previous exercise ([`1-redis_op.js`](1-redis_op.js)).
  + Using `promisify`, modify the function `displaySchoolValue` to use ES6's `async / await`.
  + Same result as [`1-redis_op.js`](1-redis_op.js).

+ [x] 4. **Node Redis client and advanced operations**
+ [x] 5. **Node Redis client publisher and subscriber**
+ [x] 6. **Create the Job creator**
  + In a file named [`6-job_creator.js`](6-job_creator.js):
    + Create a queue with `Kue`.
    + Create an object containing the Job data with the following format:
      ```js
      {
        phoneNumber: string,
        message: string,
      }
      ```
    + Create a queue named `push_notification_code`, and create a job with the object created before.
    + When the job is created without error, log to the console `Notification job created: JOB ID`.
    + When the job is completed, log to the console `Notification job completed`.
    + When the job is failing, log to the console `Notification job failed`.
  + Nothing else will happen - to process the job, go to the next task!
  + If you execute multiple time this file, you will see the `JOB ID` increasing - it means you are storing new job to process…

+ [x] 7. **Create the Job processor**
  + In a file named [`6-job_processor.js`](6-job_processor.js):
  + Create a queue with `Kue`.
  + Create a function named `sendNotification`:
    + It will take two arguments `phoneNumber` and `message`.
    + It will log to the console `Sending notification to PHONE_NUMBER, with message: MESSAGE`.
  + Write the queue process that will listen to new jobs on `push_notification_code`:
    + Every new job should call the `sendNotification` function with the phone number and the message contained within the job data.
  + **Requirements:**
    + You only need one Redis server to execute the program.
    + You will need to have two node processes to run each script at the same time.
    + You must use `Kue` to set up the queue.
  + [`6-job_processor.js`](6-job_processor.js) and [`6-job_creator.js`](6-job_creator.js) are the same as [`5-subscriber.js`](5-subscriber.js) and [`5-publisher.js`](5-publisher.js) respectively but with a module to manage jobs.


