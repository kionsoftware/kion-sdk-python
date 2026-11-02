from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.associate_labels import AssociateLabels
from ...models.put_cloud_rule_labels_response_200 import PutCloudRuleLabelsResponse200
from ...models.put_cloud_rule_labels_response_400 import PutCloudRuleLabelsResponse400
from ...models.put_cloud_rule_labels_response_401 import PutCloudRuleLabelsResponse401
from ...models.put_cloud_rule_labels_response_404 import PutCloudRuleLabelsResponse404
from ...models.put_cloud_rule_labels_response_422 import PutCloudRuleLabelsResponse422
from ...models.put_cloud_rule_labels_response_500 import PutCloudRuleLabelsResponse500
from typing import cast



def _get_kwargs(
    cloud_rule_id: int,
    *,
    body: AssociateLabels,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/cloud-rule/{cloud_rule_id}/labels".format(cloud_rule_id=quote(str(cloud_rule_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutCloudRuleLabelsResponse200 | PutCloudRuleLabelsResponse400 | PutCloudRuleLabelsResponse401 | PutCloudRuleLabelsResponse404 | PutCloudRuleLabelsResponse422 | PutCloudRuleLabelsResponse500 | None:
    if response.status_code == 200:
        response_200 = PutCloudRuleLabelsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PutCloudRuleLabelsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PutCloudRuleLabelsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = PutCloudRuleLabelsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PutCloudRuleLabelsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PutCloudRuleLabelsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutCloudRuleLabelsResponse200 | PutCloudRuleLabelsResponse400 | PutCloudRuleLabelsResponse401 | PutCloudRuleLabelsResponse404 | PutCloudRuleLabelsResponse422 | PutCloudRuleLabelsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> Response[PutCloudRuleLabelsResponse200 | PutCloudRuleLabelsResponse400 | PutCloudRuleLabelsResponse401 | PutCloudRuleLabelsResponse404 | PutCloudRuleLabelsResponse422 | PutCloudRuleLabelsResponse500]:
    """ Replaces labels on the given cloud rule.

     This replaces labels on the given cloud rule with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        cloud_rule_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutCloudRuleLabelsResponse200 | PutCloudRuleLabelsResponse400 | PutCloudRuleLabelsResponse401 | PutCloudRuleLabelsResponse404 | PutCloudRuleLabelsResponse422 | PutCloudRuleLabelsResponse500]
     """


    kwargs = _get_kwargs(
        cloud_rule_id=cloud_rule_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> PutCloudRuleLabelsResponse200 | PutCloudRuleLabelsResponse400 | PutCloudRuleLabelsResponse401 | PutCloudRuleLabelsResponse404 | PutCloudRuleLabelsResponse422 | PutCloudRuleLabelsResponse500 | None:
    """ Replaces labels on the given cloud rule.

     This replaces labels on the given cloud rule with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        cloud_rule_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutCloudRuleLabelsResponse200 | PutCloudRuleLabelsResponse400 | PutCloudRuleLabelsResponse401 | PutCloudRuleLabelsResponse404 | PutCloudRuleLabelsResponse422 | PutCloudRuleLabelsResponse500
     """


    return sync_detailed(
        cloud_rule_id=cloud_rule_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> Response[PutCloudRuleLabelsResponse200 | PutCloudRuleLabelsResponse400 | PutCloudRuleLabelsResponse401 | PutCloudRuleLabelsResponse404 | PutCloudRuleLabelsResponse422 | PutCloudRuleLabelsResponse500]:
    """ Replaces labels on the given cloud rule.

     This replaces labels on the given cloud rule with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        cloud_rule_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutCloudRuleLabelsResponse200 | PutCloudRuleLabelsResponse400 | PutCloudRuleLabelsResponse401 | PutCloudRuleLabelsResponse404 | PutCloudRuleLabelsResponse422 | PutCloudRuleLabelsResponse500]
     """


    kwargs = _get_kwargs(
        cloud_rule_id=cloud_rule_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> PutCloudRuleLabelsResponse200 | PutCloudRuleLabelsResponse400 | PutCloudRuleLabelsResponse401 | PutCloudRuleLabelsResponse404 | PutCloudRuleLabelsResponse422 | PutCloudRuleLabelsResponse500 | None:
    """ Replaces labels on the given cloud rule.

     This replaces labels on the given cloud rule with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        cloud_rule_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutCloudRuleLabelsResponse200 | PutCloudRuleLabelsResponse400 | PutCloudRuleLabelsResponse401 | PutCloudRuleLabelsResponse404 | PutCloudRuleLabelsResponse422 | PutCloudRuleLabelsResponse500
     """


    return (await asyncio_detailed(
        cloud_rule_id=cloud_rule_id,
client=client,
body=body,

    )).parsed
