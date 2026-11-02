from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_linkage_source_url import AccountLinkageSourceURL
from ...models.google_link_start_response_201 import GoogleLinkStartResponse201
from ...models.google_link_start_response_400 import GoogleLinkStartResponse400
from ...models.google_link_start_response_401 import GoogleLinkStartResponse401
from ...models.google_link_start_response_404 import GoogleLinkStartResponse404
from ...models.google_link_start_response_422 import GoogleLinkStartResponse422
from ...models.google_link_start_response_500 import GoogleLinkStartResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: AccountLinkageSourceURL,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account/{id}/link-google".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GoogleLinkStartResponse201 | GoogleLinkStartResponse400 | GoogleLinkStartResponse401 | GoogleLinkStartResponse404 | GoogleLinkStartResponse422 | GoogleLinkStartResponse500 | None:
    if response.status_code == 201:
        response_201 = GoogleLinkStartResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = GoogleLinkStartResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GoogleLinkStartResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = GoogleLinkStartResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = GoogleLinkStartResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = GoogleLinkStartResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GoogleLinkStartResponse201 | GoogleLinkStartResponse400 | GoogleLinkStartResponse401 | GoogleLinkStartResponse404 | GoogleLinkStartResponse422 | GoogleLinkStartResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AccountLinkageSourceURL,

) -> Response[GoogleLinkStartResponse201 | GoogleLinkStartResponse400 | GoogleLinkStartResponse401 | GoogleLinkStartResponse404 | GoogleLinkStartResponse422 | GoogleLinkStartResponse500]:
    r""" Creates a URL with which you can redirect a user to Google OAuth to link a Kion account to a Google
    account.

     When account linkage completes, Kion will redirect the user back to the provided source URL with the
    following
    query parameters -
    1. \"trigger\" - This defines the type of callback that's occurring. This is useful if you use the
    same endpoint to react to multiple different callbacks.
    It will be set to \"linkage-result-google\" when redirected to by this endpoint.
    2. \"link-success\" - This will be either the string \"true\" or \"false\" and will signify whether
    or not the account was linked successfully.
    3. \"link-result-message\" - This is a descriptive string which should be displayed to the user. It
    may express that linkage succeeded or will give more detail on why the linkage failed.

    Args:
        id (int):
        body (AccountLinkageSourceURL): AccountLinkageSourceURL contains a link to the URL the
            user should be redirected back to after completing the account linkage process.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleLinkStartResponse201 | GoogleLinkStartResponse400 | GoogleLinkStartResponse401 | GoogleLinkStartResponse404 | GoogleLinkStartResponse422 | GoogleLinkStartResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AccountLinkageSourceURL,

) -> GoogleLinkStartResponse201 | GoogleLinkStartResponse400 | GoogleLinkStartResponse401 | GoogleLinkStartResponse404 | GoogleLinkStartResponse422 | GoogleLinkStartResponse500 | None:
    r""" Creates a URL with which you can redirect a user to Google OAuth to link a Kion account to a Google
    account.

     When account linkage completes, Kion will redirect the user back to the provided source URL with the
    following
    query parameters -
    1. \"trigger\" - This defines the type of callback that's occurring. This is useful if you use the
    same endpoint to react to multiple different callbacks.
    It will be set to \"linkage-result-google\" when redirected to by this endpoint.
    2. \"link-success\" - This will be either the string \"true\" or \"false\" and will signify whether
    or not the account was linked successfully.
    3. \"link-result-message\" - This is a descriptive string which should be displayed to the user. It
    may express that linkage succeeded or will give more detail on why the linkage failed.

    Args:
        id (int):
        body (AccountLinkageSourceURL): AccountLinkageSourceURL contains a link to the URL the
            user should be redirected back to after completing the account linkage process.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleLinkStartResponse201 | GoogleLinkStartResponse400 | GoogleLinkStartResponse401 | GoogleLinkStartResponse404 | GoogleLinkStartResponse422 | GoogleLinkStartResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AccountLinkageSourceURL,

) -> Response[GoogleLinkStartResponse201 | GoogleLinkStartResponse400 | GoogleLinkStartResponse401 | GoogleLinkStartResponse404 | GoogleLinkStartResponse422 | GoogleLinkStartResponse500]:
    r""" Creates a URL with which you can redirect a user to Google OAuth to link a Kion account to a Google
    account.

     When account linkage completes, Kion will redirect the user back to the provided source URL with the
    following
    query parameters -
    1. \"trigger\" - This defines the type of callback that's occurring. This is useful if you use the
    same endpoint to react to multiple different callbacks.
    It will be set to \"linkage-result-google\" when redirected to by this endpoint.
    2. \"link-success\" - This will be either the string \"true\" or \"false\" and will signify whether
    or not the account was linked successfully.
    3. \"link-result-message\" - This is a descriptive string which should be displayed to the user. It
    may express that linkage succeeded or will give more detail on why the linkage failed.

    Args:
        id (int):
        body (AccountLinkageSourceURL): AccountLinkageSourceURL contains a link to the URL the
            user should be redirected back to after completing the account linkage process.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleLinkStartResponse201 | GoogleLinkStartResponse400 | GoogleLinkStartResponse401 | GoogleLinkStartResponse404 | GoogleLinkStartResponse422 | GoogleLinkStartResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AccountLinkageSourceURL,

) -> GoogleLinkStartResponse201 | GoogleLinkStartResponse400 | GoogleLinkStartResponse401 | GoogleLinkStartResponse404 | GoogleLinkStartResponse422 | GoogleLinkStartResponse500 | None:
    r""" Creates a URL with which you can redirect a user to Google OAuth to link a Kion account to a Google
    account.

     When account linkage completes, Kion will redirect the user back to the provided source URL with the
    following
    query parameters -
    1. \"trigger\" - This defines the type of callback that's occurring. This is useful if you use the
    same endpoint to react to multiple different callbacks.
    It will be set to \"linkage-result-google\" when redirected to by this endpoint.
    2. \"link-success\" - This will be either the string \"true\" or \"false\" and will signify whether
    or not the account was linked successfully.
    3. \"link-result-message\" - This is a descriptive string which should be displayed to the user. It
    may express that linkage succeeded or will give more detail on why the linkage failed.

    Args:
        id (int):
        body (AccountLinkageSourceURL): AccountLinkageSourceURL contains a link to the URL the
            user should be redirected back to after completing the account linkage process.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleLinkStartResponse201 | GoogleLinkStartResponse400 | GoogleLinkStartResponse401 | GoogleLinkStartResponse404 | GoogleLinkStartResponse422 | GoogleLinkStartResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
