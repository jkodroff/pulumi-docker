// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package docker

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// ## Import
//
// Docker secret cannot be imported as the secret data, once set, is never exposed again.
type Secret struct {
	pulumi.CustomResourceState

	// The base64 encoded data of the secret.
	Data pulumi.StringOutput `pulumi:"data"`
	// See Labels below for details.
	Labels SecretLabelArrayOutput `pulumi:"labels"`
	// The name of the Docker secret.
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewSecret registers a new resource with the given unique name, arguments, and options.
func NewSecret(ctx *pulumi.Context,
	name string, args *SecretArgs, opts ...pulumi.ResourceOption) (*Secret, error) {
	if args == nil || args.Data == nil {
		return nil, errors.New("missing required argument 'Data'")
	}
	if args == nil {
		args = &SecretArgs{}
	}
	var resource Secret
	err := ctx.RegisterResource("docker:index/secret:Secret", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSecret gets an existing Secret resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecret(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SecretState, opts ...pulumi.ResourceOption) (*Secret, error) {
	var resource Secret
	err := ctx.ReadResource("docker:index/secret:Secret", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Secret resources.
type secretState struct {
	// The base64 encoded data of the secret.
	Data *string `pulumi:"data"`
	// See Labels below for details.
	Labels []SecretLabel `pulumi:"labels"`
	// The name of the Docker secret.
	Name *string `pulumi:"name"`
}

type SecretState struct {
	// The base64 encoded data of the secret.
	Data pulumi.StringPtrInput
	// See Labels below for details.
	Labels SecretLabelArrayInput
	// The name of the Docker secret.
	Name pulumi.StringPtrInput
}

func (SecretState) ElementType() reflect.Type {
	return reflect.TypeOf((*secretState)(nil)).Elem()
}

type secretArgs struct {
	// The base64 encoded data of the secret.
	Data string `pulumi:"data"`
	// See Labels below for details.
	Labels []SecretLabel `pulumi:"labels"`
	// The name of the Docker secret.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a Secret resource.
type SecretArgs struct {
	// The base64 encoded data of the secret.
	Data pulumi.StringInput
	// See Labels below for details.
	Labels SecretLabelArrayInput
	// The name of the Docker secret.
	Name pulumi.StringPtrInput
}

func (SecretArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*secretArgs)(nil)).Elem()
}

type SecretInput interface {
	pulumi.Input

	ToSecretOutput() SecretOutput
	ToSecretOutputWithContext(ctx context.Context) SecretOutput
}

func (Secret) ElementType() reflect.Type {
	return reflect.TypeOf((*Secret)(nil)).Elem()
}

func (i Secret) ToSecretOutput() SecretOutput {
	return i.ToSecretOutputWithContext(context.Background())
}

func (i Secret) ToSecretOutputWithContext(ctx context.Context) SecretOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretOutput)
}

type SecretOutput struct {
	*pulumi.OutputState
}

func (SecretOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SecretOutput)(nil)).Elem()
}

func (o SecretOutput) ToSecretOutput() SecretOutput {
	return o
}

func (o SecretOutput) ToSecretOutputWithContext(ctx context.Context) SecretOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(SecretOutput{})
}
