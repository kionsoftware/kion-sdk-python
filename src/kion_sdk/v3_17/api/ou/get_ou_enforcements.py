from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_ou_enforcements_response_200 import GetOUEnforcementsResponse200
from ...models.get_ou_enforcements_response_400 import GetOUEnforcementsResponse400
from ...models.get_ou_enforcements_response_401 import GetOUEnforcementsResponse401
from ...models.get_ou_enforcements_response_403 import GetOUEnforcementsResponse403
from ...models.get_ou_enforcements_response_404 import GetOUEnforcementsResponse404
from ...models.get_ou_enforcements_response_500 import GetOUEnforcementsResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/ou/{id}/enforcement".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOUEnforcementsResponse200 | GetOUEnforcementsResponse400 | GetOUEnforcementsResponse401 | GetOUEnforcementsResponse403 | GetOUEnforcementsResponse404 | GetOUEnforcementsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetOUEnforcementsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetOUEnforcementsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetOUEnforcementsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetOUEnforcementsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetOUEnforcementsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetOUEnforcementsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOUEnforcementsResponse200 | GetOUEnforcementsResponse400 | GetOUEnforcementsResponse401 | GetOUEnforcementsResponse403 | GetOUEnforcementsResponse404 | GetOUEnforcementsResponse500]:
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

) -> Response[GetOUEnforcementsResponse200 | GetOUEnforcementsResponse400 | GetOUEnforcementsResponse401 | GetOUEnforcementsResponse403 | GetOUEnforcementsResponse404 | GetOUEnforcementsResponse500]:
    """ Retrieves all the enforcements for a given OU.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUEnforcementsResponse200 | GetOUEnforcementsResponse400 | GetOUEnforcementsResponse401 | GetOUEnforcementsResponse403 | GetOUEnforcementsResponse404 | GetOUEnforcementsResponse500]
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

) -> GetOUEnforcementsResponse200 | GetOUEnforcementsResponse400 | GetOUEnforcementsResponse401 | GetOUEnforcementsResponse403 | GetOUEnforcementsResponse404 | GetOUEnforcementsResponse500 | None:
    """ Retrieves all the enforcements for a given OU.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUEnforcementsResponse200 | GetOUEnforcementsResponse400 | GetOUEnforcementsResponse401 | GetOUEnforcementsResponse403 | GetOUEnforcementsResponse404 | GetOUEnforcementsResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetOUEnforcementsResponse200 | GetOUEnforcementsResponse400 | GetOUEnforcementsResponse401 | GetOUEnforcementsResponse403 | GetOUEnforcementsResponse404 | GetOUEnforcementsResponse500]:
    """ Retrieves all the enforcements for a given OU.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUEnforcementsResponse200 | GetOUEnforcementsResponse400 | GetOUEnforcementsResponse401 | GetOUEnforcementsResponse403 | GetOUEnforcementsResponse404 | GetOUEnforcementsResponse500]
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

) -> GetOUEnforcementsResponse200 | GetOUEnforcementsResponse400 | GetOUEnforcementsResponse401 | GetOUEnforcementsResponse403 | GetOUEnforcementsResponse404 | GetOUEnforcementsResponse500 | None:
    """ Retrieves all the enforcements for a given OU.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUEnforcementsResponse200 | GetOUEnforcementsResponse400 | GetOUEnforcementsResponse401 | GetOUEnforcementsResponse403 | GetOUEnforcementsResponse404 | GetOUEnforcementsResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
