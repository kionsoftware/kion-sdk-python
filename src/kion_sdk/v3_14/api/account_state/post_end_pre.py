from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_end_pre_response_200 import PostEndPreResponse200
from ...models.post_end_pre_response_400 import PostEndPreResponse400
from ...models.post_end_pre_response_401 import PostEndPreResponse401
from ...models.post_end_pre_response_403 import PostEndPreResponse403
from ...models.post_end_pre_response_500 import PostEndPreResponse500
from typing import cast



def _get_kwargs(
    id: int,
    cloud_rule_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account/{id}/cloud-rule/{cloud_rule_id}/end-pre-webhook".format(id=quote(str(id), safe=""),cloud_rule_id=quote(str(cloud_rule_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostEndPreResponse200 | PostEndPreResponse400 | PostEndPreResponse401 | PostEndPreResponse403 | PostEndPreResponse500 | None:
    if response.status_code == 200:
        response_200 = PostEndPreResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostEndPreResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostEndPreResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostEndPreResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PostEndPreResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostEndPreResponse200 | PostEndPreResponse400 | PostEndPreResponse401 | PostEndPreResponse403 | PostEndPreResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[PostEndPreResponse200 | PostEndPreResponse400 | PostEndPreResponse401 | PostEndPreResponse403 | PostEndPreResponse500]:
    """ Mark the pre webhook as ended for the account/cloud rule.

    Args:
        id (int):
        cloud_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostEndPreResponse200 | PostEndPreResponse400 | PostEndPreResponse401 | PostEndPreResponse403 | PostEndPreResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
cloud_rule_id=cloud_rule_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,

) -> PostEndPreResponse200 | PostEndPreResponse400 | PostEndPreResponse401 | PostEndPreResponse403 | PostEndPreResponse500 | None:
    """ Mark the pre webhook as ended for the account/cloud rule.

    Args:
        id (int):
        cloud_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostEndPreResponse200 | PostEndPreResponse400 | PostEndPreResponse401 | PostEndPreResponse403 | PostEndPreResponse500
     """


    return sync_detailed(
        id=id,
cloud_rule_id=cloud_rule_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[PostEndPreResponse200 | PostEndPreResponse400 | PostEndPreResponse401 | PostEndPreResponse403 | PostEndPreResponse500]:
    """ Mark the pre webhook as ended for the account/cloud rule.

    Args:
        id (int):
        cloud_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostEndPreResponse200 | PostEndPreResponse400 | PostEndPreResponse401 | PostEndPreResponse403 | PostEndPreResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
cloud_rule_id=cloud_rule_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    cloud_rule_id: int,
    *,
    client: AuthenticatedClient,

) -> PostEndPreResponse200 | PostEndPreResponse400 | PostEndPreResponse401 | PostEndPreResponse403 | PostEndPreResponse500 | None:
    """ Mark the pre webhook as ended for the account/cloud rule.

    Args:
        id (int):
        cloud_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostEndPreResponse200 | PostEndPreResponse400 | PostEndPreResponse401 | PostEndPreResponse403 | PostEndPreResponse500
     """


    return (await asyncio_detailed(
        id=id,
cloud_rule_id=cloud_rule_id,
client=client,

    )).parsed
