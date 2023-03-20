# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._enums import *
from ._inputs import *

__all__ = ['ImageArgs', 'Image']

@pulumi.input_type
class ImageArgs:
    def __init__(__self__, *,
                 image_name: pulumi.Input[str],
                 build: Optional[pulumi.Input['DockerBuildArgs']] = None,
                 registry: Optional[pulumi.Input['RegistryArgs']] = None,
                 skip_push: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Image resource.
        :param pulumi.Input[str] image_name: The image name
        :param pulumi.Input['DockerBuildArgs'] build: The Docker build context
        :param pulumi.Input['RegistryArgs'] registry: The registry to push the image to
        :param pulumi.Input[bool] skip_push: A flag to skip a registry push.
        """
        pulumi.set(__self__, "image_name", image_name)
        if build is not None:
            pulumi.set(__self__, "build", build)
        if registry is not None:
            pulumi.set(__self__, "registry", registry)
        if skip_push is None:
            skip_push = False
        if skip_push is not None:
            pulumi.set(__self__, "skip_push", skip_push)

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[str]:
        """
        The image name
        """
        return pulumi.get(self, "image_name")

    @image_name.setter
    def image_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "image_name", value)

    @property
    @pulumi.getter
    def build(self) -> Optional[pulumi.Input['DockerBuildArgs']]:
        """
        The Docker build context
        """
        return pulumi.get(self, "build")

    @build.setter
    def build(self, value: Optional[pulumi.Input['DockerBuildArgs']]):
        pulumi.set(self, "build", value)

    @property
    @pulumi.getter
    def registry(self) -> Optional[pulumi.Input['RegistryArgs']]:
        """
        The registry to push the image to
        """
        return pulumi.get(self, "registry")

    @registry.setter
    def registry(self, value: Optional[pulumi.Input['RegistryArgs']]):
        pulumi.set(self, "registry", value)

    @property
    @pulumi.getter(name="skipPush")
    def skip_push(self) -> Optional[pulumi.Input[bool]]:
        """
        A flag to skip a registry push.
        """
        return pulumi.get(self, "skip_push")

    @skip_push.setter
    def skip_push(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_push", value)


class Image(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 build: Optional[pulumi.Input[pulumi.InputType['DockerBuildArgs']]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 registry: Optional[pulumi.Input[pulumi.InputType['RegistryArgs']]] = None,
                 skip_push: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Builds a Docker Image and pushes to a Docker registry.

        ## Example Usage
        ### A Docker image build
        ```python
        import pulumi
        import pulumi_docker as docker

        demo_image = docker.Image("demo-image",
            build=docker.DockerBuildArgs(
                context=".",
                dockerfile="Dockerfile",
            ),
            image_name="username/image:tag1",
            skip_push=True)
        pulumi.export("imageName", demo_image.image_name)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DockerBuildArgs']] build: The Docker build context
        :param pulumi.Input[str] image_name: The image name
        :param pulumi.Input[pulumi.InputType['RegistryArgs']] registry: The registry to push the image to
        :param pulumi.Input[bool] skip_push: A flag to skip a registry push.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ImageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Builds a Docker Image and pushes to a Docker registry.

        ## Example Usage
        ### A Docker image build
        ```python
        import pulumi
        import pulumi_docker as docker

        demo_image = docker.Image("demo-image",
            build=docker.DockerBuildArgs(
                context=".",
                dockerfile="Dockerfile",
            ),
            image_name="username/image:tag1",
            skip_push=True)
        pulumi.export("imageName", demo_image.image_name)
        ```

        :param str resource_name: The name of the resource.
        :param ImageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ImageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 build: Optional[pulumi.Input[pulumi.InputType['DockerBuildArgs']]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 registry: Optional[pulumi.Input[pulumi.InputType['RegistryArgs']]] = None,
                 skip_push: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ImageArgs.__new__(ImageArgs)

            __props__.__dict__["build"] = build
            if image_name is None and not opts.urn:
                raise TypeError("Missing required property 'image_name'")
            __props__.__dict__["image_name"] = image_name
            __props__.__dict__["registry"] = registry
            if skip_push is None:
                skip_push = False
            __props__.__dict__["skip_push"] = skip_push
            __props__.__dict__["base_image_name"] = None
            __props__.__dict__["context"] = None
            __props__.__dict__["dockerfile"] = None
            __props__.__dict__["registry_server"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="docker:image:Image")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Image, __self__).__init__(
            'docker:index/image:Image',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Image':
        """
        Get an existing Image resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ImageArgs.__new__(ImageArgs)

        __props__.__dict__["base_image_name"] = None
        __props__.__dict__["context"] = None
        __props__.__dict__["dockerfile"] = None
        __props__.__dict__["image_name"] = None
        __props__.__dict__["registry_server"] = None
        return Image(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="baseImageName")
    def base_image_name(self) -> pulumi.Output[str]:
        """
        The fully qualified image name that was pushed to the registry.
        """
        return pulumi.get(self, "base_image_name")

    @property
    @pulumi.getter
    def context(self) -> pulumi.Output[str]:
        """
        The path to the build context to use.
        """
        return pulumi.get(self, "context")

    @property
    @pulumi.getter
    def dockerfile(self) -> pulumi.Output[str]:
        """
        The location of the Dockerfile relative to the docker build context.
        """
        return pulumi.get(self, "dockerfile")

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Output[str]:
        """
        The fully qualified image name
        """
        return pulumi.get(self, "image_name")

    @property
    @pulumi.getter(name="registryServer")
    def registry_server(self) -> pulumi.Output[str]:
        """
        The name of the registry server hosting the image.
        """
        return pulumi.get(self, "registry_server")

