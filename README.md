# simple-sqs-consumer (using Loafer)

This project uses [Loafer](https://github.com/georgeyk/loafer) to consume an AWS SQS queue.

# Install

```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

# Configure

```
$ cp env-sample .env
```

Open .env and fill in the requested values.

# Running

```
$ python -m sqs_consumer
```

Add messages on queue and see how it works!
Adjust print_handler and error_handler for your purpouses.

