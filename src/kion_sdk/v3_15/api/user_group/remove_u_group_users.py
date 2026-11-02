from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.remove_u_group_users_response_200 import RemoveUGroupUsersResponse200
from ...models.remove_u_group_users_response_400 import RemoveUGroupUsersResponse400
from ...models.remove_u_group_users_response_401 import RemoveUGroupUsersResponse401
from ...models.remove_u_group_users_response_403 import RemoveUGroupUsersResponse403
from ...models.remove_u_group_users_response_404 import RemoveUGroupUsersResponse404
from ...models.remove_u_group_users_response_422 import RemoveUGroupUsersResponse422
from ...models.remove_u_group_users_response_500 import RemoveUGroupUsersResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: list[int],

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/user-group/{id}/user".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RemoveUGroupUsersResponse200 | RemoveUGroupUsersResponse400 | RemoveUGroupUsersResponse401 | RemoveUGroupUsersResponse403 | RemoveUGroupUsersResponse404 | RemoveUGroupUsersResponse422 | RemoveUGroupUsersResponse500 | None:
    if response.status_code == 200:
        response_200 = RemoveUGroupUsersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = RemoveUGroupUsersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = RemoveUGroupUsersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = RemoveUGroupUsersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = RemoveUGroupUsersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = RemoveUGroupUsersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = RemoveUGroupUsersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RemoveUGroupUsersResponse200 | RemoveUGroupUsersResponse400 | RemoveUGroupUsersResponse401 | RemoveUGroupUsersResponse403 | RemoveUGroupUsersResponse404 | RemoveUGroupUsersResponse422 | RemoveUGroupUsersResponse500]:
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

) -> Response[RemoveUGroupUsersResponse200 | RemoveUGroupUsersResponse400 | RemoveUGroupUsersResponse401 | RemoveUGroupUsersResponse403 | RemoveUGroupUsersResponse404 | RemoveUGroupUsersResponse422 | RemoveUGroupUsersResponse500]:
    """ Removes users as members of a user group in the application.

    Args:
        id (int):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveUGroupUsersResponse200 | RemoveUGroupUsersResponse400 | RemoveUGroupUsersResponse401 | RemoveUGroupUsersResponse403 | RemoveUGroupUsersResponse404 | RemoveUGroupUsersResponse422 | RemoveUGroupUsersResponse500]
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

) -> RemoveUGroupUsersResponse200 | RemoveUGroupUsersResponse400 | RemoveUGroupUsersResponse401 | RemoveUGroupUsersResponse403 | RemoveUGroupUsersResponse404 | RemoveUGroupUsersResponse422 | RemoveUGroupUsersResponse500 | None:
    """ Removes users as members of a user group in the application.

    Args:
        id (int):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveUGroupUsersResponse200 | RemoveUGroupUsersResponse400 | RemoveUGroupUsersResponse401 | RemoveUGroupUsersResponse403 | RemoveUGroupUsersResponse404 | RemoveUGroupUsersResponse422 | RemoveUGroupUsersResponse500
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

) -> Response[RemoveUGroupUsersResponse200 | RemoveUGroupUsersResponse400 | RemoveUGroupUsersResponse401 | RemoveUGroupUsersResponse403 | RemoveUGroupUsersResponse404 | RemoveUGroupUsersResponse422 | RemoveUGroupUsersResponse500]:
    """ Removes users as members of a user group in the application.

    Args:
        id (int):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveUGroupUsersResponse200 | RemoveUGroupUsersResponse400 | RemoveUGroupUsersResponse401 | RemoveUGroupUsersResponse403 | RemoveUGroupUsersResponse404 | RemoveUGroupUsersResponse422 | RemoveUGroupUsersResponse500]
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

) -> RemoveUGroupUsersResponse200 | RemoveUGroupUsersResponse400 | RemoveUGroupUsersResponse401 | RemoveUGroupUsersResponse403 | RemoveUGroupUsersResponse404 | RemoveUGroupUsersResponse422 | RemoveUGroupUsersResponse500 | None:
    """ Removes users as members of a user group in the application.

    Args:
        id (int):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveUGroupUsersResponse200 | RemoveUGroupUsersResponse400 | RemoveUGroupUsersResponse401 | RemoveUGroupUsersResponse403 | RemoveUGroupUsersResponse404 | RemoveUGroupUsersResponse422 | RemoveUGroupUsersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
