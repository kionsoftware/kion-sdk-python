from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_cloud_rule_labels_response_200 import GetCloudRuleLabelsResponse200
from ...models.get_cloud_rule_labels_response_400 import GetCloudRuleLabelsResponse400
from ...models.get_cloud_rule_labels_response_401 import GetCloudRuleLabelsResponse401
from ...models.get_cloud_rule_labels_response_403 import GetCloudRuleLabelsResponse403
from ...models.get_cloud_rule_labels_response_500 import GetCloudRuleLabelsResponse500
from typing import cast



def _get_kwargs(
    cloud_rule_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/cloud-rule/{cloud_rule_id}/labels".format(cloud_rule_id=quote(str(cloud_rule_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCloudRuleLabelsResponse200 | GetCloudRuleLabelsResponse400 | GetCloudRuleLabelsResponse401 | GetCloudRuleLabelsResponse403 | GetCloudRuleLabelsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCloudRuleLabelsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetCloudRuleLabelsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetCloudRuleLabelsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetCloudRuleLabelsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetCloudRuleLabelsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCloudRuleLabelsResponse200 | GetCloudRuleLabelsResponse400 | GetCloudRuleLabelsResponse401 | GetCloudRuleLabelsResponse403 | GetCloudRuleLabelsResponse500]:
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

) -> Response[GetCloudRuleLabelsResponse200 | GetCloudRuleLabelsResponse400 | GetCloudRuleLabelsResponse401 | GetCloudRuleLabelsResponse403 | GetCloudRuleLabelsResponse500]:
    """ Gets all labels associated with a given cloud rule ID.

    Args:
        cloud_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudRuleLabelsResponse200 | GetCloudRuleLabelsResponse400 | GetCloudRuleLabelsResponse401 | GetCloudRuleLabelsResponse403 | GetCloudRuleLabelsResponse500]
     """


    kwargs = _get_kwargs(
        cloud_rule_id=cloud_rule_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,

) -> GetCloudRuleLabelsResponse200 | GetCloudRuleLabelsResponse400 | GetCloudRuleLabelsResponse401 | GetCloudRuleLabelsResponse403 | GetCloudRuleLabelsResponse500 | None:
    """ Gets all labels associated with a given cloud rule ID.

    Args:
        cloud_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudRuleLabelsResponse200 | GetCloudRuleLabelsResponse400 | GetCloudRuleLabelsResponse401 | GetCloudRuleLabelsResponse403 | GetCloudRuleLabelsResponse500
     """


    return sync_detailed(
        cloud_rule_id=cloud_rule_id,
client=client,

    ).parsed

async def asyncio_detailed(
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetCloudRuleLabelsResponse200 | GetCloudRuleLabelsResponse400 | GetCloudRuleLabelsResponse401 | GetCloudRuleLabelsResponse403 | GetCloudRuleLabelsResponse500]:
    """ Gets all labels associated with a given cloud rule ID.

    Args:
        cloud_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudRuleLabelsResponse200 | GetCloudRuleLabelsResponse400 | GetCloudRuleLabelsResponse401 | GetCloudRuleLabelsResponse403 | GetCloudRuleLabelsResponse500]
     """


    kwargs = _get_kwargs(
        cloud_rule_id=cloud_rule_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,

) -> GetCloudRuleLabelsResponse200 | GetCloudRuleLabelsResponse400 | GetCloudRuleLabelsResponse401 | GetCloudRuleLabelsResponse403 | GetCloudRuleLabelsResponse500 | None:
    """ Gets all labels associated with a given cloud rule ID.

    Args:
        cloud_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudRuleLabelsResponse200 | GetCloudRuleLabelsResponse400 | GetCloudRuleLabelsResponse401 | GetCloudRuleLabelsResponse403 | GetCloudRuleLabelsResponse500
     """


    return (await asyncio_detailed(
        cloud_rule_id=cloud_rule_id,
client=client,

    )).parsed
