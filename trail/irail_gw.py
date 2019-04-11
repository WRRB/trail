import requests
import logging


def base():
    return 'https://api.irail.be'


def headers():
    return {'Accept': 'application/json'}


def status_check(success):
    def sc_decorator(func):
        def arg_wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            sc = response.status_code
            if sc == success:
                return response.json()
            else:
                logging.error('Status check failed\n\treceived: {}\n\tmessage: {}'.format(sc, response.content))
        return arg_wrapper
    return sc_decorator


@status_check(success=200)
def connections(request_params):
    request_params_list = ['{}={}'.format(k, v) for k, v in request_params.iteritems()]
    url = 'connections/?{}'.format("&".join(request_params_list))
    return requests.get(url='{}/{}'.format(base(), url), headers=headers())

