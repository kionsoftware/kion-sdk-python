from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.open_id_access_rule_update import OpenIDAccessRuleUpdate
from ...models.patch_open_id_access_rule_response_200 import PatchOpenIDAccessRuleResponse200
from ...models.patch_open_id_access_rule_response_400 import PatchOpenIDAccessRuleResponse400
from ...models.patch_open_id_access_rule_response_401 import PatchOpenIDAccessRuleResponse401
from ...models.patch_open_id_access_rule_response_403 import PatchOpenIDAccessRuleResponse403
from ...models.patch_open_id_access_rule_response_404 import PatchOpenIDAccessRuleResponse404
from ...models.patch_open_id_access_rule_response_422 import PatchOpenIDAccessRuleResponse422
from ...models.patch_open_id_access_rule_response_500 import PatchOpenIDAccessRuleResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: OpenIDAccessRuleUpdate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v4/idms/open-id/access-rule/{id}".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchOpenIDAccessRuleResponse200 | PatchOpenIDAccessRuleResponse400 | PatchOpenIDAccessRuleResponse401 | PatchOpenIDAccessRuleResponse403 | PatchOpenIDAccessRuleResponse404 | PatchOpenIDAccessRuleResponse422 | PatchOpenIDAccessRuleResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchOpenIDAccessRuleResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchOpenIDAccessRuleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchOpenIDAccessRuleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchOpenIDAccessRuleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchOpenIDAccessRuleResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchOpenIDAccessRuleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchOpenIDAccessRuleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchOpenIDAccessRuleResponse200 | PatchOpenIDAccessRuleResponse400 | PatchOpenIDAccessRuleResponse401 | PatchOpenIDAccessRuleResponse403 | PatchOpenIDAccessRuleResponse404 | PatchOpenIDAccessRuleResponse422 | PatchOpenIDAccessRuleResponse500]:
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
    body: OpenIDAccessRuleUpdate | Unset = UNSET,

) -> Response[PatchOpenIDAccessRuleResponse200 | PatchOpenIDAccessRuleResponse400 | PatchOpenIDAccessRuleResponse401 | PatchOpenIDAccessRuleResponse403 | PatchOpenIDAccessRuleResponse404 | PatchOpenIDAccessRuleResponse422 | PatchOpenIDAccessRuleResponse500]:
    """ Updates an openID IDMS access rule in the application.

    Args:
        id (int):
        body (OpenIDAccessRuleUpdate | Unset): OpenIDAccessRuleUpdate defines the expected payload
            for updating an OpenID access rule in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchOpenIDAccessRuleResponse200 | PatchOpenIDAccessRuleResponse400 | PatchOpenIDAccessRuleResponse401 | PatchOpenIDAccessRuleResponse403 | PatchOpenIDAccessRuleResponse404 | PatchOpenIDAccessRuleResponse422 | PatchOpenIDAccessRuleResponse500]
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
    body: OpenIDAccessRuleUpdate | Unset = UNSET,

) -> PatchOpenIDAccessRuleResponse200 | PatchOpenIDAccessRuleResponse400 | PatchOpenIDAccessRuleResponse401 | PatchOpenIDAccessRuleResponse403 | PatchOpenIDAccessRuleResponse404 | PatchOpenIDAccessRuleResponse422 | PatchOpenIDAccessRuleResponse500 | None:
    """ Updates an openID IDMS access rule in the application.

    Args:
        id (int):
        body (OpenIDAccessRuleUpdate | Unset): OpenIDAccessRuleUpdate defines the expected payload
            for updating an OpenID access rule in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchOpenIDAccessRuleResponse200 | PatchOpenIDAccessRuleResponse400 | PatchOpenIDAccessRuleResponse401 | PatchOpenIDAccessRuleResponse403 | PatchOpenIDAccessRuleResponse404 | PatchOpenIDAccessRuleResponse422 | PatchOpenIDAccessRuleResponse500
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
    body: OpenIDAccessRuleUpdate | Unset = UNSET,

) -> Response[PatchOpenIDAccessRuleResponse200 | PatchOpenIDAccessRuleResponse400 | PatchOpenIDAccessRuleResponse401 | PatchOpenIDAccessRuleResponse403 | PatchOpenIDAccessRuleResponse404 | PatchOpenIDAccessRuleResponse422 | PatchOpenIDAccessRuleResponse500]:
    """ Updates an openID IDMS access rule in the application.

    Args:
        id (int):
        body (OpenIDAccessRuleUpdate | Unset): OpenIDAccessRuleUpdate defines the expected payload
            for updating an OpenID access rule in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchOpenIDAccessRuleResponse200 | PatchOpenIDAccessRuleResponse400 | PatchOpenIDAccessRuleResponse401 | PatchOpenIDAccessRuleResponse403 | PatchOpenIDAccessRuleResponse404 | PatchOpenIDAccessRuleResponse422 | PatchOpenIDAccessRuleResponse500]
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
    body: OpenIDAccessRuleUpdate | Unset = UNSET,

) -> PatchOpenIDAccessRuleResponse200 | PatchOpenIDAccessRuleResponse400 | PatchOpenIDAccessRuleResponse401 | PatchOpenIDAccessRuleResponse403 | PatchOpenIDAccessRuleResponse404 | PatchOpenIDAccessRuleResponse422 | PatchOpenIDAccessRuleResponse500 | None:
    """ Updates an openID IDMS access rule in the application.

    Args:
        id (int):
        body (OpenIDAccessRuleUpdate | Unset): OpenIDAccessRuleUpdate defines the expected payload
            for updating an OpenID access rule in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchOpenIDAccessRuleResponse200 | PatchOpenIDAccessRuleResponse400 | PatchOpenIDAccessRuleResponse401 | PatchOpenIDAccessRuleResponse403 | PatchOpenIDAccessRuleResponse404 | PatchOpenIDAccessRuleResponse422 | PatchOpenIDAccessRuleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
