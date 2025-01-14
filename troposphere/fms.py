# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.fms import validate_json_checker


class NotificationChannel(AWSObject):
    """
    `NotificationChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html>`__
    """

    resource_type = "AWS::FMS::NotificationChannel"

    props: PropsDictType = {
        "SnsRoleName": (str, True),
        "SnsTopicArn": (str, True),
    }


class IEMap(AWSProperty):
    """
    `IEMap <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html>`__
    """

    props: PropsDictType = {
        "ACCOUNT": ([str], False),
        "ORGUNIT": ([str], False),
    }


class IcmpTypeCode(AWSProperty):
    """
    `IcmpTypeCode <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-icmptypecode.html>`__
    """

    props: PropsDictType = {
        "Code": (integer, True),
        "Type": (integer, True),
    }


class PortRange(AWSProperty):
    """
    `PortRange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-portrange.html>`__
    """

    props: PropsDictType = {
        "From": (integer, True),
        "To": (integer, True),
    }


class NetworkAclEntry(AWSProperty):
    """
    `NetworkAclEntry <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentry.html>`__
    """

    props: PropsDictType = {
        "CidrBlock": (str, False),
        "Egress": (boolean, True),
        "IcmpTypeCode": (IcmpTypeCode, False),
        "Ipv6CidrBlock": (str, False),
        "PortRange": (PortRange, False),
        "Protocol": (str, True),
        "RuleAction": (str, True),
    }


class NetworkAclEntrySet(AWSProperty):
    """
    `NetworkAclEntrySet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentryset.html>`__
    """

    props: PropsDictType = {
        "FirstEntries": ([NetworkAclEntry], False),
        "ForceRemediateForFirstEntries": (boolean, True),
        "ForceRemediateForLastEntries": (boolean, True),
        "LastEntries": ([NetworkAclEntry], False),
    }


class NetworkAclCommonPolicy(AWSProperty):
    """
    `NetworkAclCommonPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclcommonpolicy.html>`__
    """

    props: PropsDictType = {
        "NetworkAclEntrySet": (NetworkAclEntrySet, True),
    }


class NetworkFirewallPolicy(AWSProperty):
    """
    `NetworkFirewallPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`__
    """

    props: PropsDictType = {
        "FirewallDeploymentModel": (str, True),
    }


class ThirdPartyFirewallPolicy(AWSProperty):
    """
    `ThirdPartyFirewallPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`__
    """

    props: PropsDictType = {
        "FirewallDeploymentModel": (str, True),
    }


class PolicyOption(AWSProperty):
    """
    `PolicyOption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html>`__
    """

    props: PropsDictType = {
        "NetworkAclCommonPolicy": (NetworkAclCommonPolicy, False),
        "NetworkFirewallPolicy": (NetworkFirewallPolicy, False),
        "ThirdPartyFirewallPolicy": (ThirdPartyFirewallPolicy, False),
    }


class SecurityServicePolicyData(AWSProperty):
    """
    `SecurityServicePolicyData <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html>`__
    """

    props: PropsDictType = {
        "ManagedServiceData": (str, False),
        "PolicyOption": (PolicyOption, False),
        "Type": (str, True),
    }


class Policy(AWSObject):
    """
    `Policy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html>`__
    """

    resource_type = "AWS::FMS::Policy"

    props: PropsDictType = {
        "DeleteAllPolicyResources": (boolean, False),
        "ExcludeMap": (IEMap, False),
        "ExcludeResourceTags": (boolean, True),
        "IncludeMap": (IEMap, False),
        "PolicyDescription": (str, False),
        "PolicyName": (str, True),
        "RemediationEnabled": (boolean, True),
        "ResourceSetIds": ([str], False),
        "ResourceTags": (Tags, False),
        "ResourceType": (str, False),
        "ResourceTypeList": ([str], False),
        "ResourcesCleanUp": (boolean, False),
        "SecurityServicePolicyData": (validate_json_checker, True),
        "Tags": (Tags, False),
    }


class ResourceSet(AWSObject):
    """
    `ResourceSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html>`__
    """

    resource_type = "AWS::FMS::ResourceSet"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "ResourceTypeList": ([str], True),
        "Resources": ([str], False),
        "Tags": (Tags, False),
    }
