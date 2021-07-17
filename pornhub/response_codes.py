import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def check_response(response):
    known_codes = {"1001", "1002", "1003", "2001", "2002", "3001", "3002", "3003"}
    response = response.json()
    if "code" in response and response["code"] in known_codes:
        logging.info('response')
        raise ValueError(f'error message: {response["message"]}')
