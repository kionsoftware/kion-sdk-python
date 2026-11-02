from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.google_cloud_service_account_create import GoogleCloudServiceAccountCreate
from ...models.post_service_account_response_201 import PostServiceAccountResponse201
from ...models.post_service_account_response_400 import PostServiceAccountResponse400
from ...models.post_service_account_response_401 import PostServiceAccountResponse401
from ...models.post_service_account_response_403 import PostServiceAccountResponse403
from ...models.post_service_account_response_422 import PostServiceAccountResponse422
from ...models.post_service_account_response_500 import PostServiceAccountResponse500
from typing import cast



def _get_kwargs(
    *,
    body: GoogleCloudServiceAccountCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/gcp/service-account",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostServiceAccountResponse201 | PostServiceAccountResponse400 | PostServiceAccountResponse401 | PostServiceAccountResponse403 | PostServiceAccountResponse422 | PostServiceAccountResponse500 | None:
    if response.status_code == 201:
        response_201 = PostServiceAccountResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostServiceAccountResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostServiceAccountResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostServiceAccountResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostServiceAccountResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostServiceAccountResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostServiceAccountResponse201 | PostServiceAccountResponse400 | PostServiceAccountResponse401 | PostServiceAccountResponse403 | PostServiceAccountResponse422 | PostServiceAccountResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GoogleCloudServiceAccountCreate,

) -> Response[PostServiceAccountResponse201 | PostServiceAccountResponse400 | PostServiceAccountResponse401 | PostServiceAccountResponse403 | PostServiceAccountResponse422 | PostServiceAccountResponse500]:
    """ Creates a GCPServiceAccount in the application.

    Args:
        body (GoogleCloudServiceAccountCreate): GoogleCloudServiceAccountCreate defines adding a
            Google Cloud service account to cloudtamer.io.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServiceAccountResponse201 | PostServiceAccountResponse400 | PostServiceAccountResponse401 | PostServiceAccountResponse403 | PostServiceAccountResponse422 | PostServiceAccountResponse500]
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
    body: GoogleCloudServiceAccountCreate,

) -> PostServiceAccountResponse201 | PostServiceAccountResponse400 | PostServiceAccountResponse401 | PostServiceAccountResponse403 | PostServiceAccountResponse422 | PostServiceAccountResponse500 | None:
    """ Creates a GCPServiceAccount in the application.

    Args:
        body (GoogleCloudServiceAccountCreate): GoogleCloudServiceAccountCreate defines adding a
            Google Cloud service account to cloudtamer.io.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServiceAccountResponse201 | PostServiceAccountResponse400 | PostServiceAccountResponse401 | PostServiceAccountResponse403 | PostServiceAccountResponse422 | PostServiceAccountResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GoogleCloudServiceAccountCreate,

) -> Response[PostServiceAccountResponse201 | PostServiceAccountResponse400 | PostServiceAccountResponse401 | PostServiceAccountResponse403 | PostServiceAccountResponse422 | PostServiceAccountResponse500]:
    """ Creates a GCPServiceAccount in the application.

    Args:
        body (GoogleCloudServiceAccountCreate): GoogleCloudServiceAccountCreate defines adding a
            Google Cloud service account to cloudtamer.io.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServiceAccountResponse201 | PostServiceAccountResponse400 | PostServiceAccountResponse401 | PostServiceAccountResponse403 | PostServiceAccountResponse422 | PostServiceAccountResponse500]
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
    body: GoogleCloudServiceAccountCreate,

) -> PostServiceAccountResponse201 | PostServiceAccountResponse400 | PostServiceAccountResponse401 | PostServiceAccountResponse403 | PostServiceAccountResponse422 | PostServiceAccountResponse500 | None:
    """ Creates a GCPServiceAccount in the application.

    Args:
        body (GoogleCloudServiceAccountCreate): GoogleCloudServiceAccountCreate defines adding a
            Google Cloud service account to cloudtamer.io.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServiceAccountResponse201 | PostServiceAccountResponse400 | PostServiceAccountResponse401 | PostServiceAccountResponse403 | PostServiceAccountResponse422 | PostServiceAccountResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
