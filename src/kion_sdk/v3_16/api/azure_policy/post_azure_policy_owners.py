from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.azure_policy_definition_owners import AzurePolicyDefinitionOwners
from ...models.post_azure_policy_owners_response_200 import PostAzurePolicyOwnersResponse200
from ...models.post_azure_policy_owners_response_400 import PostAzurePolicyOwnersResponse400
from ...models.post_azure_policy_owners_response_401 import PostAzurePolicyOwnersResponse401
from ...models.post_azure_policy_owners_response_403 import PostAzurePolicyOwnersResponse403
from ...models.post_azure_policy_owners_response_422 import PostAzurePolicyOwnersResponse422
from ...models.post_azure_policy_owners_response_500 import PostAzurePolicyOwnersResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: AzurePolicyDefinitionOwners | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/azure-policy/{id}/owner".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAzurePolicyOwnersResponse200 | PostAzurePolicyOwnersResponse400 | PostAzurePolicyOwnersResponse401 | PostAzurePolicyOwnersResponse403 | PostAzurePolicyOwnersResponse422 | PostAzurePolicyOwnersResponse500 | None:
    if response.status_code == 200:
        response_200 = PostAzurePolicyOwnersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostAzurePolicyOwnersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAzurePolicyOwnersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAzurePolicyOwnersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAzurePolicyOwnersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAzurePolicyOwnersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAzurePolicyOwnersResponse200 | PostAzurePolicyOwnersResponse400 | PostAzurePolicyOwnersResponse401 | PostAzurePolicyOwnersResponse403 | PostAzurePolicyOwnersResponse422 | PostAzurePolicyOwnersResponse500]:
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
    body: AzurePolicyDefinitionOwners | Unset = UNSET,

) -> Response[PostAzurePolicyOwnersResponse200 | PostAzurePolicyOwnersResponse400 | PostAzurePolicyOwnersResponse401 | PostAzurePolicyOwnersResponse403 | PostAzurePolicyOwnersResponse422 | PostAzurePolicyOwnersResponse500]:
    """ Adds new user and/or group owners to azure policy definitions.

    Args:
        id (int):
        body (AzurePolicyDefinitionOwners | Unset): AzurePolicyDefinitionOwners is a payload for
            updating the users and groups that own an azure policy definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAzurePolicyOwnersResponse200 | PostAzurePolicyOwnersResponse400 | PostAzurePolicyOwnersResponse401 | PostAzurePolicyOwnersResponse403 | PostAzurePolicyOwnersResponse422 | PostAzurePolicyOwnersResponse500]
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
    body: AzurePolicyDefinitionOwners | Unset = UNSET,

) -> PostAzurePolicyOwnersResponse200 | PostAzurePolicyOwnersResponse400 | PostAzurePolicyOwnersResponse401 | PostAzurePolicyOwnersResponse403 | PostAzurePolicyOwnersResponse422 | PostAzurePolicyOwnersResponse500 | None:
    """ Adds new user and/or group owners to azure policy definitions.

    Args:
        id (int):
        body (AzurePolicyDefinitionOwners | Unset): AzurePolicyDefinitionOwners is a payload for
            updating the users and groups that own an azure policy definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAzurePolicyOwnersResponse200 | PostAzurePolicyOwnersResponse400 | PostAzurePolicyOwnersResponse401 | PostAzurePolicyOwnersResponse403 | PostAzurePolicyOwnersResponse422 | PostAzurePolicyOwnersResponse500
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
    body: AzurePolicyDefinitionOwners | Unset = UNSET,

) -> Response[PostAzurePolicyOwnersResponse200 | PostAzurePolicyOwnersResponse400 | PostAzurePolicyOwnersResponse401 | PostAzurePolicyOwnersResponse403 | PostAzurePolicyOwnersResponse422 | PostAzurePolicyOwnersResponse500]:
    """ Adds new user and/or group owners to azure policy definitions.

    Args:
        id (int):
        body (AzurePolicyDefinitionOwners | Unset): AzurePolicyDefinitionOwners is a payload for
            updating the users and groups that own an azure policy definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAzurePolicyOwnersResponse200 | PostAzurePolicyOwnersResponse400 | PostAzurePolicyOwnersResponse401 | PostAzurePolicyOwnersResponse403 | PostAzurePolicyOwnersResponse422 | PostAzurePolicyOwnersResponse500]
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
    body: AzurePolicyDefinitionOwners | Unset = UNSET,

) -> PostAzurePolicyOwnersResponse200 | PostAzurePolicyOwnersResponse400 | PostAzurePolicyOwnersResponse401 | PostAzurePolicyOwnersResponse403 | PostAzurePolicyOwnersResponse422 | PostAzurePolicyOwnersResponse500 | None:
    """ Adds new user and/or group owners to azure policy definitions.

    Args:
        id (int):
        body (AzurePolicyDefinitionOwners | Unset): AzurePolicyDefinitionOwners is a payload for
            updating the users and groups that own an azure policy definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAzurePolicyOwnersResponse200 | PostAzurePolicyOwnersResponse400 | PostAzurePolicyOwnersResponse401 | PostAzurePolicyOwnersResponse403 | PostAzurePolicyOwnersResponse422 | PostAzurePolicyOwnersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
