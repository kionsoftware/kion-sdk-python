from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_webhook_response_201 import PostWebhookResponse201
from ...models.post_webhook_response_400 import PostWebhookResponse400
from ...models.post_webhook_response_401 import PostWebhookResponse401
from ...models.post_webhook_response_403 import PostWebhookResponse403
from ...models.post_webhook_response_422 import PostWebhookResponse422
from ...models.post_webhook_response_500 import PostWebhookResponse500
from ...models.webhook_create import WebhookCreate
from typing import cast



def _get_kwargs(
    *,
    body: WebhookCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/webhook",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostWebhookResponse201 | PostWebhookResponse400 | PostWebhookResponse401 | PostWebhookResponse403 | PostWebhookResponse422 | PostWebhookResponse500 | None:
    if response.status_code == 201:
        response_201 = PostWebhookResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostWebhookResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostWebhookResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostWebhookResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostWebhookResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostWebhookResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostWebhookResponse201 | PostWebhookResponse400 | PostWebhookResponse401 | PostWebhookResponse403 | PostWebhookResponse422 | PostWebhookResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookCreate,

) -> Response[PostWebhookResponse201 | PostWebhookResponse400 | PostWebhookResponse401 | PostWebhookResponse403 | PostWebhookResponse422 | PostWebhookResponse500]:
    """ Creates a webhook in the application.

    Args:
        body (WebhookCreate): WebhookCreate defines a webhook creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostWebhookResponse201 | PostWebhookResponse400 | PostWebhookResponse401 | PostWebhookResponse403 | PostWebhookResponse422 | PostWebhookResponse500]
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
    body: WebhookCreate,

) -> PostWebhookResponse201 | PostWebhookResponse400 | PostWebhookResponse401 | PostWebhookResponse403 | PostWebhookResponse422 | PostWebhookResponse500 | None:
    """ Creates a webhook in the application.

    Args:
        body (WebhookCreate): WebhookCreate defines a webhook creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostWebhookResponse201 | PostWebhookResponse400 | PostWebhookResponse401 | PostWebhookResponse403 | PostWebhookResponse422 | PostWebhookResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookCreate,

) -> Response[PostWebhookResponse201 | PostWebhookResponse400 | PostWebhookResponse401 | PostWebhookResponse403 | PostWebhookResponse422 | PostWebhookResponse500]:
    """ Creates a webhook in the application.

    Args:
        body (WebhookCreate): WebhookCreate defines a webhook creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostWebhookResponse201 | PostWebhookResponse400 | PostWebhookResponse401 | PostWebhookResponse403 | PostWebhookResponse422 | PostWebhookResponse500]
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
    body: WebhookCreate,

) -> PostWebhookResponse201 | PostWebhookResponse400 | PostWebhookResponse401 | PostWebhookResponse403 | PostWebhookResponse422 | PostWebhookResponse500 | None:
    """ Creates a webhook in the application.

    Args:
        body (WebhookCreate): WebhookCreate defines a webhook creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostWebhookResponse201 | PostWebhookResponse400 | PostWebhookResponse401 | PostWebhookResponse403 | PostWebhookResponse422 | PostWebhookResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
