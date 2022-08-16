// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Inputs
{

    public sealed class ServiceModeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The global service mode. Defaults to `false`
        /// </summary>
        [Input("global")]
        public Input<bool>? Global { get; set; }

        /// <summary>
        /// The replicated service mode
        /// </summary>
        [Input("replicated")]
        public Input<Inputs.ServiceModeReplicatedArgs>? Replicated { get; set; }

        public ServiceModeArgs()
        {
        }
        public static new ServiceModeArgs Empty => new ServiceModeArgs();
    }
}
