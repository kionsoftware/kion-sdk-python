from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_funding_source_label_response_200 import DeleteFundingSourceLabelResponse200
from ...models.delete_funding_source_label_response_400 import DeleteFundingSourceLabelResponse400
from ...models.delete_funding_source_label_response_401 import DeleteFundingSourceLabelResponse401
from ...models.delete_funding_source_label_response_404 import DeleteFundingSourceLabelResponse404
from ...models.delete_funding_source_label_response_422 import DeleteFundingSourceLabelResponse422
from ...models.delete_funding_source_label_response_500 import DeleteFundingSourceLabelResponse500
from typing import cast



def _get_kwargs(
    funding_source_id: int,
    label_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/funding-source/{funding_source_id}/labels/{label_id}".format(funding_source_id=quote(str(funding_source_id), safe=""),label_id=quote(str(label_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteFundingSourceLabelResponse200 | DeleteFundingSourceLabelResponse400 | DeleteFundingSourceLabelResponse401 | DeleteFundingSourceLabelResponse404 | DeleteFundingSourceLabelResponse422 | DeleteFundingSourceLabelResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteFundingSourceLabelResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteFundingSourceLabelResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteFundingSourceLabelResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = DeleteFundingSourceLabelResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteFundingSourceLabelResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteFundingSourceLabelResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteFundingSourceLabelResponse200 | DeleteFundingSourceLabelResponse400 | DeleteFundingSourceLabelResponse401 | DeleteFundingSourceLabelResponse404 | DeleteFundingSourceLabelResponse422 | DeleteFundingSourceLabelResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    funding_source_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteFundingSourceLabelResponse200 | DeleteFundingSourceLabelResponse400 | DeleteFundingSourceLabelResponse401 | DeleteFundingSourceLabelResponse404 | DeleteFundingSourceLabelResponse422 | DeleteFundingSourceLabelResponse500]:
    """ Removes a label from the given funding source by label ID.

    Args:
        funding_source_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFundingSourceLabelResponse200 | DeleteFundingSourceLabelResponse400 | DeleteFundingSourceLabelResponse401 | DeleteFundingSourceLabelResponse404 | DeleteFundingSourceLabelResponse422 | DeleteFundingSourceLabelResponse500]
     """


    kwargs = _get_kwargs(
        funding_source_id=funding_source_id,
label_id=label_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    funding_source_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteFundingSourceLabelResponse200 | DeleteFundingSourceLabelResponse400 | DeleteFundingSourceLabelResponse401 | DeleteFundingSourceLabelResponse404 | DeleteFundingSourceLabelResponse422 | DeleteFundingSourceLabelResponse500 | None:
    """ Removes a label from the given funding source by label ID.

    Args:
        funding_source_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFundingSourceLabelResponse200 | DeleteFundingSourceLabelResponse400 | DeleteFundingSourceLabelResponse401 | DeleteFundingSourceLabelResponse404 | DeleteFundingSourceLabelResponse422 | DeleteFundingSourceLabelResponse500
     """


    return sync_detailed(
        funding_source_id=funding_source_id,
label_id=label_id,
client=client,

    ).parsed

async def asyncio_detailed(
    funding_source_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteFundingSourceLabelResponse200 | DeleteFundingSourceLabelResponse400 | DeleteFundingSourceLabelResponse401 | DeleteFundingSourceLabelResponse404 | DeleteFundingSourceLabelResponse422 | DeleteFundingSourceLabelResponse500]:
    """ Removes a label from the given funding source by label ID.

    Args:
        funding_source_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFundingSourceLabelResponse200 | DeleteFundingSourceLabelResponse400 | DeleteFundingSourceLabelResponse401 | DeleteFundingSourceLabelResponse404 | DeleteFundingSourceLabelResponse422 | DeleteFundingSourceLabelResponse500]
     """


    kwargs = _get_kwargs(
        funding_source_id=funding_source_id,
label_id=label_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    funding_source_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteFundingSourceLabelResponse200 | DeleteFundingSourceLabelResponse400 | DeleteFundingSourceLabelResponse401 | DeleteFundingSourceLabelResponse404 | DeleteFundingSourceLabelResponse422 | DeleteFundingSourceLabelResponse500 | None:
    """ Removes a label from the given funding source by label ID.

    Args:
        funding_source_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFundingSourceLabelResponse200 | DeleteFundingSourceLabelResponse400 | DeleteFundingSourceLabelResponse401 | DeleteFundingSourceLabelResponse404 | DeleteFundingSourceLabelResponse422 | DeleteFundingSourceLabelResponse500
     """


    return (await asyncio_detailed(
        funding_source_id=funding_source_id,
label_id=label_id,
client=client,

    )).parsed
