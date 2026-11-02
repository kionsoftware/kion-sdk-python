from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_start_cft_response_200 import PostStartCFTResponse200
from ...models.post_start_cft_response_400 import PostStartCFTResponse400
from ...models.post_start_cft_response_401 import PostStartCFTResponse401
from ...models.post_start_cft_response_403 import PostStartCFTResponse403
from ...models.post_start_cft_response_500 import PostStartCFTResponse500
from typing import cast



def _get_kwargs(
    id: int,
    cloud_rule_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account/{id}/cloud-rule/{cloud_rule_id}/start-cft".format(id=quote(str(id), safe=""),cloud_rule_id=quote(str(cloud_rule_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostStartCFTResponse200 | PostStartCFTResponse400 | PostStartCFTResponse401 | PostStartCFTResponse403 | PostStartCFTResponse500 | None:
    if response.status_code == 200:
        response_200 = PostStartCFTResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostStartCFTResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostStartCFTResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostStartCFTResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PostStartCFTResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostStartCFTResponse200 | PostStartCFTResponse400 | PostStartCFTResponse401 | PostStartCFTResponse403 | PostStartCFTResponse500]:
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

) -> Response[PostStartCFTResponse200 | PostStartCFTResponse400 | PostStartCFTResponse401 | PostStartCFTResponse403 | PostStartCFTResponse500]:
    """ Mark the cft as started for the account/cloud rule.

    Args:
        id (int):
        cloud_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostStartCFTResponse200 | PostStartCFTResponse400 | PostStartCFTResponse401 | PostStartCFTResponse403 | PostStartCFTResponse500]
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

) -> PostStartCFTResponse200 | PostStartCFTResponse400 | PostStartCFTResponse401 | PostStartCFTResponse403 | PostStartCFTResponse500 | None:
    """ Mark the cft as started for the account/cloud rule.

    Args:
        id (int):
        cloud_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostStartCFTResponse200 | PostStartCFTResponse400 | PostStartCFTResponse401 | PostStartCFTResponse403 | PostStartCFTResponse500
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

) -> Response[PostStartCFTResponse200 | PostStartCFTResponse400 | PostStartCFTResponse401 | PostStartCFTResponse403 | PostStartCFTResponse500]:
    """ Mark the cft as started for the account/cloud rule.

    Args:
        id (int):
        cloud_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostStartCFTResponse200 | PostStartCFTResponse400 | PostStartCFTResponse401 | PostStartCFTResponse403 | PostStartCFTResponse500]
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

) -> PostStartCFTResponse200 | PostStartCFTResponse400 | PostStartCFTResponse401 | PostStartCFTResponse403 | PostStartCFTResponse500 | None:
    """ Mark the cft as started for the account/cloud rule.

    Args:
        id (int):
        cloud_rule_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostStartCFTResponse200 | PostStartCFTResponse400 | PostStartCFTResponse401 | PostStartCFTResponse403 | PostStartCFTResponse500
     """


    return (await asyncio_detailed(
        id=id,
cloud_rule_id=cloud_rule_id,
client=client,

    )).parsed
