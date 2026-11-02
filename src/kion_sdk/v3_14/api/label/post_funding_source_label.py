from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.associate_label import AssociateLabel
from ...models.post_funding_source_label_response_201 import PostFundingSourceLabelResponse201
from ...models.post_funding_source_label_response_400 import PostFundingSourceLabelResponse400
from ...models.post_funding_source_label_response_401 import PostFundingSourceLabelResponse401
from ...models.post_funding_source_label_response_404 import PostFundingSourceLabelResponse404
from ...models.post_funding_source_label_response_422 import PostFundingSourceLabelResponse422
from ...models.post_funding_source_label_response_500 import PostFundingSourceLabelResponse500
from typing import cast



def _get_kwargs(
    funding_source_id: int,
    *,
    body: AssociateLabel,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/funding-source/{funding_source_id}/labels".format(funding_source_id=quote(str(funding_source_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostFundingSourceLabelResponse201 | PostFundingSourceLabelResponse400 | PostFundingSourceLabelResponse401 | PostFundingSourceLabelResponse404 | PostFundingSourceLabelResponse422 | PostFundingSourceLabelResponse500 | None:
    if response.status_code == 201:
        response_201 = PostFundingSourceLabelResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostFundingSourceLabelResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostFundingSourceLabelResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = PostFundingSourceLabelResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PostFundingSourceLabelResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostFundingSourceLabelResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostFundingSourceLabelResponse201 | PostFundingSourceLabelResponse400 | PostFundingSourceLabelResponse401 | PostFundingSourceLabelResponse404 | PostFundingSourceLabelResponse422 | PostFundingSourceLabelResponse500]:
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
    body: AssociateLabel,

) -> Response[PostFundingSourceLabelResponse201 | PostFundingSourceLabelResponse400 | PostFundingSourceLabelResponse401 | PostFundingSourceLabelResponse404 | PostFundingSourceLabelResponse422 | PostFundingSourceLabelResponse500]:
    """ Associates a label with the given funding source.

     The label must already exist.
    You may pass just the label ID, or just the key/value pair.

    Args:
        funding_source_id (int):
        body (AssociateLabel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFundingSourceLabelResponse201 | PostFundingSourceLabelResponse400 | PostFundingSourceLabelResponse401 | PostFundingSourceLabelResponse404 | PostFundingSourceLabelResponse422 | PostFundingSourceLabelResponse500]
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
    body: AssociateLabel,

) -> PostFundingSourceLabelResponse201 | PostFundingSourceLabelResponse400 | PostFundingSourceLabelResponse401 | PostFundingSourceLabelResponse404 | PostFundingSourceLabelResponse422 | PostFundingSourceLabelResponse500 | None:
    """ Associates a label with the given funding source.

     The label must already exist.
    You may pass just the label ID, or just the key/value pair.

    Args:
        funding_source_id (int):
        body (AssociateLabel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFundingSourceLabelResponse201 | PostFundingSourceLabelResponse400 | PostFundingSourceLabelResponse401 | PostFundingSourceLabelResponse404 | PostFundingSourceLabelResponse422 | PostFundingSourceLabelResponse500
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
    body: AssociateLabel,

) -> Response[PostFundingSourceLabelResponse201 | PostFundingSourceLabelResponse400 | PostFundingSourceLabelResponse401 | PostFundingSourceLabelResponse404 | PostFundingSourceLabelResponse422 | PostFundingSourceLabelResponse500]:
    """ Associates a label with the given funding source.

     The label must already exist.
    You may pass just the label ID, or just the key/value pair.

    Args:
        funding_source_id (int):
        body (AssociateLabel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFundingSourceLabelResponse201 | PostFundingSourceLabelResponse400 | PostFundingSourceLabelResponse401 | PostFundingSourceLabelResponse404 | PostFundingSourceLabelResponse422 | PostFundingSourceLabelResponse500]
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
    body: AssociateLabel,

) -> PostFundingSourceLabelResponse201 | PostFundingSourceLabelResponse400 | PostFundingSourceLabelResponse401 | PostFundingSourceLabelResponse404 | PostFundingSourceLabelResponse422 | PostFundingSourceLabelResponse500 | None:
    """ Associates a label with the given funding source.

     The label must already exist.
    You may pass just the label ID, or just the key/value pair.

    Args:
        funding_source_id (int):
        body (AssociateLabel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFundingSourceLabelResponse201 | PostFundingSourceLabelResponse400 | PostFundingSourceLabelResponse401 | PostFundingSourceLabelResponse404 | PostFundingSourceLabelResponse422 | PostFundingSourceLabelResponse500
     """


    return (await asyncio_detailed(
        funding_source_id=funding_source_id,
client=client,
body=body,

    )).parsed
