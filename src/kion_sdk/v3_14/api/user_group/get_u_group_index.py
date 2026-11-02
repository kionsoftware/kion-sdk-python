from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_u_group_index_response_200 import GetUGroupIndexResponse200
from ...models.get_u_group_index_response_401 import GetUGroupIndexResponse401
from ...models.get_u_group_index_response_500 import GetUGroupIndexResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    name: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["name"] = name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/user-group",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetUGroupIndexResponse200 | GetUGroupIndexResponse401 | GetUGroupIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetUGroupIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetUGroupIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetUGroupIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetUGroupIndexResponse200 | GetUGroupIndexResponse401 | GetUGroupIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,

) -> Response[GetUGroupIndexResponse200 | GetUGroupIndexResponse401 | GetUGroupIndexResponse500]:
    """ Returns a list of user groups in the application.

    Args:
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUGroupIndexResponse200 | GetUGroupIndexResponse401 | GetUGroupIndexResponse500]
     """


    kwargs = _get_kwargs(
        name=name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,

) -> GetUGroupIndexResponse200 | GetUGroupIndexResponse401 | GetUGroupIndexResponse500 | None:
    """ Returns a list of user groups in the application.

    Args:
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUGroupIndexResponse200 | GetUGroupIndexResponse401 | GetUGroupIndexResponse500
     """


    return sync_detailed(
        client=client,
name=name,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,

) -> Response[GetUGroupIndexResponse200 | GetUGroupIndexResponse401 | GetUGroupIndexResponse500]:
    """ Returns a list of user groups in the application.

    Args:
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUGroupIndexResponse200 | GetUGroupIndexResponse401 | GetUGroupIndexResponse500]
     """


    kwargs = _get_kwargs(
        name=name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,

) -> GetUGroupIndexResponse200 | GetUGroupIndexResponse401 | GetUGroupIndexResponse500 | None:
    """ Returns a list of user groups in the application.

    Args:
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUGroupIndexResponse200 | GetUGroupIndexResponse401 | GetUGroupIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,
name=name,

    )).parsed
