# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class ChannelTargetInfo(AWSProperty):
    """
    `ChannelTargetInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-channeltargetinfo.html>`__
    """

    props: PropsDictType = {
        "ChannelId": (str, True),
        "RetryIntervalInMinutes": (integer, True),
    }


class ContactTargetInfo(AWSProperty):
    """
    `ContactTargetInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-contacttargetinfo.html>`__
    """

    props: PropsDictType = {
        "ContactId": (str, True),
        "IsEssential": (boolean, True),
    }


class Targets(AWSProperty):
    """
    `Targets <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-targets.html>`__
    """

    props: PropsDictType = {
        "ChannelTargetInfo": (ChannelTargetInfo, False),
        "ContactTargetInfo": (ContactTargetInfo, False),
    }


class Stage(AWSProperty):
    """
    `Stage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-stage.html>`__
    """

    props: PropsDictType = {
        "DurationInMinutes": (integer, True),
        "Targets": ([Targets], False),
    }


class Contact(AWSObject):
    """
    `Contact <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html>`__
    """

    resource_type = "AWS::SSMContacts::Contact"

    props: PropsDictType = {
        "Alias": (str, True),
        "DisplayName": (str, True),
        "Plan": ([Stage], False),
        "Type": (str, True),
    }


class ContactChannel(AWSObject):
    """
    `ContactChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html>`__
    """

    resource_type = "AWS::SSMContacts::ContactChannel"

    props: PropsDictType = {
        "ChannelAddress": (str, True),
        "ChannelName": (str, True),
        "ChannelType": (str, True),
        "ContactId": (str, True),
        "DeferActivation": (boolean, False),
    }


class Plan(AWSObject):
    """
    `Plan <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-plan.html>`__
    """

    resource_type = "AWS::SSMContacts::Plan"

    props: PropsDictType = {
        "ContactId": (str, True),
        "RotationIds": ([str], False),
        "Stages": ([Stage], False),
    }


class MonthlySetting(AWSProperty):
    """
    `MonthlySetting <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-monthlysetting.html>`__
    """

    props: PropsDictType = {
        "DayOfMonth": (integer, True),
        "HandOffTime": (str, True),
    }


class CoverageTime(AWSProperty):
    """
    `CoverageTime <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-coveragetime.html>`__
    """

    props: PropsDictType = {
        "EndTime": (str, True),
        "StartTime": (str, True),
    }


class ShiftCoverage(AWSProperty):
    """
    `ShiftCoverage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-shiftcoverage.html>`__
    """

    props: PropsDictType = {
        "CoverageTimes": ([CoverageTime], True),
        "DayOfWeek": (str, True),
    }


class WeeklySetting(AWSProperty):
    """
    `WeeklySetting <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-weeklysetting.html>`__
    """

    props: PropsDictType = {
        "DayOfWeek": (str, True),
        "HandOffTime": (str, True),
    }


class RecurrenceSettings(AWSProperty):
    """
    `RecurrenceSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html>`__
    """

    props: PropsDictType = {
        "DailySettings": ([str], False),
        "MonthlySettings": ([MonthlySetting], False),
        "NumberOfOnCalls": (integer, True),
        "RecurrenceMultiplier": (integer, True),
        "ShiftCoverages": ([ShiftCoverage], False),
        "WeeklySettings": ([WeeklySetting], False),
    }


class Rotation(AWSObject):
    """
    `Rotation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html>`__
    """

    resource_type = "AWS::SSMContacts::Rotation"

    props: PropsDictType = {
        "ContactIds": ([str], True),
        "Name": (str, True),
        "Recurrence": (RecurrenceSettings, True),
        "StartTime": (str, True),
        "Tags": (Tags, False),
        "TimeZoneId": (str, True),
    }
