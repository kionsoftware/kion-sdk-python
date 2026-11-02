from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_ou_funding_sources_response_200 import GetOUFundingSourcesResponse200
from ...models.get_ou_funding_sources_response_400 import GetOUFundingSourcesResponse400
from ...models.get_ou_funding_sources_response_401 import GetOUFundingSourcesResponse401
from ...models.get_ou_funding_sources_response_403 import GetOUFundingSourcesResponse403
from ...models.get_ou_funding_sources_response_404 import GetOUFundingSourcesResponse404
from ...models.get_ou_funding_sources_response_500 import GetOUFundingSourcesResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/ou/{id}/funding-source".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOUFundingSourcesResponse200 | GetOUFundingSourcesResponse400 | GetOUFundingSourcesResponse401 | GetOUFundingSourcesResponse403 | GetOUFundingSourcesResponse404 | GetOUFundingSourcesResponse500 | None:
    if response.status_code == 200:
        response_200 = GetOUFundingSourcesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetOUFundingSourcesResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetOUFundingSourcesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetOUFundingSourcesResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetOUFundingSourcesResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetOUFundingSourcesResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOUFundingSourcesResponse200 | GetOUFundingSourcesResponse400 | GetOUFundingSourcesResponse401 | GetOUFundingSourcesResponse403 | GetOUFundingSourcesResponse404 | GetOUFundingSourcesResponse500]:
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

) -> Response[GetOUFundingSourcesResponse200 | GetOUFundingSourcesResponse400 | GetOUFundingSourcesResponse401 | GetOUFundingSourcesResponse403 | GetOUFundingSourcesResponse404 | GetOUFundingSourcesResponse500]:
    """ Finds the funding sources in an OU.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUFundingSourcesResponse200 | GetOUFundingSourcesResponse400 | GetOUFundingSourcesResponse401 | GetOUFundingSourcesResponse403 | GetOUFundingSourcesResponse404 | GetOUFundingSourcesResponse500]
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

) -> GetOUFundingSourcesResponse200 | GetOUFundingSourcesResponse400 | GetOUFundingSourcesResponse401 | GetOUFundingSourcesResponse403 | GetOUFundingSourcesResponse404 | GetOUFundingSourcesResponse500 | None:
    """ Finds the funding sources in an OU.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUFundingSourcesResponse200 | GetOUFundingSourcesResponse400 | GetOUFundingSourcesResponse401 | GetOUFundingSourcesResponse403 | GetOUFundingSourcesResponse404 | GetOUFundingSourcesResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetOUFundingSourcesResponse200 | GetOUFundingSourcesResponse400 | GetOUFundingSourcesResponse401 | GetOUFundingSourcesResponse403 | GetOUFundingSourcesResponse404 | GetOUFundingSourcesResponse500]:
    """ Finds the funding sources in an OU.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUFundingSourcesResponse200 | GetOUFundingSourcesResponse400 | GetOUFundingSourcesResponse401 | GetOUFundingSourcesResponse403 | GetOUFundingSourcesResponse404 | GetOUFundingSourcesResponse500]
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

) -> GetOUFundingSourcesResponse200 | GetOUFundingSourcesResponse400 | GetOUFundingSourcesResponse401 | GetOUFundingSourcesResponse403 | GetOUFundingSourcesResponse404 | GetOUFundingSourcesResponse500 | None:
    """ Finds the funding sources in an OU.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUFundingSourcesResponse200 | GetOUFundingSourcesResponse400 | GetOUFundingSourcesResponse401 | GetOUFundingSourcesResponse403 | GetOUFundingSourcesResponse404 | GetOUFundingSourcesResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
