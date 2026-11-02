from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.associate_labels import AssociateLabels
from ...models.put_ou_labels_response_200 import PutOULabelsResponse200
from ...models.put_ou_labels_response_400 import PutOULabelsResponse400
from ...models.put_ou_labels_response_401 import PutOULabelsResponse401
from ...models.put_ou_labels_response_404 import PutOULabelsResponse404
from ...models.put_ou_labels_response_422 import PutOULabelsResponse422
from ...models.put_ou_labels_response_500 import PutOULabelsResponse500
from typing import cast



def _get_kwargs(
    ou_id: int,
    *,
    body: AssociateLabels,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/ou/{ou_id}/labels".format(ou_id=quote(str(ou_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutOULabelsResponse200 | PutOULabelsResponse400 | PutOULabelsResponse401 | PutOULabelsResponse404 | PutOULabelsResponse422 | PutOULabelsResponse500 | None:
    if response.status_code == 200:
        response_200 = PutOULabelsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PutOULabelsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PutOULabelsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = PutOULabelsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PutOULabelsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PutOULabelsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutOULabelsResponse200 | PutOULabelsResponse400 | PutOULabelsResponse401 | PutOULabelsResponse404 | PutOULabelsResponse422 | PutOULabelsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ou_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> Response[PutOULabelsResponse200 | PutOULabelsResponse400 | PutOULabelsResponse401 | PutOULabelsResponse404 | PutOULabelsResponse422 | PutOULabelsResponse500]:
    """ Replaces labels on the given OU.

     This replaces labels on the given OU with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        ou_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutOULabelsResponse200 | PutOULabelsResponse400 | PutOULabelsResponse401 | PutOULabelsResponse404 | PutOULabelsResponse422 | PutOULabelsResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    ou_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> PutOULabelsResponse200 | PutOULabelsResponse400 | PutOULabelsResponse401 | PutOULabelsResponse404 | PutOULabelsResponse422 | PutOULabelsResponse500 | None:
    """ Replaces labels on the given OU.

     This replaces labels on the given OU with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        ou_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutOULabelsResponse200 | PutOULabelsResponse400 | PutOULabelsResponse401 | PutOULabelsResponse404 | PutOULabelsResponse422 | PutOULabelsResponse500
     """


    return sync_detailed(
        ou_id=ou_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    ou_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> Response[PutOULabelsResponse200 | PutOULabelsResponse400 | PutOULabelsResponse401 | PutOULabelsResponse404 | PutOULabelsResponse422 | PutOULabelsResponse500]:
    """ Replaces labels on the given OU.

     This replaces labels on the given OU with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        ou_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutOULabelsResponse200 | PutOULabelsResponse400 | PutOULabelsResponse401 | PutOULabelsResponse404 | PutOULabelsResponse422 | PutOULabelsResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    ou_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> PutOULabelsResponse200 | PutOULabelsResponse400 | PutOULabelsResponse401 | PutOULabelsResponse404 | PutOULabelsResponse422 | PutOULabelsResponse500 | None:
    """ Replaces labels on the given OU.

     This replaces labels on the given OU with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        ou_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutOULabelsResponse200 | PutOULabelsResponse400 | PutOULabelsResponse401 | PutOULabelsResponse404 | PutOULabelsResponse422 | PutOULabelsResponse500
     """


    return (await asyncio_detailed(
        ou_id=ou_id,
client=client,
body=body,

    )).parsed
