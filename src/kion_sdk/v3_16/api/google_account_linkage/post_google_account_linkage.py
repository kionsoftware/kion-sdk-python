from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.google_account_linkage_create import GoogleAccountLinkageCreate
from ...models.post_google_account_linkage_response_201 import PostGoogleAccountLinkageResponse201
from ...models.post_google_account_linkage_response_400 import PostGoogleAccountLinkageResponse400
from ...models.post_google_account_linkage_response_401 import PostGoogleAccountLinkageResponse401
from ...models.post_google_account_linkage_response_422 import PostGoogleAccountLinkageResponse422
from ...models.post_google_account_linkage_response_500 import PostGoogleAccountLinkageResponse500
from typing import cast



def _get_kwargs(
    *,
    body: GoogleAccountLinkageCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account-linkages/google",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostGoogleAccountLinkageResponse201 | PostGoogleAccountLinkageResponse400 | PostGoogleAccountLinkageResponse401 | PostGoogleAccountLinkageResponse422 | PostGoogleAccountLinkageResponse500 | None:
    if response.status_code == 201:
        response_201 = PostGoogleAccountLinkageResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostGoogleAccountLinkageResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostGoogleAccountLinkageResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = PostGoogleAccountLinkageResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostGoogleAccountLinkageResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostGoogleAccountLinkageResponse201 | PostGoogleAccountLinkageResponse400 | PostGoogleAccountLinkageResponse401 | PostGoogleAccountLinkageResponse422 | PostGoogleAccountLinkageResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GoogleAccountLinkageCreate,

) -> Response[PostGoogleAccountLinkageResponse201 | PostGoogleAccountLinkageResponse400 | PostGoogleAccountLinkageResponse401 | PostGoogleAccountLinkageResponse422 | PostGoogleAccountLinkageResponse500]:
    """ Creates a Google Account Linkage for the specified user.

    Args:
        body (GoogleAccountLinkageCreate): GoogleAccountLinkageCreate is the request body for
            creating a Google Account Linkage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGoogleAccountLinkageResponse201 | PostGoogleAccountLinkageResponse400 | PostGoogleAccountLinkageResponse401 | PostGoogleAccountLinkageResponse422 | PostGoogleAccountLinkageResponse500]
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
    body: GoogleAccountLinkageCreate,

) -> PostGoogleAccountLinkageResponse201 | PostGoogleAccountLinkageResponse400 | PostGoogleAccountLinkageResponse401 | PostGoogleAccountLinkageResponse422 | PostGoogleAccountLinkageResponse500 | None:
    """ Creates a Google Account Linkage for the specified user.

    Args:
        body (GoogleAccountLinkageCreate): GoogleAccountLinkageCreate is the request body for
            creating a Google Account Linkage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGoogleAccountLinkageResponse201 | PostGoogleAccountLinkageResponse400 | PostGoogleAccountLinkageResponse401 | PostGoogleAccountLinkageResponse422 | PostGoogleAccountLinkageResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GoogleAccountLinkageCreate,

) -> Response[PostGoogleAccountLinkageResponse201 | PostGoogleAccountLinkageResponse400 | PostGoogleAccountLinkageResponse401 | PostGoogleAccountLinkageResponse422 | PostGoogleAccountLinkageResponse500]:
    """ Creates a Google Account Linkage for the specified user.

    Args:
        body (GoogleAccountLinkageCreate): GoogleAccountLinkageCreate is the request body for
            creating a Google Account Linkage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGoogleAccountLinkageResponse201 | PostGoogleAccountLinkageResponse400 | PostGoogleAccountLinkageResponse401 | PostGoogleAccountLinkageResponse422 | PostGoogleAccountLinkageResponse500]
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
    body: GoogleAccountLinkageCreate,

) -> PostGoogleAccountLinkageResponse201 | PostGoogleAccountLinkageResponse400 | PostGoogleAccountLinkageResponse401 | PostGoogleAccountLinkageResponse422 | PostGoogleAccountLinkageResponse500 | None:
    """ Creates a Google Account Linkage for the specified user.

    Args:
        body (GoogleAccountLinkageCreate): GoogleAccountLinkageCreate is the request body for
            creating a Google Account Linkage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGoogleAccountLinkageResponse201 | PostGoogleAccountLinkageResponse400 | PostGoogleAccountLinkageResponse401 | PostGoogleAccountLinkageResponse422 | PostGoogleAccountLinkageResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
