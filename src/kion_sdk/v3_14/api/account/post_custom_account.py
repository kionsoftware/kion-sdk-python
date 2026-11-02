from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.custom_account_create import CustomAccountCreate
from ...models.post_custom_account_response_201 import PostCustomAccountResponse201
from ...models.post_custom_account_response_400 import PostCustomAccountResponse400
from ...models.post_custom_account_response_401 import PostCustomAccountResponse401
from ...models.post_custom_account_response_403 import PostCustomAccountResponse403
from ...models.post_custom_account_response_422 import PostCustomAccountResponse422
from ...models.post_custom_account_response_500 import PostCustomAccountResponse500
from typing import cast



def _get_kwargs(
    *,
    body: CustomAccountCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account/__qs__/account-type/custom",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostCustomAccountResponse201 | PostCustomAccountResponse400 | PostCustomAccountResponse401 | PostCustomAccountResponse403 | PostCustomAccountResponse422 | PostCustomAccountResponse500 | None:
    if response.status_code == 201:
        response_201 = PostCustomAccountResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostCustomAccountResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostCustomAccountResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostCustomAccountResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostCustomAccountResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostCustomAccountResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostCustomAccountResponse201 | PostCustomAccountResponse400 | PostCustomAccountResponse401 | PostCustomAccountResponse403 | PostCustomAccountResponse422 | PostCustomAccountResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CustomAccountCreate,

) -> Response[PostCustomAccountResponse201 | PostCustomAccountResponse400 | PostCustomAccountResponse401 | PostCustomAccountResponse403 | PostCustomAccountResponse422 | PostCustomAccountResponse500]:
    """ Attaches a custom account to a project in the application.

    Args:
        body (CustomAccountCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCustomAccountResponse201 | PostCustomAccountResponse400 | PostCustomAccountResponse401 | PostCustomAccountResponse403 | PostCustomAccountResponse422 | PostCustomAccountResponse500]
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
    body: CustomAccountCreate,

) -> PostCustomAccountResponse201 | PostCustomAccountResponse400 | PostCustomAccountResponse401 | PostCustomAccountResponse403 | PostCustomAccountResponse422 | PostCustomAccountResponse500 | None:
    """ Attaches a custom account to a project in the application.

    Args:
        body (CustomAccountCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCustomAccountResponse201 | PostCustomAccountResponse400 | PostCustomAccountResponse401 | PostCustomAccountResponse403 | PostCustomAccountResponse422 | PostCustomAccountResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CustomAccountCreate,

) -> Response[PostCustomAccountResponse201 | PostCustomAccountResponse400 | PostCustomAccountResponse401 | PostCustomAccountResponse403 | PostCustomAccountResponse422 | PostCustomAccountResponse500]:
    """ Attaches a custom account to a project in the application.

    Args:
        body (CustomAccountCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCustomAccountResponse201 | PostCustomAccountResponse400 | PostCustomAccountResponse401 | PostCustomAccountResponse403 | PostCustomAccountResponse422 | PostCustomAccountResponse500]
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
    body: CustomAccountCreate,

) -> PostCustomAccountResponse201 | PostCustomAccountResponse400 | PostCustomAccountResponse401 | PostCustomAccountResponse403 | PostCustomAccountResponse422 | PostCustomAccountResponse500 | None:
    """ Attaches a custom account to a project in the application.

    Args:
        body (CustomAccountCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCustomAccountResponse201 | PostCustomAccountResponse400 | PostCustomAccountResponse401 | PostCustomAccountResponse403 | PostCustomAccountResponse422 | PostCustomAccountResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
