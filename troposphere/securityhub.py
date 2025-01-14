# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, double, integer


class NoteUpdate(AWSProperty):
    """
    `NoteUpdate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-noteupdate.html>`__
    """

    props: PropsDictType = {
        "Text": (str, True),
        "UpdatedBy": (dict, True),
    }


class RelatedFinding(AWSProperty):
    """
    `RelatedFinding <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-relatedfinding.html>`__
    """

    props: PropsDictType = {
        "Id": (dict, True),
        "ProductArn": (str, True),
    }


class SeverityUpdate(AWSProperty):
    """
    `SeverityUpdate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-severityupdate.html>`__
    """

    props: PropsDictType = {
        "Label": (str, False),
        "Normalized": (integer, False),
        "Product": (double, False),
    }


class WorkflowUpdate(AWSProperty):
    """
    `WorkflowUpdate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-workflowupdate.html>`__
    """

    props: PropsDictType = {
        "Status": (str, True),
    }


class AutomationRulesFindingFieldsUpdate(AWSProperty):
    """
    `AutomationRulesFindingFieldsUpdate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html>`__
    """

    props: PropsDictType = {
        "Confidence": (integer, False),
        "Criticality": (integer, False),
        "Note": (NoteUpdate, False),
        "RelatedFindings": ([RelatedFinding], False),
        "Severity": (SeverityUpdate, False),
        "Types": ([str], False),
        "UserDefinedFields": (dict, False),
        "VerificationState": (str, False),
        "Workflow": (WorkflowUpdate, False),
    }


class AutomationRulesAction(AWSProperty):
    """
    `AutomationRulesAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesaction.html>`__
    """

    props: PropsDictType = {
        "FindingFieldsUpdate": (AutomationRulesFindingFieldsUpdate, True),
        "Type": (str, True),
    }


class DateRange(AWSProperty):
    """
    `DateRange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-daterange.html>`__
    """

    props: PropsDictType = {
        "Unit": (str, True),
        "Value": (double, True),
    }


class DateFilter(AWSProperty):
    """
    `DateFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-datefilter.html>`__
    """

    props: PropsDictType = {
        "DateRange": (DateRange, False),
        "End": (str, False),
        "Start": (str, False),
    }


class MapFilter(AWSProperty):
    """
    `MapFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-mapfilter.html>`__
    """

    props: PropsDictType = {
        "Comparison": (str, True),
        "Key": (str, True),
        "Value": (str, True),
    }


class NumberFilter(AWSProperty):
    """
    `NumberFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-numberfilter.html>`__
    """

    props: PropsDictType = {
        "Eq": (double, False),
        "Gte": (double, False),
        "Lte": (double, False),
    }


class StringFilter(AWSProperty):
    """
    `StringFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-stringfilter.html>`__
    """

    props: PropsDictType = {
        "Comparison": (str, True),
        "Value": (str, True),
    }


class AutomationRulesFindingFilters(AWSProperty):
    """
    `AutomationRulesFindingFilters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html>`__
    """

    props: PropsDictType = {
        "AwsAccountId": ([StringFilter], False),
        "CompanyName": ([StringFilter], False),
        "ComplianceAssociatedStandardsId": ([StringFilter], False),
        "ComplianceSecurityControlId": ([StringFilter], False),
        "ComplianceStatus": ([StringFilter], False),
        "Confidence": ([NumberFilter], False),
        "CreatedAt": ([DateFilter], False),
        "Criticality": ([NumberFilter], False),
        "Description": ([StringFilter], False),
        "FirstObservedAt": ([DateFilter], False),
        "GeneratorId": ([StringFilter], False),
        "Id": ([StringFilter], False),
        "LastObservedAt": ([DateFilter], False),
        "NoteText": ([StringFilter], False),
        "NoteUpdatedAt": ([DateFilter], False),
        "NoteUpdatedBy": ([StringFilter], False),
        "ProductArn": ([StringFilter], False),
        "ProductName": ([StringFilter], False),
        "RecordState": ([StringFilter], False),
        "RelatedFindingsId": ([StringFilter], False),
        "RelatedFindingsProductArn": ([StringFilter], False),
        "ResourceDetailsOther": ([MapFilter], False),
        "ResourceId": ([StringFilter], False),
        "ResourcePartition": ([StringFilter], False),
        "ResourceRegion": ([StringFilter], False),
        "ResourceTags": ([MapFilter], False),
        "ResourceType": ([StringFilter], False),
        "SeverityLabel": ([StringFilter], False),
        "SourceUrl": ([StringFilter], False),
        "Title": ([StringFilter], False),
        "Type": ([StringFilter], False),
        "UpdatedAt": ([DateFilter], False),
        "UserDefinedFields": ([MapFilter], False),
        "VerificationState": ([StringFilter], False),
        "WorkflowStatus": ([StringFilter], False),
    }


class AutomationRule(AWSObject):
    """
    `AutomationRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html>`__
    """

    resource_type = "AWS::SecurityHub::AutomationRule"

    props: PropsDictType = {
        "Actions": ([AutomationRulesAction], True),
        "Criteria": (AutomationRulesFindingFilters, True),
        "Description": (str, True),
        "IsTerminal": (boolean, False),
        "RuleName": (str, True),
        "RuleOrder": (integer, True),
        "RuleStatus": (str, False),
        "Tags": (dict, False),
    }


class ParameterValue(AWSProperty):
    """
    `ParameterValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-securitycontrol-parametervalue.html>`__
    """

    props: PropsDictType = {
        "Boolean": (boolean, False),
        "Double": (double, False),
        "Enum": (str, False),
        "EnumList": ([str], False),
        "Integer": (integer, False),
        "IntegerList": ([integer], False),
        "String": (str, False),
        "StringList": ([str], False),
    }


class ParameterConfiguration(AWSProperty):
    """
    `ParameterConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-securitycontrol-parameterconfiguration.html>`__
    """

    props: PropsDictType = {
        "Value": (ParameterValue, False),
        "ValueType": (str, True),
    }


class SecurityControlCustomParameter(AWSProperty):
    """
    `SecurityControlCustomParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-configurationpolicy-securitycontrolcustomparameter.html>`__
    """

    props: PropsDictType = {
        "Parameters": (dict, False),
        "SecurityControlId": (str, False),
    }


class SecurityControlsConfiguration(AWSProperty):
    """
    `SecurityControlsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-configurationpolicy-securitycontrolsconfiguration.html>`__
    """

    props: PropsDictType = {
        "DisabledSecurityControlIdentifiers": ([str], False),
        "EnabledSecurityControlIdentifiers": ([str], False),
        "SecurityControlCustomParameters": ([SecurityControlCustomParameter], False),
    }


class SecurityHubPolicy(AWSProperty):
    """
    `SecurityHubPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-configurationpolicy-securityhubpolicy.html>`__
    """

    props: PropsDictType = {
        "EnabledStandardIdentifiers": ([str], False),
        "SecurityControlsConfiguration": (SecurityControlsConfiguration, False),
        "ServiceEnabled": (boolean, False),
    }


class Policy(AWSProperty):
    """
    `Policy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-configurationpolicy-policy.html>`__
    """

    props: PropsDictType = {
        "SecurityHub": (SecurityHubPolicy, False),
    }


class ConfigurationPolicy(AWSObject):
    """
    `ConfigurationPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-configurationpolicy.html>`__
    """

    resource_type = "AWS::SecurityHub::ConfigurationPolicy"

    props: PropsDictType = {
        "ConfigurationPolicy": (Policy, True),
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (dict, False),
    }


class DelegatedAdmin(AWSObject):
    """
    `DelegatedAdmin <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-delegatedadmin.html>`__
    """

    resource_type = "AWS::SecurityHub::DelegatedAdmin"

    props: PropsDictType = {
        "AdminAccountId": (str, True),
    }


class FindingAggregator(AWSObject):
    """
    `FindingAggregator <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-findingaggregator.html>`__
    """

    resource_type = "AWS::SecurityHub::FindingAggregator"

    props: PropsDictType = {
        "RegionLinkingMode": (str, True),
        "Regions": ([str], False),
    }


class Hub(AWSObject):
    """
    `Hub <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html>`__
    """

    resource_type = "AWS::SecurityHub::Hub"

    props: PropsDictType = {
        "AutoEnableControls": (boolean, False),
        "ControlFindingGenerator": (str, False),
        "EnableDefaultStandards": (boolean, False),
        "Tags": (dict, False),
    }


class BooleanFilter(AWSProperty):
    """
    `BooleanFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-booleanfilter.html>`__
    """

    props: PropsDictType = {
        "Value": (boolean, True),
    }


class IpFilter(AWSProperty):
    """
    `IpFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-ipfilter.html>`__
    """

    props: PropsDictType = {
        "Cidr": (str, True),
    }


class AwsSecurityFindingFilters(AWSProperty):
    """
    `AwsSecurityFindingFilters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html>`__
    """

    props: PropsDictType = {
        "AwsAccountId": ([StringFilter], False),
        "AwsAccountName": ([StringFilter], False),
        "CompanyName": ([StringFilter], False),
        "ComplianceAssociatedStandardsId": ([StringFilter], False),
        "ComplianceSecurityControlId": ([StringFilter], False),
        "ComplianceSecurityControlParametersName": ([StringFilter], False),
        "ComplianceSecurityControlParametersValue": ([StringFilter], False),
        "ComplianceStatus": ([StringFilter], False),
        "Confidence": ([NumberFilter], False),
        "CreatedAt": ([DateFilter], False),
        "Criticality": ([NumberFilter], False),
        "Description": ([StringFilter], False),
        "FindingProviderFieldsConfidence": ([NumberFilter], False),
        "FindingProviderFieldsCriticality": ([NumberFilter], False),
        "FindingProviderFieldsRelatedFindingsId": ([StringFilter], False),
        "FindingProviderFieldsRelatedFindingsProductArn": ([StringFilter], False),
        "FindingProviderFieldsSeverityLabel": ([StringFilter], False),
        "FindingProviderFieldsSeverityOriginal": ([StringFilter], False),
        "FindingProviderFieldsTypes": ([StringFilter], False),
        "FirstObservedAt": ([DateFilter], False),
        "GeneratorId": ([StringFilter], False),
        "Id": ([StringFilter], False),
        "LastObservedAt": ([DateFilter], False),
        "MalwareName": ([StringFilter], False),
        "MalwarePath": ([StringFilter], False),
        "MalwareState": ([StringFilter], False),
        "MalwareType": ([StringFilter], False),
        "NetworkDestinationDomain": ([StringFilter], False),
        "NetworkDestinationIpV4": ([IpFilter], False),
        "NetworkDestinationIpV6": ([IpFilter], False),
        "NetworkDestinationPort": ([NumberFilter], False),
        "NetworkDirection": ([StringFilter], False),
        "NetworkProtocol": ([StringFilter], False),
        "NetworkSourceDomain": ([StringFilter], False),
        "NetworkSourceIpV4": ([IpFilter], False),
        "NetworkSourceIpV6": ([IpFilter], False),
        "NetworkSourceMac": ([StringFilter], False),
        "NetworkSourcePort": ([NumberFilter], False),
        "NoteText": ([StringFilter], False),
        "NoteUpdatedAt": ([DateFilter], False),
        "NoteUpdatedBy": ([StringFilter], False),
        "ProcessLaunchedAt": ([DateFilter], False),
        "ProcessName": ([StringFilter], False),
        "ProcessParentPid": ([NumberFilter], False),
        "ProcessPath": ([StringFilter], False),
        "ProcessPid": ([NumberFilter], False),
        "ProcessTerminatedAt": ([DateFilter], False),
        "ProductArn": ([StringFilter], False),
        "ProductFields": ([MapFilter], False),
        "ProductName": ([StringFilter], False),
        "RecommendationText": ([StringFilter], False),
        "RecordState": ([StringFilter], False),
        "Region": ([StringFilter], False),
        "RelatedFindingsId": ([StringFilter], False),
        "RelatedFindingsProductArn": ([StringFilter], False),
        "ResourceApplicationArn": ([StringFilter], False),
        "ResourceApplicationName": ([StringFilter], False),
        "ResourceAwsEc2InstanceIamInstanceProfileArn": ([StringFilter], False),
        "ResourceAwsEc2InstanceImageId": ([StringFilter], False),
        "ResourceAwsEc2InstanceIpV4Addresses": ([IpFilter], False),
        "ResourceAwsEc2InstanceIpV6Addresses": ([IpFilter], False),
        "ResourceAwsEc2InstanceKeyName": ([StringFilter], False),
        "ResourceAwsEc2InstanceLaunchedAt": ([DateFilter], False),
        "ResourceAwsEc2InstanceSubnetId": ([StringFilter], False),
        "ResourceAwsEc2InstanceType": ([StringFilter], False),
        "ResourceAwsEc2InstanceVpcId": ([StringFilter], False),
        "ResourceAwsIamAccessKeyCreatedAt": ([DateFilter], False),
        "ResourceAwsIamAccessKeyPrincipalName": ([StringFilter], False),
        "ResourceAwsIamAccessKeyStatus": ([StringFilter], False),
        "ResourceAwsIamUserUserName": ([StringFilter], False),
        "ResourceAwsS3BucketOwnerId": ([StringFilter], False),
        "ResourceAwsS3BucketOwnerName": ([StringFilter], False),
        "ResourceContainerImageId": ([StringFilter], False),
        "ResourceContainerImageName": ([StringFilter], False),
        "ResourceContainerLaunchedAt": ([DateFilter], False),
        "ResourceContainerName": ([StringFilter], False),
        "ResourceDetailsOther": ([MapFilter], False),
        "ResourceId": ([StringFilter], False),
        "ResourcePartition": ([StringFilter], False),
        "ResourceRegion": ([StringFilter], False),
        "ResourceTags": ([MapFilter], False),
        "ResourceType": ([StringFilter], False),
        "Sample": ([BooleanFilter], False),
        "SeverityLabel": ([StringFilter], False),
        "SourceUrl": ([StringFilter], False),
        "ThreatIntelIndicatorCategory": ([StringFilter], False),
        "ThreatIntelIndicatorLastObservedAt": ([DateFilter], False),
        "ThreatIntelIndicatorSource": ([StringFilter], False),
        "ThreatIntelIndicatorSourceUrl": ([StringFilter], False),
        "ThreatIntelIndicatorType": ([StringFilter], False),
        "ThreatIntelIndicatorValue": ([StringFilter], False),
        "Title": ([StringFilter], False),
        "Type": ([StringFilter], False),
        "UpdatedAt": ([DateFilter], False),
        "UserDefinedFields": ([MapFilter], False),
        "VerificationState": ([StringFilter], False),
        "VulnerabilitiesExploitAvailable": ([StringFilter], False),
        "VulnerabilitiesFixAvailable": ([StringFilter], False),
        "WorkflowState": ([StringFilter], False),
        "WorkflowStatus": ([StringFilter], False),
    }


class Insight(AWSObject):
    """
    `Insight <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-insight.html>`__
    """

    resource_type = "AWS::SecurityHub::Insight"

    props: PropsDictType = {
        "Filters": (AwsSecurityFindingFilters, True),
        "GroupByAttribute": (str, True),
        "Name": (str, True),
    }


class OrganizationConfiguration(AWSObject):
    """
    `OrganizationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-organizationconfiguration.html>`__
    """

    resource_type = "AWS::SecurityHub::OrganizationConfiguration"

    props: PropsDictType = {
        "AutoEnable": (boolean, True),
        "AutoEnableStandards": (str, False),
        "ConfigurationType": (str, False),
    }


class PolicyAssociation(AWSObject):
    """
    `PolicyAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-policyassociation.html>`__
    """

    resource_type = "AWS::SecurityHub::PolicyAssociation"

    props: PropsDictType = {
        "ConfigurationPolicyId": (str, True),
        "TargetId": (str, True),
        "TargetType": (str, True),
    }


class ProductSubscription(AWSObject):
    """
    `ProductSubscription <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-productsubscription.html>`__
    """

    resource_type = "AWS::SecurityHub::ProductSubscription"

    props: PropsDictType = {
        "ProductArn": (str, True),
    }


class SecurityControl(AWSObject):
    """
    `SecurityControl <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-securitycontrol.html>`__
    """

    resource_type = "AWS::SecurityHub::SecurityControl"

    props: PropsDictType = {
        "LastUpdateReason": (str, False),
        "Parameters": (dict, True),
        "SecurityControlArn": (str, False),
        "SecurityControlId": (str, False),
    }


class StandardsControl(AWSProperty):
    """
    `StandardsControl <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-standard-standardscontrol.html>`__
    """

    props: PropsDictType = {
        "Reason": (str, False),
        "StandardsControlArn": (str, True),
    }


class Standard(AWSObject):
    """
    `Standard <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-standard.html>`__
    """

    resource_type = "AWS::SecurityHub::Standard"

    props: PropsDictType = {
        "DisabledStandardsControls": ([StandardsControl], False),
        "StandardsArn": (str, True),
    }
