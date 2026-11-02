from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_funding_source_response_200 import DeleteFundingSourceResponse200
from ...models.delete_funding_source_response_400 import DeleteFundingSourceResponse400
from ...models.delete_funding_source_response_401 import DeleteFundingSourceResponse401
from ...models.delete_funding_source_response_403 import DeleteFundingSourceResponse403
from ...models.delete_funding_source_response_404 import DeleteFundingSourceResponse404
from ...models.delete_funding_source_response_500 import DeleteFundingSourceResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/funding-source/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteFundingSourceResponse200 | DeleteFundingSourceResponse400 | DeleteFundingSourceResponse401 | DeleteFundingSourceResponse403 | DeleteFundingSourceResponse404 | DeleteFundingSourceResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteFundingSourceResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteFundingSourceResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteFundingSourceResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteFundingSourceResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteFundingSourceResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteFundingSourceResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteFundingSourceResponse200 | DeleteFundingSourceResponse400 | DeleteFundingSourceResponse401 | DeleteFundingSourceResponse403 | DeleteFundingSourceResponse404 | DeleteFundingSourceResponse500]:
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

) -> Response[DeleteFundingSourceResponse200 | DeleteFundingSourceResponse400 | DeleteFundingSourceResponse401 | DeleteFundingSourceResponse403 | DeleteFundingSourceResponse404 | DeleteFundingSourceResponse500]:
    """ Deletes a funding source in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFundingSourceResponse200 | DeleteFundingSourceResponse400 | DeleteFundingSourceResponse401 | DeleteFundingSourceResponse403 | DeleteFundingSourceResponse404 | DeleteFundingSourceResponse500]
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

) -> DeleteFundingSourceResponse200 | DeleteFundingSourceResponse400 | DeleteFundingSourceResponse401 | DeleteFundingSourceResponse403 | DeleteFundingSourceResponse404 | DeleteFundingSourceResponse500 | None:
    """ Deletes a funding source in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFundingSourceResponse200 | DeleteFundingSourceResponse400 | DeleteFundingSourceResponse401 | DeleteFundingSourceResponse403 | DeleteFundingSourceResponse404 | DeleteFundingSourceResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteFundingSourceResponse200 | DeleteFundingSourceResponse400 | DeleteFundingSourceResponse401 | DeleteFundingSourceResponse403 | DeleteFundingSourceResponse404 | DeleteFundingSourceResponse500]:
    """ Deletes a funding source in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFundingSourceResponse200 | DeleteFundingSourceResponse400 | DeleteFundingSourceResponse401 | DeleteFundingSourceResponse403 | DeleteFundingSourceResponse404 | DeleteFundingSourceResponse500]
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

) -> DeleteFundingSourceResponse200 | DeleteFundingSourceResponse400 | DeleteFundingSourceResponse401 | DeleteFundingSourceResponse403 | DeleteFundingSourceResponse404 | DeleteFundingSourceResponse500 | None:
    """ Deletes a funding source in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFundingSourceResponse200 | DeleteFundingSourceResponse400 | DeleteFundingSourceResponse401 | DeleteFundingSourceResponse403 | DeleteFundingSourceResponse404 | DeleteFundingSourceResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
