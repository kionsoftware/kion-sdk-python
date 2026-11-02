from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.car_restricted_entities import CARRestrictedEntities
from ...models.iam_policy_remove_car_restricted_entities_response_200 import IAMPolicyRemoveCARRestrictedEntitiesResponse200
from ...models.iam_policy_remove_car_restricted_entities_response_400 import IAMPolicyRemoveCARRestrictedEntitiesResponse400
from ...models.iam_policy_remove_car_restricted_entities_response_401 import IAMPolicyRemoveCARRestrictedEntitiesResponse401
from ...models.iam_policy_remove_car_restricted_entities_response_403 import IAMPolicyRemoveCARRestrictedEntitiesResponse403
from ...models.iam_policy_remove_car_restricted_entities_response_404 import IAMPolicyRemoveCARRestrictedEntitiesResponse404
from ...models.iam_policy_remove_car_restricted_entities_response_422 import IAMPolicyRemoveCARRestrictedEntitiesResponse422
from ...models.iam_policy_remove_car_restricted_entities_response_500 import IAMPolicyRemoveCARRestrictedEntitiesResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: CARRestrictedEntities,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/iam-policy/{id}/car-restricted-entities".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IAMPolicyRemoveCARRestrictedEntitiesResponse200 | IAMPolicyRemoveCARRestrictedEntitiesResponse400 | IAMPolicyRemoveCARRestrictedEntitiesResponse401 | IAMPolicyRemoveCARRestrictedEntitiesResponse403 | IAMPolicyRemoveCARRestrictedEntitiesResponse404 | IAMPolicyRemoveCARRestrictedEntitiesResponse422 | IAMPolicyRemoveCARRestrictedEntitiesResponse500 | None:
    if response.status_code == 200:
        response_200 = IAMPolicyRemoveCARRestrictedEntitiesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = IAMPolicyRemoveCARRestrictedEntitiesResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = IAMPolicyRemoveCARRestrictedEntitiesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = IAMPolicyRemoveCARRestrictedEntitiesResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = IAMPolicyRemoveCARRestrictedEntitiesResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = IAMPolicyRemoveCARRestrictedEntitiesResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = IAMPolicyRemoveCARRestrictedEntitiesResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IAMPolicyRemoveCARRestrictedEntitiesResponse200 | IAMPolicyRemoveCARRestrictedEntitiesResponse400 | IAMPolicyRemoveCARRestrictedEntitiesResponse401 | IAMPolicyRemoveCARRestrictedEntitiesResponse403 | IAMPolicyRemoveCARRestrictedEntitiesResponse404 | IAMPolicyRemoveCARRestrictedEntitiesResponse422 | IAMPolicyRemoveCARRestrictedEntitiesResponse500]:
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
    body: CARRestrictedEntities,

) -> Response[IAMPolicyRemoveCARRestrictedEntitiesResponse200 | IAMPolicyRemoveCARRestrictedEntitiesResponse400 | IAMPolicyRemoveCARRestrictedEntitiesResponse401 | IAMPolicyRemoveCARRestrictedEntitiesResponse403 | IAMPolicyRemoveCARRestrictedEntitiesResponse404 | IAMPolicyRemoveCARRestrictedEntitiesResponse422 | IAMPolicyRemoveCARRestrictedEntitiesResponse500]:
    """ Removes users and groups that were able to use the IAM policy on a Cloud Access Role.

    Args:
        id (int):
        body (CARRestrictedEntities): CARRestrictedEntities defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IAMPolicyRemoveCARRestrictedEntitiesResponse200 | IAMPolicyRemoveCARRestrictedEntitiesResponse400 | IAMPolicyRemoveCARRestrictedEntitiesResponse401 | IAMPolicyRemoveCARRestrictedEntitiesResponse403 | IAMPolicyRemoveCARRestrictedEntitiesResponse404 | IAMPolicyRemoveCARRestrictedEntitiesResponse422 | IAMPolicyRemoveCARRestrictedEntitiesResponse500]
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
    body: CARRestrictedEntities,

) -> IAMPolicyRemoveCARRestrictedEntitiesResponse200 | IAMPolicyRemoveCARRestrictedEntitiesResponse400 | IAMPolicyRemoveCARRestrictedEntitiesResponse401 | IAMPolicyRemoveCARRestrictedEntitiesResponse403 | IAMPolicyRemoveCARRestrictedEntitiesResponse404 | IAMPolicyRemoveCARRestrictedEntitiesResponse422 | IAMPolicyRemoveCARRestrictedEntitiesResponse500 | None:
    """ Removes users and groups that were able to use the IAM policy on a Cloud Access Role.

    Args:
        id (int):
        body (CARRestrictedEntities): CARRestrictedEntities defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IAMPolicyRemoveCARRestrictedEntitiesResponse200 | IAMPolicyRemoveCARRestrictedEntitiesResponse400 | IAMPolicyRemoveCARRestrictedEntitiesResponse401 | IAMPolicyRemoveCARRestrictedEntitiesResponse403 | IAMPolicyRemoveCARRestrictedEntitiesResponse404 | IAMPolicyRemoveCARRestrictedEntitiesResponse422 | IAMPolicyRemoveCARRestrictedEntitiesResponse500
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
    body: CARRestrictedEntities,

) -> Response[IAMPolicyRemoveCARRestrictedEntitiesResponse200 | IAMPolicyRemoveCARRestrictedEntitiesResponse400 | IAMPolicyRemoveCARRestrictedEntitiesResponse401 | IAMPolicyRemoveCARRestrictedEntitiesResponse403 | IAMPolicyRemoveCARRestrictedEntitiesResponse404 | IAMPolicyRemoveCARRestrictedEntitiesResponse422 | IAMPolicyRemoveCARRestrictedEntitiesResponse500]:
    """ Removes users and groups that were able to use the IAM policy on a Cloud Access Role.

    Args:
        id (int):
        body (CARRestrictedEntities): CARRestrictedEntities defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IAMPolicyRemoveCARRestrictedEntitiesResponse200 | IAMPolicyRemoveCARRestrictedEntitiesResponse400 | IAMPolicyRemoveCARRestrictedEntitiesResponse401 | IAMPolicyRemoveCARRestrictedEntitiesResponse403 | IAMPolicyRemoveCARRestrictedEntitiesResponse404 | IAMPolicyRemoveCARRestrictedEntitiesResponse422 | IAMPolicyRemoveCARRestrictedEntitiesResponse500]
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
    body: CARRestrictedEntities,

) -> IAMPolicyRemoveCARRestrictedEntitiesResponse200 | IAMPolicyRemoveCARRestrictedEntitiesResponse400 | IAMPolicyRemoveCARRestrictedEntitiesResponse401 | IAMPolicyRemoveCARRestrictedEntitiesResponse403 | IAMPolicyRemoveCARRestrictedEntitiesResponse404 | IAMPolicyRemoveCARRestrictedEntitiesResponse422 | IAMPolicyRemoveCARRestrictedEntitiesResponse500 | None:
    """ Removes users and groups that were able to use the IAM policy on a Cloud Access Role.

    Args:
        id (int):
        body (CARRestrictedEntities): CARRestrictedEntities defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IAMPolicyRemoveCARRestrictedEntitiesResponse200 | IAMPolicyRemoveCARRestrictedEntitiesResponse400 | IAMPolicyRemoveCARRestrictedEntitiesResponse401 | IAMPolicyRemoveCARRestrictedEntitiesResponse403 | IAMPolicyRemoveCARRestrictedEntitiesResponse404 | IAMPolicyRemoveCARRestrictedEntitiesResponse422 | IAMPolicyRemoveCARRestrictedEntitiesResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
