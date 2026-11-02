from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_cloud_rule_prewebhook_response_200 import DeleteCloudRulePrewebhookResponse200
from ...models.delete_cloud_rule_prewebhook_response_400 import DeleteCloudRulePrewebhookResponse400
from ...models.delete_cloud_rule_prewebhook_response_401 import DeleteCloudRulePrewebhookResponse401
from ...models.delete_cloud_rule_prewebhook_response_403 import DeleteCloudRulePrewebhookResponse403
from ...models.delete_cloud_rule_prewebhook_response_404 import DeleteCloudRulePrewebhookResponse404
from ...models.delete_cloud_rule_prewebhook_response_500 import DeleteCloudRulePrewebhookResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/cloud-rule/{id}/pre-webhook".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteCloudRulePrewebhookResponse200 | DeleteCloudRulePrewebhookResponse400 | DeleteCloudRulePrewebhookResponse401 | DeleteCloudRulePrewebhookResponse403 | DeleteCloudRulePrewebhookResponse404 | DeleteCloudRulePrewebhookResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteCloudRulePrewebhookResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteCloudRulePrewebhookResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteCloudRulePrewebhookResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteCloudRulePrewebhookResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteCloudRulePrewebhookResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteCloudRulePrewebhookResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteCloudRulePrewebhookResponse200 | DeleteCloudRulePrewebhookResponse400 | DeleteCloudRulePrewebhookResponse401 | DeleteCloudRulePrewebhookResponse403 | DeleteCloudRulePrewebhookResponse404 | DeleteCloudRulePrewebhookResponse500]:
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

) -> Response[DeleteCloudRulePrewebhookResponse200 | DeleteCloudRulePrewebhookResponse400 | DeleteCloudRulePrewebhookResponse401 | DeleteCloudRulePrewebhookResponse403 | DeleteCloudRulePrewebhookResponse404 | DeleteCloudRulePrewebhookResponse500]:
    """ Removes the pre webhook from a cloud rule in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCloudRulePrewebhookResponse200 | DeleteCloudRulePrewebhookResponse400 | DeleteCloudRulePrewebhookResponse401 | DeleteCloudRulePrewebhookResponse403 | DeleteCloudRulePrewebhookResponse404 | DeleteCloudRulePrewebhookResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteCloudRulePrewebhookResponse200 | DeleteCloudRulePrewebhookResponse400 | DeleteCloudRulePrewebhookResponse401 | DeleteCloudRulePrewebhookResponse403 | DeleteCloudRulePrewebhookResponse404 | DeleteCloudRulePrewebhookResponse500 | None:
    """ Removes the pre webhook from a cloud rule in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCloudRulePrewebhookResponse200 | DeleteCloudRulePrewebhookResponse400 | DeleteCloudRulePrewebhookResponse401 | DeleteCloudRulePrewebhookResponse403 | DeleteCloudRulePrewebhookResponse404 | DeleteCloudRulePrewebhookResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteCloudRulePrewebhookResponse200 | DeleteCloudRulePrewebhookResponse400 | DeleteCloudRulePrewebhookResponse401 | DeleteCloudRulePrewebhookResponse403 | DeleteCloudRulePrewebhookResponse404 | DeleteCloudRulePrewebhookResponse500]:
    """ Removes the pre webhook from a cloud rule in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCloudRulePrewebhookResponse200 | DeleteCloudRulePrewebhookResponse400 | DeleteCloudRulePrewebhookResponse401 | DeleteCloudRulePrewebhookResponse403 | DeleteCloudRulePrewebhookResponse404 | DeleteCloudRulePrewebhookResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteCloudRulePrewebhookResponse200 | DeleteCloudRulePrewebhookResponse400 | DeleteCloudRulePrewebhookResponse401 | DeleteCloudRulePrewebhookResponse403 | DeleteCloudRulePrewebhookResponse404 | DeleteCloudRulePrewebhookResponse500 | None:
    """ Removes the pre webhook from a cloud rule in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCloudRulePrewebhookResponse200 | DeleteCloudRulePrewebhookResponse400 | DeleteCloudRulePrewebhookResponse401 | DeleteCloudRulePrewebhookResponse403 | DeleteCloudRulePrewebhookResponse404 | DeleteCloudRulePrewebhookResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
