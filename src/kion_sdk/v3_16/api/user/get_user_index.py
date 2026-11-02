from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_user_index_response_200 import GetUserIndexResponse200
from ...models.get_user_index_response_401 import GetUserIndexResponse401
from ...models.get_user_index_response_403 import GetUserIndexResponse403
from ...models.get_user_index_response_500 import GetUserIndexResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    state: str | Unset = 'all',
    include_deleted: bool | Unset = False,
    username: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["state"] = state

    params["include-deleted"] = include_deleted

    params["username"] = username


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/user",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetUserIndexResponse200 | GetUserIndexResponse401 | GetUserIndexResponse403 | GetUserIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetUserIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetUserIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetUserIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetUserIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetUserIndexResponse200 | GetUserIndexResponse401 | GetUserIndexResponse403 | GetUserIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    state: str | Unset = 'all',
    include_deleted: bool | Unset = False,
    username: str | Unset = UNSET,

) -> Response[GetUserIndexResponse200 | GetUserIndexResponse401 | GetUserIndexResponse403 | GetUserIndexResponse500]:
    """ Returns a list of users from the application.

    Args:
        state (str | Unset):  Default: 'all'.
        include_deleted (bool | Unset):  Default: False.
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserIndexResponse200 | GetUserIndexResponse401 | GetUserIndexResponse403 | GetUserIndexResponse500]
     """


    kwargs = _get_kwargs(
        state=state,
include_deleted=include_deleted,
username=username,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    state: str | Unset = 'all',
    include_deleted: bool | Unset = False,
    username: str | Unset = UNSET,

) -> GetUserIndexResponse200 | GetUserIndexResponse401 | GetUserIndexResponse403 | GetUserIndexResponse500 | None:
    """ Returns a list of users from the application.

    Args:
        state (str | Unset):  Default: 'all'.
        include_deleted (bool | Unset):  Default: False.
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserIndexResponse200 | GetUserIndexResponse401 | GetUserIndexResponse403 | GetUserIndexResponse500
     """


    return sync_detailed(
        client=client,
state=state,
include_deleted=include_deleted,
username=username,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    state: str | Unset = 'all',
    include_deleted: bool | Unset = False,
    username: str | Unset = UNSET,

) -> Response[GetUserIndexResponse200 | GetUserIndexResponse401 | GetUserIndexResponse403 | GetUserIndexResponse500]:
    """ Returns a list of users from the application.

    Args:
        state (str | Unset):  Default: 'all'.
        include_deleted (bool | Unset):  Default: False.
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserIndexResponse200 | GetUserIndexResponse401 | GetUserIndexResponse403 | GetUserIndexResponse500]
     """


    kwargs = _get_kwargs(
        state=state,
include_deleted=include_deleted,
username=username,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    state: str | Unset = 'all',
    include_deleted: bool | Unset = False,
    username: str | Unset = UNSET,

) -> GetUserIndexResponse200 | GetUserIndexResponse401 | GetUserIndexResponse403 | GetUserIndexResponse500 | None:
    """ Returns a list of users from the application.

    Args:
        state (str | Unset):  Default: 'all'.
        include_deleted (bool | Unset):  Default: False.
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserIndexResponse200 | GetUserIndexResponse401 | GetUserIndexResponse403 | GetUserIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,
state=state,
include_deleted=include_deleted,
username=username,

    )).parsed
