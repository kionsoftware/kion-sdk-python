from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gcp_account_cache_new_gcp_project import GCPAccountCacheNewGCPProject
from ...models.post_account_cache_create_new_gcp_response_201 import PostAccountCacheCreateNewGCPResponse201
from ...models.post_account_cache_create_new_gcp_response_400 import PostAccountCacheCreateNewGCPResponse400
from ...models.post_account_cache_create_new_gcp_response_401 import PostAccountCacheCreateNewGCPResponse401
from ...models.post_account_cache_create_new_gcp_response_403 import PostAccountCacheCreateNewGCPResponse403
from ...models.post_account_cache_create_new_gcp_response_422 import PostAccountCacheCreateNewGCPResponse422
from ...models.post_account_cache_create_new_gcp_response_500 import PostAccountCacheCreateNewGCPResponse500
from typing import cast



def _get_kwargs(
    *,
    body: GCPAccountCacheNewGCPProject,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account-cache/create/__qs__/account-type/google-cloud",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAccountCacheCreateNewGCPResponse201 | PostAccountCacheCreateNewGCPResponse400 | PostAccountCacheCreateNewGCPResponse401 | PostAccountCacheCreateNewGCPResponse403 | PostAccountCacheCreateNewGCPResponse422 | PostAccountCacheCreateNewGCPResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAccountCacheCreateNewGCPResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAccountCacheCreateNewGCPResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAccountCacheCreateNewGCPResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAccountCacheCreateNewGCPResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAccountCacheCreateNewGCPResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAccountCacheCreateNewGCPResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAccountCacheCreateNewGCPResponse201 | PostAccountCacheCreateNewGCPResponse400 | PostAccountCacheCreateNewGCPResponse401 | PostAccountCacheCreateNewGCPResponse403 | PostAccountCacheCreateNewGCPResponse422 | PostAccountCacheCreateNewGCPResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPAccountCacheNewGCPProject,

) -> Response[PostAccountCacheCreateNewGCPResponse201 | PostAccountCacheCreateNewGCPResponse400 | PostAccountCacheCreateNewGCPResponse401 | PostAccountCacheCreateNewGCPResponse403 | PostAccountCacheCreateNewGCPResponse422 | PostAccountCacheCreateNewGCPResponse500]:
    """ Creates a new Google Cloud Project and adds it to the account cache in the application.

     The cached ID will be returned immediately.  The Google Cloud Project may take a few minutes to
    provision.  If the
    project fails to provision, the cached account will be removed.

    Args:
        body (GCPAccountCacheNewGCPProject): GCPAccountCacheNewGCPProject defines a payload for
            creating a new GCP Project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountCacheCreateNewGCPResponse201 | PostAccountCacheCreateNewGCPResponse400 | PostAccountCacheCreateNewGCPResponse401 | PostAccountCacheCreateNewGCPResponse403 | PostAccountCacheCreateNewGCPResponse422 | PostAccountCacheCreateNewGCPResponse500]
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
    body: GCPAccountCacheNewGCPProject,

) -> PostAccountCacheCreateNewGCPResponse201 | PostAccountCacheCreateNewGCPResponse400 | PostAccountCacheCreateNewGCPResponse401 | PostAccountCacheCreateNewGCPResponse403 | PostAccountCacheCreateNewGCPResponse422 | PostAccountCacheCreateNewGCPResponse500 | None:
    """ Creates a new Google Cloud Project and adds it to the account cache in the application.

     The cached ID will be returned immediately.  The Google Cloud Project may take a few minutes to
    provision.  If the
    project fails to provision, the cached account will be removed.

    Args:
        body (GCPAccountCacheNewGCPProject): GCPAccountCacheNewGCPProject defines a payload for
            creating a new GCP Project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountCacheCreateNewGCPResponse201 | PostAccountCacheCreateNewGCPResponse400 | PostAccountCacheCreateNewGCPResponse401 | PostAccountCacheCreateNewGCPResponse403 | PostAccountCacheCreateNewGCPResponse422 | PostAccountCacheCreateNewGCPResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPAccountCacheNewGCPProject,

) -> Response[PostAccountCacheCreateNewGCPResponse201 | PostAccountCacheCreateNewGCPResponse400 | PostAccountCacheCreateNewGCPResponse401 | PostAccountCacheCreateNewGCPResponse403 | PostAccountCacheCreateNewGCPResponse422 | PostAccountCacheCreateNewGCPResponse500]:
    """ Creates a new Google Cloud Project and adds it to the account cache in the application.

     The cached ID will be returned immediately.  The Google Cloud Project may take a few minutes to
    provision.  If the
    project fails to provision, the cached account will be removed.

    Args:
        body (GCPAccountCacheNewGCPProject): GCPAccountCacheNewGCPProject defines a payload for
            creating a new GCP Project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountCacheCreateNewGCPResponse201 | PostAccountCacheCreateNewGCPResponse400 | PostAccountCacheCreateNewGCPResponse401 | PostAccountCacheCreateNewGCPResponse403 | PostAccountCacheCreateNewGCPResponse422 | PostAccountCacheCreateNewGCPResponse500]
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
    body: GCPAccountCacheNewGCPProject,

) -> PostAccountCacheCreateNewGCPResponse201 | PostAccountCacheCreateNewGCPResponse400 | PostAccountCacheCreateNewGCPResponse401 | PostAccountCacheCreateNewGCPResponse403 | PostAccountCacheCreateNewGCPResponse422 | PostAccountCacheCreateNewGCPResponse500 | None:
    """ Creates a new Google Cloud Project and adds it to the account cache in the application.

     The cached ID will be returned immediately.  The Google Cloud Project may take a few minutes to
    provision.  If the
    project fails to provision, the cached account will be removed.

    Args:
        body (GCPAccountCacheNewGCPProject): GCPAccountCacheNewGCPProject defines a payload for
            creating a new GCP Project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountCacheCreateNewGCPResponse201 | PostAccountCacheCreateNewGCPResponse400 | PostAccountCacheCreateNewGCPResponse401 | PostAccountCacheCreateNewGCPResponse403 | PostAccountCacheCreateNewGCPResponse422 | PostAccountCacheCreateNewGCPResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
