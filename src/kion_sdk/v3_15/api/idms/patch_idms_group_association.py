from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_idms_group_association_response_200 import PatchIDMSGroupAssociationResponse200
from ...models.patch_idms_group_association_response_400 import PatchIDMSGroupAssociationResponse400
from ...models.patch_idms_group_association_response_401 import PatchIDMSGroupAssociationResponse401
from ...models.patch_idms_group_association_response_403 import PatchIDMSGroupAssociationResponse403
from ...models.patch_idms_group_association_response_404 import PatchIDMSGroupAssociationResponse404
from ...models.patch_idms_group_association_response_500 import PatchIDMSGroupAssociationResponse500
from ...models.update_saml_group_association import UpdateSAMLGroupAssociation
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: UpdateSAMLGroupAssociation | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/idms/group-association/{id}".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchIDMSGroupAssociationResponse200 | PatchIDMSGroupAssociationResponse400 | PatchIDMSGroupAssociationResponse401 | PatchIDMSGroupAssociationResponse403 | PatchIDMSGroupAssociationResponse404 | PatchIDMSGroupAssociationResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchIDMSGroupAssociationResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchIDMSGroupAssociationResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchIDMSGroupAssociationResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchIDMSGroupAssociationResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchIDMSGroupAssociationResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = PatchIDMSGroupAssociationResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchIDMSGroupAssociationResponse200 | PatchIDMSGroupAssociationResponse400 | PatchIDMSGroupAssociationResponse401 | PatchIDMSGroupAssociationResponse403 | PatchIDMSGroupAssociationResponse404 | PatchIDMSGroupAssociationResponse500]:
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
    body: UpdateSAMLGroupAssociation | Unset = UNSET,

) -> Response[PatchIDMSGroupAssociationResponse200 | PatchIDMSGroupAssociationResponse400 | PatchIDMSGroupAssociationResponse401 | PatchIDMSGroupAssociationResponse403 | PatchIDMSGroupAssociationResponse404 | PatchIDMSGroupAssociationResponse500]:
    """ Updates a saml IDMS user group association from the application.

    Args:
        id (int):
        body (UpdateSAMLGroupAssociation | Unset): UpdateSAMLGroupAssociation defines an saml
            group association update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchIDMSGroupAssociationResponse200 | PatchIDMSGroupAssociationResponse400 | PatchIDMSGroupAssociationResponse401 | PatchIDMSGroupAssociationResponse403 | PatchIDMSGroupAssociationResponse404 | PatchIDMSGroupAssociationResponse500]
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
    body: UpdateSAMLGroupAssociation | Unset = UNSET,

) -> PatchIDMSGroupAssociationResponse200 | PatchIDMSGroupAssociationResponse400 | PatchIDMSGroupAssociationResponse401 | PatchIDMSGroupAssociationResponse403 | PatchIDMSGroupAssociationResponse404 | PatchIDMSGroupAssociationResponse500 | None:
    """ Updates a saml IDMS user group association from the application.

    Args:
        id (int):
        body (UpdateSAMLGroupAssociation | Unset): UpdateSAMLGroupAssociation defines an saml
            group association update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchIDMSGroupAssociationResponse200 | PatchIDMSGroupAssociationResponse400 | PatchIDMSGroupAssociationResponse401 | PatchIDMSGroupAssociationResponse403 | PatchIDMSGroupAssociationResponse404 | PatchIDMSGroupAssociationResponse500
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
    body: UpdateSAMLGroupAssociation | Unset = UNSET,

) -> Response[PatchIDMSGroupAssociationResponse200 | PatchIDMSGroupAssociationResponse400 | PatchIDMSGroupAssociationResponse401 | PatchIDMSGroupAssociationResponse403 | PatchIDMSGroupAssociationResponse404 | PatchIDMSGroupAssociationResponse500]:
    """ Updates a saml IDMS user group association from the application.

    Args:
        id (int):
        body (UpdateSAMLGroupAssociation | Unset): UpdateSAMLGroupAssociation defines an saml
            group association update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchIDMSGroupAssociationResponse200 | PatchIDMSGroupAssociationResponse400 | PatchIDMSGroupAssociationResponse401 | PatchIDMSGroupAssociationResponse403 | PatchIDMSGroupAssociationResponse404 | PatchIDMSGroupAssociationResponse500]
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
    body: UpdateSAMLGroupAssociation | Unset = UNSET,

) -> PatchIDMSGroupAssociationResponse200 | PatchIDMSGroupAssociationResponse400 | PatchIDMSGroupAssociationResponse401 | PatchIDMSGroupAssociationResponse403 | PatchIDMSGroupAssociationResponse404 | PatchIDMSGroupAssociationResponse500 | None:
    """ Updates a saml IDMS user group association from the application.

    Args:
        id (int):
        body (UpdateSAMLGroupAssociation | Unset): UpdateSAMLGroupAssociation defines an saml
            group association update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchIDMSGroupAssociationResponse200 | PatchIDMSGroupAssociationResponse400 | PatchIDMSGroupAssociationResponse401 | PatchIDMSGroupAssociationResponse403 | PatchIDMSGroupAssociationResponse404 | PatchIDMSGroupAssociationResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
