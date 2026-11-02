from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.google_cloud_service_account_key_create import GoogleCloudServiceAccountKeyCreate
from ...models.post_service_account_key_response_201 import PostServiceAccountKeyResponse201
from ...models.post_service_account_key_response_401 import PostServiceAccountKeyResponse401
from ...models.post_service_account_key_response_403 import PostServiceAccountKeyResponse403
from ...models.post_service_account_key_response_404 import PostServiceAccountKeyResponse404
from ...models.post_service_account_key_response_500 import PostServiceAccountKeyResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: GoogleCloudServiceAccountKeyCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/gcp/service-account/{id}/key".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostServiceAccountKeyResponse201 | PostServiceAccountKeyResponse401 | PostServiceAccountKeyResponse403 | PostServiceAccountKeyResponse404 | PostServiceAccountKeyResponse500 | None:
    if response.status_code == 201:
        response_201 = PostServiceAccountKeyResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = PostServiceAccountKeyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostServiceAccountKeyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostServiceAccountKeyResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = PostServiceAccountKeyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostServiceAccountKeyResponse201 | PostServiceAccountKeyResponse401 | PostServiceAccountKeyResponse403 | PostServiceAccountKeyResponse404 | PostServiceAccountKeyResponse500]:
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
    body: GoogleCloudServiceAccountKeyCreate,

) -> Response[PostServiceAccountKeyResponse201 | PostServiceAccountKeyResponse401 | PostServiceAccountKeyResponse403 | PostServiceAccountKeyResponse404 | PostServiceAccountKeyResponse500]:
    """ Creates a key associated with the specified gcp service account.

    Args:
        id (int):
        body (GoogleCloudServiceAccountKeyCreate): GoogleCloudServiceAccountKeyCreate defines
            creating a key attached to a google cloud service account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServiceAccountKeyResponse201 | PostServiceAccountKeyResponse401 | PostServiceAccountKeyResponse403 | PostServiceAccountKeyResponse404 | PostServiceAccountKeyResponse500]
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
    body: GoogleCloudServiceAccountKeyCreate,

) -> PostServiceAccountKeyResponse201 | PostServiceAccountKeyResponse401 | PostServiceAccountKeyResponse403 | PostServiceAccountKeyResponse404 | PostServiceAccountKeyResponse500 | None:
    """ Creates a key associated with the specified gcp service account.

    Args:
        id (int):
        body (GoogleCloudServiceAccountKeyCreate): GoogleCloudServiceAccountKeyCreate defines
            creating a key attached to a google cloud service account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServiceAccountKeyResponse201 | PostServiceAccountKeyResponse401 | PostServiceAccountKeyResponse403 | PostServiceAccountKeyResponse404 | PostServiceAccountKeyResponse500
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
    body: GoogleCloudServiceAccountKeyCreate,

) -> Response[PostServiceAccountKeyResponse201 | PostServiceAccountKeyResponse401 | PostServiceAccountKeyResponse403 | PostServiceAccountKeyResponse404 | PostServiceAccountKeyResponse500]:
    """ Creates a key associated with the specified gcp service account.

    Args:
        id (int):
        body (GoogleCloudServiceAccountKeyCreate): GoogleCloudServiceAccountKeyCreate defines
            creating a key attached to a google cloud service account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServiceAccountKeyResponse201 | PostServiceAccountKeyResponse401 | PostServiceAccountKeyResponse403 | PostServiceAccountKeyResponse404 | PostServiceAccountKeyResponse500]
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
    body: GoogleCloudServiceAccountKeyCreate,

) -> PostServiceAccountKeyResponse201 | PostServiceAccountKeyResponse401 | PostServiceAccountKeyResponse403 | PostServiceAccountKeyResponse404 | PostServiceAccountKeyResponse500 | None:
    """ Creates a key associated with the specified gcp service account.

    Args:
        id (int):
        body (GoogleCloudServiceAccountKeyCreate): GoogleCloudServiceAccountKeyCreate defines
            creating a key attached to a google cloud service account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServiceAccountKeyResponse201 | PostServiceAccountKeyResponse401 | PostServiceAccountKeyResponse403 | PostServiceAccountKeyResponse404 | PostServiceAccountKeyResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
