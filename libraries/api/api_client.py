import requests
import logging
from typing import Dict, Any, Optional
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class APIClient:
    def __init__(
        self,
        base_url: str,
        timeout: int = 10,
        retries: int = 3,
        backoff_factor: float = 0.5,
    ):
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout

        self._logger = logging.getLogger(self.__class__.__name__)

        self._session = requests.Session()
        self._session.headers.update({
            "Content-Type": "application/json"
        })

        retry_strategy = Retry(
            total=retries,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"],
            backoff_factor=backoff_factor,
            raise_on_status=False,
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        self._session.mount("http://", adapter)
        self._session.mount("https://", adapter)

    # ---------- http verbs ----------

    def get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> requests.Response:
        return self._request("GET", path, params=params, headers=headers)

    def post(
        self,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> requests.Response:
        return self._request("POST", path, json=json, headers=headers)

    def put(
        self,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> requests.Response:
        return self._request("PUT", path, json=json, headers=headers)

    def delete(
        self,
        path: str,
        headers: Optional[Dict[str, str]] = None,
    ) -> requests.Response:
        return self._request("DELETE", path, headers=headers)

    # ---------- core ----------

    def _request(
        self,
        method: str,
        path: str,
        **kwargs,
    ) -> requests.Response:
        url = f"{self._base_url}/{path.lstrip('/')}"

        self._logger.info("%s %s", method, url)
        response = self._session.request(
            method=method,
            url=url,
            timeout=self._timeout,
            **kwargs,
        )

        self._logger.info(
            "Response %s %s -> %s",
            method,
            url,
            response.status_code,
        )

        return response
