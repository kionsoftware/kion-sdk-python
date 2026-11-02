from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.idms_create import IDMSCreate
from ...models.post_idms_response_201 import PostIDMSResponse201
from ...models.post_idms_response_400 import PostIDMSResponse400
from ...models.post_idms_response_401 import PostIDMSResponse401
from ...models.post_idms_response_403 import PostIDMSResponse403
from ...models.post_idms_response_422 import PostIDMSResponse422
from ...models.post_idms_response_500 import PostIDMSResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: IDMSCreate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/idms",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostIDMSResponse201 | PostIDMSResponse400 | PostIDMSResponse401 | PostIDMSResponse403 | PostIDMSResponse422 | PostIDMSResponse500 | None:
    if response.status_code == 201:
        response_201 = PostIDMSResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostIDMSResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostIDMSResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostIDMSResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostIDMSResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostIDMSResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostIDMSResponse201 | PostIDMSResponse400 | PostIDMSResponse401 | PostIDMSResponse403 | PostIDMSResponse422 | PostIDMSResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: IDMSCreate | Unset = UNSET,

) -> Response[PostIDMSResponse201 | PostIDMSResponse400 | PostIDMSResponse401 | PostIDMSResponse403 | PostIDMSResponse422 | PostIDMSResponse500]:
    """ Creates an IDMS in the application.

    Args:
        body (IDMSCreate | Unset): IDMSCreate defines an identity management system creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostIDMSResponse201 | PostIDMSResponse400 | PostIDMSResponse401 | PostIDMSResponse403 | PostIDMSResponse422 | PostIDMSResponse500]
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
    body: IDMSCreate | Unset = UNSET,

) -> PostIDMSResponse201 | PostIDMSResponse400 | PostIDMSResponse401 | PostIDMSResponse403 | PostIDMSResponse422 | PostIDMSResponse500 | None:
    """ Creates an IDMS in the application.

    Args:
        body (IDMSCreate | Unset): IDMSCreate defines an identity management system creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostIDMSResponse201 | PostIDMSResponse400 | PostIDMSResponse401 | PostIDMSResponse403 | PostIDMSResponse422 | PostIDMSResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: IDMSCreate | Unset = UNSET,

) -> Response[PostIDMSResponse201 | PostIDMSResponse400 | PostIDMSResponse401 | PostIDMSResponse403 | PostIDMSResponse422 | PostIDMSResponse500]:
    """ Creates an IDMS in the application.

    Args:
        body (IDMSCreate | Unset): IDMSCreate defines an identity management system creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostIDMSResponse201 | PostIDMSResponse400 | PostIDMSResponse401 | PostIDMSResponse403 | PostIDMSResponse422 | PostIDMSResponse500]
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
    body: IDMSCreate | Unset = UNSET,

) -> PostIDMSResponse201 | PostIDMSResponse400 | PostIDMSResponse401 | PostIDMSResponse403 | PostIDMSResponse422 | PostIDMSResponse500 | None:
    """ Creates an IDMS in the application.

    Args:
        body (IDMSCreate | Unset): IDMSCreate defines an identity management system creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostIDMSResponse201 | PostIDMSResponse400 | PostIDMSResponse401 | PostIDMSResponse403 | PostIDMSResponse422 | PostIDMSResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
