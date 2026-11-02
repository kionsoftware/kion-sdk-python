from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.billing_rule_create_deprecated import BillingRuleCreateDeprecated
from ...models.post_billing_rule_2_response_201 import PostBillingRule2Response201
from ...models.post_billing_rule_2_response_400 import PostBillingRule2Response400
from ...models.post_billing_rule_2_response_401 import PostBillingRule2Response401
from ...models.post_billing_rule_2_response_403 import PostBillingRule2Response403
from ...models.post_billing_rule_2_response_422 import PostBillingRule2Response422
from ...models.post_billing_rule_2_response_500 import PostBillingRule2Response500
from typing import cast



def _get_kwargs(
    *,
    body: BillingRuleCreateDeprecated,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/billing-rule",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostBillingRule2Response201 | PostBillingRule2Response400 | PostBillingRule2Response401 | PostBillingRule2Response403 | PostBillingRule2Response422 | PostBillingRule2Response500 | None:
    if response.status_code == 201:
        response_201 = PostBillingRule2Response201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostBillingRule2Response400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostBillingRule2Response401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostBillingRule2Response403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostBillingRule2Response422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostBillingRule2Response500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostBillingRule2Response201 | PostBillingRule2Response400 | PostBillingRule2Response401 | PostBillingRule2Response403 | PostBillingRule2Response422 | PostBillingRule2Response500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BillingRuleCreateDeprecated,

) -> Response[PostBillingRule2Response201 | PostBillingRule2Response400 | PostBillingRule2Response401 | PostBillingRule2Response403 | PostBillingRule2Response422 | PostBillingRule2Response500]:
    """ Creates a BillingRules.

    Args:
        body (BillingRuleCreateDeprecated):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostBillingRule2Response201 | PostBillingRule2Response400 | PostBillingRule2Response401 | PostBillingRule2Response403 | PostBillingRule2Response422 | PostBillingRule2Response500]
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
    body: BillingRuleCreateDeprecated,

) -> PostBillingRule2Response201 | PostBillingRule2Response400 | PostBillingRule2Response401 | PostBillingRule2Response403 | PostBillingRule2Response422 | PostBillingRule2Response500 | None:
    """ Creates a BillingRules.

    Args:
        body (BillingRuleCreateDeprecated):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostBillingRule2Response201 | PostBillingRule2Response400 | PostBillingRule2Response401 | PostBillingRule2Response403 | PostBillingRule2Response422 | PostBillingRule2Response500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BillingRuleCreateDeprecated,

) -> Response[PostBillingRule2Response201 | PostBillingRule2Response400 | PostBillingRule2Response401 | PostBillingRule2Response403 | PostBillingRule2Response422 | PostBillingRule2Response500]:
    """ Creates a BillingRules.

    Args:
        body (BillingRuleCreateDeprecated):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostBillingRule2Response201 | PostBillingRule2Response400 | PostBillingRule2Response401 | PostBillingRule2Response403 | PostBillingRule2Response422 | PostBillingRule2Response500]
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
    body: BillingRuleCreateDeprecated,

) -> PostBillingRule2Response201 | PostBillingRule2Response400 | PostBillingRule2Response401 | PostBillingRule2Response403 | PostBillingRule2Response422 | PostBillingRule2Response500 | None:
    """ Creates a BillingRules.

    Args:
        body (BillingRuleCreateDeprecated):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostBillingRule2Response201 | PostBillingRule2Response400 | PostBillingRule2Response401 | PostBillingRule2Response403 | PostBillingRule2Response422 | PostBillingRule2Response500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
