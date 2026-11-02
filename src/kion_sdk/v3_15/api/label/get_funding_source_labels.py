from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_funding_source_labels_response_200 import GetFundingSourceLabelsResponse200
from ...models.get_funding_source_labels_response_400 import GetFundingSourceLabelsResponse400
from ...models.get_funding_source_labels_response_401 import GetFundingSourceLabelsResponse401
from ...models.get_funding_source_labels_response_403 import GetFundingSourceLabelsResponse403
from ...models.get_funding_source_labels_response_500 import GetFundingSourceLabelsResponse500
from typing import cast



def _get_kwargs(
    funding_source_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/funding-source/{funding_source_id}/labels".format(funding_source_id=quote(str(funding_source_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetFundingSourceLabelsResponse200 | GetFundingSourceLabelsResponse400 | GetFundingSourceLabelsResponse401 | GetFundingSourceLabelsResponse403 | GetFundingSourceLabelsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetFundingSourceLabelsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetFundingSourceLabelsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetFundingSourceLabelsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetFundingSourceLabelsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetFundingSourceLabelsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetFundingSourceLabelsResponse200 | GetFundingSourceLabelsResponse400 | GetFundingSourceLabelsResponse401 | GetFundingSourceLabelsResponse403 | GetFundingSourceLabelsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    funding_source_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetFundingSourceLabelsResponse200 | GetFundingSourceLabelsResponse400 | GetFundingSourceLabelsResponse401 | GetFundingSourceLabelsResponse403 | GetFundingSourceLabelsResponse500]:
    """ Gets all labels associated with a given funding source ID.

    Args:
        funding_source_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFundingSourceLabelsResponse200 | GetFundingSourceLabelsResponse400 | GetFundingSourceLabelsResponse401 | GetFundingSourceLabelsResponse403 | GetFundingSourceLabelsResponse500]
     """


    kwargs = _get_kwargs(
        funding_source_id=funding_source_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    funding_source_id: int,
    *,
    client: AuthenticatedClient,

) -> GetFundingSourceLabelsResponse200 | GetFundingSourceLabelsResponse400 | GetFundingSourceLabelsResponse401 | GetFundingSourceLabelsResponse403 | GetFundingSourceLabelsResponse500 | None:
    """ Gets all labels associated with a given funding source ID.

    Args:
        funding_source_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFundingSourceLabelsResponse200 | GetFundingSourceLabelsResponse400 | GetFundingSourceLabelsResponse401 | GetFundingSourceLabelsResponse403 | GetFundingSourceLabelsResponse500
     """


    return sync_detailed(
        funding_source_id=funding_source_id,
client=client,

    ).parsed

async def asyncio_detailed(
    funding_source_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetFundingSourceLabelsResponse200 | GetFundingSourceLabelsResponse400 | GetFundingSourceLabelsResponse401 | GetFundingSourceLabelsResponse403 | GetFundingSourceLabelsResponse500]:
    """ Gets all labels associated with a given funding source ID.

    Args:
        funding_source_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFundingSourceLabelsResponse200 | GetFundingSourceLabelsResponse400 | GetFundingSourceLabelsResponse401 | GetFundingSourceLabelsResponse403 | GetFundingSourceLabelsResponse500]
     """


    kwargs = _get_kwargs(
        funding_source_id=funding_source_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    funding_source_id: int,
    *,
    client: AuthenticatedClient,

) -> GetFundingSourceLabelsResponse200 | GetFundingSourceLabelsResponse400 | GetFundingSourceLabelsResponse401 | GetFundingSourceLabelsResponse403 | GetFundingSourceLabelsResponse500 | None:
    """ Gets all labels associated with a given funding source ID.

    Args:
        funding_source_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFundingSourceLabelsResponse200 | GetFundingSourceLabelsResponse400 | GetFundingSourceLabelsResponse401 | GetFundingSourceLabelsResponse403 | GetFundingSourceLabelsResponse500
     """


    return (await asyncio_detailed(
        funding_source_id=funding_source_id,
client=client,

    )).parsed
