# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, double, integer


class DataSource(AWSProperty):
    """
    `DataSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasource.html>`__
    """

    props: PropsDictType = {
        "DataLocation": (str, False),
    }


class DatasetImportJob(AWSProperty):
    """
    `DatasetImportJob <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html>`__
    """

    props: PropsDictType = {
        "DataSource": (DataSource, False),
        "DatasetArn": (str, False),
        "DatasetImportJobArn": (str, False),
        "JobName": (str, False),
        "RoleArn": (str, False),
    }


class Dataset(AWSObject):
    """
    `Dataset <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html>`__
    """

    resource_type = "AWS::Personalize::Dataset"

    props: PropsDictType = {
        "DatasetGroupArn": (str, True),
        "DatasetImportJob": (DatasetImportJob, False),
        "DatasetType": (str, True),
        "Name": (str, True),
        "SchemaArn": (str, True),
    }


class DatasetGroup(AWSObject):
    """
    `DatasetGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html>`__
    """

    resource_type = "AWS::Personalize::DatasetGroup"

    props: PropsDictType = {
        "Domain": (str, False),
        "KmsKeyArn": (str, False),
        "Name": (str, True),
        "RoleArn": (str, False),
    }


class Schema(AWSObject):
    """
    `Schema <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html>`__
    """

    resource_type = "AWS::Personalize::Schema"

    props: PropsDictType = {
        "Domain": (str, False),
        "Name": (str, True),
        "Schema": (str, True),
    }


class AutoMLConfig(AWSProperty):
    """
    `AutoMLConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-automlconfig.html>`__
    """

    props: PropsDictType = {
        "MetricName": (str, False),
        "RecipeList": ([str], False),
    }


class CategoricalHyperParameterRange(AWSProperty):
    """
    `CategoricalHyperParameterRange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-categoricalhyperparameterrange.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Values": ([str], False),
    }


class ContinuousHyperParameterRange(AWSProperty):
    """
    `ContinuousHyperParameterRange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-continuoushyperparameterrange.html>`__
    """

    props: PropsDictType = {
        "MaxValue": (double, False),
        "MinValue": (double, False),
        "Name": (str, False),
    }


class IntegerHyperParameterRange(AWSProperty):
    """
    `IntegerHyperParameterRange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-integerhyperparameterrange.html>`__
    """

    props: PropsDictType = {
        "MaxValue": (integer, False),
        "MinValue": (integer, False),
        "Name": (str, False),
    }


class AlgorithmHyperParameterRanges(AWSProperty):
    """
    `AlgorithmHyperParameterRanges <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-algorithmhyperparameterranges.html>`__
    """

    props: PropsDictType = {
        "CategoricalHyperParameterRanges": ([CategoricalHyperParameterRange], False),
        "ContinuousHyperParameterRanges": ([ContinuousHyperParameterRange], False),
        "IntegerHyperParameterRanges": ([IntegerHyperParameterRange], False),
    }


class HpoObjective(AWSProperty):
    """
    `HpoObjective <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoobjective.html>`__
    """

    props: PropsDictType = {
        "MetricName": (str, False),
        "MetricRegex": (str, False),
        "Type": (str, False),
    }


class HpoResourceConfig(AWSProperty):
    """
    `HpoResourceConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hporesourceconfig.html>`__
    """

    props: PropsDictType = {
        "MaxNumberOfTrainingJobs": (str, False),
        "MaxParallelTrainingJobs": (str, False),
    }


class HpoConfig(AWSProperty):
    """
    `HpoConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoconfig.html>`__
    """

    props: PropsDictType = {
        "AlgorithmHyperParameterRanges": (AlgorithmHyperParameterRanges, False),
        "HpoObjective": (HpoObjective, False),
        "HpoResourceConfig": (HpoResourceConfig, False),
    }


class SolutionConfig(AWSProperty):
    """
    `SolutionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html>`__
    """

    props: PropsDictType = {
        "AlgorithmHyperParameters": (dict, False),
        "AutoMLConfig": (AutoMLConfig, False),
        "EventValueThreshold": (str, False),
        "FeatureTransformationParameters": (dict, False),
        "HpoConfig": (HpoConfig, False),
    }


class Solution(AWSObject):
    """
    `Solution <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html>`__
    """

    resource_type = "AWS::Personalize::Solution"

    props: PropsDictType = {
        "DatasetGroupArn": (str, True),
        "EventType": (str, False),
        "Name": (str, True),
        "PerformAutoML": (boolean, False),
        "PerformHPO": (boolean, False),
        "RecipeArn": (str, False),
        "SolutionConfig": (SolutionConfig, False),
    }
