from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_account_cache_convert_response_201 import PostAccountCacheConvertResponse201
from ...models.post_account_cache_convert_response_400 import PostAccountCacheConvertResponse400
from ...models.post_account_cache_convert_response_401 import PostAccountCacheConvertResponse401
from ...models.post_account_cache_convert_response_403 import PostAccountCacheConvertResponse403
from ...models.post_account_cache_convert_response_500 import PostAccountCacheConvertResponse500
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
        "method": "post",
        "url": "/v3/account-cache/{id}/convert/{project_id}".format(id=quote(str(id), safe=""),project_id=quote(str(project_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAccountCacheConvertResponse201 | PostAccountCacheConvertResponse400 | PostAccountCacheConvertResponse401 | PostAccountCacheConvertResponse403 | PostAccountCacheConvertResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAccountCacheConvertResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAccountCacheConvertResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAccountCacheConvertResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAccountCacheConvertResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PostAccountCacheConvertResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAccountCacheConvertResponse201 | PostAccountCacheConvertResponse400 | PostAccountCacheConvertResponse401 | PostAccountCacheConvertResponse403 | PostAccountCacheConvertResponse500]:
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

) -> Response[PostAccountCacheConvertResponse201 | PostAccountCacheConvertResponse400 | PostAccountCacheConvertResponse401 | PostAccountCacheConvertResponse403 | PostAccountCacheConvertResponse500]:
    """ Converts an account from the cache into a normal account with a project.

     Returns the ID for the converted account.

    Args:
        id (int):
        project_id (int):
        start_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountCacheConvertResponse201 | PostAccountCacheConvertResponse400 | PostAccountCacheConvertResponse401 | PostAccountCacheConvertResponse403 | PostAccountCacheConvertResponse500]
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

) -> PostAccountCacheConvertResponse201 | PostAccountCacheConvertResponse400 | PostAccountCacheConvertResponse401 | PostAccountCacheConvertResponse403 | PostAccountCacheConvertResponse500 | None:
    """ Converts an account from the cache into a normal account with a project.

     Returns the ID for the converted account.

    Args:
        id (int):
        project_id (int):
        start_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountCacheConvertResponse201 | PostAccountCacheConvertResponse400 | PostAccountCacheConvertResponse401 | PostAccountCacheConvertResponse403 | PostAccountCacheConvertResponse500
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

) -> Response[PostAccountCacheConvertResponse201 | PostAccountCacheConvertResponse400 | PostAccountCacheConvertResponse401 | PostAccountCacheConvertResponse403 | PostAccountCacheConvertResponse500]:
    """ Converts an account from the cache into a normal account with a project.

     Returns the ID for the converted account.

    Args:
        id (int):
        project_id (int):
        start_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountCacheConvertResponse201 | PostAccountCacheConvertResponse400 | PostAccountCacheConvertResponse401 | PostAccountCacheConvertResponse403 | PostAccountCacheConvertResponse500]
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

) -> PostAccountCacheConvertResponse201 | PostAccountCacheConvertResponse400 | PostAccountCacheConvertResponse401 | PostAccountCacheConvertResponse403 | PostAccountCacheConvertResponse500 | None:
    """ Converts an account from the cache into a normal account with a project.

     Returns the ID for the converted account.

    Args:
        id (int):
        project_id (int):
        start_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountCacheConvertResponse201 | PostAccountCacheConvertResponse400 | PostAccountCacheConvertResponse401 | PostAccountCacheConvertResponse403 | PostAccountCacheConvertResponse500
     """


    return (await asyncio_detailed(
        id=id,
project_id=project_id,
client=client,
start_datecode=start_datecode,

    )).parsed
