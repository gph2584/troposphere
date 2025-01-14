# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class PipeEnrichmentHttpParameters(AWSProperty):
    """
    `PipeEnrichmentHttpParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmenthttpparameters.html>`__
    """

    props: PropsDictType = {
        "HeaderParameters": (dict, False),
        "PathParameterValues": ([str], False),
        "QueryStringParameters": (dict, False),
    }


class PipeEnrichmentParameters(AWSProperty):
    """
    `PipeEnrichmentParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmentparameters.html>`__
    """

    props: PropsDictType = {
        "HttpParameters": (PipeEnrichmentHttpParameters, False),
        "InputTemplate": (str, False),
    }


class CloudwatchLogsLogDestination(AWSProperty):
    """
    `CloudwatchLogsLogDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-cloudwatchlogslogdestination.html>`__
    """

    props: PropsDictType = {
        "LogGroupArn": (str, False),
    }


class FirehoseLogDestination(AWSProperty):
    """
    `FirehoseLogDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-firehoselogdestination.html>`__
    """

    props: PropsDictType = {
        "DeliveryStreamArn": (str, False),
    }


class S3LogDestination(AWSProperty):
    """
    `S3LogDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-s3logdestination.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, False),
        "BucketOwner": (str, False),
        "OutputFormat": (str, False),
        "Prefix": (str, False),
    }


class PipeLogConfiguration(AWSProperty):
    """
    `PipeLogConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipelogconfiguration.html>`__
    """

    props: PropsDictType = {
        "CloudwatchLogsLogDestination": (CloudwatchLogsLogDestination, False),
        "FirehoseLogDestination": (FirehoseLogDestination, False),
        "IncludeExecutionData": ([str], False),
        "Level": (str, False),
        "S3LogDestination": (S3LogDestination, False),
    }


class Filter(AWSProperty):
    """
    `Filter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-filter.html>`__
    """

    props: PropsDictType = {
        "Pattern": (str, False),
    }


class FilterCriteria(AWSProperty):
    """
    `FilterCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-filtercriteria.html>`__
    """

    props: PropsDictType = {
        "Filters": ([Filter], False),
    }


class MQBrokerAccessCredentials(AWSProperty):
    """
    `MQBrokerAccessCredentials <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-mqbrokeraccesscredentials.html>`__
    """

    props: PropsDictType = {
        "BasicAuth": (str, True),
    }


class PipeSourceActiveMQBrokerParameters(AWSProperty):
    """
    `PipeSourceActiveMQBrokerParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters.html>`__
    """

    props: PropsDictType = {
        "BatchSize": (integer, False),
        "Credentials": (MQBrokerAccessCredentials, True),
        "MaximumBatchingWindowInSeconds": (integer, False),
        "QueueName": (str, True),
    }


class DeadLetterConfig(AWSProperty):
    """
    `DeadLetterConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-deadletterconfig.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, False),
    }


class PipeSourceDynamoDBStreamParameters(AWSProperty):
    """
    `PipeSourceDynamoDBStreamParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html>`__
    """

    props: PropsDictType = {
        "BatchSize": (integer, False),
        "DeadLetterConfig": (DeadLetterConfig, False),
        "MaximumBatchingWindowInSeconds": (integer, False),
        "MaximumRecordAgeInSeconds": (integer, False),
        "MaximumRetryAttempts": (integer, False),
        "OnPartialBatchItemFailure": (str, False),
        "ParallelizationFactor": (integer, False),
        "StartingPosition": (str, True),
    }


class PipeSourceKinesisStreamParameters(AWSProperty):
    """
    `PipeSourceKinesisStreamParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html>`__
    """

    props: PropsDictType = {
        "BatchSize": (integer, False),
        "DeadLetterConfig": (DeadLetterConfig, False),
        "MaximumBatchingWindowInSeconds": (integer, False),
        "MaximumRecordAgeInSeconds": (integer, False),
        "MaximumRetryAttempts": (integer, False),
        "OnPartialBatchItemFailure": (str, False),
        "ParallelizationFactor": (integer, False),
        "StartingPosition": (str, True),
        "StartingPositionTimestamp": (str, False),
    }


class MSKAccessCredentials(AWSProperty):
    """
    `MSKAccessCredentials <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-mskaccesscredentials.html>`__
    """

    props: PropsDictType = {
        "ClientCertificateTlsAuth": (str, False),
        "SaslScram512Auth": (str, False),
    }


class PipeSourceManagedStreamingKafkaParameters(AWSProperty):
    """
    `PipeSourceManagedStreamingKafkaParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html>`__
    """

    props: PropsDictType = {
        "BatchSize": (integer, False),
        "ConsumerGroupID": (str, False),
        "Credentials": (MSKAccessCredentials, False),
        "MaximumBatchingWindowInSeconds": (integer, False),
        "StartingPosition": (str, False),
        "TopicName": (str, True),
    }


class PipeSourceRabbitMQBrokerParameters(AWSProperty):
    """
    `PipeSourceRabbitMQBrokerParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html>`__
    """

    props: PropsDictType = {
        "BatchSize": (integer, False),
        "Credentials": (MQBrokerAccessCredentials, True),
        "MaximumBatchingWindowInSeconds": (integer, False),
        "QueueName": (str, True),
        "VirtualHost": (str, False),
    }


class SelfManagedKafkaAccessConfigurationCredentials(AWSProperty):
    """
    `SelfManagedKafkaAccessConfigurationCredentials <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials.html>`__
    """

    props: PropsDictType = {
        "BasicAuth": (str, False),
        "ClientCertificateTlsAuth": (str, False),
        "SaslScram256Auth": (str, False),
        "SaslScram512Auth": (str, False),
    }


class SelfManagedKafkaAccessConfigurationVpc(AWSProperty):
    """
    `SelfManagedKafkaAccessConfigurationVpc <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc.html>`__
    """

    props: PropsDictType = {
        "SecurityGroup": ([str], False),
        "Subnets": ([str], False),
    }


class PipeSourceSelfManagedKafkaParameters(AWSProperty):
    """
    `PipeSourceSelfManagedKafkaParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html>`__
    """

    props: PropsDictType = {
        "AdditionalBootstrapServers": ([str], False),
        "BatchSize": (integer, False),
        "ConsumerGroupID": (str, False),
        "Credentials": (SelfManagedKafkaAccessConfigurationCredentials, False),
        "MaximumBatchingWindowInSeconds": (integer, False),
        "ServerRootCaCertificate": (str, False),
        "StartingPosition": (str, False),
        "TopicName": (str, True),
        "Vpc": (SelfManagedKafkaAccessConfigurationVpc, False),
    }


class PipeSourceSqsQueueParameters(AWSProperty):
    """
    `PipeSourceSqsQueueParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcesqsqueueparameters.html>`__
    """

    props: PropsDictType = {
        "BatchSize": (integer, False),
        "MaximumBatchingWindowInSeconds": (integer, False),
    }


class PipeSourceParameters(AWSProperty):
    """
    `PipeSourceParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html>`__
    """

    props: PropsDictType = {
        "ActiveMQBrokerParameters": (PipeSourceActiveMQBrokerParameters, False),
        "DynamoDBStreamParameters": (PipeSourceDynamoDBStreamParameters, False),
        "FilterCriteria": (FilterCriteria, False),
        "KinesisStreamParameters": (PipeSourceKinesisStreamParameters, False),
        "ManagedStreamingKafkaParameters": (
            PipeSourceManagedStreamingKafkaParameters,
            False,
        ),
        "RabbitMQBrokerParameters": (PipeSourceRabbitMQBrokerParameters, False),
        "SelfManagedKafkaParameters": (PipeSourceSelfManagedKafkaParameters, False),
        "SqsQueueParameters": (PipeSourceSqsQueueParameters, False),
    }


class BatchArrayProperties(AWSProperty):
    """
    `BatchArrayProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batcharrayproperties.html>`__
    """

    props: PropsDictType = {
        "Size": (integer, False),
    }


class BatchEnvironmentVariable(AWSProperty):
    """
    `BatchEnvironmentVariable <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchenvironmentvariable.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class BatchResourceRequirement(AWSProperty):
    """
    `BatchResourceRequirement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchresourcerequirement.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (str, True),
    }


class BatchContainerOverrides(AWSProperty):
    """
    `BatchContainerOverrides <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchcontaineroverrides.html>`__
    """

    props: PropsDictType = {
        "Command": ([str], False),
        "Environment": ([BatchEnvironmentVariable], False),
        "InstanceType": (str, False),
        "ResourceRequirements": ([BatchResourceRequirement], False),
    }


class BatchJobDependency(AWSProperty):
    """
    `BatchJobDependency <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchjobdependency.html>`__
    """

    props: PropsDictType = {
        "JobId": (str, False),
        "Type": (str, False),
    }


class BatchRetryStrategy(AWSProperty):
    """
    `BatchRetryStrategy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchretrystrategy.html>`__
    """

    props: PropsDictType = {
        "Attempts": (integer, False),
    }


class PipeTargetBatchJobParameters(AWSProperty):
    """
    `PipeTargetBatchJobParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html>`__
    """

    props: PropsDictType = {
        "ArrayProperties": (BatchArrayProperties, False),
        "ContainerOverrides": (BatchContainerOverrides, False),
        "DependsOn": ([BatchJobDependency], False),
        "JobDefinition": (str, True),
        "JobName": (str, True),
        "Parameters": (dict, False),
        "RetryStrategy": (BatchRetryStrategy, False),
    }


class PipeTargetCloudWatchLogsParameters(AWSProperty):
    """
    `PipeTargetCloudWatchLogsParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetcloudwatchlogsparameters.html>`__
    """

    props: PropsDictType = {
        "LogStreamName": (str, False),
        "Timestamp": (str, False),
    }


class CapacityProviderStrategyItem(AWSProperty):
    """
    `CapacityProviderStrategyItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-capacityproviderstrategyitem.html>`__
    """

    props: PropsDictType = {
        "Base": (integer, False),
        "CapacityProvider": (str, True),
        "Weight": (integer, False),
    }


class EcsEnvironmentFile(AWSProperty):
    """
    `EcsEnvironmentFile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentfile.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (str, True),
    }


class EcsEnvironmentVariable(AWSProperty):
    """
    `EcsEnvironmentVariable <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentvariable.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class EcsResourceRequirement(AWSProperty):
    """
    `EcsResourceRequirement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsresourcerequirement.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (str, True),
    }


class EcsContainerOverride(AWSProperty):
    """
    `EcsContainerOverride <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html>`__
    """

    props: PropsDictType = {
        "Command": ([str], False),
        "Cpu": (integer, False),
        "Environment": ([EcsEnvironmentVariable], False),
        "EnvironmentFiles": ([EcsEnvironmentFile], False),
        "Memory": (integer, False),
        "MemoryReservation": (integer, False),
        "Name": (str, False),
        "ResourceRequirements": ([EcsResourceRequirement], False),
    }


class EcsEphemeralStorage(AWSProperty):
    """
    `EcsEphemeralStorage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsephemeralstorage.html>`__
    """

    props: PropsDictType = {
        "SizeInGiB": (integer, True),
    }


class EcsInferenceAcceleratorOverride(AWSProperty):
    """
    `EcsInferenceAcceleratorOverride <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsinferenceacceleratoroverride.html>`__
    """

    props: PropsDictType = {
        "DeviceName": (str, False),
        "DeviceType": (str, False),
    }


class EcsTaskOverride(AWSProperty):
    """
    `EcsTaskOverride <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html>`__
    """

    props: PropsDictType = {
        "ContainerOverrides": ([EcsContainerOverride], False),
        "Cpu": (str, False),
        "EphemeralStorage": (EcsEphemeralStorage, False),
        "ExecutionRoleArn": (str, False),
        "InferenceAcceleratorOverrides": ([EcsInferenceAcceleratorOverride], False),
        "Memory": (str, False),
        "TaskRoleArn": (str, False),
    }


class AwsVpcConfiguration(AWSProperty):
    """
    `AwsVpcConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-awsvpcconfiguration.html>`__
    """

    props: PropsDictType = {
        "AssignPublicIp": (str, False),
        "SecurityGroups": ([str], False),
        "Subnets": ([str], True),
    }


class NetworkConfiguration(AWSProperty):
    """
    `NetworkConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-networkconfiguration.html>`__
    """

    props: PropsDictType = {
        "AwsvpcConfiguration": (AwsVpcConfiguration, False),
    }


class PlacementConstraint(AWSProperty):
    """
    `PlacementConstraint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementconstraint.html>`__
    """

    props: PropsDictType = {
        "Expression": (str, False),
        "Type": (str, False),
    }


class PlacementStrategy(AWSProperty):
    """
    `PlacementStrategy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementstrategy.html>`__
    """

    props: PropsDictType = {
        "Field": (str, False),
        "Type": (str, False),
    }


class PipeTargetEcsTaskParameters(AWSProperty):
    """
    `PipeTargetEcsTaskParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html>`__
    """

    props: PropsDictType = {
        "CapacityProviderStrategy": ([CapacityProviderStrategyItem], False),
        "EnableECSManagedTags": (boolean, False),
        "EnableExecuteCommand": (boolean, False),
        "Group": (str, False),
        "LaunchType": (str, False),
        "NetworkConfiguration": (NetworkConfiguration, False),
        "Overrides": (EcsTaskOverride, False),
        "PlacementConstraints": ([PlacementConstraint], False),
        "PlacementStrategy": ([PlacementStrategy], False),
        "PlatformVersion": (str, False),
        "PropagateTags": (str, False),
        "ReferenceId": (str, False),
        "Tags": (Tags, False),
        "TaskCount": (integer, False),
        "TaskDefinitionArn": (str, True),
    }


class PipeTargetEventBridgeEventBusParameters(AWSProperty):
    """
    `PipeTargetEventBridgeEventBusParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargeteventbridgeeventbusparameters.html>`__
    """

    props: PropsDictType = {
        "DetailType": (str, False),
        "EndpointId": (str, False),
        "Resources": ([str], False),
        "Source": (str, False),
        "Time": (str, False),
    }


class PipeTargetHttpParameters(AWSProperty):
    """
    `PipeTargetHttpParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargethttpparameters.html>`__
    """

    props: PropsDictType = {
        "HeaderParameters": (dict, False),
        "PathParameterValues": ([str], False),
        "QueryStringParameters": (dict, False),
    }


class PipeTargetKinesisStreamParameters(AWSProperty):
    """
    `PipeTargetKinesisStreamParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetkinesisstreamparameters.html>`__
    """

    props: PropsDictType = {
        "PartitionKey": (str, True),
    }


class PipeTargetLambdaFunctionParameters(AWSProperty):
    """
    `PipeTargetLambdaFunctionParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetlambdafunctionparameters.html>`__
    """

    props: PropsDictType = {
        "InvocationType": (str, False),
    }


class PipeTargetRedshiftDataParameters(AWSProperty):
    """
    `PipeTargetRedshiftDataParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html>`__
    """

    props: PropsDictType = {
        "Database": (str, True),
        "DbUser": (str, False),
        "SecretManagerArn": (str, False),
        "Sqls": ([str], True),
        "StatementName": (str, False),
        "WithEvent": (boolean, False),
    }


class SageMakerPipelineParameter(AWSProperty):
    """
    `SageMakerPipelineParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-sagemakerpipelineparameter.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Value": (str, True),
    }


class PipeTargetSageMakerPipelineParameters(AWSProperty):
    """
    `PipeTargetSageMakerPipelineParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetsagemakerpipelineparameters.html>`__
    """

    props: PropsDictType = {
        "PipelineParameterList": ([SageMakerPipelineParameter], False),
    }


class PipeTargetSqsQueueParameters(AWSProperty):
    """
    `PipeTargetSqsQueueParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetsqsqueueparameters.html>`__
    """

    props: PropsDictType = {
        "MessageDeduplicationId": (str, False),
        "MessageGroupId": (str, False),
    }


class PipeTargetStateMachineParameters(AWSProperty):
    """
    `PipeTargetStateMachineParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetstatemachineparameters.html>`__
    """

    props: PropsDictType = {
        "InvocationType": (str, False),
    }


class DimensionMapping(AWSProperty):
    """
    `DimensionMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-dimensionmapping.html>`__
    """

    props: PropsDictType = {
        "DimensionName": (str, True),
        "DimensionValue": (str, True),
        "DimensionValueType": (str, True),
    }


class MultiMeasureAttributeMapping(AWSProperty):
    """
    `MultiMeasureAttributeMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-multimeasureattributemapping.html>`__
    """

    props: PropsDictType = {
        "MeasureValue": (str, True),
        "MeasureValueType": (str, True),
        "MultiMeasureAttributeName": (str, True),
    }


class MultiMeasureMapping(AWSProperty):
    """
    `MultiMeasureMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-multimeasuremapping.html>`__
    """

    props: PropsDictType = {
        "MultiMeasureAttributeMappings": ([MultiMeasureAttributeMapping], True),
        "MultiMeasureName": (str, True),
    }


class SingleMeasureMapping(AWSProperty):
    """
    `SingleMeasureMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-singlemeasuremapping.html>`__
    """

    props: PropsDictType = {
        "MeasureName": (str, True),
        "MeasureValue": (str, True),
        "MeasureValueType": (str, True),
    }


class PipeTargetTimestreamParameters(AWSProperty):
    """
    `PipeTargetTimestreamParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargettimestreamparameters.html>`__
    """

    props: PropsDictType = {
        "DimensionMappings": ([DimensionMapping], True),
        "EpochTimeUnit": (str, False),
        "MultiMeasureMappings": ([MultiMeasureMapping], False),
        "SingleMeasureMappings": ([SingleMeasureMapping], False),
        "TimeFieldType": (str, False),
        "TimeValue": (str, True),
        "TimestampFormat": (str, False),
        "VersionValue": (str, True),
    }


class PipeTargetParameters(AWSProperty):
    """
    `PipeTargetParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html>`__
    """

    props: PropsDictType = {
        "BatchJobParameters": (PipeTargetBatchJobParameters, False),
        "CloudWatchLogsParameters": (PipeTargetCloudWatchLogsParameters, False),
        "EcsTaskParameters": (PipeTargetEcsTaskParameters, False),
        "EventBridgeEventBusParameters": (
            PipeTargetEventBridgeEventBusParameters,
            False,
        ),
        "HttpParameters": (PipeTargetHttpParameters, False),
        "InputTemplate": (str, False),
        "KinesisStreamParameters": (PipeTargetKinesisStreamParameters, False),
        "LambdaFunctionParameters": (PipeTargetLambdaFunctionParameters, False),
        "RedshiftDataParameters": (PipeTargetRedshiftDataParameters, False),
        "SageMakerPipelineParameters": (PipeTargetSageMakerPipelineParameters, False),
        "SqsQueueParameters": (PipeTargetSqsQueueParameters, False),
        "StepFunctionStateMachineParameters": (PipeTargetStateMachineParameters, False),
        "TimestreamParameters": (PipeTargetTimestreamParameters, False),
    }


class Pipe(AWSObject):
    """
    `Pipe <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html>`__
    """

    resource_type = "AWS::Pipes::Pipe"

    props: PropsDictType = {
        "Description": (str, False),
        "DesiredState": (str, False),
        "Enrichment": (str, False),
        "EnrichmentParameters": (PipeEnrichmentParameters, False),
        "KmsKeyIdentifier": (str, False),
        "LogConfiguration": (PipeLogConfiguration, False),
        "Name": (str, False),
        "RoleArn": (str, True),
        "Source": (str, True),
        "SourceParameters": (PipeSourceParameters, False),
        "Tags": (dict, False),
        "Target": (str, True),
        "TargetParameters": (PipeTargetParameters, False),
    }
