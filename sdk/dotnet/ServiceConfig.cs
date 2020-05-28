// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker
{
    /// <summary>
    /// Manages the configuration of a Docker service in a swarm.
    /// 
    /// 
    /// ## Basic
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Docker = Pulumi.Docker;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         // Creates a config
    ///         var fooConfig = new Docker.ServiceConfig("fooConfig", new Docker.ServiceConfigArgs
    ///         {
    ///             Data = "ewogICJzZXJIfQo=",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class ServiceConfig : Pulumi.CustomResource
    {
        /// <summary>
        /// The base64 encoded data of the config.
        /// </summary>
        [Output("data")]
        public Output<string> Data { get; private set; } = null!;

        /// <summary>
        /// The name of the Docker config.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a ServiceConfig resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServiceConfig(string name, ServiceConfigArgs args, CustomResourceOptions? options = null)
            : base("docker:index/serviceConfig:ServiceConfig", name, args ?? new ServiceConfigArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ServiceConfig(string name, Input<string> id, ServiceConfigState? state = null, CustomResourceOptions? options = null)
            : base("docker:index/serviceConfig:ServiceConfig", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ServiceConfig resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServiceConfig Get(string name, Input<string> id, ServiceConfigState? state = null, CustomResourceOptions? options = null)
        {
            return new ServiceConfig(name, id, state, options);
        }
    }

    public sealed class ServiceConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The base64 encoded data of the config.
        /// </summary>
        [Input("data", required: true)]
        public Input<string> Data { get; set; } = null!;

        /// <summary>
        /// The name of the Docker config.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ServiceConfigArgs()
        {
        }
    }

    public sealed class ServiceConfigState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The base64 encoded data of the config.
        /// </summary>
        [Input("data")]
        public Input<string>? Data { get; set; }

        /// <summary>
        /// The name of the Docker config.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ServiceConfigState()
        {
        }
    }
}
