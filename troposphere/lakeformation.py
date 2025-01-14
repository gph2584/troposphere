# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean


class ColumnWildcard(AWSProperty):
    """
    `ColumnWildcard <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-columnwildcard.html>`__
    """

    props: PropsDictType = {
        "ExcludedColumnNames": ([str], False),
    }


class RowFilter(AWSProperty):
    """
    `RowFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html>`__
    """

    props: PropsDictType = {
        "AllRowsWildcard": (dict, False),
        "FilterExpression": (str, False),
    }


class DataCellsFilter(AWSObject):
    """
    `DataCellsFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html>`__
    """

    resource_type = "AWS::LakeFormation::DataCellsFilter"

    props: PropsDictType = {
        "ColumnNames": ([str], False),
        "ColumnWildcard": (ColumnWildcard, False),
        "DatabaseName": (str, True),
        "Name": (str, True),
        "RowFilter": (RowFilter, False),
        "TableCatalogId": (str, True),
        "TableName": (str, True),
    }


class DataLakePrincipal(AWSProperty):
    """
    `DataLakePrincipal <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalakeprincipal.html>`__
    """

    props: PropsDictType = {
        "DataLakePrincipalIdentifier": (str, False),
    }


class DataLakeSettings(AWSObject):
    """
    `DataLakeSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html>`__
    """

    resource_type = "AWS::LakeFormation::DataLakeSettings"

    props: PropsDictType = {
        "Admins": ([DataLakePrincipal], False),
        "AllowExternalDataFiltering": (boolean, False),
        "AllowFullTableExternalDataAccess": (boolean, False),
        "AuthorizedSessionTagValueList": ([str], False),
        "CreateDatabaseDefaultPermissions": ([], False),
        "CreateTableDefaultPermissions": ([], False),
        "ExternalDataFilteringAllowList": ([], False),
        "MutationType": (str, False),
        "Parameters": (dict, False),
        "TrustedResourceOwners": ([str], False),
    }


class DatabaseResource(AWSProperty):
    """
    `DatabaseResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html>`__
    """

    props: PropsDictType = {
        "CatalogId": (str, True),
        "Name": (str, True),
    }


class PermissionsDataLocationResource(AWSProperty):
    """
    `PermissionsDataLocationResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html>`__
    """

    props: PropsDictType = {
        "CatalogId": (str, False),
        "S3Resource": (str, False),
    }


class TableResource(AWSProperty):
    """
    `TableResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html>`__
    """

    props: PropsDictType = {
        "CatalogId": (str, True),
        "DatabaseName": (str, True),
        "Name": (str, False),
        "TableWildcard": (dict, False),
    }


class TableWithColumnsResource(AWSProperty):
    """
    `TableWithColumnsResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html>`__
    """

    props: PropsDictType = {
        "CatalogId": (str, True),
        "ColumnNames": ([str], False),
        "ColumnWildcard": (ColumnWildcard, False),
        "DatabaseName": (str, True),
        "Name": (str, True),
    }


class ResourceProperty(AWSProperty):
    """
    `ResourceProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html>`__
    """

    props: PropsDictType = {
        "DataLocationResource": (PermissionsDataLocationResource, False),
        "DatabaseResource": (DatabaseResource, False),
        "TableResource": (TableResource, False),
        "TableWithColumnsResource": (TableWithColumnsResource, False),
    }


class Permissions(AWSObject):
    """
    `Permissions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html>`__
    """

    resource_type = "AWS::LakeFormation::Permissions"

    props: PropsDictType = {
        "DataLakePrincipal": (DataLakePrincipal, True),
        "Permissions": ([str], False),
        "PermissionsWithGrantOption": ([str], False),
        "Resource": (ResourceProperty, True),
    }


class DataCellsFilterResource(AWSProperty):
    """
    `DataCellsFilterResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html>`__
    """

    props: PropsDictType = {
        "DatabaseName": (str, True),
        "Name": (str, True),
        "TableCatalogId": (str, True),
        "TableName": (str, True),
    }


class DataLocationResource(AWSProperty):
    """
    `DataLocationResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html>`__
    """

    props: PropsDictType = {
        "CatalogId": (str, True),
        "ResourceArn": (str, True),
    }


class LFTagKeyResource(AWSProperty):
    """
    `LFTagKeyResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html>`__
    """

    props: PropsDictType = {
        "CatalogId": (str, True),
        "TagKey": (str, True),
        "TagValues": ([str], True),
    }


class LFTag(AWSProperty):
    """
    `LFTag <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html>`__
    """

    props: PropsDictType = {
        "TagKey": (str, False),
        "TagValues": ([str], False),
    }


class LFTagPolicyResource(AWSProperty):
    """
    `LFTagPolicyResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html>`__
    """

    props: PropsDictType = {
        "CatalogId": (str, True),
        "Expression": ([LFTag], True),
        "ResourceType": (str, True),
    }


class PrincipalResource(AWSProperty):
    """
    `PrincipalResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html>`__
    """

    props: PropsDictType = {
        "Catalog": (dict, False),
        "DataCellsFilter": (DataCellsFilterResource, False),
        "DataLocation": (DataLocationResource, False),
        "Database": (DatabaseResource, False),
        "LFTag": (LFTagKeyResource, False),
        "LFTagPolicy": (LFTagPolicyResource, False),
        "Table": (TableResource, False),
        "TableWithColumns": (TableWithColumnsResource, False),
    }


class PrincipalPermissions(AWSObject):
    """
    `PrincipalPermissions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html>`__
    """

    resource_type = "AWS::LakeFormation::PrincipalPermissions"

    props: PropsDictType = {
        "Catalog": (str, False),
        "Permissions": ([str], True),
        "PermissionsWithGrantOption": ([str], True),
        "Principal": (DataLakePrincipal, True),
        "Resource": (PrincipalResource, True),
    }


class Resource(AWSObject):
    """
    `Resource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html>`__
    """

    resource_type = "AWS::LakeFormation::Resource"

    props: PropsDictType = {
        "HybridAccessEnabled": (boolean, False),
        "ResourceArn": (str, True),
        "RoleArn": (str, False),
        "UseServiceLinkedRole": (boolean, True),
        "WithFederation": (boolean, False),
    }


class Tag(AWSObject):
    """
    `Tag <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html>`__
    """

    resource_type = "AWS::LakeFormation::Tag"

    props: PropsDictType = {
        "CatalogId": (str, False),
        "TagKey": (str, True),
        "TagValues": ([str], True),
    }


class LFTagPair(AWSProperty):
    """
    `LFTagPair <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html>`__
    """

    props: PropsDictType = {
        "CatalogId": (str, True),
        "TagKey": (str, True),
        "TagValues": ([str], True),
    }


class TagAssociationTableWithColumnsResource(AWSProperty):
    """
    `TagAssociationTableWithColumnsResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html>`__
    """

    props: PropsDictType = {
        "CatalogId": (str, True),
        "ColumnNames": ([str], True),
        "DatabaseName": (str, True),
        "Name": (str, True),
    }


class TagAssociationResource(AWSProperty):
    """
    `TagAssociationResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html>`__
    """

    props: PropsDictType = {
        "Catalog": (dict, False),
        "Database": (DatabaseResource, False),
        "Table": (TableResource, False),
        "TableWithColumns": (TagAssociationTableWithColumnsResource, False),
    }


class TagAssociation(AWSObject):
    """
    `TagAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html>`__
    """

    resource_type = "AWS::LakeFormation::TagAssociation"

    props: PropsDictType = {
        "LFTags": ([LFTagPair], True),
        "Resource": (TagAssociationResource, True),
    }


class PrincipalPermissionsProperty(AWSProperty):
    """
    `PrincipalPermissionsProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-principalpermissions.html>`__
    """

    props: PropsDictType = {
        "Permissions": ([str], True),
        "Principal": (DataLakePrincipal, True),
    }


class TableWildcard(AWSProperty):
    """
    `TableWildcard <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewildcard.html>`__
    """

    props: PropsDictType = {}
