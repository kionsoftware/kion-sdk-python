from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_account_cache_convert_response_200 import GetAccountCacheConvertResponse200
from ...models.get_account_cache_convert_response_400 import GetAccountCacheConvertResponse400
from ...models.get_account_cache_convert_response_401 import GetAccountCacheConvertResponse401
from ...models.get_account_cache_convert_response_403 import GetAccountCacheConvertResponse403
from ...models.get_account_cache_convert_response_500 import GetAccountCacheConvertResponse500
from typing import cast



def _get_kwargs(
    id: int,
    project_id: int,
    *,
    start_datecode: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["start_datecode"] = start_datecode


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/account-cache/{id}/convert/{project_id}".format(id=quote(str(id), safe=""),project_id=quote(str(project_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAccountCacheConvertResponse200 | GetAccountCacheConvertResponse400 | GetAccountCacheConvertResponse401 | GetAccountCacheConvertResponse403 | GetAccountCacheConvertResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAccountCacheConvertResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAccountCacheConvertResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAccountCacheConvertResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAccountCacheConvertResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetAccountCacheConvertResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAccountCacheConvertResponse200 | GetAccountCacheConvertResponse400 | GetAccountCacheConvertResponse401 | GetAccountCacheConvertResponse403 | GetAccountCacheConvertResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    project_id: int,
    *,
    client: AuthenticatedClient,
    start_datecode: str,

) -> Response[GetAccountCacheConvertResponse200 | GetAccountCacheConvertResponse400 | GetAccountCacheConvertResponse401 | GetAccountCacheConvertResponse403 | GetAccountCacheConvertResponse500]:
    """ Converts an account from the cache into a normal account with a project.

     This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/{id}/convert/{project_id} instead.

    Args:
        id (int):
        project_id (int):
        start_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountCacheConvertResponse200 | GetAccountCacheConvertResponse400 | GetAccountCacheConvertResponse401 | GetAccountCacheConvertResponse403 | GetAccountCacheConvertResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
project_id=project_id,
start_datecode=start_datecode,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    project_id: int,
    *,
    client: AuthenticatedClient,
    start_datecode: str,

) -> GetAccountCacheConvertResponse200 | GetAccountCacheConvertResponse400 | GetAccountCacheConvertResponse401 | GetAccountCacheConvertResponse403 | GetAccountCacheConvertResponse500 | None:
    """ Converts an account from the cache into a normal account with a project.

     This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/{id}/convert/{project_id} instead.

    Args:
        id (int):
        project_id (int):
        start_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountCacheConvertResponse200 | GetAccountCacheConvertResponse400 | GetAccountCacheConvertResponse401 | GetAccountCacheConvertResponse403 | GetAccountCacheConvertResponse500
     """


    return sync_detailed(
        id=id,
project_id=project_id,
client=client,
start_datecode=start_datecode,

    ).parsed

async def asyncio_detailed(
    id: int,
    project_id: int,
    *,
    client: AuthenticatedClient,
    start_datecode: str,

) -> Response[GetAccountCacheConvertResponse200 | GetAccountCacheConvertResponse400 | GetAccountCacheConvertResponse401 | GetAccountCacheConvertResponse403 | GetAccountCacheConvertResponse500]:
    """ Converts an account from the cache into a normal account with a project.

     This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/{id}/convert/{project_id} instead.

    Args:
        id (int):
        project_id (int):
        start_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountCacheConvertResponse200 | GetAccountCacheConvertResponse400 | GetAccountCacheConvertResponse401 | GetAccountCacheConvertResponse403 | GetAccountCacheConvertResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
project_id=project_id,
start_datecode=start_datecode,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    project_id: int,
    *,
    client: AuthenticatedClient,
    start_datecode: str,

) -> GetAccountCacheConvertResponse200 | GetAccountCacheConvertResponse400 | GetAccountCacheConvertResponse401 | GetAccountCacheConvertResponse403 | GetAccountCacheConvertResponse500 | None:
    """ Converts an account from the cache into a normal account with a project.

     This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/{id}/convert/{project_id} instead.

    Args:
        id (int):
        project_id (int):
        start_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountCacheConvertResponse200 | GetAccountCacheConvertResponse400 | GetAccountCacheConvertResponse401 | GetAccountCacheConvertResponse403 | GetAccountCacheConvertResponse500
     """


    return (await asyncio_detailed(
        id=id,
project_id=project_id,
client=client,
start_datecode=start_datecode,

    )).parsed
