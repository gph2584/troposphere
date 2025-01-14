# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.opsworks import (
    validate_block_device_mapping,
    validate_data_source_type,
    validate_json_checker,
    validate_stack,
    validate_tags_or_list,
    validate_volume_configuration,
    validate_volume_type,
)


class DataSource(AWSProperty):
    """
    `DataSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, False),
        "DatabaseName": (str, False),
        "Type": (validate_data_source_type, False),
    }


class Environment(AWSProperty):
    """
    `Environment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Secure": (boolean, False),
        "Value": (str, True),
    }


class Source(AWSProperty):
    """
    `Source <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html>`__
    """

    props: PropsDictType = {
        "Password": (str, False),
        "Revision": (str, False),
        "SshKey": (str, False),
        "Type": (str, False),
        "Url": (str, False),
        "Username": (str, False),
    }


class SslConfiguration(AWSProperty):
    """
    `SslConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html>`__
    """

    props: PropsDictType = {
        "Certificate": (str, False),
        "Chain": (str, False),
        "PrivateKey": (str, False),
    }


class App(AWSObject):
    """
    `App <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html>`__
    """

    resource_type = "AWS::OpsWorks::App"

    props: PropsDictType = {
        "AppSource": (Source, False),
        "Attributes": (dict, False),
        "DataSources": ([DataSource], False),
        "Description": (str, False),
        "Domains": ([str], False),
        "EnableSsl": (boolean, False),
        "Environment": ([Environment], False),
        "Name": (str, True),
        "Shortname": (str, False),
        "SslConfiguration": (SslConfiguration, False),
        "StackId": (str, True),
        "Type": (str, True),
    }


class ElasticLoadBalancerAttachment(AWSObject):
    """
    `ElasticLoadBalancerAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html>`__
    """

    resource_type = "AWS::OpsWorks::ElasticLoadBalancerAttachment"

    props: PropsDictType = {
        "ElasticLoadBalancerName": (str, True),
        "LayerId": (str, True),
    }


class EbsBlockDevice(AWSProperty):
    """
    `EbsBlockDevice <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html>`__
    """

    props: PropsDictType = {
        "DeleteOnTermination": (boolean, False),
        "Iops": (integer, False),
        "SnapshotId": (str, False),
        "VolumeSize": (integer, False),
        "VolumeType": (str, False),
    }


class BlockDeviceMapping(AWSProperty):
    """
    `BlockDeviceMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html>`__
    """

    props: PropsDictType = {
        "DeviceName": (str, False),
        "Ebs": (EbsBlockDevice, False),
        "NoDevice": (str, False),
        "VirtualName": (str, False),
    }

    def validate(self):
        validate_block_device_mapping(self)


class TimeBasedAutoScaling(AWSProperty):
    """
    `TimeBasedAutoScaling <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html>`__
    """

    props: PropsDictType = {
        "Friday": (dict, False),
        "Monday": (dict, False),
        "Saturday": (dict, False),
        "Sunday": (dict, False),
        "Thursday": (dict, False),
        "Tuesday": (dict, False),
        "Wednesday": (dict, False),
    }


class Instance(AWSObject):
    """
    `Instance <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html>`__
    """

    resource_type = "AWS::OpsWorks::Instance"

    props: PropsDictType = {
        "AgentVersion": (str, False),
        "AmiId": (str, False),
        "Architecture": (str, False),
        "AutoScalingType": (str, False),
        "AvailabilityZone": (str, False),
        "BlockDeviceMappings": ([BlockDeviceMapping], False),
        "EbsOptimized": (boolean, False),
        "ElasticIps": ([str], False),
        "Hostname": (str, False),
        "InstallUpdatesOnBoot": (boolean, False),
        "InstanceType": (str, True),
        "LayerIds": ([str], True),
        "Os": (str, False),
        "RootDeviceType": (str, False),
        "SshKeyName": (str, False),
        "StackId": (str, True),
        "SubnetId": (str, False),
        "Tenancy": (str, False),
        "TimeBasedAutoScaling": (TimeBasedAutoScaling, False),
        "VirtualizationType": (str, False),
        "Volumes": ([str], False),
    }


class ShutdownEventConfiguration(AWSProperty):
    """
    `ShutdownEventConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html>`__
    """

    props: PropsDictType = {
        "DelayUntilElbConnectionsDrained": (boolean, False),
        "ExecutionTimeout": (integer, False),
    }


class LifeCycleConfiguration(AWSProperty):
    """
    `LifeCycleConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration.html>`__
    """

    props: PropsDictType = {
        "ShutdownEventConfiguration": (ShutdownEventConfiguration, False),
    }


class AutoScalingThresholds(AWSProperty):
    """
    `AutoScalingThresholds <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html>`__
    """

    props: PropsDictType = {
        "CpuThreshold": (double, False),
        "IgnoreMetricsTime": (integer, False),
        "InstanceCount": (integer, False),
        "LoadThreshold": (double, False),
        "MemoryThreshold": (double, False),
        "ThresholdsWaitTime": (integer, False),
    }


class LoadBasedAutoScaling(AWSProperty):
    """
    `LoadBasedAutoScaling <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html>`__
    """

    props: PropsDictType = {
        "DownScaling": (AutoScalingThresholds, False),
        "Enable": (boolean, False),
        "UpScaling": (AutoScalingThresholds, False),
    }


class Recipes(AWSProperty):
    """
    `Recipes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html>`__
    """

    props: PropsDictType = {
        "Configure": ([str], False),
        "Deploy": ([str], False),
        "Setup": ([str], False),
        "Shutdown": ([str], False),
        "Undeploy": ([str], False),
    }


class VolumeConfiguration(AWSProperty):
    """
    `VolumeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html>`__
    """

    props: PropsDictType = {
        "Encrypted": (boolean, False),
        "Iops": (integer, False),
        "MountPoint": (str, False),
        "NumberOfDisks": (integer, False),
        "RaidLevel": (integer, False),
        "Size": (integer, False),
        "VolumeType": (validate_volume_type, False),
    }

    def validate(self):
        validate_volume_configuration(self)


class Layer(AWSObject):
    """
    `Layer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html>`__
    """

    resource_type = "AWS::OpsWorks::Layer"

    props: PropsDictType = {
        "Attributes": (dict, False),
        "AutoAssignElasticIps": (boolean, True),
        "AutoAssignPublicIps": (boolean, True),
        "CustomInstanceProfileArn": (str, False),
        "CustomJson": (validate_json_checker, False),
        "CustomRecipes": (Recipes, False),
        "CustomSecurityGroupIds": ([str], False),
        "EnableAutoHealing": (boolean, True),
        "InstallUpdatesOnBoot": (boolean, False),
        "LifecycleEventConfiguration": (LifeCycleConfiguration, False),
        "LoadBasedAutoScaling": (LoadBasedAutoScaling, False),
        "Name": (str, True),
        "Packages": ([str], False),
        "Shortname": (str, True),
        "StackId": (str, True),
        "Tags": (Tags, False),
        "Type": (str, True),
        "UseEbsOptimizedInstances": (boolean, False),
        "VolumeConfigurations": ([VolumeConfiguration], False),
    }


class ChefConfiguration(AWSProperty):
    """
    `ChefConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html>`__
    """

    props: PropsDictType = {
        "BerkshelfVersion": (str, False),
        "ManageBerkshelf": (boolean, False),
    }


class ElasticIp(AWSProperty):
    """
    `ElasticIp <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html>`__
    """

    props: PropsDictType = {
        "Ip": (str, True),
        "Name": (str, False),
    }


class RdsDbInstance(AWSProperty):
    """
    `RdsDbInstance <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html>`__
    """

    props: PropsDictType = {
        "DbPassword": (str, True),
        "DbUser": (str, True),
        "RdsDbInstanceArn": (str, True),
    }


class StackConfigurationManager(AWSProperty):
    """
    `StackConfigurationManager <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigmanager.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Version": (str, False),
    }


class Stack(AWSObject):
    """
    `Stack <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html>`__
    """

    resource_type = "AWS::OpsWorks::Stack"

    props: PropsDictType = {
        "AgentVersion": (str, False),
        "Attributes": (dict, False),
        "ChefConfiguration": (ChefConfiguration, False),
        "CloneAppIds": ([str], False),
        "ClonePermissions": (boolean, False),
        "ConfigurationManager": (StackConfigurationManager, False),
        "CustomCookbooksSource": (Source, False),
        "CustomJson": (validate_json_checker, False),
        "DefaultAvailabilityZone": (str, False),
        "DefaultInstanceProfileArn": (str, True),
        "DefaultOs": (str, False),
        "DefaultRootDeviceType": (str, False),
        "DefaultSshKeyName": (str, False),
        "DefaultSubnetId": (str, False),
        "EcsClusterArn": (str, False),
        "ElasticIps": ([ElasticIp], False),
        "HostnameTheme": (str, False),
        "Name": (str, True),
        "RdsDbInstances": ([RdsDbInstance], False),
        "ServiceRoleArn": (str, True),
        "SourceStackId": (str, False),
        "Tags": (validate_tags_or_list, False),
        "UseCustomCookbooks": (boolean, False),
        "UseOpsworksSecurityGroups": (boolean, False),
        "VpcId": (str, False),
    }

    def validate(self):
        validate_stack(self)


class UserProfile(AWSObject):
    """
    `UserProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html>`__
    """

    resource_type = "AWS::OpsWorks::UserProfile"

    props: PropsDictType = {
        "AllowSelfManagement": (boolean, False),
        "IamUserArn": (str, True),
        "SshPublicKey": (str, False),
        "SshUsername": (str, False),
    }


class Volume(AWSObject):
    """
    `Volume <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html>`__
    """

    resource_type = "AWS::OpsWorks::Volume"

    props: PropsDictType = {
        "Ec2VolumeId": (str, True),
        "MountPoint": (str, False),
        "Name": (str, False),
        "StackId": (str, True),
    }
