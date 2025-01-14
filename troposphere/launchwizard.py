# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, PropsDictType, Tags


class Deployment(AWSObject):
    """
    `Deployment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html>`__
    """

    resource_type = "AWS::LaunchWizard::Deployment"

    props: PropsDictType = {
        "DeploymentPatternName": (str, True),
        "Name": (str, True),
        "Specifications": (dict, True),
        "Tags": (Tags, False),
        "WorkloadName": (str, True),
    }
