from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_u_group_owners_response_200 import DeleteUGroupOwnersResponse200
from ...models.delete_u_group_owners_response_400 import DeleteUGroupOwnersResponse400
from ...models.delete_u_group_owners_response_401 import DeleteUGroupOwnersResponse401
from ...models.delete_u_group_owners_response_403 import DeleteUGroupOwnersResponse403
from ...models.delete_u_group_owners_response_404 import DeleteUGroupOwnersResponse404
from ...models.delete_u_group_owners_response_422 import DeleteUGroupOwnersResponse422
from ...models.delete_u_group_owners_response_500 import DeleteUGroupOwnersResponse500
from ...models.u_group_owners import UGroupOwners
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: UGroupOwners,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/user-group/{id}/owner".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteUGroupOwnersResponse200 | DeleteUGroupOwnersResponse400 | DeleteUGroupOwnersResponse401 | DeleteUGroupOwnersResponse403 | DeleteUGroupOwnersResponse404 | DeleteUGroupOwnersResponse422 | DeleteUGroupOwnersResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteUGroupOwnersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteUGroupOwnersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteUGroupOwnersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteUGroupOwnersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteUGroupOwnersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteUGroupOwnersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteUGroupOwnersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteUGroupOwnersResponse200 | DeleteUGroupOwnersResponse400 | DeleteUGroupOwnersResponse401 | DeleteUGroupOwnersResponse403 | DeleteUGroupOwnersResponse404 | DeleteUGroupOwnersResponse422 | DeleteUGroupOwnersResponse500]:
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
    body: UGroupOwners,

) -> Response[DeleteUGroupOwnersResponse200 | DeleteUGroupOwnersResponse400 | DeleteUGroupOwnersResponse401 | DeleteUGroupOwnersResponse403 | DeleteUGroupOwnersResponse404 | DeleteUGroupOwnersResponse422 | DeleteUGroupOwnersResponse500]:
    """ Removes users and groups as owners of a user group in the application.

    Args:
        id (int):
        body (UGroupOwners): UGroupOwners defines a user group owner update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUGroupOwnersResponse200 | DeleteUGroupOwnersResponse400 | DeleteUGroupOwnersResponse401 | DeleteUGroupOwnersResponse403 | DeleteUGroupOwnersResponse404 | DeleteUGroupOwnersResponse422 | DeleteUGroupOwnersResponse500]
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
    body: UGroupOwners,

) -> DeleteUGroupOwnersResponse200 | DeleteUGroupOwnersResponse400 | DeleteUGroupOwnersResponse401 | DeleteUGroupOwnersResponse403 | DeleteUGroupOwnersResponse404 | DeleteUGroupOwnersResponse422 | DeleteUGroupOwnersResponse500 | None:
    """ Removes users and groups as owners of a user group in the application.

    Args:
        id (int):
        body (UGroupOwners): UGroupOwners defines a user group owner update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUGroupOwnersResponse200 | DeleteUGroupOwnersResponse400 | DeleteUGroupOwnersResponse401 | DeleteUGroupOwnersResponse403 | DeleteUGroupOwnersResponse404 | DeleteUGroupOwnersResponse422 | DeleteUGroupOwnersResponse500
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
    body: UGroupOwners,

) -> Response[DeleteUGroupOwnersResponse200 | DeleteUGroupOwnersResponse400 | DeleteUGroupOwnersResponse401 | DeleteUGroupOwnersResponse403 | DeleteUGroupOwnersResponse404 | DeleteUGroupOwnersResponse422 | DeleteUGroupOwnersResponse500]:
    """ Removes users and groups as owners of a user group in the application.

    Args:
        id (int):
        body (UGroupOwners): UGroupOwners defines a user group owner update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUGroupOwnersResponse200 | DeleteUGroupOwnersResponse400 | DeleteUGroupOwnersResponse401 | DeleteUGroupOwnersResponse403 | DeleteUGroupOwnersResponse404 | DeleteUGroupOwnersResponse422 | DeleteUGroupOwnersResponse500]
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
    body: UGroupOwners,

) -> DeleteUGroupOwnersResponse200 | DeleteUGroupOwnersResponse400 | DeleteUGroupOwnersResponse401 | DeleteUGroupOwnersResponse403 | DeleteUGroupOwnersResponse404 | DeleteUGroupOwnersResponse422 | DeleteUGroupOwnersResponse500 | None:
    """ Removes users and groups as owners of a user group in the application.

    Args:
        id (int):
        body (UGroupOwners): UGroupOwners defines a user group owner update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUGroupOwnersResponse200 | DeleteUGroupOwnersResponse400 | DeleteUGroupOwnersResponse401 | DeleteUGroupOwnersResponse403 | DeleteUGroupOwnersResponse404 | DeleteUGroupOwnersResponse422 | DeleteUGroupOwnersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
