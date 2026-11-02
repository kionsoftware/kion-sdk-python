from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_create_global_user_mapping_response_200 import PostCreateGlobalUserMappingResponse200
from ...models.post_create_global_user_mapping_response_400 import PostCreateGlobalUserMappingResponse400
from ...models.post_create_global_user_mapping_response_401 import PostCreateGlobalUserMappingResponse401
from ...models.post_create_global_user_mapping_response_403 import PostCreateGlobalUserMappingResponse403
from ...models.post_create_global_user_mapping_response_422 import PostCreateGlobalUserMappingResponse422
from ...models.post_create_global_user_mapping_response_500 import PostCreateGlobalUserMappingResponse500
from ...models.user_mapping import UserMapping
from typing import cast



def _get_kwargs(
    *,
    body: list[UserMapping],

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/global/permission-mapping",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostCreateGlobalUserMappingResponse200 | PostCreateGlobalUserMappingResponse400 | PostCreateGlobalUserMappingResponse401 | PostCreateGlobalUserMappingResponse403 | PostCreateGlobalUserMappingResponse422 | PostCreateGlobalUserMappingResponse500 | None:
    if response.status_code == 200:
        response_200 = PostCreateGlobalUserMappingResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostCreateGlobalUserMappingResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostCreateGlobalUserMappingResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostCreateGlobalUserMappingResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostCreateGlobalUserMappingResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostCreateGlobalUserMappingResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostCreateGlobalUserMappingResponse200 | PostCreateGlobalUserMappingResponse400 | PostCreateGlobalUserMappingResponse401 | PostCreateGlobalUserMappingResponse403 | PostCreateGlobalUserMappingResponse422 | PostCreateGlobalUserMappingResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: list[UserMapping],

) -> Response[PostCreateGlobalUserMappingResponse200 | PostCreateGlobalUserMappingResponse400 | PostCreateGlobalUserMappingResponse401 | PostCreateGlobalUserMappingResponse403 | PostCreateGlobalUserMappingResponse422 | PostCreateGlobalUserMappingResponse500]:
    """ Creates permission mappings for the application.

    Args:
        body (list[UserMapping]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCreateGlobalUserMappingResponse200 | PostCreateGlobalUserMappingResponse400 | PostCreateGlobalUserMappingResponse401 | PostCreateGlobalUserMappingResponse403 | PostCreateGlobalUserMappingResponse422 | PostCreateGlobalUserMappingResponse500]
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
    body: list[UserMapping],

) -> PostCreateGlobalUserMappingResponse200 | PostCreateGlobalUserMappingResponse400 | PostCreateGlobalUserMappingResponse401 | PostCreateGlobalUserMappingResponse403 | PostCreateGlobalUserMappingResponse422 | PostCreateGlobalUserMappingResponse500 | None:
    """ Creates permission mappings for the application.

    Args:
        body (list[UserMapping]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCreateGlobalUserMappingResponse200 | PostCreateGlobalUserMappingResponse400 | PostCreateGlobalUserMappingResponse401 | PostCreateGlobalUserMappingResponse403 | PostCreateGlobalUserMappingResponse422 | PostCreateGlobalUserMappingResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: list[UserMapping],

) -> Response[PostCreateGlobalUserMappingResponse200 | PostCreateGlobalUserMappingResponse400 | PostCreateGlobalUserMappingResponse401 | PostCreateGlobalUserMappingResponse403 | PostCreateGlobalUserMappingResponse422 | PostCreateGlobalUserMappingResponse500]:
    """ Creates permission mappings for the application.

    Args:
        body (list[UserMapping]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCreateGlobalUserMappingResponse200 | PostCreateGlobalUserMappingResponse400 | PostCreateGlobalUserMappingResponse401 | PostCreateGlobalUserMappingResponse403 | PostCreateGlobalUserMappingResponse422 | PostCreateGlobalUserMappingResponse500]
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
    body: list[UserMapping],

) -> PostCreateGlobalUserMappingResponse200 | PostCreateGlobalUserMappingResponse400 | PostCreateGlobalUserMappingResponse401 | PostCreateGlobalUserMappingResponse403 | PostCreateGlobalUserMappingResponse422 | PostCreateGlobalUserMappingResponse500 | None:
    """ Creates permission mappings for the application.

    Args:
        body (list[UserMapping]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCreateGlobalUserMappingResponse200 | PostCreateGlobalUserMappingResponse400 | PostCreateGlobalUserMappingResponse401 | PostCreateGlobalUserMappingResponse403 | PostCreateGlobalUserMappingResponse422 | PostCreateGlobalUserMappingResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
