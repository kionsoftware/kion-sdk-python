from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ou_create import OUCreate
from ...models.post_ou_response_201 import PostOUResponse201
from ...models.post_ou_response_400 import PostOUResponse400
from ...models.post_ou_response_401 import PostOUResponse401
from ...models.post_ou_response_403 import PostOUResponse403
from ...models.post_ou_response_422 import PostOUResponse422
from ...models.post_ou_response_500 import PostOUResponse500
from typing import cast



def _get_kwargs(
    *,
    body: OUCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/ou",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostOUResponse201 | PostOUResponse400 | PostOUResponse401 | PostOUResponse403 | PostOUResponse422 | PostOUResponse500 | None:
    if response.status_code == 201:
        response_201 = PostOUResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostOUResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostOUResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostOUResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostOUResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostOUResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostOUResponse201 | PostOUResponse400 | PostOUResponse401 | PostOUResponse403 | PostOUResponse422 | PostOUResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OUCreate,

) -> Response[PostOUResponse201 | PostOUResponse400 | PostOUResponse401 | PostOUResponse403 | PostOUResponse422 | PostOUResponse500]:
    """ Creates an OU in the application.

    Args:
        body (OUCreate): OUCreate defines an OU creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOUResponse201 | PostOUResponse400 | PostOUResponse401 | PostOUResponse403 | PostOUResponse422 | PostOUResponse500]
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
    body: OUCreate,

) -> PostOUResponse201 | PostOUResponse400 | PostOUResponse401 | PostOUResponse403 | PostOUResponse422 | PostOUResponse500 | None:
    """ Creates an OU in the application.

    Args:
        body (OUCreate): OUCreate defines an OU creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOUResponse201 | PostOUResponse400 | PostOUResponse401 | PostOUResponse403 | PostOUResponse422 | PostOUResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OUCreate,

) -> Response[PostOUResponse201 | PostOUResponse400 | PostOUResponse401 | PostOUResponse403 | PostOUResponse422 | PostOUResponse500]:
    """ Creates an OU in the application.

    Args:
        body (OUCreate): OUCreate defines an OU creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOUResponse201 | PostOUResponse400 | PostOUResponse401 | PostOUResponse403 | PostOUResponse422 | PostOUResponse500]
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
    body: OUCreate,

) -> PostOUResponse201 | PostOUResponse400 | PostOUResponse401 | PostOUResponse403 | PostOUResponse422 | PostOUResponse500 | None:
    """ Creates an OU in the application.

    Args:
        body (OUCreate): OUCreate defines an OU creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOUResponse201 | PostOUResponse400 | PostOUResponse401 | PostOUResponse403 | PostOUResponse422 | PostOUResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
