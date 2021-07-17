def check_response(response):
    faults = {"1001", "1002", "1003", "2001", "2002"}
    if "code" in response and response["code"] in faults:
        raise ValueError(f'{response["message"]}')
