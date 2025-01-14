# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import double, integer


class Farm(AWSObject):
    """
    `Farm <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-farm.html>`__
    """

    resource_type = "AWS::Deadline::Farm"

    props: PropsDictType = {
        "Description": (str, False),
        "DisplayName": (str, True),
        "KmsKeyArn": (str, False),
        "Tags": (Tags, False),
    }


class AcceleratorCountRange(AWSProperty):
    """
    `AcceleratorCountRange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-acceleratorcountrange.html>`__
    """

    props: PropsDictType = {
        "Max": (integer, False),
        "Min": (integer, True),
    }


class AcceleratorTotalMemoryMiBRange(AWSProperty):
    """
    `AcceleratorTotalMemoryMiBRange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-acceleratortotalmemorymibrange.html>`__
    """

    props: PropsDictType = {
        "Max": (integer, False),
        "Min": (integer, True),
    }


class FleetAmountCapability(AWSProperty):
    """
    `FleetAmountCapability <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetamountcapability.html>`__
    """

    props: PropsDictType = {
        "Max": (double, False),
        "Min": (double, True),
        "Name": (str, True),
    }


class FleetAttributeCapability(AWSProperty):
    """
    `FleetAttributeCapability <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetattributecapability.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Values": ([str], True),
    }


class MemoryMiBRange(AWSProperty):
    """
    `MemoryMiBRange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-memorymibrange.html>`__
    """

    props: PropsDictType = {
        "Max": (integer, False),
        "Min": (integer, True),
    }


class VCpuCountRange(AWSProperty):
    """
    `VCpuCountRange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-vcpucountrange.html>`__
    """

    props: PropsDictType = {
        "Max": (integer, False),
        "Min": (integer, True),
    }


class CustomerManagedWorkerCapabilities(AWSProperty):
    """
    `CustomerManagedWorkerCapabilities <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedworkercapabilities.html>`__
    """

    props: PropsDictType = {
        "AcceleratorCount": (AcceleratorCountRange, False),
        "AcceleratorTotalMemoryMiB": (AcceleratorTotalMemoryMiBRange, False),
        "AcceleratorTypes": ([str], False),
        "CpuArchitectureType": (str, True),
        "CustomAmounts": ([FleetAmountCapability], False),
        "CustomAttributes": ([FleetAttributeCapability], False),
        "MemoryMiB": (MemoryMiBRange, True),
        "OsFamily": (str, True),
        "VCpuCount": (VCpuCountRange, True),
    }


class CustomerManagedFleetConfiguration(AWSProperty):
    """
    `CustomerManagedFleetConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-customermanagedfleetconfiguration.html>`__
    """

    props: PropsDictType = {
        "Mode": (str, True),
        "StorageProfileId": (str, False),
        "WorkerCapabilities": (CustomerManagedWorkerCapabilities, True),
    }


class AcceleratorSelection(AWSProperty):
    """
    `AcceleratorSelection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-acceleratorselection.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Runtime": (str, False),
    }


class AcceleratorCapabilities(AWSProperty):
    """
    `AcceleratorCapabilities <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-acceleratorcapabilities.html>`__
    """

    props: PropsDictType = {
        "Count": (AcceleratorCountRange, False),
        "Selections": ([AcceleratorSelection], True),
    }


class Ec2EbsVolume(AWSProperty):
    """
    `Ec2EbsVolume <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-ec2ebsvolume.html>`__
    """

    props: PropsDictType = {
        "Iops": (integer, False),
        "SizeGiB": (integer, False),
        "ThroughputMiB": (integer, False),
    }


class ServiceManagedEc2InstanceCapabilities(AWSProperty):
    """
    `ServiceManagedEc2InstanceCapabilities <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancecapabilities.html>`__
    """

    props: PropsDictType = {
        "AcceleratorCapabilities": (AcceleratorCapabilities, False),
        "AllowedInstanceTypes": ([str], False),
        "CpuArchitectureType": (str, True),
        "CustomAmounts": ([FleetAmountCapability], False),
        "CustomAttributes": ([FleetAttributeCapability], False),
        "ExcludedInstanceTypes": ([str], False),
        "MemoryMiB": (MemoryMiBRange, True),
        "OsFamily": (str, True),
        "RootEbsVolume": (Ec2EbsVolume, False),
        "VCpuCount": (VCpuCountRange, True),
    }


class ServiceManagedEc2InstanceMarketOptions(AWSProperty):
    """
    `ServiceManagedEc2InstanceMarketOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
    }


class ServiceManagedEc2FleetConfiguration(AWSProperty):
    """
    `ServiceManagedEc2FleetConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-servicemanagedec2fleetconfiguration.html>`__
    """

    props: PropsDictType = {
        "InstanceCapabilities": (ServiceManagedEc2InstanceCapabilities, True),
        "InstanceMarketOptions": (ServiceManagedEc2InstanceMarketOptions, True),
    }


class FleetConfiguration(AWSProperty):
    """
    `FleetConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetconfiguration.html>`__
    """

    props: PropsDictType = {
        "CustomerManaged": (CustomerManagedFleetConfiguration, False),
        "ServiceManagedEc2": (ServiceManagedEc2FleetConfiguration, False),
    }


class Fleet(AWSObject):
    """
    `Fleet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-fleet.html>`__
    """

    resource_type = "AWS::Deadline::Fleet"

    props: PropsDictType = {
        "Configuration": (FleetConfiguration, True),
        "Description": (str, False),
        "DisplayName": (str, True),
        "FarmId": (str, True),
        "MaxWorkerCount": (integer, True),
        "MinWorkerCount": (integer, False),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
    }


class LicenseEndpoint(AWSObject):
    """
    `LicenseEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-licenseendpoint.html>`__
    """

    resource_type = "AWS::Deadline::LicenseEndpoint"

    props: PropsDictType = {
        "SecurityGroupIds": ([str], True),
        "SubnetIds": ([str], True),
        "Tags": (Tags, False),
        "VpcId": (str, True),
    }


class MeteredProduct(AWSObject):
    """
    `MeteredProduct <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-meteredproduct.html>`__
    """

    resource_type = "AWS::Deadline::MeteredProduct"

    props: PropsDictType = {
        "LicenseEndpointId": (str, False),
        "ProductId": (str, False),
    }


class Monitor(AWSObject):
    """
    `Monitor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-monitor.html>`__
    """

    resource_type = "AWS::Deadline::Monitor"

    props: PropsDictType = {
        "DisplayName": (str, True),
        "IdentityCenterInstanceArn": (str, True),
        "RoleArn": (str, True),
        "Subdomain": (str, True),
    }


class JobAttachmentSettings(AWSProperty):
    """
    `JobAttachmentSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-jobattachmentsettings.html>`__
    """

    props: PropsDictType = {
        "RootPrefix": (str, True),
        "S3BucketName": (str, True),
    }


class PosixUser(AWSProperty):
    """
    `PosixUser <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-posixuser.html>`__
    """

    props: PropsDictType = {
        "Group": (str, True),
        "User": (str, True),
    }


class WindowsUser(AWSProperty):
    """
    `WindowsUser <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-windowsuser.html>`__
    """

    props: PropsDictType = {
        "PasswordArn": (str, True),
        "User": (str, True),
    }


class JobRunAsUser(AWSProperty):
    """
    `JobRunAsUser <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-queue-jobrunasuser.html>`__
    """

    props: PropsDictType = {
        "Posix": (PosixUser, False),
        "RunAs": (str, True),
        "Windows": (WindowsUser, False),
    }


class Queue(AWSObject):
    """
    `Queue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queue.html>`__
    """

    resource_type = "AWS::Deadline::Queue"

    props: PropsDictType = {
        "AllowedStorageProfileIds": ([str], False),
        "DefaultBudgetAction": (str, False),
        "Description": (str, False),
        "DisplayName": (str, True),
        "FarmId": (str, True),
        "JobAttachmentSettings": (JobAttachmentSettings, False),
        "JobRunAsUser": (JobRunAsUser, False),
        "RequiredFileSystemLocationNames": ([str], False),
        "RoleArn": (str, False),
        "Tags": (Tags, False),
    }


class QueueEnvironment(AWSObject):
    """
    `QueueEnvironment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queueenvironment.html>`__
    """

    resource_type = "AWS::Deadline::QueueEnvironment"

    props: PropsDictType = {
        "FarmId": (str, True),
        "Priority": (integer, True),
        "QueueId": (str, True),
        "Template": (str, True),
        "TemplateType": (str, True),
    }


class QueueFleetAssociation(AWSObject):
    """
    `QueueFleetAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-queuefleetassociation.html>`__
    """

    resource_type = "AWS::Deadline::QueueFleetAssociation"

    props: PropsDictType = {
        "FarmId": (str, True),
        "FleetId": (str, True),
        "QueueId": (str, True),
    }


class FileSystemLocation(AWSProperty):
    """
    `FileSystemLocation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-storageprofile-filesystemlocation.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Path": (str, True),
        "Type": (str, True),
    }


class StorageProfile(AWSObject):
    """
    `StorageProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-storageprofile.html>`__
    """

    resource_type = "AWS::Deadline::StorageProfile"

    props: PropsDictType = {
        "DisplayName": (str, True),
        "FarmId": (str, True),
        "FileSystemLocations": ([FileSystemLocation], False),
        "OsFamily": (str, True),
    }


class FleetCapabilities(AWSProperty):
    """
    `FleetCapabilities <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-deadline-fleet-fleetcapabilities.html>`__
    """

    props: PropsDictType = {
        "Amounts": ([FleetAmountCapability], False),
        "Attributes": ([FleetAttributeCapability], False),
    }
