from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.user_add_u_groups_response_200 import UserAddUGroupsResponse200
from ...models.user_add_u_groups_response_401 import UserAddUGroupsResponse401
from ...models.user_add_u_groups_response_403 import UserAddUGroupsResponse403
from ...models.user_add_u_groups_response_404 import UserAddUGroupsResponse404
from ...models.user_add_u_groups_response_422 import UserAddUGroupsResponse422
from ...models.user_add_u_groups_response_500 import UserAddUGroupsResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: list[int],

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/user/{id}/user-group".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UserAddUGroupsResponse200 | UserAddUGroupsResponse401 | UserAddUGroupsResponse403 | UserAddUGroupsResponse404 | UserAddUGroupsResponse422 | UserAddUGroupsResponse500 | None:
    if response.status_code == 200:
        response_200 = UserAddUGroupsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = UserAddUGroupsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = UserAddUGroupsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = UserAddUGroupsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = UserAddUGroupsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = UserAddUGroupsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UserAddUGroupsResponse200 | UserAddUGroupsResponse401 | UserAddUGroupsResponse403 | UserAddUGroupsResponse404 | UserAddUGroupsResponse422 | UserAddUGroupsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: list[int],

) -> Response[UserAddUGroupsResponse200 | UserAddUGroupsResponse401 | UserAddUGroupsResponse403 | UserAddUGroupsResponse404 | UserAddUGroupsResponse422 | UserAddUGroupsResponse500]:
    """ Adds a user to a user group in the application.

    Args:
        id (int):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserAddUGroupsResponse200 | UserAddUGroupsResponse401 | UserAddUGroupsResponse403 | UserAddUGroupsResponse404 | UserAddUGroupsResponse422 | UserAddUGroupsResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: list[int],

) -> UserAddUGroupsResponse200 | UserAddUGroupsResponse401 | UserAddUGroupsResponse403 | UserAddUGroupsResponse404 | UserAddUGroupsResponse422 | UserAddUGroupsResponse500 | None:
    """ Adds a user to a user group in the application.

    Args:
        id (int):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserAddUGroupsResponse200 | UserAddUGroupsResponse401 | UserAddUGroupsResponse403 | UserAddUGroupsResponse404 | UserAddUGroupsResponse422 | UserAddUGroupsResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: list[int],

) -> Response[UserAddUGroupsResponse200 | UserAddUGroupsResponse401 | UserAddUGroupsResponse403 | UserAddUGroupsResponse404 | UserAddUGroupsResponse422 | UserAddUGroupsResponse500]:
    """ Adds a user to a user group in the application.

    Args:
        id (int):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserAddUGroupsResponse200 | UserAddUGroupsResponse401 | UserAddUGroupsResponse403 | UserAddUGroupsResponse404 | UserAddUGroupsResponse422 | UserAddUGroupsResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: list[int],

) -> UserAddUGroupsResponse200 | UserAddUGroupsResponse401 | UserAddUGroupsResponse403 | UserAddUGroupsResponse404 | UserAddUGroupsResponse422 | UserAddUGroupsResponse500 | None:
    """ Adds a user to a user group in the application.

    Args:
        id (int):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserAddUGroupsResponse200 | UserAddUGroupsResponse401 | UserAddUGroupsResponse403 | UserAddUGroupsResponse404 | UserAddUGroupsResponse422 | UserAddUGroupsResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
