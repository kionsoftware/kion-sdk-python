from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cloud_rule_associations import CloudRuleAssociations
from ...models.post_cloud_rule_associations_response_200 import PostCloudRuleAssociationsResponse200
from ...models.post_cloud_rule_associations_response_400 import PostCloudRuleAssociationsResponse400
from ...models.post_cloud_rule_associations_response_401 import PostCloudRuleAssociationsResponse401
from ...models.post_cloud_rule_associations_response_403 import PostCloudRuleAssociationsResponse403
from ...models.post_cloud_rule_associations_response_404 import PostCloudRuleAssociationsResponse404
from ...models.post_cloud_rule_associations_response_422 import PostCloudRuleAssociationsResponse422
from ...models.post_cloud_rule_associations_response_500 import PostCloudRuleAssociationsResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: CloudRuleAssociations,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/cloud-rule/{id}/association".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostCloudRuleAssociationsResponse200 | PostCloudRuleAssociationsResponse400 | PostCloudRuleAssociationsResponse401 | PostCloudRuleAssociationsResponse403 | PostCloudRuleAssociationsResponse404 | PostCloudRuleAssociationsResponse422 | PostCloudRuleAssociationsResponse500 | None:
    if response.status_code == 200:
        response_200 = PostCloudRuleAssociationsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostCloudRuleAssociationsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostCloudRuleAssociationsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostCloudRuleAssociationsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostCloudRuleAssociationsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PostCloudRuleAssociationsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostCloudRuleAssociationsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostCloudRuleAssociationsResponse200 | PostCloudRuleAssociationsResponse400 | PostCloudRuleAssociationsResponse401 | PostCloudRuleAssociationsResponse403 | PostCloudRuleAssociationsResponse404 | PostCloudRuleAssociationsResponse422 | PostCloudRuleAssociationsResponse500]:
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
    body: CloudRuleAssociations,

) -> Response[PostCloudRuleAssociationsResponse200 | PostCloudRuleAssociationsResponse400 | PostCloudRuleAssociationsResponse401 | PostCloudRuleAssociationsResponse403 | PostCloudRuleAssociationsResponse404 | PostCloudRuleAssociationsResponse422 | PostCloudRuleAssociationsResponse500]:
    """ Adds associations to a cloud rule in the application.

    Args:
        id (int):
        body (CloudRuleAssociations): CloudRuleAssociations defines a Cloud Rule association
            update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCloudRuleAssociationsResponse200 | PostCloudRuleAssociationsResponse400 | PostCloudRuleAssociationsResponse401 | PostCloudRuleAssociationsResponse403 | PostCloudRuleAssociationsResponse404 | PostCloudRuleAssociationsResponse422 | PostCloudRuleAssociationsResponse500]
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
    body: CloudRuleAssociations,

) -> PostCloudRuleAssociationsResponse200 | PostCloudRuleAssociationsResponse400 | PostCloudRuleAssociationsResponse401 | PostCloudRuleAssociationsResponse403 | PostCloudRuleAssociationsResponse404 | PostCloudRuleAssociationsResponse422 | PostCloudRuleAssociationsResponse500 | None:
    """ Adds associations to a cloud rule in the application.

    Args:
        id (int):
        body (CloudRuleAssociations): CloudRuleAssociations defines a Cloud Rule association
            update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCloudRuleAssociationsResponse200 | PostCloudRuleAssociationsResponse400 | PostCloudRuleAssociationsResponse401 | PostCloudRuleAssociationsResponse403 | PostCloudRuleAssociationsResponse404 | PostCloudRuleAssociationsResponse422 | PostCloudRuleAssociationsResponse500
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
    body: CloudRuleAssociations,

) -> Response[PostCloudRuleAssociationsResponse200 | PostCloudRuleAssociationsResponse400 | PostCloudRuleAssociationsResponse401 | PostCloudRuleAssociationsResponse403 | PostCloudRuleAssociationsResponse404 | PostCloudRuleAssociationsResponse422 | PostCloudRuleAssociationsResponse500]:
    """ Adds associations to a cloud rule in the application.

    Args:
        id (int):
        body (CloudRuleAssociations): CloudRuleAssociations defines a Cloud Rule association
            update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCloudRuleAssociationsResponse200 | PostCloudRuleAssociationsResponse400 | PostCloudRuleAssociationsResponse401 | PostCloudRuleAssociationsResponse403 | PostCloudRuleAssociationsResponse404 | PostCloudRuleAssociationsResponse422 | PostCloudRuleAssociationsResponse500]
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
    body: CloudRuleAssociations,

) -> PostCloudRuleAssociationsResponse200 | PostCloudRuleAssociationsResponse400 | PostCloudRuleAssociationsResponse401 | PostCloudRuleAssociationsResponse403 | PostCloudRuleAssociationsResponse404 | PostCloudRuleAssociationsResponse422 | PostCloudRuleAssociationsResponse500 | None:
    """ Adds associations to a cloud rule in the application.

    Args:
        id (int):
        body (CloudRuleAssociations): CloudRuleAssociations defines a Cloud Rule association
            update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCloudRuleAssociationsResponse200 | PostCloudRuleAssociationsResponse400 | PostCloudRuleAssociationsResponse401 | PostCloudRuleAssociationsResponse403 | PostCloudRuleAssociationsResponse404 | PostCloudRuleAssociationsResponse422 | PostCloudRuleAssociationsResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
