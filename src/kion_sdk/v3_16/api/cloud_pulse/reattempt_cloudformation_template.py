from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reattempt_cloudformation_template_response_400 import ReattemptCloudformationTemplateResponse400
from ...models.reattempt_cloudformation_template_response_401 import ReattemptCloudformationTemplateResponse401
from ...models.reattempt_cloudformation_template_response_403 import ReattemptCloudformationTemplateResponse403
from ...models.reattempt_cloudformation_template_response_500 import ReattemptCloudformationTemplateResponse500
from ...models.reattempt_cloudformation_template_status import ReattemptCloudformationTemplateStatus
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    cloudformation_template_id: int,
    *,
    region: str | Unset = UNSET,
    delete_and_create: bool | Unset = UNSET,
    status: ReattemptCloudformationTemplateStatus | Unset = UNSET,
    account_ids: str | Unset = UNSET,
    account_ids_exclusive: bool | Unset = UNSET,
    cft_ids: str | Unset = UNSET,
    cft_ids_exclusive: bool | Unset = UNSET,
    cloud_rule_ids: str | Unset = UNSET,
    cloud_rule_ids_exclusive: bool | Unset = UNSET,
    project_ids: str | Unset = UNSET,
    project_ids_exclusive: bool | Unset = UNSET,
    ou_ids: str | Unset = UNSET,
    ou_ids_exclusive: bool | Unset = UNSET,
    ou_direct_descendants_only: bool | Unset = UNSET,
    keyword: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["region"] = region

    params["delete_and_create"] = delete_and_create

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["account_ids"] = account_ids

    params["account_ids_exclusive"] = account_ids_exclusive

    params["cft_ids"] = cft_ids

    params["cft_ids_exclusive"] = cft_ids_exclusive

    params["cloud_rule_ids"] = cloud_rule_ids

    params["cloud_rule_ids_exclusive"] = cloud_rule_ids_exclusive

    params["project_ids"] = project_ids

    params["project_ids_exclusive"] = project_ids_exclusive

    params["ou_ids"] = ou_ids

    params["ou_ids_exclusive"] = ou_ids_exclusive

    params["ou_direct_descendants_only"] = ou_direct_descendants_only

    params["keyword"] = keyword


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/cloud-pulse/{cloudformation_template_id}/reattempt".format(cloudformation_template_id=quote(str(cloudformation_template_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ReattemptCloudformationTemplateResponse400 | ReattemptCloudformationTemplateResponse401 | ReattemptCloudformationTemplateResponse403 | ReattemptCloudformationTemplateResponse500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ReattemptCloudformationTemplateResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ReattemptCloudformationTemplateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ReattemptCloudformationTemplateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = ReattemptCloudformationTemplateResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ReattemptCloudformationTemplateResponse400 | ReattemptCloudformationTemplateResponse401 | ReattemptCloudformationTemplateResponse403 | ReattemptCloudformationTemplateResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cloudformation_template_id: int,
    *,
    client: AuthenticatedClient,
    region: str | Unset = UNSET,
    delete_and_create: bool | Unset = UNSET,
    status: ReattemptCloudformationTemplateStatus | Unset = UNSET,
    account_ids: str | Unset = UNSET,
    account_ids_exclusive: bool | Unset = UNSET,
    cft_ids: str | Unset = UNSET,
    cft_ids_exclusive: bool | Unset = UNSET,
    cloud_rule_ids: str | Unset = UNSET,
    cloud_rule_ids_exclusive: bool | Unset = UNSET,
    project_ids: str | Unset = UNSET,
    project_ids_exclusive: bool | Unset = UNSET,
    ou_ids: str | Unset = UNSET,
    ou_ids_exclusive: bool | Unset = UNSET,
    ou_direct_descendants_only: bool | Unset = UNSET,
    keyword: str | Unset = UNSET,

) -> Response[Any | ReattemptCloudformationTemplateResponse400 | ReattemptCloudformationTemplateResponse401 | ReattemptCloudformationTemplateResponse403 | ReattemptCloudformationTemplateResponse500]:
    """ Reattempts the deployment of CloudFormation templates.

    Args:
        cloudformation_template_id (int):
        region (str | Unset):
        delete_and_create (bool | Unset):
        status (ReattemptCloudformationTemplateStatus | Unset):
        account_ids (str | Unset):
        account_ids_exclusive (bool | Unset):
        cft_ids (str | Unset):
        cft_ids_exclusive (bool | Unset):
        cloud_rule_ids (str | Unset):
        cloud_rule_ids_exclusive (bool | Unset):
        project_ids (str | Unset):
        project_ids_exclusive (bool | Unset):
        ou_ids (str | Unset):
        ou_ids_exclusive (bool | Unset):
        ou_direct_descendants_only (bool | Unset):
        keyword (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReattemptCloudformationTemplateResponse400 | ReattemptCloudformationTemplateResponse401 | ReattemptCloudformationTemplateResponse403 | ReattemptCloudformationTemplateResponse500]
     """


    kwargs = _get_kwargs(
        cloudformation_template_id=cloudformation_template_id,
region=region,
delete_and_create=delete_and_create,
status=status,
account_ids=account_ids,
account_ids_exclusive=account_ids_exclusive,
cft_ids=cft_ids,
cft_ids_exclusive=cft_ids_exclusive,
cloud_rule_ids=cloud_rule_ids,
cloud_rule_ids_exclusive=cloud_rule_ids_exclusive,
project_ids=project_ids,
project_ids_exclusive=project_ids_exclusive,
ou_ids=ou_ids,
ou_ids_exclusive=ou_ids_exclusive,
ou_direct_descendants_only=ou_direct_descendants_only,
keyword=keyword,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    cloudformation_template_id: int,
    *,
    client: AuthenticatedClient,
    region: str | Unset = UNSET,
    delete_and_create: bool | Unset = UNSET,
    status: ReattemptCloudformationTemplateStatus | Unset = UNSET,
    account_ids: str | Unset = UNSET,
    account_ids_exclusive: bool | Unset = UNSET,
    cft_ids: str | Unset = UNSET,
    cft_ids_exclusive: bool | Unset = UNSET,
    cloud_rule_ids: str | Unset = UNSET,
    cloud_rule_ids_exclusive: bool | Unset = UNSET,
    project_ids: str | Unset = UNSET,
    project_ids_exclusive: bool | Unset = UNSET,
    ou_ids: str | Unset = UNSET,
    ou_ids_exclusive: bool | Unset = UNSET,
    ou_direct_descendants_only: bool | Unset = UNSET,
    keyword: str | Unset = UNSET,

) -> Any | ReattemptCloudformationTemplateResponse400 | ReattemptCloudformationTemplateResponse401 | ReattemptCloudformationTemplateResponse403 | ReattemptCloudformationTemplateResponse500 | None:
    """ Reattempts the deployment of CloudFormation templates.

    Args:
        cloudformation_template_id (int):
        region (str | Unset):
        delete_and_create (bool | Unset):
        status (ReattemptCloudformationTemplateStatus | Unset):
        account_ids (str | Unset):
        account_ids_exclusive (bool | Unset):
        cft_ids (str | Unset):
        cft_ids_exclusive (bool | Unset):
        cloud_rule_ids (str | Unset):
        cloud_rule_ids_exclusive (bool | Unset):
        project_ids (str | Unset):
        project_ids_exclusive (bool | Unset):
        ou_ids (str | Unset):
        ou_ids_exclusive (bool | Unset):
        ou_direct_descendants_only (bool | Unset):
        keyword (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReattemptCloudformationTemplateResponse400 | ReattemptCloudformationTemplateResponse401 | ReattemptCloudformationTemplateResponse403 | ReattemptCloudformationTemplateResponse500
     """


    return sync_detailed(
        cloudformation_template_id=cloudformation_template_id,
client=client,
region=region,
delete_and_create=delete_and_create,
status=status,
account_ids=account_ids,
account_ids_exclusive=account_ids_exclusive,
cft_ids=cft_ids,
cft_ids_exclusive=cft_ids_exclusive,
cloud_rule_ids=cloud_rule_ids,
cloud_rule_ids_exclusive=cloud_rule_ids_exclusive,
project_ids=project_ids,
project_ids_exclusive=project_ids_exclusive,
ou_ids=ou_ids,
ou_ids_exclusive=ou_ids_exclusive,
ou_direct_descendants_only=ou_direct_descendants_only,
keyword=keyword,

    ).parsed

async def asyncio_detailed(
    cloudformation_template_id: int,
    *,
    client: AuthenticatedClient,
    region: str | Unset = UNSET,
    delete_and_create: bool | Unset = UNSET,
    status: ReattemptCloudformationTemplateStatus | Unset = UNSET,
    account_ids: str | Unset = UNSET,
    account_ids_exclusive: bool | Unset = UNSET,
    cft_ids: str | Unset = UNSET,
    cft_ids_exclusive: bool | Unset = UNSET,
    cloud_rule_ids: str | Unset = UNSET,
    cloud_rule_ids_exclusive: bool | Unset = UNSET,
    project_ids: str | Unset = UNSET,
    project_ids_exclusive: bool | Unset = UNSET,
    ou_ids: str | Unset = UNSET,
    ou_ids_exclusive: bool | Unset = UNSET,
    ou_direct_descendants_only: bool | Unset = UNSET,
    keyword: str | Unset = UNSET,

) -> Response[Any | ReattemptCloudformationTemplateResponse400 | ReattemptCloudformationTemplateResponse401 | ReattemptCloudformationTemplateResponse403 | ReattemptCloudformationTemplateResponse500]:
    """ Reattempts the deployment of CloudFormation templates.

    Args:
        cloudformation_template_id (int):
        region (str | Unset):
        delete_and_create (bool | Unset):
        status (ReattemptCloudformationTemplateStatus | Unset):
        account_ids (str | Unset):
        account_ids_exclusive (bool | Unset):
        cft_ids (str | Unset):
        cft_ids_exclusive (bool | Unset):
        cloud_rule_ids (str | Unset):
        cloud_rule_ids_exclusive (bool | Unset):
        project_ids (str | Unset):
        project_ids_exclusive (bool | Unset):
        ou_ids (str | Unset):
        ou_ids_exclusive (bool | Unset):
        ou_direct_descendants_only (bool | Unset):
        keyword (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReattemptCloudformationTemplateResponse400 | ReattemptCloudformationTemplateResponse401 | ReattemptCloudformationTemplateResponse403 | ReattemptCloudformationTemplateResponse500]
     """


    kwargs = _get_kwargs(
        cloudformation_template_id=cloudformation_template_id,
region=region,
delete_and_create=delete_and_create,
status=status,
account_ids=account_ids,
account_ids_exclusive=account_ids_exclusive,
cft_ids=cft_ids,
cft_ids_exclusive=cft_ids_exclusive,
cloud_rule_ids=cloud_rule_ids,
cloud_rule_ids_exclusive=cloud_rule_ids_exclusive,
project_ids=project_ids,
project_ids_exclusive=project_ids_exclusive,
ou_ids=ou_ids,
ou_ids_exclusive=ou_ids_exclusive,
ou_direct_descendants_only=ou_direct_descendants_only,
keyword=keyword,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    cloudformation_template_id: int,
    *,
    client: AuthenticatedClient,
    region: str | Unset = UNSET,
    delete_and_create: bool | Unset = UNSET,
    status: ReattemptCloudformationTemplateStatus | Unset = UNSET,
    account_ids: str | Unset = UNSET,
    account_ids_exclusive: bool | Unset = UNSET,
    cft_ids: str | Unset = UNSET,
    cft_ids_exclusive: bool | Unset = UNSET,
    cloud_rule_ids: str | Unset = UNSET,
    cloud_rule_ids_exclusive: bool | Unset = UNSET,
    project_ids: str | Unset = UNSET,
    project_ids_exclusive: bool | Unset = UNSET,
    ou_ids: str | Unset = UNSET,
    ou_ids_exclusive: bool | Unset = UNSET,
    ou_direct_descendants_only: bool | Unset = UNSET,
    keyword: str | Unset = UNSET,

) -> Any | ReattemptCloudformationTemplateResponse400 | ReattemptCloudformationTemplateResponse401 | ReattemptCloudformationTemplateResponse403 | ReattemptCloudformationTemplateResponse500 | None:
    """ Reattempts the deployment of CloudFormation templates.

    Args:
        cloudformation_template_id (int):
        region (str | Unset):
        delete_and_create (bool | Unset):
        status (ReattemptCloudformationTemplateStatus | Unset):
        account_ids (str | Unset):
        account_ids_exclusive (bool | Unset):
        cft_ids (str | Unset):
        cft_ids_exclusive (bool | Unset):
        cloud_rule_ids (str | Unset):
        cloud_rule_ids_exclusive (bool | Unset):
        project_ids (str | Unset):
        project_ids_exclusive (bool | Unset):
        ou_ids (str | Unset):
        ou_ids_exclusive (bool | Unset):
        ou_direct_descendants_only (bool | Unset):
        keyword (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReattemptCloudformationTemplateResponse400 | ReattemptCloudformationTemplateResponse401 | ReattemptCloudformationTemplateResponse403 | ReattemptCloudformationTemplateResponse500
     """


    return (await asyncio_detailed(
        cloudformation_template_id=cloudformation_template_id,
client=client,
region=region,
delete_and_create=delete_and_create,
status=status,
account_ids=account_ids,
account_ids_exclusive=account_ids_exclusive,
cft_ids=cft_ids,
cft_ids_exclusive=cft_ids_exclusive,
cloud_rule_ids=cloud_rule_ids,
cloud_rule_ids_exclusive=cloud_rule_ids_exclusive,
project_ids=project_ids,
project_ids_exclusive=project_ids_exclusive,
ou_ids=ou_ids,
ou_ids_exclusive=ou_ids_exclusive,
ou_direct_descendants_only=ou_direct_descendants_only,
keyword=keyword,

    )).parsed
