from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_check_add_owners_response_200 import ComplianceCheckAddOwnersResponse200
from ...models.compliance_check_add_owners_response_400 import ComplianceCheckAddOwnersResponse400
from ...models.compliance_check_add_owners_response_401 import ComplianceCheckAddOwnersResponse401
from ...models.compliance_check_add_owners_response_403 import ComplianceCheckAddOwnersResponse403
from ...models.compliance_check_add_owners_response_404 import ComplianceCheckAddOwnersResponse404
from ...models.compliance_check_add_owners_response_422 import ComplianceCheckAddOwnersResponse422
from ...models.compliance_check_add_owners_response_500 import ComplianceCheckAddOwnersResponse500
from ...models.compliance_check_owners import ComplianceCheckOwners
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ComplianceCheckOwners | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/compliance/check/{id}/owner".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ComplianceCheckAddOwnersResponse200 | ComplianceCheckAddOwnersResponse400 | ComplianceCheckAddOwnersResponse401 | ComplianceCheckAddOwnersResponse403 | ComplianceCheckAddOwnersResponse404 | ComplianceCheckAddOwnersResponse422 | ComplianceCheckAddOwnersResponse500 | None:
    if response.status_code == 200:
        response_200 = ComplianceCheckAddOwnersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ComplianceCheckAddOwnersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ComplianceCheckAddOwnersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ComplianceCheckAddOwnersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ComplianceCheckAddOwnersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = ComplianceCheckAddOwnersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = ComplianceCheckAddOwnersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ComplianceCheckAddOwnersResponse200 | ComplianceCheckAddOwnersResponse400 | ComplianceCheckAddOwnersResponse401 | ComplianceCheckAddOwnersResponse403 | ComplianceCheckAddOwnersResponse404 | ComplianceCheckAddOwnersResponse422 | ComplianceCheckAddOwnersResponse500]:
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
    body: ComplianceCheckOwners | Unset = UNSET,

) -> Response[ComplianceCheckAddOwnersResponse200 | ComplianceCheckAddOwnersResponse400 | ComplianceCheckAddOwnersResponse401 | ComplianceCheckAddOwnersResponse403 | ComplianceCheckAddOwnersResponse404 | ComplianceCheckAddOwnersResponse422 | ComplianceCheckAddOwnersResponse500]:
    """ Adds users and user groups to a compliance check in the application.

    Args:
        id (int):
        body (ComplianceCheckOwners | Unset): ComplianceCheckOwners defines user and group ID
            lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComplianceCheckAddOwnersResponse200 | ComplianceCheckAddOwnersResponse400 | ComplianceCheckAddOwnersResponse401 | ComplianceCheckAddOwnersResponse403 | ComplianceCheckAddOwnersResponse404 | ComplianceCheckAddOwnersResponse422 | ComplianceCheckAddOwnersResponse500]
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
    body: ComplianceCheckOwners | Unset = UNSET,

) -> ComplianceCheckAddOwnersResponse200 | ComplianceCheckAddOwnersResponse400 | ComplianceCheckAddOwnersResponse401 | ComplianceCheckAddOwnersResponse403 | ComplianceCheckAddOwnersResponse404 | ComplianceCheckAddOwnersResponse422 | ComplianceCheckAddOwnersResponse500 | None:
    """ Adds users and user groups to a compliance check in the application.

    Args:
        id (int):
        body (ComplianceCheckOwners | Unset): ComplianceCheckOwners defines user and group ID
            lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComplianceCheckAddOwnersResponse200 | ComplianceCheckAddOwnersResponse400 | ComplianceCheckAddOwnersResponse401 | ComplianceCheckAddOwnersResponse403 | ComplianceCheckAddOwnersResponse404 | ComplianceCheckAddOwnersResponse422 | ComplianceCheckAddOwnersResponse500
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
    body: ComplianceCheckOwners | Unset = UNSET,

) -> Response[ComplianceCheckAddOwnersResponse200 | ComplianceCheckAddOwnersResponse400 | ComplianceCheckAddOwnersResponse401 | ComplianceCheckAddOwnersResponse403 | ComplianceCheckAddOwnersResponse404 | ComplianceCheckAddOwnersResponse422 | ComplianceCheckAddOwnersResponse500]:
    """ Adds users and user groups to a compliance check in the application.

    Args:
        id (int):
        body (ComplianceCheckOwners | Unset): ComplianceCheckOwners defines user and group ID
            lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComplianceCheckAddOwnersResponse200 | ComplianceCheckAddOwnersResponse400 | ComplianceCheckAddOwnersResponse401 | ComplianceCheckAddOwnersResponse403 | ComplianceCheckAddOwnersResponse404 | ComplianceCheckAddOwnersResponse422 | ComplianceCheckAddOwnersResponse500]
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
    body: ComplianceCheckOwners | Unset = UNSET,

) -> ComplianceCheckAddOwnersResponse200 | ComplianceCheckAddOwnersResponse400 | ComplianceCheckAddOwnersResponse401 | ComplianceCheckAddOwnersResponse403 | ComplianceCheckAddOwnersResponse404 | ComplianceCheckAddOwnersResponse422 | ComplianceCheckAddOwnersResponse500 | None:
    """ Adds users and user groups to a compliance check in the application.

    Args:
        id (int):
        body (ComplianceCheckOwners | Unset): ComplianceCheckOwners defines user and group ID
            lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComplianceCheckAddOwnersResponse200 | ComplianceCheckAddOwnersResponse400 | ComplianceCheckAddOwnersResponse401 | ComplianceCheckAddOwnersResponse403 | ComplianceCheckAddOwnersResponse404 | ComplianceCheckAddOwnersResponse422 | ComplianceCheckAddOwnersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
