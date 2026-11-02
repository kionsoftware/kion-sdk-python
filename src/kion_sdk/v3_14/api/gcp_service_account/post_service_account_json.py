from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_service_account_json_body import PostServiceAccountJSONBody
from ...models.post_service_account_json_response_200 import PostServiceAccountJSONResponse200
from ...models.post_service_account_json_response_400 import PostServiceAccountJSONResponse400
from ...models.post_service_account_json_response_401 import PostServiceAccountJSONResponse401
from ...models.post_service_account_json_response_403 import PostServiceAccountJSONResponse403
from ...models.post_service_account_json_response_500 import PostServiceAccountJSONResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: PostServiceAccountJSONBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/gcp/service-account/json",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostServiceAccountJSONResponse200 | PostServiceAccountJSONResponse400 | PostServiceAccountJSONResponse401 | PostServiceAccountJSONResponse403 | PostServiceAccountJSONResponse500 | None:
    if response.status_code == 200:
        response_200 = PostServiceAccountJSONResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostServiceAccountJSONResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostServiceAccountJSONResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostServiceAccountJSONResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PostServiceAccountJSONResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostServiceAccountJSONResponse200 | PostServiceAccountJSONResponse400 | PostServiceAccountJSONResponse401 | PostServiceAccountJSONResponse403 | PostServiceAccountJSONResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostServiceAccountJSONBody | Unset = UNSET,

) -> Response[PostServiceAccountJSONResponse200 | PostServiceAccountJSONResponse400 | PostServiceAccountJSONResponse401 | PostServiceAccountJSONResponse403 | PostServiceAccountJSONResponse500]:
    r""" Uploads the JSON service account access key.

     Use multipart form key \"json\" for file upload.

    Args:
        body (PostServiceAccountJSONBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServiceAccountJSONResponse200 | PostServiceAccountJSONResponse400 | PostServiceAccountJSONResponse401 | PostServiceAccountJSONResponse403 | PostServiceAccountJSONResponse500]
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
    body: PostServiceAccountJSONBody | Unset = UNSET,

) -> PostServiceAccountJSONResponse200 | PostServiceAccountJSONResponse400 | PostServiceAccountJSONResponse401 | PostServiceAccountJSONResponse403 | PostServiceAccountJSONResponse500 | None:
    r""" Uploads the JSON service account access key.

     Use multipart form key \"json\" for file upload.

    Args:
        body (PostServiceAccountJSONBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServiceAccountJSONResponse200 | PostServiceAccountJSONResponse400 | PostServiceAccountJSONResponse401 | PostServiceAccountJSONResponse403 | PostServiceAccountJSONResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostServiceAccountJSONBody | Unset = UNSET,

) -> Response[PostServiceAccountJSONResponse200 | PostServiceAccountJSONResponse400 | PostServiceAccountJSONResponse401 | PostServiceAccountJSONResponse403 | PostServiceAccountJSONResponse500]:
    r""" Uploads the JSON service account access key.

     Use multipart form key \"json\" for file upload.

    Args:
        body (PostServiceAccountJSONBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServiceAccountJSONResponse200 | PostServiceAccountJSONResponse400 | PostServiceAccountJSONResponse401 | PostServiceAccountJSONResponse403 | PostServiceAccountJSONResponse500]
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
    body: PostServiceAccountJSONBody | Unset = UNSET,

) -> PostServiceAccountJSONResponse200 | PostServiceAccountJSONResponse400 | PostServiceAccountJSONResponse401 | PostServiceAccountJSONResponse403 | PostServiceAccountJSONResponse500 | None:
    r""" Uploads the JSON service account access key.

     Use multipart form key \"json\" for file upload.

    Args:
        body (PostServiceAccountJSONBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServiceAccountJSONResponse200 | PostServiceAccountJSONResponse400 | PostServiceAccountJSONResponse401 | PostServiceAccountJSONResponse403 | PostServiceAccountJSONResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
