// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package docker

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// `Network` provides details about a specific Docker Network.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-docker/sdk/v3/go/docker"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := docker.LookupNetwork(ctx, &GetNetworkArgs{
// 			Name: "main",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupNetwork(ctx *pulumi.Context, args *LookupNetworkArgs, opts ...pulumi.InvokeOption) (*LookupNetworkResult, error) {
	var rv LookupNetworkResult
	err := ctx.Invoke("docker:index/getNetwork:getNetwork", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNetwork.
type LookupNetworkArgs struct {
	// The name of the Docker network.
	Name string `pulumi:"name"`
}

// A collection of values returned by getNetwork.
type LookupNetworkResult struct {
	// The driver of the Docker network. Possible values are `bridge`, `host`, `overlay`, `macvlan`. See [network docs](https://docs.docker.com/network/#network-drivers) for more details.
	Driver string `pulumi:"driver"`
	// The ID of this resource.
	Id string `pulumi:"id"`
	// If `true`, the network is internal.
	Internal bool `pulumi:"internal"`
	// The IPAM configuration options
	IpamConfigs []GetNetworkIpamConfig `pulumi:"ipamConfigs"`
	// The name of the Docker network.
	Name string `pulumi:"name"`
	// Only available with bridge networks. See [bridge options docs](https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options) for more details.
	Options map[string]interface{} `pulumi:"options"`
	// Scope of the network. One of `swarm`, `global`, or `local`.
	Scope string `pulumi:"scope"`
}

func LookupNetworkOutput(ctx *pulumi.Context, args LookupNetworkOutputArgs, opts ...pulumi.InvokeOption) LookupNetworkResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupNetworkResult, error) {
			args := v.(LookupNetworkArgs)
			r, err := LookupNetwork(ctx, &args, opts...)
			var s LookupNetworkResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupNetworkResultOutput)
}

// A collection of arguments for invoking getNetwork.
type LookupNetworkOutputArgs struct {
	// The name of the Docker network.
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupNetworkOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkArgs)(nil)).Elem()
}

// A collection of values returned by getNetwork.
type LookupNetworkResultOutput struct{ *pulumi.OutputState }

func (LookupNetworkResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkResult)(nil)).Elem()
}

func (o LookupNetworkResultOutput) ToLookupNetworkResultOutput() LookupNetworkResultOutput {
	return o
}

func (o LookupNetworkResultOutput) ToLookupNetworkResultOutputWithContext(ctx context.Context) LookupNetworkResultOutput {
	return o
}

// The driver of the Docker network. Possible values are `bridge`, `host`, `overlay`, `macvlan`. See [network docs](https://docs.docker.com/network/#network-drivers) for more details.
func (o LookupNetworkResultOutput) Driver() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNetworkResult) string { return v.Driver }).(pulumi.StringOutput)
}

// The ID of this resource.
func (o LookupNetworkResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNetworkResult) string { return v.Id }).(pulumi.StringOutput)
}

// If `true`, the network is internal.
func (o LookupNetworkResultOutput) Internal() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupNetworkResult) bool { return v.Internal }).(pulumi.BoolOutput)
}

// The IPAM configuration options
func (o LookupNetworkResultOutput) IpamConfigs() GetNetworkIpamConfigArrayOutput {
	return o.ApplyT(func(v LookupNetworkResult) []GetNetworkIpamConfig { return v.IpamConfigs }).(GetNetworkIpamConfigArrayOutput)
}

// The name of the Docker network.
func (o LookupNetworkResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNetworkResult) string { return v.Name }).(pulumi.StringOutput)
}

// Only available with bridge networks. See [bridge options docs](https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options) for more details.
func (o LookupNetworkResultOutput) Options() pulumi.MapOutput {
	return o.ApplyT(func(v LookupNetworkResult) map[string]interface{} { return v.Options }).(pulumi.MapOutput)
}

// Scope of the network. One of `swarm`, `global`, or `local`.
func (o LookupNetworkResultOutput) Scope() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNetworkResult) string { return v.Scope }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNetworkResultOutput{})
}
