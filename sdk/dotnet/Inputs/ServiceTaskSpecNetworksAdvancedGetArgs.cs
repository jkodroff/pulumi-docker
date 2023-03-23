// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Inputs
{

    public sealed class ServiceTaskSpecNetworksAdvancedGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("aliases")]
        private InputList<string>? _aliases;
        public InputList<string> Aliases
        {
            get => _aliases ?? (_aliases = new InputList<string>());
            set => _aliases = value;
        }

        [Input("driverOpts")]
        private InputList<string>? _driverOpts;
        public InputList<string> DriverOpts
        {
            get => _driverOpts ?? (_driverOpts = new InputList<string>());
            set => _driverOpts = value;
        }

        /// <summary>
        /// Name of the service
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public ServiceTaskSpecNetworksAdvancedGetArgs()
        {
        }
        public static new ServiceTaskSpecNetworksAdvancedGetArgs Empty => new ServiceTaskSpecNetworksAdvancedGetArgs();
    }
}
