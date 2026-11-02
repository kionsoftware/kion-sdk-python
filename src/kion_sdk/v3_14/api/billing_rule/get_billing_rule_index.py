from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_billing_rule_index_response_200 import GetBillingRuleIndexResponse200
from ...models.get_billing_rule_index_response_400 import GetBillingRuleIndexResponse400
from ...models.get_billing_rule_index_response_401 import GetBillingRuleIndexResponse401
from ...models.get_billing_rule_index_response_403 import GetBillingRuleIndexResponse403
from ...models.get_billing_rule_index_response_500 import GetBillingRuleIndexResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_month: int | Unset = UNSET,
    end_month: int | Unset = UNSET,
    rule_type_ids: list[int] | Unset = UNSET,
    creator_ids: list[int] | Unset = UNSET,
    billing_source_ids: list[int] | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'date',
    sort_order: str | Unset = 'DESC',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["start_month"] = start_month

    params["end_month"] = end_month

    json_rule_type_ids: list[int] | Unset = UNSET
    if not isinstance(rule_type_ids, Unset):
        json_rule_type_ids = rule_type_ids


    params["rule_type_ids"] = json_rule_type_ids

    json_creator_ids: list[int] | Unset = UNSET
    if not isinstance(creator_ids, Unset):
        json_creator_ids = creator_ids


    params["creator_ids"] = json_creator_ids

    json_billing_source_ids: list[int] | Unset = UNSET
    if not isinstance(billing_source_ids, Unset):
        json_billing_source_ids = billing_source_ids


    params["billing_source_ids"] = json_billing_source_ids

    params["page"] = page

    params["count"] = count

    params["sortMethod"] = sort_method

    params["sortOrder"] = sort_order


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/billing-rule",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetBillingRuleIndexResponse200 | GetBillingRuleIndexResponse400 | GetBillingRuleIndexResponse401 | GetBillingRuleIndexResponse403 | GetBillingRuleIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetBillingRuleIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetBillingRuleIndexResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetBillingRuleIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetBillingRuleIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetBillingRuleIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetBillingRuleIndexResponse200 | GetBillingRuleIndexResponse400 | GetBillingRuleIndexResponse401 | GetBillingRuleIndexResponse403 | GetBillingRuleIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_month: int | Unset = UNSET,
    end_month: int | Unset = UNSET,
    rule_type_ids: list[int] | Unset = UNSET,
    creator_ids: list[int] | Unset = UNSET,
    billing_source_ids: list[int] | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'date',
    sort_order: str | Unset = 'DESC',

) -> Response[GetBillingRuleIndexResponse200 | GetBillingRuleIndexResponse400 | GetBillingRuleIndexResponse401 | GetBillingRuleIndexResponse403 | GetBillingRuleIndexResponse500]:
    """ Finds all BillingRules in the application.

    Args:
        start_month (int | Unset):
        end_month (int | Unset):
        rule_type_ids (list[int] | Unset):
        creator_ids (list[int] | Unset):
        billing_source_ids (list[int] | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'date'.
        sort_order (str | Unset):  Default: 'DESC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingRuleIndexResponse200 | GetBillingRuleIndexResponse400 | GetBillingRuleIndexResponse401 | GetBillingRuleIndexResponse403 | GetBillingRuleIndexResponse500]
     """


    kwargs = _get_kwargs(
        start_month=start_month,
end_month=end_month,
rule_type_ids=rule_type_ids,
creator_ids=creator_ids,
billing_source_ids=billing_source_ids,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_month: int | Unset = UNSET,
    end_month: int | Unset = UNSET,
    rule_type_ids: list[int] | Unset = UNSET,
    creator_ids: list[int] | Unset = UNSET,
    billing_source_ids: list[int] | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'date',
    sort_order: str | Unset = 'DESC',

) -> GetBillingRuleIndexResponse200 | GetBillingRuleIndexResponse400 | GetBillingRuleIndexResponse401 | GetBillingRuleIndexResponse403 | GetBillingRuleIndexResponse500 | None:
    """ Finds all BillingRules in the application.

    Args:
        start_month (int | Unset):
        end_month (int | Unset):
        rule_type_ids (list[int] | Unset):
        creator_ids (list[int] | Unset):
        billing_source_ids (list[int] | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'date'.
        sort_order (str | Unset):  Default: 'DESC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingRuleIndexResponse200 | GetBillingRuleIndexResponse400 | GetBillingRuleIndexResponse401 | GetBillingRuleIndexResponse403 | GetBillingRuleIndexResponse500
     """


    return sync_detailed(
        client=client,
start_month=start_month,
end_month=end_month,
rule_type_ids=rule_type_ids,
creator_ids=creator_ids,
billing_source_ids=billing_source_ids,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_month: int | Unset = UNSET,
    end_month: int | Unset = UNSET,
    rule_type_ids: list[int] | Unset = UNSET,
    creator_ids: list[int] | Unset = UNSET,
    billing_source_ids: list[int] | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'date',
    sort_order: str | Unset = 'DESC',

) -> Response[GetBillingRuleIndexResponse200 | GetBillingRuleIndexResponse400 | GetBillingRuleIndexResponse401 | GetBillingRuleIndexResponse403 | GetBillingRuleIndexResponse500]:
    """ Finds all BillingRules in the application.

    Args:
        start_month (int | Unset):
        end_month (int | Unset):
        rule_type_ids (list[int] | Unset):
        creator_ids (list[int] | Unset):
        billing_source_ids (list[int] | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'date'.
        sort_order (str | Unset):  Default: 'DESC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingRuleIndexResponse200 | GetBillingRuleIndexResponse400 | GetBillingRuleIndexResponse401 | GetBillingRuleIndexResponse403 | GetBillingRuleIndexResponse500]
     """


    kwargs = _get_kwargs(
        start_month=start_month,
end_month=end_month,
rule_type_ids=rule_type_ids,
creator_ids=creator_ids,
billing_source_ids=billing_source_ids,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_month: int | Unset = UNSET,
    end_month: int | Unset = UNSET,
    rule_type_ids: list[int] | Unset = UNSET,
    creator_ids: list[int] | Unset = UNSET,
    billing_source_ids: list[int] | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'date',
    sort_order: str | Unset = 'DESC',

) -> GetBillingRuleIndexResponse200 | GetBillingRuleIndexResponse400 | GetBillingRuleIndexResponse401 | GetBillingRuleIndexResponse403 | GetBillingRuleIndexResponse500 | None:
    """ Finds all BillingRules in the application.

    Args:
        start_month (int | Unset):
        end_month (int | Unset):
        rule_type_ids (list[int] | Unset):
        creator_ids (list[int] | Unset):
        billing_source_ids (list[int] | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'date'.
        sort_order (str | Unset):  Default: 'DESC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingRuleIndexResponse200 | GetBillingRuleIndexResponse400 | GetBillingRuleIndexResponse401 | GetBillingRuleIndexResponse403 | GetBillingRuleIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,
start_month=start_month,
end_month=end_month,
rule_type_ids=rule_type_ids,
creator_ids=creator_ids,
billing_source_ids=billing_source_ids,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,

    )).parsed
