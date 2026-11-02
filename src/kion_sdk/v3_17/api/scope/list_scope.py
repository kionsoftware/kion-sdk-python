from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_scope_response_200 import ListScopeResponse200
from ...models.list_scope_response_401 import ListScopeResponse401
from ...models.list_scope_response_500 import ListScopeResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    search: str | Unset = UNSET,
    project_i_ds: list[int] | Unset = UNSET,
    account_i_ds: list[int] | Unset = UNSET,
    cloud_provider_i_ds: list[int] | Unset = UNSET,
    billing_source_i_ds: list[int] | Unset = UNSET,
    month: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["Search"] = search

    json_project_i_ds: list[int] | Unset = UNSET
    if not isinstance(project_i_ds, Unset):
        json_project_i_ds = project_i_ds


    params["ProjectIDs"] = json_project_i_ds

    json_account_i_ds: list[int] | Unset = UNSET
    if not isinstance(account_i_ds, Unset):
        json_account_i_ds = account_i_ds


    params["AccountIDs"] = json_account_i_ds

    json_cloud_provider_i_ds: list[int] | Unset = UNSET
    if not isinstance(cloud_provider_i_ds, Unset):
        json_cloud_provider_i_ds = cloud_provider_i_ds


    params["CloudProviderIDs"] = json_cloud_provider_i_ds

    json_billing_source_i_ds: list[int] | Unset = UNSET
    if not isinstance(billing_source_i_ds, Unset):
        json_billing_source_i_ds = billing_source_i_ds


    params["BillingSourceIDs"] = json_billing_source_i_ds

    params["Month"] = month

    params["page"] = page

    params["count"] = count


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/beta/scope",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListScopeResponse200 | ListScopeResponse401 | ListScopeResponse500 | None:
    if response.status_code == 200:
        response_200 = ListScopeResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ListScopeResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = ListScopeResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListScopeResponse200 | ListScopeResponse401 | ListScopeResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    search: str | Unset = UNSET,
    project_i_ds: list[int] | Unset = UNSET,
    account_i_ds: list[int] | Unset = UNSET,
    cloud_provider_i_ds: list[int] | Unset = UNSET,
    billing_source_i_ds: list[int] | Unset = UNSET,
    month: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,

) -> Response[ListScopeResponse200 | ListScopeResponse401 | ListScopeResponse500]:
    """ Returns a list of Scopes from the application.

    Args:
        search (str | Unset):
        project_i_ds (list[int] | Unset):
        account_i_ds (list[int] | Unset):
        cloud_provider_i_ds (list[int] | Unset):
        billing_source_i_ds (list[int] | Unset):
        month (int | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListScopeResponse200 | ListScopeResponse401 | ListScopeResponse500]
     """


    kwargs = _get_kwargs(
        search=search,
project_i_ds=project_i_ds,
account_i_ds=account_i_ds,
cloud_provider_i_ds=cloud_provider_i_ds,
billing_source_i_ds=billing_source_i_ds,
month=month,
page=page,
count=count,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    search: str | Unset = UNSET,
    project_i_ds: list[int] | Unset = UNSET,
    account_i_ds: list[int] | Unset = UNSET,
    cloud_provider_i_ds: list[int] | Unset = UNSET,
    billing_source_i_ds: list[int] | Unset = UNSET,
    month: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,

) -> ListScopeResponse200 | ListScopeResponse401 | ListScopeResponse500 | None:
    """ Returns a list of Scopes from the application.

    Args:
        search (str | Unset):
        project_i_ds (list[int] | Unset):
        account_i_ds (list[int] | Unset):
        cloud_provider_i_ds (list[int] | Unset):
        billing_source_i_ds (list[int] | Unset):
        month (int | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListScopeResponse200 | ListScopeResponse401 | ListScopeResponse500
     """


    return sync_detailed(
        client=client,
search=search,
project_i_ds=project_i_ds,
account_i_ds=account_i_ds,
cloud_provider_i_ds=cloud_provider_i_ds,
billing_source_i_ds=billing_source_i_ds,
month=month,
page=page,
count=count,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search: str | Unset = UNSET,
    project_i_ds: list[int] | Unset = UNSET,
    account_i_ds: list[int] | Unset = UNSET,
    cloud_provider_i_ds: list[int] | Unset = UNSET,
    billing_source_i_ds: list[int] | Unset = UNSET,
    month: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,

) -> Response[ListScopeResponse200 | ListScopeResponse401 | ListScopeResponse500]:
    """ Returns a list of Scopes from the application.

    Args:
        search (str | Unset):
        project_i_ds (list[int] | Unset):
        account_i_ds (list[int] | Unset):
        cloud_provider_i_ds (list[int] | Unset):
        billing_source_i_ds (list[int] | Unset):
        month (int | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListScopeResponse200 | ListScopeResponse401 | ListScopeResponse500]
     """


    kwargs = _get_kwargs(
        search=search,
project_i_ds=project_i_ds,
account_i_ds=account_i_ds,
cloud_provider_i_ds=cloud_provider_i_ds,
billing_source_i_ds=billing_source_i_ds,
month=month,
page=page,
count=count,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    search: str | Unset = UNSET,
    project_i_ds: list[int] | Unset = UNSET,
    account_i_ds: list[int] | Unset = UNSET,
    cloud_provider_i_ds: list[int] | Unset = UNSET,
    billing_source_i_ds: list[int] | Unset = UNSET,
    month: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,

) -> ListScopeResponse200 | ListScopeResponse401 | ListScopeResponse500 | None:
    """ Returns a list of Scopes from the application.

    Args:
        search (str | Unset):
        project_i_ds (list[int] | Unset):
        account_i_ds (list[int] | Unset):
        cloud_provider_i_ds (list[int] | Unset):
        billing_source_i_ds (list[int] | Unset):
        month (int | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListScopeResponse200 | ListScopeResponse401 | ListScopeResponse500
     """


    return (await asyncio_detailed(
        client=client,
search=search,
project_i_ds=project_i_ds,
account_i_ds=account_i_ds,
cloud_provider_i_ds=cloud_provider_i_ds,
billing_source_i_ds=billing_source_i_ds,
month=month,
page=page,
count=count,

    )).parsed
