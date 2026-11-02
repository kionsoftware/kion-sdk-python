from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.billing_rule_segment_create import BillingRuleSegmentCreate
from ...models.post_billing_rule_segment_response_201 import PostBillingRuleSegmentResponse201
from ...models.post_billing_rule_segment_response_400 import PostBillingRuleSegmentResponse400
from ...models.post_billing_rule_segment_response_401 import PostBillingRuleSegmentResponse401
from ...models.post_billing_rule_segment_response_403 import PostBillingRuleSegmentResponse403
from ...models.post_billing_rule_segment_response_422 import PostBillingRuleSegmentResponse422
from ...models.post_billing_rule_segment_response_500 import PostBillingRuleSegmentResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: BillingRuleSegmentCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/beta/billing-rule/{id}/segments".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostBillingRuleSegmentResponse201 | PostBillingRuleSegmentResponse400 | PostBillingRuleSegmentResponse401 | PostBillingRuleSegmentResponse403 | PostBillingRuleSegmentResponse422 | PostBillingRuleSegmentResponse500 | None:
    if response.status_code == 201:
        response_201 = PostBillingRuleSegmentResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostBillingRuleSegmentResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostBillingRuleSegmentResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostBillingRuleSegmentResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostBillingRuleSegmentResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostBillingRuleSegmentResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostBillingRuleSegmentResponse201 | PostBillingRuleSegmentResponse400 | PostBillingRuleSegmentResponse401 | PostBillingRuleSegmentResponse403 | PostBillingRuleSegmentResponse422 | PostBillingRuleSegmentResponse500]:
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
    body: BillingRuleSegmentCreate,

) -> Response[PostBillingRuleSegmentResponse201 | PostBillingRuleSegmentResponse400 | PostBillingRuleSegmentResponse401 | PostBillingRuleSegmentResponse403 | PostBillingRuleSegmentResponse422 | PostBillingRuleSegmentResponse500]:
    """ 
    Args:
        id (int):
        body (BillingRuleSegmentCreate): Exactly one of AdjustmentRule / AllocationRule must be
            populated, matching the parent
            rule's type. The controller validates that match.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostBillingRuleSegmentResponse201 | PostBillingRuleSegmentResponse400 | PostBillingRuleSegmentResponse401 | PostBillingRuleSegmentResponse403 | PostBillingRuleSegmentResponse422 | PostBillingRuleSegmentResponse500]
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
    body: BillingRuleSegmentCreate,

) -> PostBillingRuleSegmentResponse201 | PostBillingRuleSegmentResponse400 | PostBillingRuleSegmentResponse401 | PostBillingRuleSegmentResponse403 | PostBillingRuleSegmentResponse422 | PostBillingRuleSegmentResponse500 | None:
    """ 
    Args:
        id (int):
        body (BillingRuleSegmentCreate): Exactly one of AdjustmentRule / AllocationRule must be
            populated, matching the parent
            rule's type. The controller validates that match.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostBillingRuleSegmentResponse201 | PostBillingRuleSegmentResponse400 | PostBillingRuleSegmentResponse401 | PostBillingRuleSegmentResponse403 | PostBillingRuleSegmentResponse422 | PostBillingRuleSegmentResponse500
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
    body: BillingRuleSegmentCreate,

) -> Response[PostBillingRuleSegmentResponse201 | PostBillingRuleSegmentResponse400 | PostBillingRuleSegmentResponse401 | PostBillingRuleSegmentResponse403 | PostBillingRuleSegmentResponse422 | PostBillingRuleSegmentResponse500]:
    """ 
    Args:
        id (int):
        body (BillingRuleSegmentCreate): Exactly one of AdjustmentRule / AllocationRule must be
            populated, matching the parent
            rule's type. The controller validates that match.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostBillingRuleSegmentResponse201 | PostBillingRuleSegmentResponse400 | PostBillingRuleSegmentResponse401 | PostBillingRuleSegmentResponse403 | PostBillingRuleSegmentResponse422 | PostBillingRuleSegmentResponse500]
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
    body: BillingRuleSegmentCreate,

) -> PostBillingRuleSegmentResponse201 | PostBillingRuleSegmentResponse400 | PostBillingRuleSegmentResponse401 | PostBillingRuleSegmentResponse403 | PostBillingRuleSegmentResponse422 | PostBillingRuleSegmentResponse500 | None:
    """ 
    Args:
        id (int):
        body (BillingRuleSegmentCreate): Exactly one of AdjustmentRule / AllocationRule must be
            populated, matching the parent
            rule's type. The controller validates that match.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostBillingRuleSegmentResponse201 | PostBillingRuleSegmentResponse400 | PostBillingRuleSegmentResponse401 | PostBillingRuleSegmentResponse403 | PostBillingRuleSegmentResponse422 | PostBillingRuleSegmentResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
