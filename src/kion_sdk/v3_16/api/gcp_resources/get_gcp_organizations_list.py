from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_gcp_organizations_list_response_200 import GetGCPOrganizationsListResponse200
from ...models.get_gcp_organizations_list_response_400 import GetGCPOrganizationsListResponse400
from ...models.get_gcp_organizations_list_response_401 import GetGCPOrganizationsListResponse401
from ...models.get_gcp_organizations_list_response_403 import GetGCPOrganizationsListResponse403
from ...models.get_gcp_organizations_list_response_500 import GetGCPOrganizationsListResponse500
from ...models.list_gcp_organizations_request_body import ListGCPOrganizationsRequestBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: ListGCPOrganizationsRequestBody,
    default: bool | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["default"] = default


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/gcp-resources/list-organizations",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetGCPOrganizationsListResponse200 | GetGCPOrganizationsListResponse400 | GetGCPOrganizationsListResponse401 | GetGCPOrganizationsListResponse403 | GetGCPOrganizationsListResponse500 | None:
    if response.status_code == 200:
        response_200 = GetGCPOrganizationsListResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetGCPOrganizationsListResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetGCPOrganizationsListResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetGCPOrganizationsListResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetGCPOrganizationsListResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetGCPOrganizationsListResponse200 | GetGCPOrganizationsListResponse400 | GetGCPOrganizationsListResponse401 | GetGCPOrganizationsListResponse403 | GetGCPOrganizationsListResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ListGCPOrganizationsRequestBody,
    default: bool | Unset = UNSET,

) -> Response[GetGCPOrganizationsListResponse200 | GetGCPOrganizationsListResponse400 | GetGCPOrganizationsListResponse401 | GetGCPOrganizationsListResponse403 | GetGCPOrganizationsListResponse500]:
    """ Returns a list of organizations visible to the service account for the specified payer.

    Args:
        default (bool | Unset):
        body (ListGCPOrganizationsRequestBody): ListGCPOrganizationsRequestBody is the body of a
            list organizations call

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGCPOrganizationsListResponse200 | GetGCPOrganizationsListResponse400 | GetGCPOrganizationsListResponse401 | GetGCPOrganizationsListResponse403 | GetGCPOrganizationsListResponse500]
     """


    kwargs = _get_kwargs(
        body=body,
default=default,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: ListGCPOrganizationsRequestBody,
    default: bool | Unset = UNSET,

) -> GetGCPOrganizationsListResponse200 | GetGCPOrganizationsListResponse400 | GetGCPOrganizationsListResponse401 | GetGCPOrganizationsListResponse403 | GetGCPOrganizationsListResponse500 | None:
    """ Returns a list of organizations visible to the service account for the specified payer.

    Args:
        default (bool | Unset):
        body (ListGCPOrganizationsRequestBody): ListGCPOrganizationsRequestBody is the body of a
            list organizations call

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGCPOrganizationsListResponse200 | GetGCPOrganizationsListResponse400 | GetGCPOrganizationsListResponse401 | GetGCPOrganizationsListResponse403 | GetGCPOrganizationsListResponse500
     """


    return sync_detailed(
        client=client,
body=body,
default=default,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ListGCPOrganizationsRequestBody,
    default: bool | Unset = UNSET,

) -> Response[GetGCPOrganizationsListResponse200 | GetGCPOrganizationsListResponse400 | GetGCPOrganizationsListResponse401 | GetGCPOrganizationsListResponse403 | GetGCPOrganizationsListResponse500]:
    """ Returns a list of organizations visible to the service account for the specified payer.

    Args:
        default (bool | Unset):
        body (ListGCPOrganizationsRequestBody): ListGCPOrganizationsRequestBody is the body of a
            list organizations call

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGCPOrganizationsListResponse200 | GetGCPOrganizationsListResponse400 | GetGCPOrganizationsListResponse401 | GetGCPOrganizationsListResponse403 | GetGCPOrganizationsListResponse500]
     """


    kwargs = _get_kwargs(
        body=body,
default=default,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ListGCPOrganizationsRequestBody,
    default: bool | Unset = UNSET,

) -> GetGCPOrganizationsListResponse200 | GetGCPOrganizationsListResponse400 | GetGCPOrganizationsListResponse401 | GetGCPOrganizationsListResponse403 | GetGCPOrganizationsListResponse500 | None:
    """ Returns a list of organizations visible to the service account for the specified payer.

    Args:
        default (bool | Unset):
        body (ListGCPOrganizationsRequestBody): ListGCPOrganizationsRequestBody is the body of a
            list organizations call

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGCPOrganizationsListResponse200 | GetGCPOrganizationsListResponse400 | GetGCPOrganizationsListResponse401 | GetGCPOrganizationsListResponse403 | GetGCPOrganizationsListResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,
default=default,

    )).parsed
