from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_saml_group_association import CreateSAMLGroupAssociation
from ...models.post_idms_group_associations_response_201 import PostIDMSGroupAssociationsResponse201
from ...models.post_idms_group_associations_response_400 import PostIDMSGroupAssociationsResponse400
from ...models.post_idms_group_associations_response_401 import PostIDMSGroupAssociationsResponse401
from ...models.post_idms_group_associations_response_403 import PostIDMSGroupAssociationsResponse403
from ...models.post_idms_group_associations_response_422 import PostIDMSGroupAssociationsResponse422
from ...models.post_idms_group_associations_response_500 import PostIDMSGroupAssociationsResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CreateSAMLGroupAssociation | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/idms/group-association",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostIDMSGroupAssociationsResponse201 | PostIDMSGroupAssociationsResponse400 | PostIDMSGroupAssociationsResponse401 | PostIDMSGroupAssociationsResponse403 | PostIDMSGroupAssociationsResponse422 | PostIDMSGroupAssociationsResponse500 | None:
    if response.status_code == 201:
        response_201 = PostIDMSGroupAssociationsResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostIDMSGroupAssociationsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostIDMSGroupAssociationsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostIDMSGroupAssociationsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostIDMSGroupAssociationsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostIDMSGroupAssociationsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostIDMSGroupAssociationsResponse201 | PostIDMSGroupAssociationsResponse400 | PostIDMSGroupAssociationsResponse401 | PostIDMSGroupAssociationsResponse403 | PostIDMSGroupAssociationsResponse422 | PostIDMSGroupAssociationsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSAMLGroupAssociation | Unset = UNSET,

) -> Response[PostIDMSGroupAssociationsResponse201 | PostIDMSGroupAssociationsResponse400 | PostIDMSGroupAssociationsResponse401 | PostIDMSGroupAssociationsResponse403 | PostIDMSGroupAssociationsResponse422 | PostIDMSGroupAssociationsResponse500]:
    """ Stores a saml IDMS user group association.

    Args:
        body (CreateSAMLGroupAssociation | Unset): CreateSAMLGroupAssociation defines an saml
            group association creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostIDMSGroupAssociationsResponse201 | PostIDMSGroupAssociationsResponse400 | PostIDMSGroupAssociationsResponse401 | PostIDMSGroupAssociationsResponse403 | PostIDMSGroupAssociationsResponse422 | PostIDMSGroupAssociationsResponse500]
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
    body: CreateSAMLGroupAssociation | Unset = UNSET,

) -> PostIDMSGroupAssociationsResponse201 | PostIDMSGroupAssociationsResponse400 | PostIDMSGroupAssociationsResponse401 | PostIDMSGroupAssociationsResponse403 | PostIDMSGroupAssociationsResponse422 | PostIDMSGroupAssociationsResponse500 | None:
    """ Stores a saml IDMS user group association.

    Args:
        body (CreateSAMLGroupAssociation | Unset): CreateSAMLGroupAssociation defines an saml
            group association creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostIDMSGroupAssociationsResponse201 | PostIDMSGroupAssociationsResponse400 | PostIDMSGroupAssociationsResponse401 | PostIDMSGroupAssociationsResponse403 | PostIDMSGroupAssociationsResponse422 | PostIDMSGroupAssociationsResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSAMLGroupAssociation | Unset = UNSET,

) -> Response[PostIDMSGroupAssociationsResponse201 | PostIDMSGroupAssociationsResponse400 | PostIDMSGroupAssociationsResponse401 | PostIDMSGroupAssociationsResponse403 | PostIDMSGroupAssociationsResponse422 | PostIDMSGroupAssociationsResponse500]:
    """ Stores a saml IDMS user group association.

    Args:
        body (CreateSAMLGroupAssociation | Unset): CreateSAMLGroupAssociation defines an saml
            group association creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostIDMSGroupAssociationsResponse201 | PostIDMSGroupAssociationsResponse400 | PostIDMSGroupAssociationsResponse401 | PostIDMSGroupAssociationsResponse403 | PostIDMSGroupAssociationsResponse422 | PostIDMSGroupAssociationsResponse500]
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
    body: CreateSAMLGroupAssociation | Unset = UNSET,

) -> PostIDMSGroupAssociationsResponse201 | PostIDMSGroupAssociationsResponse400 | PostIDMSGroupAssociationsResponse401 | PostIDMSGroupAssociationsResponse403 | PostIDMSGroupAssociationsResponse422 | PostIDMSGroupAssociationsResponse500 | None:
    """ Stores a saml IDMS user group association.

    Args:
        body (CreateSAMLGroupAssociation | Unset): CreateSAMLGroupAssociation defines an saml
            group association creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostIDMSGroupAssociationsResponse201 | PostIDMSGroupAssociationsResponse400 | PostIDMSGroupAssociationsResponse401 | PostIDMSGroupAssociationsResponse403 | PostIDMSGroupAssociationsResponse422 | PostIDMSGroupAssociationsResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
