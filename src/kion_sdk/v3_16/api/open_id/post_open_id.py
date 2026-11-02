from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.open_id_create import OpenIDCreate
from ...models.post_open_id_response_201 import PostOpenIDResponse201
from ...models.post_open_id_response_400 import PostOpenIDResponse400
from ...models.post_open_id_response_401 import PostOpenIDResponse401
from ...models.post_open_id_response_403 import PostOpenIDResponse403
from ...models.post_open_id_response_422 import PostOpenIDResponse422
from ...models.post_open_id_response_500 import PostOpenIDResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: OpenIDCreate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v4/idms/open-id",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostOpenIDResponse201 | PostOpenIDResponse400 | PostOpenIDResponse401 | PostOpenIDResponse403 | PostOpenIDResponse422 | PostOpenIDResponse500 | None:
    if response.status_code == 201:
        response_201 = PostOpenIDResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostOpenIDResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostOpenIDResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostOpenIDResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostOpenIDResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostOpenIDResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostOpenIDResponse201 | PostOpenIDResponse400 | PostOpenIDResponse401 | PostOpenIDResponse403 | PostOpenIDResponse422 | PostOpenIDResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OpenIDCreate | Unset = UNSET,

) -> Response[PostOpenIDResponse201 | PostOpenIDResponse400 | PostOpenIDResponse401 | PostOpenIDResponse403 | PostOpenIDResponse422 | PostOpenIDResponse500]:
    """ Creates an OpenID in the application.

    Args:
        body (OpenIDCreate | Unset): OpenIDCreate defines the expected payload for creating an
            OpenID IDMS entity in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOpenIDResponse201 | PostOpenIDResponse400 | PostOpenIDResponse401 | PostOpenIDResponse403 | PostOpenIDResponse422 | PostOpenIDResponse500]
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
    body: OpenIDCreate | Unset = UNSET,

) -> PostOpenIDResponse201 | PostOpenIDResponse400 | PostOpenIDResponse401 | PostOpenIDResponse403 | PostOpenIDResponse422 | PostOpenIDResponse500 | None:
    """ Creates an OpenID in the application.

    Args:
        body (OpenIDCreate | Unset): OpenIDCreate defines the expected payload for creating an
            OpenID IDMS entity in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOpenIDResponse201 | PostOpenIDResponse400 | PostOpenIDResponse401 | PostOpenIDResponse403 | PostOpenIDResponse422 | PostOpenIDResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OpenIDCreate | Unset = UNSET,

) -> Response[PostOpenIDResponse201 | PostOpenIDResponse400 | PostOpenIDResponse401 | PostOpenIDResponse403 | PostOpenIDResponse422 | PostOpenIDResponse500]:
    """ Creates an OpenID in the application.

    Args:
        body (OpenIDCreate | Unset): OpenIDCreate defines the expected payload for creating an
            OpenID IDMS entity in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOpenIDResponse201 | PostOpenIDResponse400 | PostOpenIDResponse401 | PostOpenIDResponse403 | PostOpenIDResponse422 | PostOpenIDResponse500]
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
    body: OpenIDCreate | Unset = UNSET,

) -> PostOpenIDResponse201 | PostOpenIDResponse400 | PostOpenIDResponse401 | PostOpenIDResponse403 | PostOpenIDResponse422 | PostOpenIDResponse500 | None:
    """ Creates an OpenID in the application.

    Args:
        body (OpenIDCreate | Unset): OpenIDCreate defines the expected payload for creating an
            OpenID IDMS entity in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOpenIDResponse201 | PostOpenIDResponse400 | PostOpenIDResponse401 | PostOpenIDResponse403 | PostOpenIDResponse422 | PostOpenIDResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
