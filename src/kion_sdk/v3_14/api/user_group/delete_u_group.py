from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_u_group_response_200 import DeleteUGroupResponse200
from ...models.delete_u_group_response_400 import DeleteUGroupResponse400
from ...models.delete_u_group_response_401 import DeleteUGroupResponse401
from ...models.delete_u_group_response_403 import DeleteUGroupResponse403
from ...models.delete_u_group_response_404 import DeleteUGroupResponse404
from ...models.delete_u_group_response_500 import DeleteUGroupResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/user-group/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteUGroupResponse200 | DeleteUGroupResponse400 | DeleteUGroupResponse401 | DeleteUGroupResponse403 | DeleteUGroupResponse404 | DeleteUGroupResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteUGroupResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteUGroupResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteUGroupResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteUGroupResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteUGroupResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteUGroupResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteUGroupResponse200 | DeleteUGroupResponse400 | DeleteUGroupResponse401 | DeleteUGroupResponse403 | DeleteUGroupResponse404 | DeleteUGroupResponse500]:
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

) -> Response[DeleteUGroupResponse200 | DeleteUGroupResponse400 | DeleteUGroupResponse401 | DeleteUGroupResponse403 | DeleteUGroupResponse404 | DeleteUGroupResponse500]:
    """ Deletes a user group by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUGroupResponse200 | DeleteUGroupResponse400 | DeleteUGroupResponse401 | DeleteUGroupResponse403 | DeleteUGroupResponse404 | DeleteUGroupResponse500]
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

) -> DeleteUGroupResponse200 | DeleteUGroupResponse400 | DeleteUGroupResponse401 | DeleteUGroupResponse403 | DeleteUGroupResponse404 | DeleteUGroupResponse500 | None:
    """ Deletes a user group by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUGroupResponse200 | DeleteUGroupResponse400 | DeleteUGroupResponse401 | DeleteUGroupResponse403 | DeleteUGroupResponse404 | DeleteUGroupResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteUGroupResponse200 | DeleteUGroupResponse400 | DeleteUGroupResponse401 | DeleteUGroupResponse403 | DeleteUGroupResponse404 | DeleteUGroupResponse500]:
    """ Deletes a user group by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUGroupResponse200 | DeleteUGroupResponse400 | DeleteUGroupResponse401 | DeleteUGroupResponse403 | DeleteUGroupResponse404 | DeleteUGroupResponse500]
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

) -> DeleteUGroupResponse200 | DeleteUGroupResponse400 | DeleteUGroupResponse401 | DeleteUGroupResponse403 | DeleteUGroupResponse404 | DeleteUGroupResponse500 | None:
    """ Deletes a user group by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUGroupResponse200 | DeleteUGroupResponse400 | DeleteUGroupResponse401 | DeleteUGroupResponse403 | DeleteUGroupResponse404 | DeleteUGroupResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
