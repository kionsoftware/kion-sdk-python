from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_label import CreateLabel
from ...models.post_label_response_201 import PostLabelResponse201
from ...models.post_label_response_400 import PostLabelResponse400
from ...models.post_label_response_401 import PostLabelResponse401
from ...models.post_label_response_403 import PostLabelResponse403
from ...models.post_label_response_422 import PostLabelResponse422
from ...models.post_label_response_500 import PostLabelResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CreateLabel | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/label",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostLabelResponse201 | PostLabelResponse400 | PostLabelResponse401 | PostLabelResponse403 | PostLabelResponse422 | PostLabelResponse500 | None:
    if response.status_code == 201:
        response_201 = PostLabelResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostLabelResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostLabelResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostLabelResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostLabelResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostLabelResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostLabelResponse201 | PostLabelResponse400 | PostLabelResponse401 | PostLabelResponse403 | PostLabelResponse422 | PostLabelResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateLabel | Unset = UNSET,

) -> Response[PostLabelResponse201 | PostLabelResponse400 | PostLabelResponse401 | PostLabelResponse403 | PostLabelResponse422 | PostLabelResponse500]:
    """ Creates a new app label in the application.

    Args:
        body (CreateLabel | Unset): CreateLabel defines a new label

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLabelResponse201 | PostLabelResponse400 | PostLabelResponse401 | PostLabelResponse403 | PostLabelResponse422 | PostLabelResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: CreateLabel | Unset = UNSET,

) -> PostLabelResponse201 | PostLabelResponse400 | PostLabelResponse401 | PostLabelResponse403 | PostLabelResponse422 | PostLabelResponse500 | None:
    """ Creates a new app label in the application.

    Args:
        body (CreateLabel | Unset): CreateLabel defines a new label

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLabelResponse201 | PostLabelResponse400 | PostLabelResponse401 | PostLabelResponse403 | PostLabelResponse422 | PostLabelResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateLabel | Unset = UNSET,

) -> Response[PostLabelResponse201 | PostLabelResponse400 | PostLabelResponse401 | PostLabelResponse403 | PostLabelResponse422 | PostLabelResponse500]:
    """ Creates a new app label in the application.

    Args:
        body (CreateLabel | Unset): CreateLabel defines a new label

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLabelResponse201 | PostLabelResponse400 | PostLabelResponse401 | PostLabelResponse403 | PostLabelResponse422 | PostLabelResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateLabel | Unset = UNSET,

) -> PostLabelResponse201 | PostLabelResponse400 | PostLabelResponse401 | PostLabelResponse403 | PostLabelResponse422 | PostLabelResponse500 | None:
    """ Creates a new app label in the application.

    Args:
        body (CreateLabel | Unset): CreateLabel defines a new label

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLabelResponse201 | PostLabelResponse400 | PostLabelResponse401 | PostLabelResponse403 | PostLabelResponse422 | PostLabelResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
