# coding: utf-8

"""
    Kinde Management API

    Provides endpoints to manage your Kinde Businesses  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@kinde.com
    Generated by: https://openapi-generator.tech
"""

from kinde_sdk.paths.api_v1_user.post import CreateUser
from kinde_sdk.paths.api_v1_user.delete import DeleteUser
from kinde_sdk.paths.api_v1_user.get import GetUserData
from kinde_sdk.paths.api_v1_users.get import GetUsers
from kinde_sdk.paths.api_v1_users_user_id_refresh_claims.post import RefreshUserClaims
from kinde_sdk.paths.api_v1_user.patch import UpdateUser
from kinde_sdk.paths.api_v1_users_user_id_feature_flags_feature_flag_key.patch import UpdateUserFeatureFlagOverride


class UsersApi(
    CreateUser,
    DeleteUser,
    GetUserData,
    GetUsers,
    RefreshUserClaims,
    UpdateUser,
    UpdateUserFeatureFlagOverride,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
