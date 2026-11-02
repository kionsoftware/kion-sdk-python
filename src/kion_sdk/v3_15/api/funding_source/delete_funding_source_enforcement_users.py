from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_funding_source_enforcement_users_response_200 import DeleteFundingSourceEnforcementUsersResponse200
from ...models.delete_funding_source_enforcement_users_response_400 import DeleteFundingSourceEnforcementUsersResponse400
from ...models.delete_funding_source_enforcement_users_response_401 import DeleteFundingSourceEnforcementUsersResponse401
from ...models.delete_funding_source_enforcement_users_response_403 import DeleteFundingSourceEnforcementUsersResponse403
from ...models.delete_funding_source_enforcement_users_response_404 import DeleteFundingSourceEnforcementUsersResponse404
from ...models.delete_funding_source_enforcement_users_response_422 import DeleteFundingSourceEnforcementUsersResponse422
from ...models.delete_funding_source_enforcement_users_response_500 import DeleteFundingSourceEnforcementUsersResponse500
from ...models.funding_source_enforcement_users import FundingSourceEnforcementUsers
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    enforcement_id: int,
    *,
    body: FundingSourceEnforcementUsers | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/funding-source/{id}/enforcement/{enforcement_id}/user".format(id=quote(str(id), safe=""),enforcement_id=quote(str(enforcement_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteFundingSourceEnforcementUsersResponse200 | DeleteFundingSourceEnforcementUsersResponse400 | DeleteFundingSourceEnforcementUsersResponse401 | DeleteFundingSourceEnforcementUsersResponse403 | DeleteFundingSourceEnforcementUsersResponse404 | DeleteFundingSourceEnforcementUsersResponse422 | DeleteFundingSourceEnforcementUsersResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteFundingSourceEnforcementUsersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteFundingSourceEnforcementUsersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteFundingSourceEnforcementUsersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteFundingSourceEnforcementUsersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteFundingSourceEnforcementUsersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteFundingSourceEnforcementUsersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteFundingSourceEnforcementUsersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteFundingSourceEnforcementUsersResponse200 | DeleteFundingSourceEnforcementUsersResponse400 | DeleteFundingSourceEnforcementUsersResponse401 | DeleteFundingSourceEnforcementUsersResponse403 | DeleteFundingSourceEnforcementUsersResponse404 | DeleteFundingSourceEnforcementUsersResponse422 | DeleteFundingSourceEnforcementUsersResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    enforcement_id: int,
    *,
    client: AuthenticatedClient,
    body: FundingSourceEnforcementUsers | Unset = UNSET,

) -> Response[DeleteFundingSourceEnforcementUsersResponse200 | DeleteFundingSourceEnforcementUsersResponse400 | DeleteFundingSourceEnforcementUsersResponse401 | DeleteFundingSourceEnforcementUsersResponse403 | DeleteFundingSourceEnforcementUsersResponse404 | DeleteFundingSourceEnforcementUsersResponse422 | DeleteFundingSourceEnforcementUsersResponse500]:
    """ Removes users and groups from a funding source enforcement.

    Args:
        id (int):
        enforcement_id (int):
        body (FundingSourceEnforcementUsers | Unset): FundingSourceEnforcementUsers .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFundingSourceEnforcementUsersResponse200 | DeleteFundingSourceEnforcementUsersResponse400 | DeleteFundingSourceEnforcementUsersResponse401 | DeleteFundingSourceEnforcementUsersResponse403 | DeleteFundingSourceEnforcementUsersResponse404 | DeleteFundingSourceEnforcementUsersResponse422 | DeleteFundingSourceEnforcementUsersResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
enforcement_id=enforcement_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    enforcement_id: int,
    *,
    client: AuthenticatedClient,
    body: FundingSourceEnforcementUsers | Unset = UNSET,

) -> DeleteFundingSourceEnforcementUsersResponse200 | DeleteFundingSourceEnforcementUsersResponse400 | DeleteFundingSourceEnforcementUsersResponse401 | DeleteFundingSourceEnforcementUsersResponse403 | DeleteFundingSourceEnforcementUsersResponse404 | DeleteFundingSourceEnforcementUsersResponse422 | DeleteFundingSourceEnforcementUsersResponse500 | None:
    """ Removes users and groups from a funding source enforcement.

    Args:
        id (int):
        enforcement_id (int):
        body (FundingSourceEnforcementUsers | Unset): FundingSourceEnforcementUsers .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFundingSourceEnforcementUsersResponse200 | DeleteFundingSourceEnforcementUsersResponse400 | DeleteFundingSourceEnforcementUsersResponse401 | DeleteFundingSourceEnforcementUsersResponse403 | DeleteFundingSourceEnforcementUsersResponse404 | DeleteFundingSourceEnforcementUsersResponse422 | DeleteFundingSourceEnforcementUsersResponse500
     """


    return sync_detailed(
        id=id,
enforcement_id=enforcement_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    enforcement_id: int,
    *,
    client: AuthenticatedClient,
    body: FundingSourceEnforcementUsers | Unset = UNSET,

) -> Response[DeleteFundingSourceEnforcementUsersResponse200 | DeleteFundingSourceEnforcementUsersResponse400 | DeleteFundingSourceEnforcementUsersResponse401 | DeleteFundingSourceEnforcementUsersResponse403 | DeleteFundingSourceEnforcementUsersResponse404 | DeleteFundingSourceEnforcementUsersResponse422 | DeleteFundingSourceEnforcementUsersResponse500]:
    """ Removes users and groups from a funding source enforcement.

    Args:
        id (int):
        enforcement_id (int):
        body (FundingSourceEnforcementUsers | Unset): FundingSourceEnforcementUsers .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFundingSourceEnforcementUsersResponse200 | DeleteFundingSourceEnforcementUsersResponse400 | DeleteFundingSourceEnforcementUsersResponse401 | DeleteFundingSourceEnforcementUsersResponse403 | DeleteFundingSourceEnforcementUsersResponse404 | DeleteFundingSourceEnforcementUsersResponse422 | DeleteFundingSourceEnforcementUsersResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
enforcement_id=enforcement_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    enforcement_id: int,
    *,
    client: AuthenticatedClient,
    body: FundingSourceEnforcementUsers | Unset = UNSET,

) -> DeleteFundingSourceEnforcementUsersResponse200 | DeleteFundingSourceEnforcementUsersResponse400 | DeleteFundingSourceEnforcementUsersResponse401 | DeleteFundingSourceEnforcementUsersResponse403 | DeleteFundingSourceEnforcementUsersResponse404 | DeleteFundingSourceEnforcementUsersResponse422 | DeleteFundingSourceEnforcementUsersResponse500 | None:
    """ Removes users and groups from a funding source enforcement.

    Args:
        id (int):
        enforcement_id (int):
        body (FundingSourceEnforcementUsers | Unset): FundingSourceEnforcementUsers .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFundingSourceEnforcementUsersResponse200 | DeleteFundingSourceEnforcementUsersResponse400 | DeleteFundingSourceEnforcementUsersResponse401 | DeleteFundingSourceEnforcementUsersResponse403 | DeleteFundingSourceEnforcementUsersResponse404 | DeleteFundingSourceEnforcementUsersResponse422 | DeleteFundingSourceEnforcementUsersResponse500
     """


    return (await asyncio_detailed(
        id=id,
enforcement_id=enforcement_id,
client=client,
body=body,

    )).parsed
