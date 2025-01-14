# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, double


class DataSet(AWSProperty):
    """
    `DataSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-dataset.html>`__
    """

    props: PropsDictType = {
        "Ccsid": (str, True),
        "Format": (str, True),
        "Length": (double, True),
        "Name": (str, True),
        "Type": (str, True),
    }


class SourceDatabaseMetadata(AWSProperty):
    """
    `SourceDatabaseMetadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-sourcedatabasemetadata.html>`__
    """

    props: PropsDictType = {
        "CaptureTool": (str, True),
        "Type": (str, True),
    }


class TargetDatabaseMetadata(AWSProperty):
    """
    `TargetDatabaseMetadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-targetdatabasemetadata.html>`__
    """

    props: PropsDictType = {
        "CaptureTool": (str, True),
        "Type": (str, True),
    }


class DatabaseCDC(AWSProperty):
    """
    `DatabaseCDC <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-databasecdc.html>`__
    """

    props: PropsDictType = {
        "SourceMetadata": (SourceDatabaseMetadata, True),
        "TargetMetadata": (TargetDatabaseMetadata, True),
    }


class FileMetadata(AWSProperty):
    """
    `FileMetadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-filemetadata.html>`__
    """

    props: PropsDictType = {
        "DataSets": ([DataSet], False),
        "DatabaseCDC": (DatabaseCDC, False),
    }


class InputFile(AWSProperty):
    """
    `InputFile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-inputfile.html>`__
    """

    props: PropsDictType = {
        "FileMetadata": (FileMetadata, True),
        "SourceLocation": (str, True),
        "TargetLocation": (str, True),
    }


class Input(AWSProperty):
    """
    `Input <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-input.html>`__
    """

    props: PropsDictType = {
        "File": (InputFile, True),
    }


class OutputFile(AWSProperty):
    """
    `OutputFile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-outputfile.html>`__
    """

    props: PropsDictType = {
        "FileLocation": (str, False),
    }


class Output(AWSProperty):
    """
    `Output <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-output.html>`__
    """

    props: PropsDictType = {
        "File": (OutputFile, True),
    }


class CompareAction(AWSProperty):
    """
    `CompareAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-compareaction.html>`__
    """

    props: PropsDictType = {
        "Input": (Input, True),
        "Output": (Output, False),
    }


class MainframeActionProperties(AWSProperty):
    """
    `MainframeActionProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-mainframeactionproperties.html>`__
    """

    props: PropsDictType = {
        "DmsTaskArn": (str, False),
    }


class Batch(AWSProperty):
    """
    `Batch <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-batch.html>`__
    """

    props: PropsDictType = {
        "BatchJobName": (str, True),
        "BatchJobParameters": (dict, False),
        "ExportDataSetNames": ([str], False),
    }


class Script(AWSProperty):
    """
    `Script <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-script.html>`__
    """

    props: PropsDictType = {
        "ScriptLocation": (str, True),
        "Type": (str, True),
    }


class TN3270(AWSProperty):
    """
    `TN3270 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-tn3270.html>`__
    """

    props: PropsDictType = {
        "ExportDataSetNames": ([str], False),
        "Script": (Script, True),
    }


class MainframeActionType(AWSProperty):
    """
    `MainframeActionType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-mainframeactiontype.html>`__
    """

    props: PropsDictType = {
        "Batch": (Batch, False),
        "Tn3270": (TN3270, False),
    }


class MainframeAction(AWSProperty):
    """
    `MainframeAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-mainframeaction.html>`__
    """

    props: PropsDictType = {
        "ActionType": (MainframeActionType, True),
        "Properties": (MainframeActionProperties, False),
        "Resource": (str, True),
    }


class CloudFormationAction(AWSProperty):
    """
    `CloudFormationAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-cloudformationaction.html>`__
    """

    props: PropsDictType = {
        "ActionType": (str, False),
        "Resource": (str, True),
    }


class M2ManagedActionProperties(AWSProperty):
    """
    `M2ManagedActionProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-m2managedactionproperties.html>`__
    """

    props: PropsDictType = {
        "ForceStop": (boolean, False),
        "ImportDataSetLocation": (str, False),
    }


class M2ManagedApplicationAction(AWSProperty):
    """
    `M2ManagedApplicationAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-m2managedapplicationaction.html>`__
    """

    props: PropsDictType = {
        "ActionType": (str, True),
        "Properties": (M2ManagedActionProperties, False),
        "Resource": (str, True),
    }


class M2NonManagedApplicationAction(AWSProperty):
    """
    `M2NonManagedApplicationAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-m2nonmanagedapplicationaction.html>`__
    """

    props: PropsDictType = {
        "ActionType": (str, True),
        "Resource": (str, True),
    }


class ResourceAction(AWSProperty):
    """
    `ResourceAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-resourceaction.html>`__
    """

    props: PropsDictType = {
        "CloudFormationAction": (CloudFormationAction, False),
        "M2ManagedApplicationAction": (M2ManagedApplicationAction, False),
        "M2NonManagedApplicationAction": (M2NonManagedApplicationAction, False),
    }


class StepAction(AWSProperty):
    """
    `StepAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-stepaction.html>`__
    """

    props: PropsDictType = {
        "CompareAction": (CompareAction, False),
        "MainframeAction": (MainframeAction, False),
        "ResourceAction": (ResourceAction, False),
    }


class Step(AWSProperty):
    """
    `Step <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-step.html>`__
    """

    props: PropsDictType = {
        "Action": (StepAction, True),
        "Description": (str, False),
        "Name": (str, True),
    }


class TestCase(AWSObject):
    """
    `TestCase <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apptest-testcase.html>`__
    """

    resource_type = "AWS::AppTest::TestCase"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Steps": ([Step], True),
        "Tags": (dict, False),
    }


class TestCaseLatestVersion(AWSProperty):
    """
    `TestCaseLatestVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-testcaselatestversion.html>`__
    """

    props: PropsDictType = {
        "Status": (str, True),
        "Version": (double, True),
    }
