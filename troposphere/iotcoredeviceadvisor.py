# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean


class DeviceUnderTest(AWSProperty):
    """
    `DeviceUnderTest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest.html>`__
    """

    props: PropsDictType = {
        "CertificateArn": (str, False),
        "ThingArn": (str, False),
    }


class SuiteDefinitionConfiguration(AWSProperty):
    """
    `SuiteDefinitionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html>`__
    """

    props: PropsDictType = {
        "DevicePermissionRoleArn": (str, True),
        "Devices": ([DeviceUnderTest], False),
        "IntendedForQualification": (boolean, False),
        "RootGroup": (str, True),
        "SuiteDefinitionName": (str, False),
    }


class SuiteDefinition(AWSObject):
    """
    `SuiteDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html>`__
    """

    resource_type = "AWS::IoTCoreDeviceAdvisor::SuiteDefinition"

    props: PropsDictType = {
        "SuiteDefinitionConfiguration": (SuiteDefinitionConfiguration, True),
        "Tags": (Tags, False),
    }
