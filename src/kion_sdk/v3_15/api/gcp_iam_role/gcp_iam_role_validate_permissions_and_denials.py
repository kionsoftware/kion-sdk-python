from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gcp_iam_role_validate_permissions_and_denials_response_200 import GcpIAMRoleValidatePermissionsAndDenialsResponse200
from ...models.gcp_iam_role_validate_permissions_and_denials_response_400 import GcpIAMRoleValidatePermissionsAndDenialsResponse400
from ...models.gcp_iam_role_validate_permissions_and_denials_response_401 import GcpIAMRoleValidatePermissionsAndDenialsResponse401
from ...models.gcp_iam_role_validate_permissions_and_denials_response_422 import GcpIAMRoleValidatePermissionsAndDenialsResponse422
from ...models.gcp_iam_role_validate_permissions_and_denials_response_500 import GcpIAMRoleValidatePermissionsAndDenialsResponse500
from ...models.gcp_role_permission_and_denials import GCPRolePermissionAndDenials
from typing import cast



def _get_kwargs(
    *,
    body: GCPRolePermissionAndDenials,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/gcp-iam-role/validate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GcpIAMRoleValidatePermissionsAndDenialsResponse200 | GcpIAMRoleValidatePermissionsAndDenialsResponse400 | GcpIAMRoleValidatePermissionsAndDenialsResponse401 | GcpIAMRoleValidatePermissionsAndDenialsResponse422 | GcpIAMRoleValidatePermissionsAndDenialsResponse500 | None:
    if response.status_code == 200:
        response_200 = GcpIAMRoleValidatePermissionsAndDenialsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GcpIAMRoleValidatePermissionsAndDenialsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GcpIAMRoleValidatePermissionsAndDenialsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = GcpIAMRoleValidatePermissionsAndDenialsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = GcpIAMRoleValidatePermissionsAndDenialsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GcpIAMRoleValidatePermissionsAndDenialsResponse200 | GcpIAMRoleValidatePermissionsAndDenialsResponse400 | GcpIAMRoleValidatePermissionsAndDenialsResponse401 | GcpIAMRoleValidatePermissionsAndDenialsResponse422 | GcpIAMRoleValidatePermissionsAndDenialsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPRolePermissionAndDenials,

) -> Response[GcpIAMRoleValidatePermissionsAndDenialsResponse200 | GcpIAMRoleValidatePermissionsAndDenialsResponse400 | GcpIAMRoleValidatePermissionsAndDenialsResponse401 | GcpIAMRoleValidatePermissionsAndDenialsResponse422 | GcpIAMRoleValidatePermissionsAndDenialsResponse500]:
    """ Validates that the provided permissions and denials are in the correct format and do not overlap.

    Args:
        body (GCPRolePermissionAndDenials): GCPRolePermissionAndDenials defines a list of
            permissions and denials to validate

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GcpIAMRoleValidatePermissionsAndDenialsResponse200 | GcpIAMRoleValidatePermissionsAndDenialsResponse400 | GcpIAMRoleValidatePermissionsAndDenialsResponse401 | GcpIAMRoleValidatePermissionsAndDenialsResponse422 | GcpIAMRoleValidatePermissionsAndDenialsResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: GCPRolePermissionAndDenials,

) -> GcpIAMRoleValidatePermissionsAndDenialsResponse200 | GcpIAMRoleValidatePermissionsAndDenialsResponse400 | GcpIAMRoleValidatePermissionsAndDenialsResponse401 | GcpIAMRoleValidatePermissionsAndDenialsResponse422 | GcpIAMRoleValidatePermissionsAndDenialsResponse500 | None:
    """ Validates that the provided permissions and denials are in the correct format and do not overlap.

    Args:
        body (GCPRolePermissionAndDenials): GCPRolePermissionAndDenials defines a list of
            permissions and denials to validate

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GcpIAMRoleValidatePermissionsAndDenialsResponse200 | GcpIAMRoleValidatePermissionsAndDenialsResponse400 | GcpIAMRoleValidatePermissionsAndDenialsResponse401 | GcpIAMRoleValidatePermissionsAndDenialsResponse422 | GcpIAMRoleValidatePermissionsAndDenialsResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPRolePermissionAndDenials,

) -> Response[GcpIAMRoleValidatePermissionsAndDenialsResponse200 | GcpIAMRoleValidatePermissionsAndDenialsResponse400 | GcpIAMRoleValidatePermissionsAndDenialsResponse401 | GcpIAMRoleValidatePermissionsAndDenialsResponse422 | GcpIAMRoleValidatePermissionsAndDenialsResponse500]:
    """ Validates that the provided permissions and denials are in the correct format and do not overlap.

    Args:
        body (GCPRolePermissionAndDenials): GCPRolePermissionAndDenials defines a list of
            permissions and denials to validate

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GcpIAMRoleValidatePermissionsAndDenialsResponse200 | GcpIAMRoleValidatePermissionsAndDenialsResponse400 | GcpIAMRoleValidatePermissionsAndDenialsResponse401 | GcpIAMRoleValidatePermissionsAndDenialsResponse422 | GcpIAMRoleValidatePermissionsAndDenialsResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GCPRolePermissionAndDenials,

) -> GcpIAMRoleValidatePermissionsAndDenialsResponse200 | GcpIAMRoleValidatePermissionsAndDenialsResponse400 | GcpIAMRoleValidatePermissionsAndDenialsResponse401 | GcpIAMRoleValidatePermissionsAndDenialsResponse422 | GcpIAMRoleValidatePermissionsAndDenialsResponse500 | None:
    """ Validates that the provided permissions and denials are in the correct format and do not overlap.

    Args:
        body (GCPRolePermissionAndDenials): GCPRolePermissionAndDenials defines a list of
            permissions and denials to validate

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GcpIAMRoleValidatePermissionsAndDenialsResponse200 | GcpIAMRoleValidatePermissionsAndDenialsResponse400 | GcpIAMRoleValidatePermissionsAndDenialsResponse401 | GcpIAMRoleValidatePermissionsAndDenialsResponse422 | GcpIAMRoleValidatePermissionsAndDenialsResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
