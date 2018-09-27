import asyncio


async def print_handler(message, *args):
    print('message is {}'.format(message))
    print('args is {}'.format(args))

    # mimic IO processing
    await asyncio.sleep(0.1)
    return True


async def error_handler(exc_info, message):
    print('exception {} received'.format(exc_info))
    # do not delete the message that originated the error
    return False
