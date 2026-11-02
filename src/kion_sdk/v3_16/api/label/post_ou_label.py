from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.associate_label import AssociateLabel
from ...models.post_ou_label_response_201 import PostOULabelResponse201
from ...models.post_ou_label_response_400 import PostOULabelResponse400
from ...models.post_ou_label_response_401 import PostOULabelResponse401
from ...models.post_ou_label_response_404 import PostOULabelResponse404
from ...models.post_ou_label_response_422 import PostOULabelResponse422
from ...models.post_ou_label_response_500 import PostOULabelResponse500
from typing import cast



def _get_kwargs(
    ou_id: int,
    *,
    body: AssociateLabel,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/ou/{ou_id}/labels".format(ou_id=quote(str(ou_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostOULabelResponse201 | PostOULabelResponse400 | PostOULabelResponse401 | PostOULabelResponse404 | PostOULabelResponse422 | PostOULabelResponse500 | None:
    if response.status_code == 201:
        response_201 = PostOULabelResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostOULabelResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostOULabelResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = PostOULabelResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PostOULabelResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostOULabelResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostOULabelResponse201 | PostOULabelResponse400 | PostOULabelResponse401 | PostOULabelResponse404 | PostOULabelResponse422 | PostOULabelResponse500]:
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
    body: AssociateLabel,

) -> Response[PostOULabelResponse201 | PostOULabelResponse400 | PostOULabelResponse401 | PostOULabelResponse404 | PostOULabelResponse422 | PostOULabelResponse500]:
    """ Associates a label with the given OU.

     The label must already exist.
    You may pass just the label ID, or just the key/value pair.

    Args:
        ou_id (int):
        body (AssociateLabel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOULabelResponse201 | PostOULabelResponse400 | PostOULabelResponse401 | PostOULabelResponse404 | PostOULabelResponse422 | PostOULabelResponse500]
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
    body: AssociateLabel,

) -> PostOULabelResponse201 | PostOULabelResponse400 | PostOULabelResponse401 | PostOULabelResponse404 | PostOULabelResponse422 | PostOULabelResponse500 | None:
    """ Associates a label with the given OU.

     The label must already exist.
    You may pass just the label ID, or just the key/value pair.

    Args:
        ou_id (int):
        body (AssociateLabel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOULabelResponse201 | PostOULabelResponse400 | PostOULabelResponse401 | PostOULabelResponse404 | PostOULabelResponse422 | PostOULabelResponse500
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
    body: AssociateLabel,

) -> Response[PostOULabelResponse201 | PostOULabelResponse400 | PostOULabelResponse401 | PostOULabelResponse404 | PostOULabelResponse422 | PostOULabelResponse500]:
    """ Associates a label with the given OU.

     The label must already exist.
    You may pass just the label ID, or just the key/value pair.

    Args:
        ou_id (int):
        body (AssociateLabel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOULabelResponse201 | PostOULabelResponse400 | PostOULabelResponse401 | PostOULabelResponse404 | PostOULabelResponse422 | PostOULabelResponse500]
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
    body: AssociateLabel,

) -> PostOULabelResponse201 | PostOULabelResponse400 | PostOULabelResponse401 | PostOULabelResponse404 | PostOULabelResponse422 | PostOULabelResponse500 | None:
    """ Associates a label with the given OU.

     The label must already exist.
    You may pass just the label ID, or just the key/value pair.

    Args:
        ou_id (int):
        body (AssociateLabel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOULabelResponse201 | PostOULabelResponse400 | PostOULabelResponse401 | PostOULabelResponse404 | PostOULabelResponse422 | PostOULabelResponse500
     """


    return (await asyncio_detailed(
        ou_id=ou_id,
client=client,
body=body,

    )).parsed
