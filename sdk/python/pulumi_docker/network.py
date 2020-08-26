# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Network']


class Network(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attachable: Optional[pulumi.Input[bool]] = None,
                 check_duplicate: Optional[pulumi.Input[bool]] = None,
                 driver: Optional[pulumi.Input[str]] = None,
                 ingress: Optional[pulumi.Input[bool]] = None,
                 internal: Optional[pulumi.Input[bool]] = None,
                 ipam_configs: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['NetworkIpamConfigArgs']]]]] = None,
                 ipam_driver: Optional[pulumi.Input[str]] = None,
                 ipv6: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['NetworkLabelArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Docker Network. This can be used alongside
        [docker\_container](https://www.terraform.io/docs/providers/docker/r/container.html)
        to create virtual networks within the docker environment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_docker as docker

        # Create a new docker network
        private_network = docker.Network("privateNetwork")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] attachable: Enable manual container attachment to the network.
               Defaults to `false`.
        :param pulumi.Input[bool] check_duplicate: Requests daemon to check for networks
               with same name.
        :param pulumi.Input[str] driver: Name of the network driver to use. Defaults to
               `bridge` driver.
        :param pulumi.Input[bool] ingress: Create swarm routing-mesh network.
               Defaults to `false`.
        :param pulumi.Input[bool] internal: Restrict external access to the network.
               Defaults to `false`.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['NetworkIpamConfigArgs']]]] ipam_configs: See IPAM config below for
               details.
        :param pulumi.Input[str] ipam_driver: Driver used by the custom IP scheme of the
               network.
        :param pulumi.Input[bool] ipv6: Enable IPv6 networking.
               Defaults to `false`.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['NetworkLabelArgs']]]] labels: See Labels below for details.
        :param pulumi.Input[str] name: The name of the Docker network.
        :param pulumi.Input[Mapping[str, Any]] options: Network specific options to be used by
               the drivers.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['attachable'] = attachable
            __props__['check_duplicate'] = check_duplicate
            __props__['driver'] = driver
            __props__['ingress'] = ingress
            __props__['internal'] = internal
            __props__['ipam_configs'] = ipam_configs
            __props__['ipam_driver'] = ipam_driver
            __props__['ipv6'] = ipv6
            __props__['labels'] = labels
            __props__['name'] = name
            __props__['options'] = options
            __props__['scope'] = None
        super(Network, __self__).__init__(
            'docker:index/network:Network',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            attachable: Optional[pulumi.Input[bool]] = None,
            check_duplicate: Optional[pulumi.Input[bool]] = None,
            driver: Optional[pulumi.Input[str]] = None,
            ingress: Optional[pulumi.Input[bool]] = None,
            internal: Optional[pulumi.Input[bool]] = None,
            ipam_configs: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['NetworkIpamConfigArgs']]]]] = None,
            ipam_driver: Optional[pulumi.Input[str]] = None,
            ipv6: Optional[pulumi.Input[bool]] = None,
            labels: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['NetworkLabelArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            options: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            scope: Optional[pulumi.Input[str]] = None) -> 'Network':
        """
        Get an existing Network resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] attachable: Enable manual container attachment to the network.
               Defaults to `false`.
        :param pulumi.Input[bool] check_duplicate: Requests daemon to check for networks
               with same name.
        :param pulumi.Input[str] driver: Name of the network driver to use. Defaults to
               `bridge` driver.
        :param pulumi.Input[bool] ingress: Create swarm routing-mesh network.
               Defaults to `false`.
        :param pulumi.Input[bool] internal: Restrict external access to the network.
               Defaults to `false`.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['NetworkIpamConfigArgs']]]] ipam_configs: See IPAM config below for
               details.
        :param pulumi.Input[str] ipam_driver: Driver used by the custom IP scheme of the
               network.
        :param pulumi.Input[bool] ipv6: Enable IPv6 networking.
               Defaults to `false`.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['NetworkLabelArgs']]]] labels: See Labels below for details.
        :param pulumi.Input[str] name: The name of the Docker network.
        :param pulumi.Input[Mapping[str, Any]] options: Network specific options to be used by
               the drivers.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["attachable"] = attachable
        __props__["check_duplicate"] = check_duplicate
        __props__["driver"] = driver
        __props__["ingress"] = ingress
        __props__["internal"] = internal
        __props__["ipam_configs"] = ipam_configs
        __props__["ipam_driver"] = ipam_driver
        __props__["ipv6"] = ipv6
        __props__["labels"] = labels
        __props__["name"] = name
        __props__["options"] = options
        __props__["scope"] = scope
        return Network(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def attachable(self) -> Optional[bool]:
        """
        Enable manual container attachment to the network.
        Defaults to `false`.
        """
        return pulumi.get(self, "attachable")

    @property
    @pulumi.getter(name="checkDuplicate")
    def check_duplicate(self) -> Optional[bool]:
        """
        Requests daemon to check for networks
        with same name.
        """
        return pulumi.get(self, "check_duplicate")

    @property
    @pulumi.getter
    def driver(self) -> str:
        """
        Name of the network driver to use. Defaults to
        `bridge` driver.
        """
        return pulumi.get(self, "driver")

    @property
    @pulumi.getter
    def ingress(self) -> Optional[bool]:
        """
        Create swarm routing-mesh network.
        Defaults to `false`.
        """
        return pulumi.get(self, "ingress")

    @property
    @pulumi.getter
    def internal(self) -> bool:
        """
        Restrict external access to the network.
        Defaults to `false`.
        """
        return pulumi.get(self, "internal")

    @property
    @pulumi.getter(name="ipamConfigs")
    def ipam_configs(self) -> List['outputs.NetworkIpamConfig']:
        """
        See IPAM config below for
        details.
        """
        return pulumi.get(self, "ipam_configs")

    @property
    @pulumi.getter(name="ipamDriver")
    def ipam_driver(self) -> Optional[str]:
        """
        Driver used by the custom IP scheme of the
        network.
        """
        return pulumi.get(self, "ipam_driver")

    @property
    @pulumi.getter
    def ipv6(self) -> Optional[bool]:
        """
        Enable IPv6 networking.
        Defaults to `false`.
        """
        return pulumi.get(self, "ipv6")

    @property
    @pulumi.getter
    def labels(self) -> Optional[List['outputs.NetworkLabel']]:
        """
        See Labels below for details.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Docker network.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def options(self) -> Mapping[str, Any]:
        """
        Network specific options to be used by
        the drivers.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter
    def scope(self) -> str:
        return pulumi.get(self, "scope")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

