from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_ou_response_400 import DeleteOUResponse400
from ...models.delete_ou_response_401 import DeleteOUResponse401
from ...models.delete_ou_response_403 import DeleteOUResponse403
from ...models.delete_ou_response_404 import DeleteOUResponse404
from ...models.delete_ou_response_500 import DeleteOUResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/ou/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | DeleteOUResponse400 | DeleteOUResponse401 | DeleteOUResponse403 | DeleteOUResponse404 | DeleteOUResponse500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = DeleteOUResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteOUResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteOUResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteOUResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteOUResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | DeleteOUResponse400 | DeleteOUResponse401 | DeleteOUResponse403 | DeleteOUResponse404 | DeleteOUResponse500]:
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

) -> Response[Any | DeleteOUResponse400 | DeleteOUResponse401 | DeleteOUResponse403 | DeleteOUResponse404 | DeleteOUResponse500]:
    """ Delete an OU

     Deletes the specified OU from the system. The OU cannot be deleted if it has child OUs, projects,
    funding sources, transactions, or a balance.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteOUResponse400 | DeleteOUResponse401 | DeleteOUResponse403 | DeleteOUResponse404 | DeleteOUResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Any | DeleteOUResponse400 | DeleteOUResponse401 | DeleteOUResponse403 | DeleteOUResponse404 | DeleteOUResponse500 | None:
    """ Delete an OU

     Deletes the specified OU from the system. The OU cannot be deleted if it has child OUs, projects,
    funding sources, transactions, or a balance.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteOUResponse400 | DeleteOUResponse401 | DeleteOUResponse403 | DeleteOUResponse404 | DeleteOUResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Any | DeleteOUResponse400 | DeleteOUResponse401 | DeleteOUResponse403 | DeleteOUResponse404 | DeleteOUResponse500]:
    """ Delete an OU

     Deletes the specified OU from the system. The OU cannot be deleted if it has child OUs, projects,
    funding sources, transactions, or a balance.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteOUResponse400 | DeleteOUResponse401 | DeleteOUResponse403 | DeleteOUResponse404 | DeleteOUResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Any | DeleteOUResponse400 | DeleteOUResponse401 | DeleteOUResponse403 | DeleteOUResponse404 | DeleteOUResponse500 | None:
    """ Delete an OU

     Deletes the specified OU from the system. The OU cannot be deleted if it has child OUs, projects,
    funding sources, transactions, or a balance.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteOUResponse400 | DeleteOUResponse401 | DeleteOUResponse403 | DeleteOUResponse404 | DeleteOUResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
