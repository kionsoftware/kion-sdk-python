from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_u_group_response_201 import PostUGroupResponse201
from ...models.post_u_group_response_400 import PostUGroupResponse400
from ...models.post_u_group_response_401 import PostUGroupResponse401
from ...models.post_u_group_response_403 import PostUGroupResponse403
from ...models.post_u_group_response_422 import PostUGroupResponse422
from ...models.post_u_group_response_500 import PostUGroupResponse500
from ...models.u_group_create import UGroupCreate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UGroupCreate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/user-group",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostUGroupResponse201 | PostUGroupResponse400 | PostUGroupResponse401 | PostUGroupResponse403 | PostUGroupResponse422 | PostUGroupResponse500 | None:
    if response.status_code == 201:
        response_201 = PostUGroupResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostUGroupResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostUGroupResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostUGroupResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostUGroupResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostUGroupResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostUGroupResponse201 | PostUGroupResponse400 | PostUGroupResponse401 | PostUGroupResponse403 | PostUGroupResponse422 | PostUGroupResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UGroupCreate | Unset = UNSET,

) -> Response[PostUGroupResponse201 | PostUGroupResponse400 | PostUGroupResponse401 | PostUGroupResponse403 | PostUGroupResponse422 | PostUGroupResponse500]:
    """ Creates a user group in the application.

    Args:
        body (UGroupCreate | Unset): UGroupCreate defines a user group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUGroupResponse201 | PostUGroupResponse400 | PostUGroupResponse401 | PostUGroupResponse403 | PostUGroupResponse422 | PostUGroupResponse500]
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
    body: UGroupCreate | Unset = UNSET,

) -> PostUGroupResponse201 | PostUGroupResponse400 | PostUGroupResponse401 | PostUGroupResponse403 | PostUGroupResponse422 | PostUGroupResponse500 | None:
    """ Creates a user group in the application.

    Args:
        body (UGroupCreate | Unset): UGroupCreate defines a user group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUGroupResponse201 | PostUGroupResponse400 | PostUGroupResponse401 | PostUGroupResponse403 | PostUGroupResponse422 | PostUGroupResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UGroupCreate | Unset = UNSET,

) -> Response[PostUGroupResponse201 | PostUGroupResponse400 | PostUGroupResponse401 | PostUGroupResponse403 | PostUGroupResponse422 | PostUGroupResponse500]:
    """ Creates a user group in the application.

    Args:
        body (UGroupCreate | Unset): UGroupCreate defines a user group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUGroupResponse201 | PostUGroupResponse400 | PostUGroupResponse401 | PostUGroupResponse403 | PostUGroupResponse422 | PostUGroupResponse500]
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
    body: UGroupCreate | Unset = UNSET,

) -> PostUGroupResponse201 | PostUGroupResponse400 | PostUGroupResponse401 | PostUGroupResponse403 | PostUGroupResponse422 | PostUGroupResponse500 | None:
    """ Creates a user group in the application.

    Args:
        body (UGroupCreate | Unset): UGroupCreate defines a user group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUGroupResponse201 | PostUGroupResponse400 | PostUGroupResponse401 | PostUGroupResponse403 | PostUGroupResponse422 | PostUGroupResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
