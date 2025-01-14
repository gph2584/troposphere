# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean
from .validators.chatbot import validate_logginglevel


class CustomActionAttachmentCriteria(AWSProperty):
    """
    `CustomActionAttachmentCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chatbot-customaction-customactionattachmentcriteria.html>`__
    """

    props: PropsDictType = {
        "Operator": (str, True),
        "Value": (str, False),
        "VariableName": (str, True),
    }


class CustomActionAttachment(AWSProperty):
    """
    `CustomActionAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chatbot-customaction-customactionattachment.html>`__
    """

    props: PropsDictType = {
        "ButtonText": (str, False),
        "Criteria": ([CustomActionAttachmentCriteria], False),
        "NotificationType": (str, False),
        "Variables": (dict, False),
    }


class CustomActionDefinition(AWSProperty):
    """
    `CustomActionDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chatbot-customaction-customactiondefinition.html>`__
    """

    props: PropsDictType = {
        "CommandText": (str, True),
    }


class CustomAction(AWSObject):
    """
    `CustomAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-customaction.html>`__
    """

    resource_type = "AWS::Chatbot::CustomAction"

    props: PropsDictType = {
        "ActionName": (str, True),
        "AliasName": (str, False),
        "Attachments": ([CustomActionAttachment], False),
        "Definition": (CustomActionDefinition, True),
        "Tags": (Tags, False),
    }


class MicrosoftTeamsChannelConfiguration(AWSObject):
    """
    `MicrosoftTeamsChannelConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html>`__
    """

    resource_type = "AWS::Chatbot::MicrosoftTeamsChannelConfiguration"

    props: PropsDictType = {
        "ConfigurationName": (str, True),
        "CustomizationResourceArns": ([str], False),
        "GuardrailPolicies": ([str], False),
        "IamRoleArn": (str, True),
        "LoggingLevel": (str, False),
        "SnsTopicArns": ([str], False),
        "Tags": (Tags, False),
        "TeamId": (str, True),
        "TeamsChannelId": (str, True),
        "TeamsTenantId": (str, True),
        "UserRoleRequired": (boolean, False),
    }


class SlackChannelConfiguration(AWSObject):
    """
    `SlackChannelConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html>`__
    """

    resource_type = "AWS::Chatbot::SlackChannelConfiguration"

    props: PropsDictType = {
        "ConfigurationName": (str, True),
        "CustomizationResourceArns": ([str], False),
        "GuardrailPolicies": ([str], False),
        "IamRoleArn": (str, True),
        "LoggingLevel": (validate_logginglevel, False),
        "SlackChannelId": (str, True),
        "SlackWorkspaceId": (str, True),
        "SnsTopicArns": ([str], False),
        "Tags": (Tags, False),
        "UserRoleRequired": (boolean, False),
    }
