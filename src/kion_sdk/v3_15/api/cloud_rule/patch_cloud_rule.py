from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cloud_rule_update import CloudRuleUpdate
from ...models.patch_cloud_rule_response_200 import PatchCloudRuleResponse200
from ...models.patch_cloud_rule_response_400 import PatchCloudRuleResponse400
from ...models.patch_cloud_rule_response_401 import PatchCloudRuleResponse401
from ...models.patch_cloud_rule_response_403 import PatchCloudRuleResponse403
from ...models.patch_cloud_rule_response_404 import PatchCloudRuleResponse404
from ...models.patch_cloud_rule_response_422 import PatchCloudRuleResponse422
from ...models.patch_cloud_rule_response_500 import PatchCloudRuleResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: CloudRuleUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/cloud-rule/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchCloudRuleResponse200 | PatchCloudRuleResponse400 | PatchCloudRuleResponse401 | PatchCloudRuleResponse403 | PatchCloudRuleResponse404 | PatchCloudRuleResponse422 | PatchCloudRuleResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchCloudRuleResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchCloudRuleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchCloudRuleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchCloudRuleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchCloudRuleResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchCloudRuleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchCloudRuleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchCloudRuleResponse200 | PatchCloudRuleResponse400 | PatchCloudRuleResponse401 | PatchCloudRuleResponse403 | PatchCloudRuleResponse404 | PatchCloudRuleResponse422 | PatchCloudRuleResponse500]:
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
    body: CloudRuleUpdate,

) -> Response[PatchCloudRuleResponse200 | PatchCloudRuleResponse400 | PatchCloudRuleResponse401 | PatchCloudRuleResponse403 | PatchCloudRuleResponse404 | PatchCloudRuleResponse422 | PatchCloudRuleResponse500]:
    """ Updates a cloud rule in the application.

    Args:
        id (int):
        body (CloudRuleUpdate): CloudRuleUpdate defines a Cloud Rule update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchCloudRuleResponse200 | PatchCloudRuleResponse400 | PatchCloudRuleResponse401 | PatchCloudRuleResponse403 | PatchCloudRuleResponse404 | PatchCloudRuleResponse422 | PatchCloudRuleResponse500]
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
    body: CloudRuleUpdate,

) -> PatchCloudRuleResponse200 | PatchCloudRuleResponse400 | PatchCloudRuleResponse401 | PatchCloudRuleResponse403 | PatchCloudRuleResponse404 | PatchCloudRuleResponse422 | PatchCloudRuleResponse500 | None:
    """ Updates a cloud rule in the application.

    Args:
        id (int):
        body (CloudRuleUpdate): CloudRuleUpdate defines a Cloud Rule update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchCloudRuleResponse200 | PatchCloudRuleResponse400 | PatchCloudRuleResponse401 | PatchCloudRuleResponse403 | PatchCloudRuleResponse404 | PatchCloudRuleResponse422 | PatchCloudRuleResponse500
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
    body: CloudRuleUpdate,

) -> Response[PatchCloudRuleResponse200 | PatchCloudRuleResponse400 | PatchCloudRuleResponse401 | PatchCloudRuleResponse403 | PatchCloudRuleResponse404 | PatchCloudRuleResponse422 | PatchCloudRuleResponse500]:
    """ Updates a cloud rule in the application.

    Args:
        id (int):
        body (CloudRuleUpdate): CloudRuleUpdate defines a Cloud Rule update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchCloudRuleResponse200 | PatchCloudRuleResponse400 | PatchCloudRuleResponse401 | PatchCloudRuleResponse403 | PatchCloudRuleResponse404 | PatchCloudRuleResponse422 | PatchCloudRuleResponse500]
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
    body: CloudRuleUpdate,

) -> PatchCloudRuleResponse200 | PatchCloudRuleResponse400 | PatchCloudRuleResponse401 | PatchCloudRuleResponse403 | PatchCloudRuleResponse404 | PatchCloudRuleResponse422 | PatchCloudRuleResponse500 | None:
    """ Updates a cloud rule in the application.

    Args:
        id (int):
        body (CloudRuleUpdate): CloudRuleUpdate defines a Cloud Rule update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchCloudRuleResponse200 | PatchCloudRuleResponse400 | PatchCloudRuleResponse401 | PatchCloudRuleResponse403 | PatchCloudRuleResponse404 | PatchCloudRuleResponse422 | PatchCloudRuleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
