from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.app_role_create import AppRoleCreate
from ...models.post_app_role_response_201 import PostAppRoleResponse201
from ...models.post_app_role_response_400 import PostAppRoleResponse400
from ...models.post_app_role_response_401 import PostAppRoleResponse401
from ...models.post_app_role_response_403 import PostAppRoleResponse403
from ...models.post_app_role_response_422 import PostAppRoleResponse422
from ...models.post_app_role_response_500 import PostAppRoleResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AppRoleCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/app-role",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAppRoleResponse201 | PostAppRoleResponse400 | PostAppRoleResponse401 | PostAppRoleResponse403 | PostAppRoleResponse422 | PostAppRoleResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAppRoleResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAppRoleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAppRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAppRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAppRoleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAppRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAppRoleResponse201 | PostAppRoleResponse400 | PostAppRoleResponse401 | PostAppRoleResponse403 | PostAppRoleResponse422 | PostAppRoleResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AppRoleCreate,

) -> Response[PostAppRoleResponse201 | PostAppRoleResponse400 | PostAppRoleResponse401 | PostAppRoleResponse403 | PostAppRoleResponse422 | PostAppRoleResponse500]:
    """ Creates an App Role in the application.

    Args:
        body (AppRoleCreate): AppRoleCreate defines an App role creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAppRoleResponse201 | PostAppRoleResponse400 | PostAppRoleResponse401 | PostAppRoleResponse403 | PostAppRoleResponse422 | PostAppRoleResponse500]
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
    body: AppRoleCreate,

) -> PostAppRoleResponse201 | PostAppRoleResponse400 | PostAppRoleResponse401 | PostAppRoleResponse403 | PostAppRoleResponse422 | PostAppRoleResponse500 | None:
    """ Creates an App Role in the application.

    Args:
        body (AppRoleCreate): AppRoleCreate defines an App role creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAppRoleResponse201 | PostAppRoleResponse400 | PostAppRoleResponse401 | PostAppRoleResponse403 | PostAppRoleResponse422 | PostAppRoleResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AppRoleCreate,

) -> Response[PostAppRoleResponse201 | PostAppRoleResponse400 | PostAppRoleResponse401 | PostAppRoleResponse403 | PostAppRoleResponse422 | PostAppRoleResponse500]:
    """ Creates an App Role in the application.

    Args:
        body (AppRoleCreate): AppRoleCreate defines an App role creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAppRoleResponse201 | PostAppRoleResponse400 | PostAppRoleResponse401 | PostAppRoleResponse403 | PostAppRoleResponse422 | PostAppRoleResponse500]
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
    body: AppRoleCreate,

) -> PostAppRoleResponse201 | PostAppRoleResponse400 | PostAppRoleResponse401 | PostAppRoleResponse403 | PostAppRoleResponse422 | PostAppRoleResponse500 | None:
    """ Creates an App Role in the application.

    Args:
        body (AppRoleCreate): AppRoleCreate defines an App role creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAppRoleResponse201 | PostAppRoleResponse400 | PostAppRoleResponse401 | PostAppRoleResponse403 | PostAppRoleResponse422 | PostAppRoleResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
