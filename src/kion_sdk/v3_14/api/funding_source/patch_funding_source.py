from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.funding_source import FundingSource
from ...models.patch_funding_source_response_200 import PatchFundingSourceResponse200
from ...models.patch_funding_source_response_400 import PatchFundingSourceResponse400
from ...models.patch_funding_source_response_401 import PatchFundingSourceResponse401
from ...models.patch_funding_source_response_403 import PatchFundingSourceResponse403
from ...models.patch_funding_source_response_404 import PatchFundingSourceResponse404
from ...models.patch_funding_source_response_422 import PatchFundingSourceResponse422
from ...models.patch_funding_source_response_500 import PatchFundingSourceResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: FundingSource,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/funding-source/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchFundingSourceResponse200 | PatchFundingSourceResponse400 | PatchFundingSourceResponse401 | PatchFundingSourceResponse403 | PatchFundingSourceResponse404 | PatchFundingSourceResponse422 | PatchFundingSourceResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchFundingSourceResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchFundingSourceResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchFundingSourceResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchFundingSourceResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchFundingSourceResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchFundingSourceResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchFundingSourceResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchFundingSourceResponse200 | PatchFundingSourceResponse400 | PatchFundingSourceResponse401 | PatchFundingSourceResponse403 | PatchFundingSourceResponse404 | PatchFundingSourceResponse422 | PatchFundingSourceResponse500]:
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
    body: FundingSource,

) -> Response[PatchFundingSourceResponse200 | PatchFundingSourceResponse400 | PatchFundingSourceResponse401 | PatchFundingSourceResponse403 | PatchFundingSourceResponse404 | PatchFundingSourceResponse422 | PatchFundingSourceResponse500]:
    """ Updates a funding source by ID in the application.

    Args:
        id (int):
        body (FundingSource): FundingSource defines a funding source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFundingSourceResponse200 | PatchFundingSourceResponse400 | PatchFundingSourceResponse401 | PatchFundingSourceResponse403 | PatchFundingSourceResponse404 | PatchFundingSourceResponse422 | PatchFundingSourceResponse500]
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
    body: FundingSource,

) -> PatchFundingSourceResponse200 | PatchFundingSourceResponse400 | PatchFundingSourceResponse401 | PatchFundingSourceResponse403 | PatchFundingSourceResponse404 | PatchFundingSourceResponse422 | PatchFundingSourceResponse500 | None:
    """ Updates a funding source by ID in the application.

    Args:
        id (int):
        body (FundingSource): FundingSource defines a funding source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFundingSourceResponse200 | PatchFundingSourceResponse400 | PatchFundingSourceResponse401 | PatchFundingSourceResponse403 | PatchFundingSourceResponse404 | PatchFundingSourceResponse422 | PatchFundingSourceResponse500
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
    body: FundingSource,

) -> Response[PatchFundingSourceResponse200 | PatchFundingSourceResponse400 | PatchFundingSourceResponse401 | PatchFundingSourceResponse403 | PatchFundingSourceResponse404 | PatchFundingSourceResponse422 | PatchFundingSourceResponse500]:
    """ Updates a funding source by ID in the application.

    Args:
        id (int):
        body (FundingSource): FundingSource defines a funding source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFundingSourceResponse200 | PatchFundingSourceResponse400 | PatchFundingSourceResponse401 | PatchFundingSourceResponse403 | PatchFundingSourceResponse404 | PatchFundingSourceResponse422 | PatchFundingSourceResponse500]
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
    body: FundingSource,

) -> PatchFundingSourceResponse200 | PatchFundingSourceResponse400 | PatchFundingSourceResponse401 | PatchFundingSourceResponse403 | PatchFundingSourceResponse404 | PatchFundingSourceResponse422 | PatchFundingSourceResponse500 | None:
    """ Updates a funding source by ID in the application.

    Args:
        id (int):
        body (FundingSource): FundingSource defines a funding source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFundingSourceResponse200 | PatchFundingSourceResponse400 | PatchFundingSourceResponse401 | PatchFundingSourceResponse403 | PatchFundingSourceResponse404 | PatchFundingSourceResponse422 | PatchFundingSourceResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
