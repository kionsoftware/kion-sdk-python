from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_funding_source_enforcements_response_200 import GetFundingSourceEnforcementsResponse200
from ...models.get_funding_source_enforcements_response_400 import GetFundingSourceEnforcementsResponse400
from ...models.get_funding_source_enforcements_response_401 import GetFundingSourceEnforcementsResponse401
from ...models.get_funding_source_enforcements_response_403 import GetFundingSourceEnforcementsResponse403
from ...models.get_funding_source_enforcements_response_404 import GetFundingSourceEnforcementsResponse404
from ...models.get_funding_source_enforcements_response_500 import GetFundingSourceEnforcementsResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/funding-source/{id}/enforcement".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetFundingSourceEnforcementsResponse200 | GetFundingSourceEnforcementsResponse400 | GetFundingSourceEnforcementsResponse401 | GetFundingSourceEnforcementsResponse403 | GetFundingSourceEnforcementsResponse404 | GetFundingSourceEnforcementsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetFundingSourceEnforcementsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetFundingSourceEnforcementsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetFundingSourceEnforcementsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetFundingSourceEnforcementsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetFundingSourceEnforcementsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetFundingSourceEnforcementsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetFundingSourceEnforcementsResponse200 | GetFundingSourceEnforcementsResponse400 | GetFundingSourceEnforcementsResponse401 | GetFundingSourceEnforcementsResponse403 | GetFundingSourceEnforcementsResponse404 | GetFundingSourceEnforcementsResponse500]:
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

) -> Response[GetFundingSourceEnforcementsResponse200 | GetFundingSourceEnforcementsResponse400 | GetFundingSourceEnforcementsResponse401 | GetFundingSourceEnforcementsResponse403 | GetFundingSourceEnforcementsResponse404 | GetFundingSourceEnforcementsResponse500]:
    """ Returns a list of enforcments that are on a funding source.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFundingSourceEnforcementsResponse200 | GetFundingSourceEnforcementsResponse400 | GetFundingSourceEnforcementsResponse401 | GetFundingSourceEnforcementsResponse403 | GetFundingSourceEnforcementsResponse404 | GetFundingSourceEnforcementsResponse500]
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

) -> GetFundingSourceEnforcementsResponse200 | GetFundingSourceEnforcementsResponse400 | GetFundingSourceEnforcementsResponse401 | GetFundingSourceEnforcementsResponse403 | GetFundingSourceEnforcementsResponse404 | GetFundingSourceEnforcementsResponse500 | None:
    """ Returns a list of enforcments that are on a funding source.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFundingSourceEnforcementsResponse200 | GetFundingSourceEnforcementsResponse400 | GetFundingSourceEnforcementsResponse401 | GetFundingSourceEnforcementsResponse403 | GetFundingSourceEnforcementsResponse404 | GetFundingSourceEnforcementsResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetFundingSourceEnforcementsResponse200 | GetFundingSourceEnforcementsResponse400 | GetFundingSourceEnforcementsResponse401 | GetFundingSourceEnforcementsResponse403 | GetFundingSourceEnforcementsResponse404 | GetFundingSourceEnforcementsResponse500]:
    """ Returns a list of enforcments that are on a funding source.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFundingSourceEnforcementsResponse200 | GetFundingSourceEnforcementsResponse400 | GetFundingSourceEnforcementsResponse401 | GetFundingSourceEnforcementsResponse403 | GetFundingSourceEnforcementsResponse404 | GetFundingSourceEnforcementsResponse500]
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

) -> GetFundingSourceEnforcementsResponse200 | GetFundingSourceEnforcementsResponse400 | GetFundingSourceEnforcementsResponse401 | GetFundingSourceEnforcementsResponse403 | GetFundingSourceEnforcementsResponse404 | GetFundingSourceEnforcementsResponse500 | None:
    """ Returns a list of enforcments that are on a funding source.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFundingSourceEnforcementsResponse200 | GetFundingSourceEnforcementsResponse400 | GetFundingSourceEnforcementsResponse401 | GetFundingSourceEnforcementsResponse403 | GetFundingSourceEnforcementsResponse404 | GetFundingSourceEnforcementsResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
