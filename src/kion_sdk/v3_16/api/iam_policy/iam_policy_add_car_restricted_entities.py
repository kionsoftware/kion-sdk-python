from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.car_restricted_entities import CARRestrictedEntities
from ...models.iam_policy_add_car_restricted_entities_response_200 import IAMPolicyAddCARRestrictedEntitiesResponse200
from ...models.iam_policy_add_car_restricted_entities_response_400 import IAMPolicyAddCARRestrictedEntitiesResponse400
from ...models.iam_policy_add_car_restricted_entities_response_401 import IAMPolicyAddCARRestrictedEntitiesResponse401
from ...models.iam_policy_add_car_restricted_entities_response_403 import IAMPolicyAddCARRestrictedEntitiesResponse403
from ...models.iam_policy_add_car_restricted_entities_response_404 import IAMPolicyAddCARRestrictedEntitiesResponse404
from ...models.iam_policy_add_car_restricted_entities_response_422 import IAMPolicyAddCARRestrictedEntitiesResponse422
from ...models.iam_policy_add_car_restricted_entities_response_500 import IAMPolicyAddCARRestrictedEntitiesResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: CARRestrictedEntities,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/iam-policy/{id}/car-restricted-entities".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IAMPolicyAddCARRestrictedEntitiesResponse200 | IAMPolicyAddCARRestrictedEntitiesResponse400 | IAMPolicyAddCARRestrictedEntitiesResponse401 | IAMPolicyAddCARRestrictedEntitiesResponse403 | IAMPolicyAddCARRestrictedEntitiesResponse404 | IAMPolicyAddCARRestrictedEntitiesResponse422 | IAMPolicyAddCARRestrictedEntitiesResponse500 | None:
    if response.status_code == 200:
        response_200 = IAMPolicyAddCARRestrictedEntitiesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = IAMPolicyAddCARRestrictedEntitiesResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = IAMPolicyAddCARRestrictedEntitiesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = IAMPolicyAddCARRestrictedEntitiesResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = IAMPolicyAddCARRestrictedEntitiesResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = IAMPolicyAddCARRestrictedEntitiesResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = IAMPolicyAddCARRestrictedEntitiesResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IAMPolicyAddCARRestrictedEntitiesResponse200 | IAMPolicyAddCARRestrictedEntitiesResponse400 | IAMPolicyAddCARRestrictedEntitiesResponse401 | IAMPolicyAddCARRestrictedEntitiesResponse403 | IAMPolicyAddCARRestrictedEntitiesResponse404 | IAMPolicyAddCARRestrictedEntitiesResponse422 | IAMPolicyAddCARRestrictedEntitiesResponse500]:
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

) -> Response[IAMPolicyAddCARRestrictedEntitiesResponse200 | IAMPolicyAddCARRestrictedEntitiesResponse400 | IAMPolicyAddCARRestrictedEntitiesResponse401 | IAMPolicyAddCARRestrictedEntitiesResponse403 | IAMPolicyAddCARRestrictedEntitiesResponse404 | IAMPolicyAddCARRestrictedEntitiesResponse422 | IAMPolicyAddCARRestrictedEntitiesResponse500]:
    """ Specifies the only users and groups able to use the IAM policy on a Cloud Access Role.

    Args:
        id (int):
        body (CARRestrictedEntities): CARRestrictedEntities defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IAMPolicyAddCARRestrictedEntitiesResponse200 | IAMPolicyAddCARRestrictedEntitiesResponse400 | IAMPolicyAddCARRestrictedEntitiesResponse401 | IAMPolicyAddCARRestrictedEntitiesResponse403 | IAMPolicyAddCARRestrictedEntitiesResponse404 | IAMPolicyAddCARRestrictedEntitiesResponse422 | IAMPolicyAddCARRestrictedEntitiesResponse500]
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

) -> IAMPolicyAddCARRestrictedEntitiesResponse200 | IAMPolicyAddCARRestrictedEntitiesResponse400 | IAMPolicyAddCARRestrictedEntitiesResponse401 | IAMPolicyAddCARRestrictedEntitiesResponse403 | IAMPolicyAddCARRestrictedEntitiesResponse404 | IAMPolicyAddCARRestrictedEntitiesResponse422 | IAMPolicyAddCARRestrictedEntitiesResponse500 | None:
    """ Specifies the only users and groups able to use the IAM policy on a Cloud Access Role.

    Args:
        id (int):
        body (CARRestrictedEntities): CARRestrictedEntities defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IAMPolicyAddCARRestrictedEntitiesResponse200 | IAMPolicyAddCARRestrictedEntitiesResponse400 | IAMPolicyAddCARRestrictedEntitiesResponse401 | IAMPolicyAddCARRestrictedEntitiesResponse403 | IAMPolicyAddCARRestrictedEntitiesResponse404 | IAMPolicyAddCARRestrictedEntitiesResponse422 | IAMPolicyAddCARRestrictedEntitiesResponse500
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

) -> Response[IAMPolicyAddCARRestrictedEntitiesResponse200 | IAMPolicyAddCARRestrictedEntitiesResponse400 | IAMPolicyAddCARRestrictedEntitiesResponse401 | IAMPolicyAddCARRestrictedEntitiesResponse403 | IAMPolicyAddCARRestrictedEntitiesResponse404 | IAMPolicyAddCARRestrictedEntitiesResponse422 | IAMPolicyAddCARRestrictedEntitiesResponse500]:
    """ Specifies the only users and groups able to use the IAM policy on a Cloud Access Role.

    Args:
        id (int):
        body (CARRestrictedEntities): CARRestrictedEntities defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IAMPolicyAddCARRestrictedEntitiesResponse200 | IAMPolicyAddCARRestrictedEntitiesResponse400 | IAMPolicyAddCARRestrictedEntitiesResponse401 | IAMPolicyAddCARRestrictedEntitiesResponse403 | IAMPolicyAddCARRestrictedEntitiesResponse404 | IAMPolicyAddCARRestrictedEntitiesResponse422 | IAMPolicyAddCARRestrictedEntitiesResponse500]
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

) -> IAMPolicyAddCARRestrictedEntitiesResponse200 | IAMPolicyAddCARRestrictedEntitiesResponse400 | IAMPolicyAddCARRestrictedEntitiesResponse401 | IAMPolicyAddCARRestrictedEntitiesResponse403 | IAMPolicyAddCARRestrictedEntitiesResponse404 | IAMPolicyAddCARRestrictedEntitiesResponse422 | IAMPolicyAddCARRestrictedEntitiesResponse500 | None:
    """ Specifies the only users and groups able to use the IAM policy on a Cloud Access Role.

    Args:
        id (int):
        body (CARRestrictedEntities): CARRestrictedEntities defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IAMPolicyAddCARRestrictedEntitiesResponse200 | IAMPolicyAddCARRestrictedEntitiesResponse400 | IAMPolicyAddCARRestrictedEntitiesResponse401 | IAMPolicyAddCARRestrictedEntitiesResponse403 | IAMPolicyAddCARRestrictedEntitiesResponse404 | IAMPolicyAddCARRestrictedEntitiesResponse422 | IAMPolicyAddCARRestrictedEntitiesResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
