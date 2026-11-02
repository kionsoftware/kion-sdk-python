from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.car_restricted_entities import CARRestrictedEntities
from ...models.gcp_iam_role_remove_car_restricted_entities_response_200 import GcpIAMRoleRemoveCARRestrictedEntitiesResponse200
from ...models.gcp_iam_role_remove_car_restricted_entities_response_400 import GcpIAMRoleRemoveCARRestrictedEntitiesResponse400
from ...models.gcp_iam_role_remove_car_restricted_entities_response_401 import GcpIAMRoleRemoveCARRestrictedEntitiesResponse401
from ...models.gcp_iam_role_remove_car_restricted_entities_response_403 import GcpIAMRoleRemoveCARRestrictedEntitiesResponse403
from ...models.gcp_iam_role_remove_car_restricted_entities_response_404 import GcpIAMRoleRemoveCARRestrictedEntitiesResponse404
from ...models.gcp_iam_role_remove_car_restricted_entities_response_422 import GcpIAMRoleRemoveCARRestrictedEntitiesResponse422
from ...models.gcp_iam_role_remove_car_restricted_entities_response_500 import GcpIAMRoleRemoveCARRestrictedEntitiesResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: CARRestrictedEntities,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/gcp-iam-role/{id}/car-restricted-entities".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GcpIAMRoleRemoveCARRestrictedEntitiesResponse200 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse400 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse401 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse403 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse404 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse422 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse500 | None:
    if response.status_code == 200:
        response_200 = GcpIAMRoleRemoveCARRestrictedEntitiesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GcpIAMRoleRemoveCARRestrictedEntitiesResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GcpIAMRoleRemoveCARRestrictedEntitiesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GcpIAMRoleRemoveCARRestrictedEntitiesResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GcpIAMRoleRemoveCARRestrictedEntitiesResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = GcpIAMRoleRemoveCARRestrictedEntitiesResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = GcpIAMRoleRemoveCARRestrictedEntitiesResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GcpIAMRoleRemoveCARRestrictedEntitiesResponse200 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse400 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse401 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse403 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse404 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse422 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse500]:
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

) -> Response[GcpIAMRoleRemoveCARRestrictedEntitiesResponse200 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse400 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse401 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse403 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse404 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse422 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse500]:
    """ Removes users and groups that were able to use the GCP IAM Role on a Cloud Access Role.

    Args:
        id (int):
        body (CARRestrictedEntities): CARRestrictedEntities defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GcpIAMRoleRemoveCARRestrictedEntitiesResponse200 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse400 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse401 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse403 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse404 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse422 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse500]
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

) -> GcpIAMRoleRemoveCARRestrictedEntitiesResponse200 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse400 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse401 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse403 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse404 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse422 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse500 | None:
    """ Removes users and groups that were able to use the GCP IAM Role on a Cloud Access Role.

    Args:
        id (int):
        body (CARRestrictedEntities): CARRestrictedEntities defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GcpIAMRoleRemoveCARRestrictedEntitiesResponse200 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse400 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse401 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse403 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse404 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse422 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse500
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

) -> Response[GcpIAMRoleRemoveCARRestrictedEntitiesResponse200 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse400 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse401 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse403 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse404 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse422 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse500]:
    """ Removes users and groups that were able to use the GCP IAM Role on a Cloud Access Role.

    Args:
        id (int):
        body (CARRestrictedEntities): CARRestrictedEntities defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GcpIAMRoleRemoveCARRestrictedEntitiesResponse200 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse400 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse401 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse403 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse404 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse422 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse500]
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

) -> GcpIAMRoleRemoveCARRestrictedEntitiesResponse200 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse400 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse401 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse403 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse404 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse422 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse500 | None:
    """ Removes users and groups that were able to use the GCP IAM Role on a Cloud Access Role.

    Args:
        id (int):
        body (CARRestrictedEntities): CARRestrictedEntities defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GcpIAMRoleRemoveCARRestrictedEntitiesResponse200 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse400 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse401 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse403 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse404 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse422 | GcpIAMRoleRemoveCARRestrictedEntitiesResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
