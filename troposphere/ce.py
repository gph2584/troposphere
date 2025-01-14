# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import double


class ResourceTag(AWSProperty):
    """
    `ResourceTag <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-resourcetag.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class AnomalyMonitor(AWSObject):
    """
    `AnomalyMonitor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html>`__
    """

    resource_type = "AWS::CE::AnomalyMonitor"

    props: PropsDictType = {
        "MonitorDimension": (str, False),
        "MonitorName": (str, True),
        "MonitorSpecification": (str, False),
        "MonitorType": (str, True),
        "ResourceTags": ([ResourceTag], False),
    }


class Subscriber(AWSProperty):
    """
    `Subscriber <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html>`__
    """

    props: PropsDictType = {
        "Address": (str, True),
        "Status": (str, False),
        "Type": (str, True),
    }


class AnomalySubscription(AWSObject):
    """
    `AnomalySubscription <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html>`__
    """

    resource_type = "AWS::CE::AnomalySubscription"

    props: PropsDictType = {
        "Frequency": (str, True),
        "MonitorArnList": ([str], True),
        "ResourceTags": ([ResourceTag], False),
        "Subscribers": ([Subscriber], True),
        "SubscriptionName": (str, True),
        "Threshold": (double, False),
        "ThresholdExpression": (str, False),
    }


class CostCategory(AWSObject):
    """
    `CostCategory <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html>`__
    """

    resource_type = "AWS::CE::CostCategory"

    props: PropsDictType = {
        "DefaultValue": (str, False),
        "Name": (str, True),
        "RuleVersion": (str, True),
        "Rules": (str, True),
        "SplitChargeRules": (str, False),
    }
