// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Outputs
{

    [OutputType]
    public sealed class ContainerNetworkData
    {
        /// <summary>
        /// The network gateway of the container.
        /// </summary>
        public readonly string? Gateway;
        public readonly string? GlobalIpv6Address;
        public readonly int? GlobalIpv6PrefixLength;
        /// <summary>
        /// The IP address of the container.
        /// </summary>
        public readonly string? IpAddress;
        /// <summary>
        /// The IP prefix length of the container.
        /// </summary>
        public readonly int? IpPrefixLength;
        public readonly string? Ipv6Gateway;
        public readonly string? NetworkName;

        [OutputConstructor]
        private ContainerNetworkData(
            string? gateway,

            string? globalIpv6Address,

            int? globalIpv6PrefixLength,

            string? ipAddress,

            int? ipPrefixLength,

            string? ipv6Gateway,

            string? networkName)
        {
            Gateway = gateway;
            GlobalIpv6Address = globalIpv6Address;
            GlobalIpv6PrefixLength = globalIpv6PrefixLength;
            IpAddress = ipAddress;
            IpPrefixLength = ipPrefixLength;
            Ipv6Gateway = ipv6Gateway;
            NetworkName = networkName;
        }
    }
}
