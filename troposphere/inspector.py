# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, PropsDictType, Tags
from .validators import integer


class AssessmentTarget(AWSObject):
    """
    `AssessmentTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html>`__
    """

    resource_type = "AWS::Inspector::AssessmentTarget"

    props: PropsDictType = {
        "AssessmentTargetName": (str, False),
        "ResourceGroupArn": (str, False),
    }


class AssessmentTemplate(AWSObject):
    """
    `AssessmentTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html>`__
    """

    resource_type = "AWS::Inspector::AssessmentTemplate"

    props: PropsDictType = {
        "AssessmentTargetArn": (str, True),
        "AssessmentTemplateName": (str, False),
        "DurationInSeconds": (integer, True),
        "RulesPackageArns": ([str], True),
        "UserAttributesForFindings": (Tags, False),
    }


class ResourceGroup(AWSObject):
    """
    `ResourceGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-resourcegroup.html>`__
    """

    resource_type = "AWS::Inspector::ResourceGroup"

    props: PropsDictType = {
        "ResourceGroupTags": (Tags, True),
    }
