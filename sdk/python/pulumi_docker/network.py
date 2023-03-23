# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['NetworkArgs', 'Network']

@pulumi.input_type
class NetworkArgs:
    def __init__(__self__, *,
                 attachable: Optional[pulumi.Input[bool]] = None,
                 check_duplicate: Optional[pulumi.Input[bool]] = None,
                 driver: Optional[pulumi.Input[str]] = None,
                 ingress: Optional[pulumi.Input[bool]] = None,
                 internal: Optional[pulumi.Input[bool]] = None,
                 ipam_configs: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkIpamConfigArgs']]]] = None,
                 ipam_driver: Optional[pulumi.Input[str]] = None,
                 ipam_options: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 ipv6: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkLabelArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a Network resource.
        :param pulumi.Input[bool] attachable: Enable manual container attachment to the network.
        :param pulumi.Input[bool] check_duplicate: Requests daemon to check for networks with same name.
        :param pulumi.Input[str] driver: The driver of the Docker network. Possible values are `bridge`, `host`, `overlay`, `macvlan`. See [network docs](https://docs.docker.com/network/#network-drivers) for more details.
        :param pulumi.Input[bool] ingress: Create swarm routing-mesh network. Defaults to `false`.
        :param pulumi.Input[bool] internal: Whether the network is internal.
        :param pulumi.Input[Sequence[pulumi.Input['NetworkIpamConfigArgs']]] ipam_configs: The IPAM configuration options
        :param pulumi.Input[str] ipam_driver: Driver used by the custom IP scheme of the network. Defaults to `default`
        :param pulumi.Input[Mapping[str, Any]] ipam_options: Provide explicit options to the IPAM driver. Valid options vary with `ipam_driver` and refer to that driver's documentation for more details.
        :param pulumi.Input[bool] ipv6: Enable IPv6 networking. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input['NetworkLabelArgs']]] labels: User-defined key/value metadata
        :param pulumi.Input[str] name: The name of the Docker network.
        :param pulumi.Input[Mapping[str, Any]] options: Only available with bridge networks. See [bridge options docs](https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options) for more details.
        """
        if attachable is not None:
            pulumi.set(__self__, "attachable", attachable)
        if check_duplicate is not None:
            pulumi.set(__self__, "check_duplicate", check_duplicate)
        if driver is not None:
            pulumi.set(__self__, "driver", driver)
        if ingress is not None:
            pulumi.set(__self__, "ingress", ingress)
        if internal is not None:
            pulumi.set(__self__, "internal", internal)
        if ipam_configs is not None:
            pulumi.set(__self__, "ipam_configs", ipam_configs)
        if ipam_driver is not None:
            pulumi.set(__self__, "ipam_driver", ipam_driver)
        if ipam_options is not None:
            pulumi.set(__self__, "ipam_options", ipam_options)
        if ipv6 is not None:
            pulumi.set(__self__, "ipv6", ipv6)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if options is not None:
            pulumi.set(__self__, "options", options)

    @property
    @pulumi.getter
    def attachable(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable manual container attachment to the network.
        """
        return pulumi.get(self, "attachable")

    @attachable.setter
    def attachable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "attachable", value)

    @property
    @pulumi.getter(name="checkDuplicate")
    def check_duplicate(self) -> Optional[pulumi.Input[bool]]:
        """
        Requests daemon to check for networks with same name.
        """
        return pulumi.get(self, "check_duplicate")

    @check_duplicate.setter
    def check_duplicate(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "check_duplicate", value)

    @property
    @pulumi.getter
    def driver(self) -> Optional[pulumi.Input[str]]:
        """
        The driver of the Docker network. Possible values are `bridge`, `host`, `overlay`, `macvlan`. See [network docs](https://docs.docker.com/network/#network-drivers) for more details.
        """
        return pulumi.get(self, "driver")

    @driver.setter
    def driver(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "driver", value)

    @property
    @pulumi.getter
    def ingress(self) -> Optional[pulumi.Input[bool]]:
        """
        Create swarm routing-mesh network. Defaults to `false`.
        """
        return pulumi.get(self, "ingress")

    @ingress.setter
    def ingress(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ingress", value)

    @property
    @pulumi.getter
    def internal(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the network is internal.
        """
        return pulumi.get(self, "internal")

    @internal.setter
    def internal(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "internal", value)

    @property
    @pulumi.getter(name="ipamConfigs")
    def ipam_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkIpamConfigArgs']]]]:
        """
        The IPAM configuration options
        """
        return pulumi.get(self, "ipam_configs")

    @ipam_configs.setter
    def ipam_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkIpamConfigArgs']]]]):
        pulumi.set(self, "ipam_configs", value)

    @property
    @pulumi.getter(name="ipamDriver")
    def ipam_driver(self) -> Optional[pulumi.Input[str]]:
        """
        Driver used by the custom IP scheme of the network. Defaults to `default`
        """
        return pulumi.get(self, "ipam_driver")

    @ipam_driver.setter
    def ipam_driver(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipam_driver", value)

    @property
    @pulumi.getter(name="ipamOptions")
    def ipam_options(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Provide explicit options to the IPAM driver. Valid options vary with `ipam_driver` and refer to that driver's documentation for more details.
        """
        return pulumi.get(self, "ipam_options")

    @ipam_options.setter
    def ipam_options(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "ipam_options", value)

    @property
    @pulumi.getter
    def ipv6(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable IPv6 networking. Defaults to `false`.
        """
        return pulumi.get(self, "ipv6")

    @ipv6.setter
    def ipv6(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ipv6", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkLabelArgs']]]]:
        """
        User-defined key/value metadata
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkLabelArgs']]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Docker network.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Only available with bridge networks. See [bridge options docs](https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options) for more details.
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "options", value)


@pulumi.input_type
class _NetworkState:
    def __init__(__self__, *,
                 attachable: Optional[pulumi.Input[bool]] = None,
                 check_duplicate: Optional[pulumi.Input[bool]] = None,
                 driver: Optional[pulumi.Input[str]] = None,
                 ingress: Optional[pulumi.Input[bool]] = None,
                 internal: Optional[pulumi.Input[bool]] = None,
                 ipam_configs: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkIpamConfigArgs']]]] = None,
                 ipam_driver: Optional[pulumi.Input[str]] = None,
                 ipam_options: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 ipv6: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkLabelArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 scope: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Network resources.
        :param pulumi.Input[bool] attachable: Enable manual container attachment to the network.
        :param pulumi.Input[bool] check_duplicate: Requests daemon to check for networks with same name.
        :param pulumi.Input[str] driver: The driver of the Docker network. Possible values are `bridge`, `host`, `overlay`, `macvlan`. See [network docs](https://docs.docker.com/network/#network-drivers) for more details.
        :param pulumi.Input[bool] ingress: Create swarm routing-mesh network. Defaults to `false`.
        :param pulumi.Input[bool] internal: Whether the network is internal.
        :param pulumi.Input[Sequence[pulumi.Input['NetworkIpamConfigArgs']]] ipam_configs: The IPAM configuration options
        :param pulumi.Input[str] ipam_driver: Driver used by the custom IP scheme of the network. Defaults to `default`
        :param pulumi.Input[Mapping[str, Any]] ipam_options: Provide explicit options to the IPAM driver. Valid options vary with `ipam_driver` and refer to that driver's documentation for more details.
        :param pulumi.Input[bool] ipv6: Enable IPv6 networking. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input['NetworkLabelArgs']]] labels: User-defined key/value metadata
        :param pulumi.Input[str] name: The name of the Docker network.
        :param pulumi.Input[Mapping[str, Any]] options: Only available with bridge networks. See [bridge options docs](https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options) for more details.
        :param pulumi.Input[str] scope: Scope of the network. One of `swarm`, `global`, or `local`.
        """
        if attachable is not None:
            pulumi.set(__self__, "attachable", attachable)
        if check_duplicate is not None:
            pulumi.set(__self__, "check_duplicate", check_duplicate)
        if driver is not None:
            pulumi.set(__self__, "driver", driver)
        if ingress is not None:
            pulumi.set(__self__, "ingress", ingress)
        if internal is not None:
            pulumi.set(__self__, "internal", internal)
        if ipam_configs is not None:
            pulumi.set(__self__, "ipam_configs", ipam_configs)
        if ipam_driver is not None:
            pulumi.set(__self__, "ipam_driver", ipam_driver)
        if ipam_options is not None:
            pulumi.set(__self__, "ipam_options", ipam_options)
        if ipv6 is not None:
            pulumi.set(__self__, "ipv6", ipv6)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if options is not None:
            pulumi.set(__self__, "options", options)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter
    def attachable(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable manual container attachment to the network.
        """
        return pulumi.get(self, "attachable")

    @attachable.setter
    def attachable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "attachable", value)

    @property
    @pulumi.getter(name="checkDuplicate")
    def check_duplicate(self) -> Optional[pulumi.Input[bool]]:
        """
        Requests daemon to check for networks with same name.
        """
        return pulumi.get(self, "check_duplicate")

    @check_duplicate.setter
    def check_duplicate(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "check_duplicate", value)

    @property
    @pulumi.getter
    def driver(self) -> Optional[pulumi.Input[str]]:
        """
        The driver of the Docker network. Possible values are `bridge`, `host`, `overlay`, `macvlan`. See [network docs](https://docs.docker.com/network/#network-drivers) for more details.
        """
        return pulumi.get(self, "driver")

    @driver.setter
    def driver(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "driver", value)

    @property
    @pulumi.getter
    def ingress(self) -> Optional[pulumi.Input[bool]]:
        """
        Create swarm routing-mesh network. Defaults to `false`.
        """
        return pulumi.get(self, "ingress")

    @ingress.setter
    def ingress(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ingress", value)

    @property
    @pulumi.getter
    def internal(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the network is internal.
        """
        return pulumi.get(self, "internal")

    @internal.setter
    def internal(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "internal", value)

    @property
    @pulumi.getter(name="ipamConfigs")
    def ipam_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkIpamConfigArgs']]]]:
        """
        The IPAM configuration options
        """
        return pulumi.get(self, "ipam_configs")

    @ipam_configs.setter
    def ipam_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkIpamConfigArgs']]]]):
        pulumi.set(self, "ipam_configs", value)

    @property
    @pulumi.getter(name="ipamDriver")
    def ipam_driver(self) -> Optional[pulumi.Input[str]]:
        """
        Driver used by the custom IP scheme of the network. Defaults to `default`
        """
        return pulumi.get(self, "ipam_driver")

    @ipam_driver.setter
    def ipam_driver(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipam_driver", value)

    @property
    @pulumi.getter(name="ipamOptions")
    def ipam_options(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Provide explicit options to the IPAM driver. Valid options vary with `ipam_driver` and refer to that driver's documentation for more details.
        """
        return pulumi.get(self, "ipam_options")

    @ipam_options.setter
    def ipam_options(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "ipam_options", value)

    @property
    @pulumi.getter
    def ipv6(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable IPv6 networking. Defaults to `false`.
        """
        return pulumi.get(self, "ipv6")

    @ipv6.setter
    def ipv6(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ipv6", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkLabelArgs']]]]:
        """
        User-defined key/value metadata
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkLabelArgs']]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Docker network.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Only available with bridge networks. See [bridge options docs](https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options) for more details.
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        Scope of the network. One of `swarm`, `global`, or `local`.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)


class Network(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attachable: Optional[pulumi.Input[bool]] = None,
                 check_duplicate: Optional[pulumi.Input[bool]] = None,
                 driver: Optional[pulumi.Input[str]] = None,
                 ingress: Optional[pulumi.Input[bool]] = None,
                 internal: Optional[pulumi.Input[bool]] = None,
                 ipam_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkIpamConfigArgs']]]]] = None,
                 ipam_driver: Optional[pulumi.Input[str]] = None,
                 ipam_options: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 ipv6: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkLabelArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        <!-- Bug: Type and Name are switched -->
        `Network` provides a docker network resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_docker as docker

        private_network = docker.Network("privateNetwork")
        ```

        ## Import

        ### Example Assuming you created a `network` as follows #!/bin/bash docker network create foo prints the long ID 87b57a9b91ecab2db2a6dbf38df74c67d7c7108cbe479d6576574ec2cd8c2d73 you provide the definition for the resource as follows terraform resource "docker_network" "foo" {

         name = "foo" } then the import command is as follows #!/bin/bash

        ```sh
         $ pulumi import docker:index/network:Network foo 87b57a9b91ecab2db2a6dbf38df74c67d7c7108cbe479d6576574ec2cd8c2d73
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] attachable: Enable manual container attachment to the network.
        :param pulumi.Input[bool] check_duplicate: Requests daemon to check for networks with same name.
        :param pulumi.Input[str] driver: The driver of the Docker network. Possible values are `bridge`, `host`, `overlay`, `macvlan`. See [network docs](https://docs.docker.com/network/#network-drivers) for more details.
        :param pulumi.Input[bool] ingress: Create swarm routing-mesh network. Defaults to `false`.
        :param pulumi.Input[bool] internal: Whether the network is internal.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkIpamConfigArgs']]]] ipam_configs: The IPAM configuration options
        :param pulumi.Input[str] ipam_driver: Driver used by the custom IP scheme of the network. Defaults to `default`
        :param pulumi.Input[Mapping[str, Any]] ipam_options: Provide explicit options to the IPAM driver. Valid options vary with `ipam_driver` and refer to that driver's documentation for more details.
        :param pulumi.Input[bool] ipv6: Enable IPv6 networking. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkLabelArgs']]]] labels: User-defined key/value metadata
        :param pulumi.Input[str] name: The name of the Docker network.
        :param pulumi.Input[Mapping[str, Any]] options: Only available with bridge networks. See [bridge options docs](https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options) for more details.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[NetworkArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- Bug: Type and Name are switched -->
        `Network` provides a docker network resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_docker as docker

        private_network = docker.Network("privateNetwork")
        ```

        ## Import

        ### Example Assuming you created a `network` as follows #!/bin/bash docker network create foo prints the long ID 87b57a9b91ecab2db2a6dbf38df74c67d7c7108cbe479d6576574ec2cd8c2d73 you provide the definition for the resource as follows terraform resource "docker_network" "foo" {

         name = "foo" } then the import command is as follows #!/bin/bash

        ```sh
         $ pulumi import docker:index/network:Network foo 87b57a9b91ecab2db2a6dbf38df74c67d7c7108cbe479d6576574ec2cd8c2d73
        ```

        :param str resource_name: The name of the resource.
        :param NetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attachable: Optional[pulumi.Input[bool]] = None,
                 check_duplicate: Optional[pulumi.Input[bool]] = None,
                 driver: Optional[pulumi.Input[str]] = None,
                 ingress: Optional[pulumi.Input[bool]] = None,
                 internal: Optional[pulumi.Input[bool]] = None,
                 ipam_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkIpamConfigArgs']]]]] = None,
                 ipam_driver: Optional[pulumi.Input[str]] = None,
                 ipam_options: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 ipv6: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkLabelArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkArgs.__new__(NetworkArgs)

            __props__.__dict__["attachable"] = attachable
            __props__.__dict__["check_duplicate"] = check_duplicate
            __props__.__dict__["driver"] = driver
            __props__.__dict__["ingress"] = ingress
            __props__.__dict__["internal"] = internal
            __props__.__dict__["ipam_configs"] = ipam_configs
            __props__.__dict__["ipam_driver"] = ipam_driver
            __props__.__dict__["ipam_options"] = ipam_options
            __props__.__dict__["ipv6"] = ipv6
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            __props__.__dict__["options"] = options
            __props__.__dict__["scope"] = None
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
            ipam_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkIpamConfigArgs']]]]] = None,
            ipam_driver: Optional[pulumi.Input[str]] = None,
            ipam_options: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            ipv6: Optional[pulumi.Input[bool]] = None,
            labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkLabelArgs']]]]] = None,
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
        :param pulumi.Input[bool] check_duplicate: Requests daemon to check for networks with same name.
        :param pulumi.Input[str] driver: The driver of the Docker network. Possible values are `bridge`, `host`, `overlay`, `macvlan`. See [network docs](https://docs.docker.com/network/#network-drivers) for more details.
        :param pulumi.Input[bool] ingress: Create swarm routing-mesh network. Defaults to `false`.
        :param pulumi.Input[bool] internal: Whether the network is internal.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkIpamConfigArgs']]]] ipam_configs: The IPAM configuration options
        :param pulumi.Input[str] ipam_driver: Driver used by the custom IP scheme of the network. Defaults to `default`
        :param pulumi.Input[Mapping[str, Any]] ipam_options: Provide explicit options to the IPAM driver. Valid options vary with `ipam_driver` and refer to that driver's documentation for more details.
        :param pulumi.Input[bool] ipv6: Enable IPv6 networking. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkLabelArgs']]]] labels: User-defined key/value metadata
        :param pulumi.Input[str] name: The name of the Docker network.
        :param pulumi.Input[Mapping[str, Any]] options: Only available with bridge networks. See [bridge options docs](https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options) for more details.
        :param pulumi.Input[str] scope: Scope of the network. One of `swarm`, `global`, or `local`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NetworkState.__new__(_NetworkState)

        __props__.__dict__["attachable"] = attachable
        __props__.__dict__["check_duplicate"] = check_duplicate
        __props__.__dict__["driver"] = driver
        __props__.__dict__["ingress"] = ingress
        __props__.__dict__["internal"] = internal
        __props__.__dict__["ipam_configs"] = ipam_configs
        __props__.__dict__["ipam_driver"] = ipam_driver
        __props__.__dict__["ipam_options"] = ipam_options
        __props__.__dict__["ipv6"] = ipv6
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["options"] = options
        __props__.__dict__["scope"] = scope
        return Network(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def attachable(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable manual container attachment to the network.
        """
        return pulumi.get(self, "attachable")

    @property
    @pulumi.getter(name="checkDuplicate")
    def check_duplicate(self) -> pulumi.Output[Optional[bool]]:
        """
        Requests daemon to check for networks with same name.
        """
        return pulumi.get(self, "check_duplicate")

    @property
    @pulumi.getter
    def driver(self) -> pulumi.Output[str]:
        """
        The driver of the Docker network. Possible values are `bridge`, `host`, `overlay`, `macvlan`. See [network docs](https://docs.docker.com/network/#network-drivers) for more details.
        """
        return pulumi.get(self, "driver")

    @property
    @pulumi.getter
    def ingress(self) -> pulumi.Output[Optional[bool]]:
        """
        Create swarm routing-mesh network. Defaults to `false`.
        """
        return pulumi.get(self, "ingress")

    @property
    @pulumi.getter
    def internal(self) -> pulumi.Output[bool]:
        """
        Whether the network is internal.
        """
        return pulumi.get(self, "internal")

    @property
    @pulumi.getter(name="ipamConfigs")
    def ipam_configs(self) -> pulumi.Output[Sequence['outputs.NetworkIpamConfig']]:
        """
        The IPAM configuration options
        """
        return pulumi.get(self, "ipam_configs")

    @property
    @pulumi.getter(name="ipamDriver")
    def ipam_driver(self) -> pulumi.Output[Optional[str]]:
        """
        Driver used by the custom IP scheme of the network. Defaults to `default`
        """
        return pulumi.get(self, "ipam_driver")

    @property
    @pulumi.getter(name="ipamOptions")
    def ipam_options(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Provide explicit options to the IPAM driver. Valid options vary with `ipam_driver` and refer to that driver's documentation for more details.
        """
        return pulumi.get(self, "ipam_options")

    @property
    @pulumi.getter
    def ipv6(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable IPv6 networking. Defaults to `false`.
        """
        return pulumi.get(self, "ipv6")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkLabel']]]:
        """
        User-defined key/value metadata
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Docker network.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def options(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Only available with bridge networks. See [bridge options docs](https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options) for more details.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        Scope of the network. One of `swarm`, `global`, or `local`.
        """
        return pulumi.get(self, "scope")

