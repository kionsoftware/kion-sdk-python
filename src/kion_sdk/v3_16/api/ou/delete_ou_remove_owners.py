from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_ou_remove_owners_response_200 import DeleteOURemoveOwnersResponse200
from ...models.delete_ou_remove_owners_response_400 import DeleteOURemoveOwnersResponse400
from ...models.delete_ou_remove_owners_response_401 import DeleteOURemoveOwnersResponse401
from ...models.delete_ou_remove_owners_response_403 import DeleteOURemoveOwnersResponse403
from ...models.delete_ou_remove_owners_response_404 import DeleteOURemoveOwnersResponse404
from ...models.delete_ou_remove_owners_response_422 import DeleteOURemoveOwnersResponse422
from ...models.delete_ou_remove_owners_response_500 import DeleteOURemoveOwnersResponse500
from ...models.ou_owners import OUOwners
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: OUOwners,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/ou/{id}/owner".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteOURemoveOwnersResponse200 | DeleteOURemoveOwnersResponse400 | DeleteOURemoveOwnersResponse401 | DeleteOURemoveOwnersResponse403 | DeleteOURemoveOwnersResponse404 | DeleteOURemoveOwnersResponse422 | DeleteOURemoveOwnersResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteOURemoveOwnersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteOURemoveOwnersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteOURemoveOwnersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteOURemoveOwnersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteOURemoveOwnersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteOURemoveOwnersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteOURemoveOwnersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteOURemoveOwnersResponse200 | DeleteOURemoveOwnersResponse400 | DeleteOURemoveOwnersResponse401 | DeleteOURemoveOwnersResponse403 | DeleteOURemoveOwnersResponse404 | DeleteOURemoveOwnersResponse422 | DeleteOURemoveOwnersResponse500]:
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
    body: OUOwners,

) -> Response[DeleteOURemoveOwnersResponse200 | DeleteOURemoveOwnersResponse400 | DeleteOURemoveOwnersResponse401 | DeleteOURemoveOwnersResponse403 | DeleteOURemoveOwnersResponse404 | DeleteOURemoveOwnersResponse422 | DeleteOURemoveOwnersResponse500]:
    """ Removes users and groups as owners of the OU in the application.

    Args:
        id (int):
        body (OUOwners): OUOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOURemoveOwnersResponse200 | DeleteOURemoveOwnersResponse400 | DeleteOURemoveOwnersResponse401 | DeleteOURemoveOwnersResponse403 | DeleteOURemoveOwnersResponse404 | DeleteOURemoveOwnersResponse422 | DeleteOURemoveOwnersResponse500]
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
    body: OUOwners,

) -> DeleteOURemoveOwnersResponse200 | DeleteOURemoveOwnersResponse400 | DeleteOURemoveOwnersResponse401 | DeleteOURemoveOwnersResponse403 | DeleteOURemoveOwnersResponse404 | DeleteOURemoveOwnersResponse422 | DeleteOURemoveOwnersResponse500 | None:
    """ Removes users and groups as owners of the OU in the application.

    Args:
        id (int):
        body (OUOwners): OUOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOURemoveOwnersResponse200 | DeleteOURemoveOwnersResponse400 | DeleteOURemoveOwnersResponse401 | DeleteOURemoveOwnersResponse403 | DeleteOURemoveOwnersResponse404 | DeleteOURemoveOwnersResponse422 | DeleteOURemoveOwnersResponse500
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
    body: OUOwners,

) -> Response[DeleteOURemoveOwnersResponse200 | DeleteOURemoveOwnersResponse400 | DeleteOURemoveOwnersResponse401 | DeleteOURemoveOwnersResponse403 | DeleteOURemoveOwnersResponse404 | DeleteOURemoveOwnersResponse422 | DeleteOURemoveOwnersResponse500]:
    """ Removes users and groups as owners of the OU in the application.

    Args:
        id (int):
        body (OUOwners): OUOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOURemoveOwnersResponse200 | DeleteOURemoveOwnersResponse400 | DeleteOURemoveOwnersResponse401 | DeleteOURemoveOwnersResponse403 | DeleteOURemoveOwnersResponse404 | DeleteOURemoveOwnersResponse422 | DeleteOURemoveOwnersResponse500]
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
    body: OUOwners,

) -> DeleteOURemoveOwnersResponse200 | DeleteOURemoveOwnersResponse400 | DeleteOURemoveOwnersResponse401 | DeleteOURemoveOwnersResponse403 | DeleteOURemoveOwnersResponse404 | DeleteOURemoveOwnersResponse422 | DeleteOURemoveOwnersResponse500 | None:
    """ Removes users and groups as owners of the OU in the application.

    Args:
        id (int):
        body (OUOwners): OUOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOURemoveOwnersResponse200 | DeleteOURemoveOwnersResponse400 | DeleteOURemoveOwnersResponse401 | DeleteOURemoveOwnersResponse403 | DeleteOURemoveOwnersResponse404 | DeleteOURemoveOwnersResponse422 | DeleteOURemoveOwnersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
