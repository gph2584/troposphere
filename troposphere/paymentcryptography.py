# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean


class Alias(AWSObject):
    """
    `Alias <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-paymentcryptography-alias.html>`__
    """

    resource_type = "AWS::PaymentCryptography::Alias"

    props: PropsDictType = {
        "AliasName": (str, True),
        "KeyArn": (str, False),
    }


class KeyModesOfUse(AWSProperty):
    """
    `KeyModesOfUse <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keymodesofuse.html>`__
    """

    props: PropsDictType = {
        "Decrypt": (boolean, False),
        "DeriveKey": (boolean, False),
        "Encrypt": (boolean, False),
        "Generate": (boolean, False),
        "NoRestrictions": (boolean, False),
        "Sign": (boolean, False),
        "Unwrap": (boolean, False),
        "Verify": (boolean, False),
        "Wrap": (boolean, False),
    }


class KeyAttributes(AWSProperty):
    """
    `KeyAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keyattributes.html>`__
    """

    props: PropsDictType = {
        "KeyAlgorithm": (str, True),
        "KeyClass": (str, True),
        "KeyModesOfUse": (KeyModesOfUse, True),
        "KeyUsage": (str, True),
    }


class Key(AWSObject):
    """
    `Key <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-paymentcryptography-key.html>`__
    """

    resource_type = "AWS::PaymentCryptography::Key"

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "Exportable": (boolean, True),
        "KeyAttributes": (KeyAttributes, True),
        "KeyCheckValueAlgorithm": (str, False),
        "Tags": (Tags, False),
    }
