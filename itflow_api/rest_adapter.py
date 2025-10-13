import requests
import requests.packages
from typing import List, Dict
from itflow_api.exceptions import ITFlowApiException
from itflow_api.models import Result
from json import JSONDecodeError
import logging

class RestAdapter:
    def __init__(self, hostname: str, api_key: str = '', ver: str = 'v1', ssl_verify: bool = True, logger: logging.Logger = None):
        """
        Constructor for RestAdapter
        :param hostname: Domain name for the IT Flow instance being accessed i.e itflow.example.com
        :param api_key: (required) string used for authentication to the IT Flow instance
        :param ver: currently always v1 - used for future versioning
        :param ssl_verify: Normally set to True, but if having SSL/TLS cert validation issues, can turn off with False
        :param logger: (optional) If your app has a logger, pass it in here.
        """
        self.url = "https://{}/api/{}/".format(hostname, ver)
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        self._logger = logger or logging.getLogger(__name__)
        if not ssl_verify:
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings()

    def _do(self, http_method: str, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        full_url = self.url + endpoint
        log_line_pre = f"method={http_method}, url={full_url}, params={ep_params}"
        log_line_post = "success={}, status_code={}, message={}"

        # Log HTTP params and perform an HTTP request, catching and re-raising any exceptions
        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(method=http_method, url=full_url, verify=self._ssl_verify, params=ep_params, json=data)
        except requests.exceptions.RequestException as e:
            # Handle any request exceptions (network issues, invalid URL, etc.)
            self._logger.error(msg=(str(e)))
            raise ITFlowApiException(f"Request failed: {e}")
        
        # If status_code in 200-299 range, return success Result with data, otherwise raise exception
        is_success = 299 >= response.status_code >= 200     # 200 to 299 is OK
        log_line = log_line_pre + ',' + log_line_post.format(is_success, response.status_code, response.reason)
        if is_success:
            self._logger.debug(msg=log_line)
            # Deserialize JSON output to Python object, or return failed Result on exception
            try:
                data_out = response.json()
            except (ValueError, JSONDecodeError) as e:
                self._logger.error(msg=log_line_post.format(False, None, e))
                raise ITFlowApiException("Bad JSON in response") from e
            return Result(response.status_code, message=response.reason, data=data_out)
        self._logger.error(msg=log_line)
        raise ITFlowApiException(f"{response.status_code}: {response.reason}")
    
    def get(self, endpoint: str, ep_params: Dict = None) -> Result:
        endpoint = endpoint.lstrip('/')
        endpoint = endpoint + "/read.php"
        if ep_params is None:
            ep_params = {}
        ep_params.update({'api_key': self._api_key})
        return self._do(http_method='GET', endpoint=endpoint, ep_params=ep_params)
    
    def create(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        endpoint = endpoint.lstrip('/')
        endpoint = endpoint + "/create.php"
        if data is None:
            data = {}
        data.update({'api_key': self._api_key})
        return self._do(http_method='POST', endpoint=endpoint, ep_params=ep_params, data=data)
    
    def update(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        endpoint = endpoint.lstrip('/')
        endpoint = endpoint + "/update.php"
        if data is None:
            data = {}
        data.update({'api_key': self._api_key})
        return self._do(http_method='POST', endpoint=endpoint, ep_params=ep_params, data=data)
    
    def delete(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        endpoint = endpoint.lstrip('/')
        endpoint = endpoint + "/delete.php"
        if data is None:
            data = {}
        data.update({'api_key': self._api_key})
        return self._do(http_method='POST', endpoint=endpoint, ep_params=ep_params, data=data)