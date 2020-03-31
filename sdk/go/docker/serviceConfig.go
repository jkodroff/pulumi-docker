// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package docker

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages the configuration of a Docker service in a swarm.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-docker/blob/master/website/docs/r/config.html.markdown.
type ServiceConfig struct {
	pulumi.CustomResourceState

	// The base64 encoded data of the config.
	Data pulumi.StringOutput `pulumi:"data"`
	// The name of the Docker config.
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewServiceConfig registers a new resource with the given unique name, arguments, and options.
func NewServiceConfig(ctx *pulumi.Context,
	name string, args *ServiceConfigArgs, opts ...pulumi.ResourceOption) (*ServiceConfig, error) {
	if args == nil || args.Data == nil {
		return nil, errors.New("missing required argument 'Data'")
	}
	if args == nil {
		args = &ServiceConfigArgs{}
	}
	var resource ServiceConfig
	err := ctx.RegisterResource("docker:index/serviceConfig:ServiceConfig", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServiceConfig gets an existing ServiceConfig resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServiceConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServiceConfigState, opts ...pulumi.ResourceOption) (*ServiceConfig, error) {
	var resource ServiceConfig
	err := ctx.ReadResource("docker:index/serviceConfig:ServiceConfig", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServiceConfig resources.
type serviceConfigState struct {
	// The base64 encoded data of the config.
	Data *string `pulumi:"data"`
	// The name of the Docker config.
	Name *string `pulumi:"name"`
}

type ServiceConfigState struct {
	// The base64 encoded data of the config.
	Data pulumi.StringPtrInput
	// The name of the Docker config.
	Name pulumi.StringPtrInput
}

func (ServiceConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceConfigState)(nil)).Elem()
}

type serviceConfigArgs struct {
	// The base64 encoded data of the config.
	Data string `pulumi:"data"`
	// The name of the Docker config.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a ServiceConfig resource.
type ServiceConfigArgs struct {
	// The base64 encoded data of the config.
	Data pulumi.StringInput
	// The name of the Docker config.
	Name pulumi.StringPtrInput
}

func (ServiceConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceConfigArgs)(nil)).Elem()
}
