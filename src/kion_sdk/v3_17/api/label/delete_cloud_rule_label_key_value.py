from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_cloud_rule_label_key_value_response_200 import DeleteCloudRuleLabelKeyValueResponse200
from ...models.delete_cloud_rule_label_key_value_response_400 import DeleteCloudRuleLabelKeyValueResponse400
from ...models.delete_cloud_rule_label_key_value_response_401 import DeleteCloudRuleLabelKeyValueResponse401
from ...models.delete_cloud_rule_label_key_value_response_404 import DeleteCloudRuleLabelKeyValueResponse404
from ...models.delete_cloud_rule_label_key_value_response_422 import DeleteCloudRuleLabelKeyValueResponse422
from ...models.delete_cloud_rule_label_key_value_response_500 import DeleteCloudRuleLabelKeyValueResponse500
from typing import cast



def _get_kwargs(
    cloud_rule_id: int,
    *,
    key: str,
    value: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["key"] = key

    params["value"] = value


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/cloud-rule/{cloud_rule_id}/labels".format(cloud_rule_id=quote(str(cloud_rule_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteCloudRuleLabelKeyValueResponse200 | DeleteCloudRuleLabelKeyValueResponse400 | DeleteCloudRuleLabelKeyValueResponse401 | DeleteCloudRuleLabelKeyValueResponse404 | DeleteCloudRuleLabelKeyValueResponse422 | DeleteCloudRuleLabelKeyValueResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteCloudRuleLabelKeyValueResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteCloudRuleLabelKeyValueResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteCloudRuleLabelKeyValueResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = DeleteCloudRuleLabelKeyValueResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteCloudRuleLabelKeyValueResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteCloudRuleLabelKeyValueResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteCloudRuleLabelKeyValueResponse200 | DeleteCloudRuleLabelKeyValueResponse400 | DeleteCloudRuleLabelKeyValueResponse401 | DeleteCloudRuleLabelKeyValueResponse404 | DeleteCloudRuleLabelKeyValueResponse422 | DeleteCloudRuleLabelKeyValueResponse500]:
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
    key: str,
    value: str,

) -> Response[DeleteCloudRuleLabelKeyValueResponse200 | DeleteCloudRuleLabelKeyValueResponse400 | DeleteCloudRuleLabelKeyValueResponse401 | DeleteCloudRuleLabelKeyValueResponse404 | DeleteCloudRuleLabelKeyValueResponse422 | DeleteCloudRuleLabelKeyValueResponse500]:
    """ Removes a label from the given cloud rule by key/value pair.

     You must pass a single key/value pair via the query string, for example:
    <pre>DELETE /v3/cloud-rule/{cloud_rule_id}/labels?key=Department&value=Engineering</pre>

    Args:
        cloud_rule_id (int):
        key (str):
        value (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCloudRuleLabelKeyValueResponse200 | DeleteCloudRuleLabelKeyValueResponse400 | DeleteCloudRuleLabelKeyValueResponse401 | DeleteCloudRuleLabelKeyValueResponse404 | DeleteCloudRuleLabelKeyValueResponse422 | DeleteCloudRuleLabelKeyValueResponse500]
     """


    kwargs = _get_kwargs(
        cloud_rule_id=cloud_rule_id,
key=key,
value=value,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,
    key: str,
    value: str,

) -> DeleteCloudRuleLabelKeyValueResponse200 | DeleteCloudRuleLabelKeyValueResponse400 | DeleteCloudRuleLabelKeyValueResponse401 | DeleteCloudRuleLabelKeyValueResponse404 | DeleteCloudRuleLabelKeyValueResponse422 | DeleteCloudRuleLabelKeyValueResponse500 | None:
    """ Removes a label from the given cloud rule by key/value pair.

     You must pass a single key/value pair via the query string, for example:
    <pre>DELETE /v3/cloud-rule/{cloud_rule_id}/labels?key=Department&value=Engineering</pre>

    Args:
        cloud_rule_id (int):
        key (str):
        value (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCloudRuleLabelKeyValueResponse200 | DeleteCloudRuleLabelKeyValueResponse400 | DeleteCloudRuleLabelKeyValueResponse401 | DeleteCloudRuleLabelKeyValueResponse404 | DeleteCloudRuleLabelKeyValueResponse422 | DeleteCloudRuleLabelKeyValueResponse500
     """


    return sync_detailed(
        cloud_rule_id=cloud_rule_id,
client=client,
key=key,
value=value,

    ).parsed

async def asyncio_detailed(
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,
    key: str,
    value: str,

) -> Response[DeleteCloudRuleLabelKeyValueResponse200 | DeleteCloudRuleLabelKeyValueResponse400 | DeleteCloudRuleLabelKeyValueResponse401 | DeleteCloudRuleLabelKeyValueResponse404 | DeleteCloudRuleLabelKeyValueResponse422 | DeleteCloudRuleLabelKeyValueResponse500]:
    """ Removes a label from the given cloud rule by key/value pair.

     You must pass a single key/value pair via the query string, for example:
    <pre>DELETE /v3/cloud-rule/{cloud_rule_id}/labels?key=Department&value=Engineering</pre>

    Args:
        cloud_rule_id (int):
        key (str):
        value (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCloudRuleLabelKeyValueResponse200 | DeleteCloudRuleLabelKeyValueResponse400 | DeleteCloudRuleLabelKeyValueResponse401 | DeleteCloudRuleLabelKeyValueResponse404 | DeleteCloudRuleLabelKeyValueResponse422 | DeleteCloudRuleLabelKeyValueResponse500]
     """


    kwargs = _get_kwargs(
        cloud_rule_id=cloud_rule_id,
key=key,
value=value,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,
    key: str,
    value: str,

) -> DeleteCloudRuleLabelKeyValueResponse200 | DeleteCloudRuleLabelKeyValueResponse400 | DeleteCloudRuleLabelKeyValueResponse401 | DeleteCloudRuleLabelKeyValueResponse404 | DeleteCloudRuleLabelKeyValueResponse422 | DeleteCloudRuleLabelKeyValueResponse500 | None:
    """ Removes a label from the given cloud rule by key/value pair.

     You must pass a single key/value pair via the query string, for example:
    <pre>DELETE /v3/cloud-rule/{cloud_rule_id}/labels?key=Department&value=Engineering</pre>

    Args:
        cloud_rule_id (int):
        key (str):
        value (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCloudRuleLabelKeyValueResponse200 | DeleteCloudRuleLabelKeyValueResponse400 | DeleteCloudRuleLabelKeyValueResponse401 | DeleteCloudRuleLabelKeyValueResponse404 | DeleteCloudRuleLabelKeyValueResponse422 | DeleteCloudRuleLabelKeyValueResponse500
     """


    return (await asyncio_detailed(
        cloud_rule_id=cloud_rule_id,
client=client,
key=key,
value=value,

    )).parsed
