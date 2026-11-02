from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.webhook_manual_run import WebhookManualRun
from ...models.webhookpost_manual_run_project_cloud_rule_response_200 import WebhookpostManualRunProjectCloudRuleResponse200
from ...models.webhookpost_manual_run_project_cloud_rule_response_400 import WebhookpostManualRunProjectCloudRuleResponse400
from ...models.webhookpost_manual_run_project_cloud_rule_response_401 import WebhookpostManualRunProjectCloudRuleResponse401
from ...models.webhookpost_manual_run_project_cloud_rule_response_403 import WebhookpostManualRunProjectCloudRuleResponse403
from ...models.webhookpost_manual_run_project_cloud_rule_response_422 import WebhookpostManualRunProjectCloudRuleResponse422
from ...models.webhookpost_manual_run_project_cloud_rule_response_500 import WebhookpostManualRunProjectCloudRuleResponse500
from typing import cast



def _get_kwargs(
    *,
    body: WebhookManualRun,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/webhook/run",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WebhookpostManualRunProjectCloudRuleResponse200 | WebhookpostManualRunProjectCloudRuleResponse400 | WebhookpostManualRunProjectCloudRuleResponse401 | WebhookpostManualRunProjectCloudRuleResponse403 | WebhookpostManualRunProjectCloudRuleResponse422 | WebhookpostManualRunProjectCloudRuleResponse500 | None:
    if response.status_code == 200:
        response_200 = WebhookpostManualRunProjectCloudRuleResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = WebhookpostManualRunProjectCloudRuleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = WebhookpostManualRunProjectCloudRuleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = WebhookpostManualRunProjectCloudRuleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = WebhookpostManualRunProjectCloudRuleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = WebhookpostManualRunProjectCloudRuleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WebhookpostManualRunProjectCloudRuleResponse200 | WebhookpostManualRunProjectCloudRuleResponse400 | WebhookpostManualRunProjectCloudRuleResponse401 | WebhookpostManualRunProjectCloudRuleResponse403 | WebhookpostManualRunProjectCloudRuleResponse422 | WebhookpostManualRunProjectCloudRuleResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookManualRun,

) -> Response[WebhookpostManualRunProjectCloudRuleResponse200 | WebhookpostManualRunProjectCloudRuleResponse400 | WebhookpostManualRunProjectCloudRuleResponse401 | WebhookpostManualRunProjectCloudRuleResponse403 | WebhookpostManualRunProjectCloudRuleResponse422 | WebhookpostManualRunProjectCloudRuleResponse500]:
    """ Runs a webhook on a cloud rule and project.

    Args:
        body (WebhookManualRun): WebhookManualRun contains the fields required to run a webhook
            manually.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookpostManualRunProjectCloudRuleResponse200 | WebhookpostManualRunProjectCloudRuleResponse400 | WebhookpostManualRunProjectCloudRuleResponse401 | WebhookpostManualRunProjectCloudRuleResponse403 | WebhookpostManualRunProjectCloudRuleResponse422 | WebhookpostManualRunProjectCloudRuleResponse500]
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
    body: WebhookManualRun,

) -> WebhookpostManualRunProjectCloudRuleResponse200 | WebhookpostManualRunProjectCloudRuleResponse400 | WebhookpostManualRunProjectCloudRuleResponse401 | WebhookpostManualRunProjectCloudRuleResponse403 | WebhookpostManualRunProjectCloudRuleResponse422 | WebhookpostManualRunProjectCloudRuleResponse500 | None:
    """ Runs a webhook on a cloud rule and project.

    Args:
        body (WebhookManualRun): WebhookManualRun contains the fields required to run a webhook
            manually.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookpostManualRunProjectCloudRuleResponse200 | WebhookpostManualRunProjectCloudRuleResponse400 | WebhookpostManualRunProjectCloudRuleResponse401 | WebhookpostManualRunProjectCloudRuleResponse403 | WebhookpostManualRunProjectCloudRuleResponse422 | WebhookpostManualRunProjectCloudRuleResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookManualRun,

) -> Response[WebhookpostManualRunProjectCloudRuleResponse200 | WebhookpostManualRunProjectCloudRuleResponse400 | WebhookpostManualRunProjectCloudRuleResponse401 | WebhookpostManualRunProjectCloudRuleResponse403 | WebhookpostManualRunProjectCloudRuleResponse422 | WebhookpostManualRunProjectCloudRuleResponse500]:
    """ Runs a webhook on a cloud rule and project.

    Args:
        body (WebhookManualRun): WebhookManualRun contains the fields required to run a webhook
            manually.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookpostManualRunProjectCloudRuleResponse200 | WebhookpostManualRunProjectCloudRuleResponse400 | WebhookpostManualRunProjectCloudRuleResponse401 | WebhookpostManualRunProjectCloudRuleResponse403 | WebhookpostManualRunProjectCloudRuleResponse422 | WebhookpostManualRunProjectCloudRuleResponse500]
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
    body: WebhookManualRun,

) -> WebhookpostManualRunProjectCloudRuleResponse200 | WebhookpostManualRunProjectCloudRuleResponse400 | WebhookpostManualRunProjectCloudRuleResponse401 | WebhookpostManualRunProjectCloudRuleResponse403 | WebhookpostManualRunProjectCloudRuleResponse422 | WebhookpostManualRunProjectCloudRuleResponse500 | None:
    """ Runs a webhook on a cloud rule and project.

    Args:
        body (WebhookManualRun): WebhookManualRun contains the fields required to run a webhook
            manually.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookpostManualRunProjectCloudRuleResponse200 | WebhookpostManualRunProjectCloudRuleResponse400 | WebhookpostManualRunProjectCloudRuleResponse401 | WebhookpostManualRunProjectCloudRuleResponse403 | WebhookpostManualRunProjectCloudRuleResponse422 | WebhookpostManualRunProjectCloudRuleResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
