from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.associate_labels import AssociateLabels
from ...models.put_funding_source_labels_response_200 import PutFundingSourceLabelsResponse200
from ...models.put_funding_source_labels_response_400 import PutFundingSourceLabelsResponse400
from ...models.put_funding_source_labels_response_401 import PutFundingSourceLabelsResponse401
from ...models.put_funding_source_labels_response_404 import PutFundingSourceLabelsResponse404
from ...models.put_funding_source_labels_response_422 import PutFundingSourceLabelsResponse422
from ...models.put_funding_source_labels_response_500 import PutFundingSourceLabelsResponse500
from typing import cast



def _get_kwargs(
    funding_source_id: int,
    *,
    body: AssociateLabels,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/funding-source/{funding_source_id}/labels".format(funding_source_id=quote(str(funding_source_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutFundingSourceLabelsResponse200 | PutFundingSourceLabelsResponse400 | PutFundingSourceLabelsResponse401 | PutFundingSourceLabelsResponse404 | PutFundingSourceLabelsResponse422 | PutFundingSourceLabelsResponse500 | None:
    if response.status_code == 200:
        response_200 = PutFundingSourceLabelsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PutFundingSourceLabelsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PutFundingSourceLabelsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = PutFundingSourceLabelsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PutFundingSourceLabelsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PutFundingSourceLabelsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutFundingSourceLabelsResponse200 | PutFundingSourceLabelsResponse400 | PutFundingSourceLabelsResponse401 | PutFundingSourceLabelsResponse404 | PutFundingSourceLabelsResponse422 | PutFundingSourceLabelsResponse500]:
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
    body: AssociateLabels,

) -> Response[PutFundingSourceLabelsResponse200 | PutFundingSourceLabelsResponse400 | PutFundingSourceLabelsResponse401 | PutFundingSourceLabelsResponse404 | PutFundingSourceLabelsResponse422 | PutFundingSourceLabelsResponse500]:
    """ Replaces labels on the given funding source.

     This replaces labels on the given funding source with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        funding_source_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutFundingSourceLabelsResponse200 | PutFundingSourceLabelsResponse400 | PutFundingSourceLabelsResponse401 | PutFundingSourceLabelsResponse404 | PutFundingSourceLabelsResponse422 | PutFundingSourceLabelsResponse500]
     """


    kwargs = _get_kwargs(
        funding_source_id=funding_source_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    funding_source_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> PutFundingSourceLabelsResponse200 | PutFundingSourceLabelsResponse400 | PutFundingSourceLabelsResponse401 | PutFundingSourceLabelsResponse404 | PutFundingSourceLabelsResponse422 | PutFundingSourceLabelsResponse500 | None:
    """ Replaces labels on the given funding source.

     This replaces labels on the given funding source with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        funding_source_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutFundingSourceLabelsResponse200 | PutFundingSourceLabelsResponse400 | PutFundingSourceLabelsResponse401 | PutFundingSourceLabelsResponse404 | PutFundingSourceLabelsResponse422 | PutFundingSourceLabelsResponse500
     """


    return sync_detailed(
        funding_source_id=funding_source_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    funding_source_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> Response[PutFundingSourceLabelsResponse200 | PutFundingSourceLabelsResponse400 | PutFundingSourceLabelsResponse401 | PutFundingSourceLabelsResponse404 | PutFundingSourceLabelsResponse422 | PutFundingSourceLabelsResponse500]:
    """ Replaces labels on the given funding source.

     This replaces labels on the given funding source with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        funding_source_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutFundingSourceLabelsResponse200 | PutFundingSourceLabelsResponse400 | PutFundingSourceLabelsResponse401 | PutFundingSourceLabelsResponse404 | PutFundingSourceLabelsResponse422 | PutFundingSourceLabelsResponse500]
     """


    kwargs = _get_kwargs(
        funding_source_id=funding_source_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    funding_source_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> PutFundingSourceLabelsResponse200 | PutFundingSourceLabelsResponse400 | PutFundingSourceLabelsResponse401 | PutFundingSourceLabelsResponse404 | PutFundingSourceLabelsResponse422 | PutFundingSourceLabelsResponse500 | None:
    """ Replaces labels on the given funding source.

     This replaces labels on the given funding source with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        funding_source_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutFundingSourceLabelsResponse200 | PutFundingSourceLabelsResponse400 | PutFundingSourceLabelsResponse401 | PutFundingSourceLabelsResponse404 | PutFundingSourceLabelsResponse422 | PutFundingSourceLabelsResponse500
     """


    return (await asyncio_detailed(
        funding_source_id=funding_source_id,
client=client,
body=body,

    )).parsed
