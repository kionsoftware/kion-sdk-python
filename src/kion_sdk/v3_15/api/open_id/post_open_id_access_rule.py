from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.open_id_access_rule_create import OpenIDAccessRuleCreate
from ...models.post_open_id_access_rule_response_201 import PostOpenIDAccessRuleResponse201
from ...models.post_open_id_access_rule_response_400 import PostOpenIDAccessRuleResponse400
from ...models.post_open_id_access_rule_response_401 import PostOpenIDAccessRuleResponse401
from ...models.post_open_id_access_rule_response_403 import PostOpenIDAccessRuleResponse403
from ...models.post_open_id_access_rule_response_404 import PostOpenIDAccessRuleResponse404
from ...models.post_open_id_access_rule_response_422 import PostOpenIDAccessRuleResponse422
from ...models.post_open_id_access_rule_response_500 import PostOpenIDAccessRuleResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: OpenIDAccessRuleCreate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v4/idms/open-id/{id}/access-rule".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostOpenIDAccessRuleResponse201 | PostOpenIDAccessRuleResponse400 | PostOpenIDAccessRuleResponse401 | PostOpenIDAccessRuleResponse403 | PostOpenIDAccessRuleResponse404 | PostOpenIDAccessRuleResponse422 | PostOpenIDAccessRuleResponse500 | None:
    if response.status_code == 201:
        response_201 = PostOpenIDAccessRuleResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostOpenIDAccessRuleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostOpenIDAccessRuleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostOpenIDAccessRuleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostOpenIDAccessRuleResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PostOpenIDAccessRuleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostOpenIDAccessRuleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostOpenIDAccessRuleResponse201 | PostOpenIDAccessRuleResponse400 | PostOpenIDAccessRuleResponse401 | PostOpenIDAccessRuleResponse403 | PostOpenIDAccessRuleResponse404 | PostOpenIDAccessRuleResponse422 | PostOpenIDAccessRuleResponse500]:
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
    body: OpenIDAccessRuleCreate | Unset = UNSET,

) -> Response[PostOpenIDAccessRuleResponse201 | PostOpenIDAccessRuleResponse400 | PostOpenIDAccessRuleResponse401 | PostOpenIDAccessRuleResponse403 | PostOpenIDAccessRuleResponse404 | PostOpenIDAccessRuleResponse422 | PostOpenIDAccessRuleResponse500]:
    """ Creates an openID IDMS access rules.

    Args:
        id (int):
        body (OpenIDAccessRuleCreate | Unset): OpenIDAccessRuleCreate defines the expected payload
            for creating an OpenID access rule in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOpenIDAccessRuleResponse201 | PostOpenIDAccessRuleResponse400 | PostOpenIDAccessRuleResponse401 | PostOpenIDAccessRuleResponse403 | PostOpenIDAccessRuleResponse404 | PostOpenIDAccessRuleResponse422 | PostOpenIDAccessRuleResponse500]
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
    body: OpenIDAccessRuleCreate | Unset = UNSET,

) -> PostOpenIDAccessRuleResponse201 | PostOpenIDAccessRuleResponse400 | PostOpenIDAccessRuleResponse401 | PostOpenIDAccessRuleResponse403 | PostOpenIDAccessRuleResponse404 | PostOpenIDAccessRuleResponse422 | PostOpenIDAccessRuleResponse500 | None:
    """ Creates an openID IDMS access rules.

    Args:
        id (int):
        body (OpenIDAccessRuleCreate | Unset): OpenIDAccessRuleCreate defines the expected payload
            for creating an OpenID access rule in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOpenIDAccessRuleResponse201 | PostOpenIDAccessRuleResponse400 | PostOpenIDAccessRuleResponse401 | PostOpenIDAccessRuleResponse403 | PostOpenIDAccessRuleResponse404 | PostOpenIDAccessRuleResponse422 | PostOpenIDAccessRuleResponse500
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
    body: OpenIDAccessRuleCreate | Unset = UNSET,

) -> Response[PostOpenIDAccessRuleResponse201 | PostOpenIDAccessRuleResponse400 | PostOpenIDAccessRuleResponse401 | PostOpenIDAccessRuleResponse403 | PostOpenIDAccessRuleResponse404 | PostOpenIDAccessRuleResponse422 | PostOpenIDAccessRuleResponse500]:
    """ Creates an openID IDMS access rules.

    Args:
        id (int):
        body (OpenIDAccessRuleCreate | Unset): OpenIDAccessRuleCreate defines the expected payload
            for creating an OpenID access rule in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOpenIDAccessRuleResponse201 | PostOpenIDAccessRuleResponse400 | PostOpenIDAccessRuleResponse401 | PostOpenIDAccessRuleResponse403 | PostOpenIDAccessRuleResponse404 | PostOpenIDAccessRuleResponse422 | PostOpenIDAccessRuleResponse500]
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
    body: OpenIDAccessRuleCreate | Unset = UNSET,

) -> PostOpenIDAccessRuleResponse201 | PostOpenIDAccessRuleResponse400 | PostOpenIDAccessRuleResponse401 | PostOpenIDAccessRuleResponse403 | PostOpenIDAccessRuleResponse404 | PostOpenIDAccessRuleResponse422 | PostOpenIDAccessRuleResponse500 | None:
    """ Creates an openID IDMS access rules.

    Args:
        id (int):
        body (OpenIDAccessRuleCreate | Unset): OpenIDAccessRuleCreate defines the expected payload
            for creating an OpenID access rule in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOpenIDAccessRuleResponse201 | PostOpenIDAccessRuleResponse400 | PostOpenIDAccessRuleResponse401 | PostOpenIDAccessRuleResponse403 | PostOpenIDAccessRuleResponse404 | PostOpenIDAccessRuleResponse422 | PostOpenIDAccessRuleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
